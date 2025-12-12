# -*- coding: utf-8 -*-
# from odoo import http


# class Training.course(http.Controller):
#     @http.route('/training.course/training.course', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/training.course/training.course/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('training.course.listing', {
#             'root': '/training.course/training.course',
#             'objects': http.request.env['training.course.training.course'].search([]),
#         })

#     @http.route('/training.course/training.course/objects/<model("training.course.training.course"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('training.course.object', {
#             'object': obj
#         })

