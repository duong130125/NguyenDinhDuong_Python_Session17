from odoo import models, fields

class Demo(models.Model): 
    _name = 'demo.hello'
    _description = 'CSDL dành cho việc demo'
    name = fields.Char(string = 'Tên', required = True)
    description = fields.Char(string = 'Mô tả')