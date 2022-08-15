# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date


class SallyFlower(models.Model):
    _inherit = 'sally.flower'

    is_watered = fields.Boolean('Is Watered', default=False)
    cron_message = fields.Char('Message')

    full_name = fields.Char("Full Name", compute="_compute_full_name",
                            # inverse="_inverse_full_name", search="_search_full_name"
                            )

    @api.onchange('common_name', 'scientific_name', 'is_watered')
    def _onchange_common_name(self):
        self.full_name = self.common_name

    # #[('full_name', '=', 'Ali Mohammed')]
    # def _search_full_name(self, operator, value):
    #     if operator == '=':
    #         return ['|', ('common_name', 'ilike', value), ('scientific_name', 'ilike', value)]
    #     return []

    @api.depends('common_name', 'scientific_name')
    @api.depends_context('lang')
    def _compute_full_name(self):
        for flower in self:
            flower.full_name = flower.common_name + flower.scientific_name

    def _inverse_full_name(self):
        for flower in self:
            flower.common_name = ''
            flower.scientific_name = ''

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

    def _cron_set_is_watered(self):
        flower_ids = self.search([])
        flower_ids.write({'cron_message': "Hi! This message was set from a shceduled action at %s" % datetime.now()})

    @api.constrains()
    def _check_test1(self):
        pass

    @api.onchange('common_name')
    def _check_test2(self):
        pass

    @api.depends('common_name')
    def _check_test3(self):
        pass

    def create(self, vals_list):
        for vals in vals_list:
            vals['common_name'] = 'OVERRIDDEN'
        return super(SallyFlower, self).create(vals_list)
