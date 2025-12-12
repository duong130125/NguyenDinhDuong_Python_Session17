from odoo import fields, models

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Title')
    pages = fields.Integer(string='Pages', default=100)
    summary = fields.Text(string='Summary', copy=False)
