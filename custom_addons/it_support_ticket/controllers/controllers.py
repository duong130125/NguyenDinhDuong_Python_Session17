# -*- coding: utf-8 -*-
# from odoo import http


# class ItSupportTicket(http.Controller):
#     @http.route('/it_support_ticket/it_support_ticket', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/it_support_ticket/it_support_ticket/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('it_support_ticket.listing', {
#             'root': '/it_support_ticket/it_support_ticket',
#             'objects': http.request.env['it_support_ticket.it_support_ticket'].search([]),
#         })

#     @http.route('/it_support_ticket/it_support_ticket/objects/<model("it_support_ticket.it_support_ticket"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('it_support_ticket.object', {
#             'object': obj
#         })

