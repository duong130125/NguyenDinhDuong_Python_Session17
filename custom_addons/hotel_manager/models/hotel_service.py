from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HotelService(models.Model):
    _name = 'hotel.service'
    _description = 'Dịch vụ khách sạn'
    
    name = fields.Char(string='Tên dịch vụ', required=True)
    price = fields.Integer(string='Giá dịch vụ', default=0)
    description = fields.Text(string='Mô tả')
    color = fields.Integer(string='Màu sắc')
    
    _sql_constraints = [
        ('price_positive', 'CHECK(price > 0)', 'Giá dịch vụ phải lớn hơn 0!'),
    ]
    
    @api.constrains('price')
    def _check_price(self):
        for service in self:
            if service.price <= 0:
                raise ValidationError(_('Giá dịch vụ phải lớn hơn 0!'))