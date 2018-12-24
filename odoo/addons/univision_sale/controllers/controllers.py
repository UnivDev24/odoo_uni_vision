# -*- coding: utf-8 -*-
from odoo import http

# class UnivisionSale(http.Controller):
#     @http.route('/univision_sale/univision_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/univision_sale/univision_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('univision_sale.listing', {
#             'root': '/univision_sale/univision_sale',
#             'objects': http.request.env['univision_sale.univision_sale'].search([]),
#         })

#     @http.route('/univision_sale/univision_sale/objects/<model("univision_sale.univision_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('univision_sale.object', {
#             'object': obj
#         })