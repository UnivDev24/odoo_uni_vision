# -*- coding: utf-8 -*-
from odoo import http

# class UnivisionWeb(http.Controller):
#     @http.route('/univision_web/univision_web/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/univision_web/univision_web/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('univision_web.listing', {
#             'root': '/univision_web/univision_web',
#             'objects': http.request.env['univision_web.univision_web'].search([]),
#         })

#     @http.route('/univision_web/univision_web/objects/<model("univision_web.univision_web"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('univision_web.object', {
#             'object': obj
#         })