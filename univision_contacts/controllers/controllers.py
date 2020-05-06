# -*- coding: utf-8 -*-
from odoo import http

# class UnivisionContacts(http.Controller):
#     @http.route('/univision_contacts/univision_contacts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/univision_contacts/univision_contacts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('univision_contacts.listing', {
#             'root': '/univision_contacts/univision_contacts',
#             'objects': http.request.env['univision_contacts.univision_contacts'].search([]),
#         })

#     @http.route('/univision_contacts/univision_contacts/objects/<model("univision_contacts.univision_contacts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('univision_contacts.object', {
#             'object': obj
#         })