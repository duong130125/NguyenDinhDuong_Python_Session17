from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = 'Loại phòng khách sạn'
    
    name = fields.Char(string='Tên loại phòng', required=True)
    code = fields.Char(string='Mã loại')
    description = fields.Text(string='Mô tả')
    
    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Mã loại phòng phải là duy nhất!'),
    ]