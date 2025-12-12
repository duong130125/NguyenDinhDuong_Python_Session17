from odoo import models, fields

class CompanyEmployee(models.Model):
    _name = 'company.employee'
    _description = 'Company Employee'

    name = fields.Char(string='Employee Name', required=True)

    position = fields.Selection(
        [
            ('staff', 'Staff'),
            ('leader', 'Leader'),
            ('manager', 'Manager'),
        ],
        string='Position',
        default='staff'
    )

    is_active = fields.Boolean(string='Active', default=True)
