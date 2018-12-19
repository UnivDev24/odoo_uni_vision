# -*- coding: utf-8 -*-
from odoo import http

# class ReportsModule(http.Controller):
#     @http.route('/reports_module/reports_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reports_module/reports_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reports_module.listing', {
#             'root': '/reports_module/reports_module',
#             'objects': http.request.env['reports_module.reports_module'].search([]),
#         })

#     @http.route('/reports_module/reports_module/objects/<model("reports_module.reports_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reports_module.object', {
#             'object': obj
#         })