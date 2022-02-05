# -*- coding: utf-8 -*-

from odoo import models, fields, api


# BUGTOFIX

#we inherit res_partner to modify the default value of customer

# class univision_contacts(models.Model):
#     _inherit ='res.partner'
    
#     customer = fields.Boolean(string='Is a Customer', default=True,
#                                help="Check this box if this contact is a customer. It can be selected in sales orders. Default value set to false.")

#     @api.multi
#     def open_record(self): 
#         return {'type': 'ir.actions.act_window', 
#                 'res_model': 'res.partner', 
#                 'name': 'Contacts', 
#                 'view_type': 'form', 
#                 'view_mode': 'form', 
#                 'res_id': self.id, 
#                 'target': 'current'}
    
#     @api.multi
#     def action_open_new_tab(self):

#         for rec in self:

#             base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')

            
#             menu = self.env.ref('contacts.menu_contacts')
#             action = self.env.ref('contacts.action_contacts')

#             record_url = base_url + "/web#id=" + str(self.id) + "&action=" + str(action.id) + "&model=res.partner&view_type=form&menu_id=" + str(menu.id)

#             client_action = {

#                 'type': 'ir.actions.act_url',

#                 'name': "Contact",


#                 'target': 'new',

#                 'url': record_url}

#         return client_action
            
#     _name = 'univision_contacts.univision_contacts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100