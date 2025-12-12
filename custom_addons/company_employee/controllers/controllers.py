# -*- coding: utf-8 -*-
# from odoo import http


# class CompanyEmployee(http.Controller):
#     @http.route('/company_employee/company_employee', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_employee/company_employee/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_employee.listing', {
#             'root': '/company_employee/company_employee',
#             'objects': http.request.env['company_employee.company_employee'].search([]),
#         })

#     @http.route('/company_employee/company_employee/objects/<model("company_employee.company_employee"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_employee.object', {
#             'object': obj
#         })

