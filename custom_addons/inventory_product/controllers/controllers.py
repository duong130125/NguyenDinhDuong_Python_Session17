# -*- coding: utf-8 -*-
# from odoo import http


# class InventoryProduct(http.Controller):
#     @http.route('/inventory_product/inventory_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory_product/inventory_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory_product.listing', {
#             'root': '/inventory_product/inventory_product',
#             'objects': http.request.env['inventory_product.inventory_product'].search([]),
#         })

#     @http.route('/inventory_product/inventory_product/objects/<model("inventory_product.inventory_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory_product.object', {
#             'object': obj
#         })

