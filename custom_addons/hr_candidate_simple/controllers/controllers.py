# -*- coding: utf-8 -*-
# from odoo import http


# class HrCandidateSimple(http.Controller):
#     @http.route('/hr_candidate_simple/hr_candidate_simple', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_candidate_simple/hr_candidate_simple/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_candidate_simple.listing', {
#             'root': '/hr_candidate_simple/hr_candidate_simple',
#             'objects': http.request.env['hr_candidate_simple.hr_candidate_simple'].search([]),
#         })

#     @http.route('/hr_candidate_simple/hr_candidate_simple/objects/<model("hr_candidate_simple.hr_candidate_simple"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_candidate_simple.object', {
#             'object': obj
#         })

