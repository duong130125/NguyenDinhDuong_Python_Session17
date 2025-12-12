from odoo import models, fields

class InventoryProduct(models.Model):
    _name = 'inventory.product'
    _description = 'Inventory Product'

    name = fields.Char()
    price = fields.Float()
    stock = fields.Integer()
