from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from datetime import datetime, timedelta

class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Phiếu đặt phòng'
    _rec_name = 'code'
    _order = 'check_in desc'
    
    code = fields.Char(string='Mã booking', required=True, readonly=True, copy=False, default='/')
    check_in = fields.Date(string='Ngày nhận phòng', required=True, default=fields.Date.today())
    check_out = fields.Date(string='Ngày trả phòng', required=True)
    duration = fields.Integer(string='Số đêm lưu trú', compute='_compute_duration', store=True)
    total_amount = fields.Integer(string='Tổng thành tiền', compute='_compute_total_amount', store=True)
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Đã hủy')
    ], string='Trạng thái', default='draft', required=True)
    
    # Relationships
    customer_id = fields.Many2one('hotel.customer', string='Khách hàng', required=True)
    room_id = fields.Many2one('hotel.room', string='Phòng', required=True)
    service_ids = fields.Many2many('hotel.service', string='Dịch vụ')
    
    # Computed fields
    room_price_per_night = fields.Integer(string='Giá phòng/đêm', related='room_id.price_per_night', store=True)
    room_status = fields.Selection(string='Trạng thái phòng', related='room_id.status', store=True)
    service_total = fields.Integer(string='Tổng tiền dịch vụ', compute='_compute_service_total')
    currency_id = fields.Many2one('res.currency', string='Tiền tệ', default=lambda self: self.env.company.currency_id)
    
    @api.depends('check_in', 'check_out')
    def _compute_duration(self):
        for booking in self:
            if booking.check_in and booking.check_out:
                check_in = fields.Date.from_string(booking.check_in)
                check_out = fields.Date.from_string(booking.check_out)
                if check_out > check_in:
                    booking.duration = (check_out - check_in).days
                else:
                    booking.duration = 0
            else:
                booking.duration = 0
    
    @api.depends('service_ids')
    def _compute_service_total(self):
        for booking in self:
            booking.service_total = sum(service.price for service in booking.service_ids)
    
    @api.depends('duration', 'room_price_per_night', 'service_ids.price')
    def _compute_total_amount(self):
        for booking in self:
            room_amount = booking.duration * booking.room_price_per_night if booking.duration else 0
            service_amount = sum(service.price for service in booking.service_ids)
            booking.total_amount = room_amount + service_amount
    
    @api.onchange('check_in')
    def _onchange_check_in(self):
        if self.check_in:
            check_in_date = fields.Date.from_string(self.check_in)
            next_day = check_in_date + timedelta(days=1)
            self.check_out = fields.Date.to_string(next_day)
    
    @api.onchange('room_id')
    def _onchange_room_id(self):
        if self.room_id and self.room_id.status == 'maintenance':
            return {
                'warning': {
                    'title': 'Cảnh báo',
                    'message': 'Phòng này đang bảo trì, vui lòng chọn phòng khác!'
                }
            }
    
    @api.constrains('check_in', 'check_out')
    def _check_dates(self):
        for booking in self:
            if booking.check_in and booking.check_out:
                if booking.check_in < fields.Date.today():
                    raise ValidationError(_('Ngày nhận phòng không được nhỏ hơn ngày hiện tại!'))
                if booking.check_out <= booking.check_in:
                    raise ValidationError(_('Ngày trả phòng không hợp lệ!'))
    
    @api.constrains('room_id')
    def _check_room_status(self):
        # Constraint này có thể gây xung đột khi đang ở trạng thái confirmed (phòng đã occupied chính bởi booking này)
        # Nên chỉ check khi tạo mới hoặc khi sửa ở trạng thái draft
        for booking in self:
            if booking.state == 'draft' and booking.room_id and booking.room_id.status == 'occupied':
                # Tuy nhiên, validation logic chính nằm ở action_confirm
                pass
    
    @api.constrains('room_id', 'check_in', 'check_out', 'state')
    def _check_room_availability(self):
        for booking in self:
            # Chỉ check khi có đủ thông tin và booking không phải là đã hủy
            if booking.check_in and booking.check_out and booking.state != 'cancel':
                domain = [
                    ('id', '!=', booking.id),
                    ('room_id', '=', booking.room_id.id),
                    ('state', 'in', ['confirmed', 'done']), # Check trùng với đơn Đã xác nhận hoặc Đã hoàn thành
                    ('check_in', '<', booking.check_out),
                    ('check_out', '>', booking.check_in),
                ]
                count = self.search_count(domain)
                if count > 0:
                    raise ValidationError(_('Phòng %s đã có người đặt (hoặc đã ở) trong khoảng thời gian này!', booking.room_id.name))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('code') or vals.get('code') == '/':
                vals['code'] = self.env['ir.sequence'].next_by_code('hotel.booking') or 'SEQUENCE-NOT-FOUND'
            # Logic check status occupied chỉ là check thời điểm hiện tại
            if vals.get('room_id'):
                room = self.env['hotel.room'].browse(vals['room_id'])
                # Không chặn cứng ở create vì có thể đặt trước cho tương lai, logic chặn chính xác nằm ở Check Availability (_check_room_availability)
                pass 
        return super(HotelBooking, self).create(vals_list)
    
    def write(self, vals):
        # Override write để handle logic khi sửa state trực tiếp (nếu có, dù UI đã chặn) hoặc các thay đổi khác
        # Nhưng logic chính shift sang buttons
        return super(HotelBooking, self).write(vals)

    def action_confirm(self):
        for booking in self:
            if booking.state == 'draft':
                if booking.room_id.status in ['maintenance', 'occupied']:
                    raise ValidationError(_('Phòng đang bảo trì hoặc đã có người ở. Không thể check-in!'))
                
                # Check availability theo thời gian
                booking._check_room_availability()
                
                # Chuyển trạng thái phòng sang 'Đang ở' (Occupied)
                booking.room_id.status = 'occupied'
                booking.state = 'confirmed'
    
    def action_done(self):
        for booking in self:
            if booking.state == 'confirmed':
                # Khi khách trả phòng, chuyển trạng thái phòng về 'Trống' (Available)
                booking.room_id.status = 'available'
                booking.state = 'done'

    def action_cancel(self):
        for booking in self:
            if booking.state == 'confirmed':
                 # Nếu đang giữ phòng thì phải trả lại phòng
                booking.room_id.status = 'available'
            booking.state = 'cancel'
    
    def action_draft(self):
        for booking in self:
            if booking.state == 'cancel':
                booking.state = 'draft'
    
    def unlink(self):
        for booking in self:
            if booking.state != 'draft':
                raise UserError(_('Không thể xóa booking đã xác nhận hoặc hoàn thành!'))
            # Nếu xóa booking nháp nhưng phòng vẫn đang bị đánh dấu occupied (trường hợp hiếm), ta reset lại
            if booking.room_id.status == 'occupied' and booking.state == 'confirmed':
                 booking.room_id.status = 'available'
        return super(HotelBooking, self).unlink()