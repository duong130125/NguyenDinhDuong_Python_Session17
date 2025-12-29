from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Phòng khách sạn'
    _rec_name = 'name'
    
    name = fields.Char(string='Số phòng', required=True)
    floor = fields.Integer(string='Tầng')
    price_per_night = fields.Integer(string='Giá mỗi đêm', required=True)
    status = fields.Selection([
        ('available', 'Trống'),
        ('occupied', 'Đang ở'),
        ('maintenance', 'Bảo trì')
    ], string='Trạng thái', default='available', required=True)
    description = fields.Text(string='Mô tả')
    type_id = fields.Many2one('hotel.room.type', string='Loại phòng', required=True)
    booking_count = fields.Integer(string='Số lần đặt', default=0)  # Tạm thời để default
    
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Số phòng phải là duy nhất!'),
        ('price_positive', 'CHECK(price_per_night > 0)', 'Giá phòng phải lớn hơn 0!'),
    ]
    
    @api.constrains('price_per_night')
    def _check_price(self):
        for room in self:
            if room.price_per_night <= 0:
                raise ValidationError(_('Giá phòng phải lớn hơn 0!'))