# -*- coding: utf-8 -*-
from odoo import models

# we inherit res_partner to modify the default value of customer
class ResPartner(models.Model):

    _inherit = 'res.partner'

    # def action_open_new_tab(self):
    #     """Open child contact form from the parent partner form view"""
    #     return {
    #         "type": "ir.actions.act_window",
    #         "res_model": "res.partner",
    #         "res_id": self.id,
    #         "view_mode": "form",
    #         "target": "new",
    #     }
    #


    def open_record(self):
        return {'type': 'ir.actions.act_window',
                'res_model': 'res.partner',
                'name': 'Contacts',
                'view_type': 'form',
                'view_mode': 'form',
                'res_id': self.id,
                'target': 'current'}

    def action_open_new_tab(self):
        for rec in self:
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')

            menu = self.env.ref('contacts.menu_contacts')
            action = self.env.ref('contacts.action_contacts')

            record_url = base_url + "/web#id=" + str(self.id) + "&action=" + str(
                action.id) + "&model=res.partner&view_type=form&menu_id=" + str(menu.id)

            return {

                'type': 'ir.actions.act_url',
                'name': "Contact",
                'target': 'new',
                'url': record_url}

