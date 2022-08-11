# -*- coding: utf-8 -*-

from odoo import models, fields


class SallyFlower(models.Model):
    _inherit = 'sally.flower'

    def action_custom_python(self):
        action = self.env.ref('sally_flower.sally_flower_action').read()[0]
        action['domain'] = [('common_name', '=', 'Test2')]
        return action

    def action_custom_url(self):
        return {
            'type': 'ir.actions.act_url',
            'name': 'Redirect to Google',
            'url': 'https://google.com',
            'target': 'new'
        }

    def server_action_set_scientific_name(self):
        self.write({
            'scientific_name': 'Science'
        })