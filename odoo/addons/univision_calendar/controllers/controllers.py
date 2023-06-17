# -*- coding: utf-8 -*-
from odoo import http

# class UnivisionCalendar(http.Controller):
#     @http.route('/univision_calendar/univision_calendar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/univision_calendar/univision_calendar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('univision_calendar.listing', {
#             'root': '/univision_calendar/univision_calendar',
#             'objects': http.request.env['univision_calendar.univision_calendar'].search([]),
#         })

#     @http.route('/univision_calendar/univision_calendar/objects/<model("univision_calendar.univision_calendar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('univision_calendar.object', {
#             'object': obj
#         })