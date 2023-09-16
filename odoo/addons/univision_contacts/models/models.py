# -*- coding: utf-8 -*-
from odoo import models

# we inherit res_partner to modify the default value of customer
class ResPartner(models.Model):

    _inherit = 'res.partner'

    def action_open_new_tab(self):
        """Open child contact form from the parent partner form view"""
        return {
            "type": "ir.actions.act_window",
            "res_model": "res.partner",
            "res_id": self.id,
            "view_mode": "form",
            "target": "current",
        }

