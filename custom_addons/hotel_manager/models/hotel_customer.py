from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'Khách hàng'
    _rec_name = 'name'
    
    name = fields.Char(string='Họ và tên', required=True)
    identity_card = fields.Char(string='CMND/CCCD')
    phone = fields.Char(string='Số điện thoại')
    email = fields.Char(string='Email')
    address = fields.Text(string='Địa chỉ')
    booking_count = fields.Integer(string='Số lần đặt phòng', default=0)  # Tạm thời để default
    
    _sql_constraints = [
        ('identity_card_unique', 'UNIQUE(identity_card)', 'Số CMND/CCCD phải là duy nhất!'),
    ]