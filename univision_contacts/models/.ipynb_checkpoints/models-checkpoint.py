# -*- coding: utf-8 -*-

from odoo import models, fields, api


#we inherit res_partner to modify the default value of customer

class univision_contacts(models.Model):
    _inherit ='res.partner'
    
    customer = fields.Boolean(string='Is a Customer', default=True,
                               help="Check this box if this contact is a customer. It can be selected in sales orders. Default value set to false.")

    @api.multi
    def open_record(self): 
        return {'type': 'ir.actions.act_window', 
                'res_model': 'res.model', 
                'name': 'Record name', 
                'view_type': 'form', 
                'view_mode': 'form', 
                'res_id': self.id, 
                'target': 'current'}
    
#     _name = 'univision_contacts.univision_contacts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100