from odoo import models, fields

class Student(models.Model):
    _name = "school.student"
    _description = "Student"

    name = fields.Char(required=True)
    age = fields.Integer()
    bio = fields.Text()
    is_active = fields.Boolean(default=True)
