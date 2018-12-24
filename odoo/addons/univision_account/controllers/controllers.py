# -*- coding: utf-8 -*-
from odoo import http

# class UnivisionReports(http.Controller):
#     @http.route('/univision_reports/univision_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/univision_reports/univision_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('univision_reports.listing', {
#             'root': '/univision_reports/univision_reports',
#             'objects': http.request.env['univision_reports.univision_reports'].search([]),
#         })

#     @http.route('/univision_reports/univision_reports/objects/<model("univision_reports.univision_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('univision_reports.object', {
#             'object': obj
#         })