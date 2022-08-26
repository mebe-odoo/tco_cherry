# -*- coding: utf-8 -*-

from odoo import models, fields, api, Command
from odoo.osv import expression
from datetime import datetime, date


class SallyFlower(models.Model):
    _name = 'sally.flower'
    _inherit = ['sally.flower', 'mail.thread']

    serial_number = fields.Char('Serial Number', tracking=True)
    watering_ids = fields.One2many('sally.flower.water', 'flower_id', string="Waterings")
    watering_count = fields.Integer("Watering Count", compute="_compute_watering_count")

    is_watered = fields.Boolean('Is Watered', default=False)
    cron_message = fields.Char('Message')

    full_name = fields.Char("Full Name", compute="_compute_full_name",
                            # inverse="_inverse_full_name", search="_search_full_name"
                            )

    @api.onchange('common_name', 'scientific_name', 'is_watered')
    def _onchange_common_name(self):
        # self.full_name = self.common_name
        self.write({'full_name': self.common_name})

    # #[('full_name', '=', 'Ali Mohammed')]
    # def _search_full_name(self, operator, value):
    #     if operator == '=':
    #         return ['|', ('common_name', 'ilike', value), ('scientific_name', 'ilike', value)]
    #     return []

    @api.depends('common_name', 'scientific_name')
    @api.depends_context('lang')
    def _compute_full_name(self):
        for flower in self:
            flower.full_name = ''
            if False:
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

    def _cron_post_message(self):
        flower_ids = self.search([])
        for flower in flower_ids:
            flower.message_post(body="Hi! This message was set from a shceduled action at %s" % datetime.now())

    @api.constrains()
    def _check_test1(self):
        pass

    @api.onchange('common_name')
    def _check_test2(self):
        pass

    @api.depends('common_name')
    def _check_test3(self):
        pass

    def test_model_methods(self):
        flower_ids = self.search([])

        # Filtered method
        filtered_flower_ids = flower_ids.filtered(lambda f: f.common_name == 'Test 2')

        # Mapped method
        mapped_flower_names = flower_ids.mapped('name')
        caretaker_names = flower_ids.mapped('partner_ids.name')

        # Sorted method
        # Sort by ID in DESCENDING order
        sorted_flower_ids = flower_ids.sorted('id', reverse=True)  # reverse=True means it's sorting in DESCENDING order
        # sort by the length of the flower names
        sorted_flower_ids_by_length = flower_ids.sorted(lambda f: len(f.name), reverse=True)

        # Filtered Domain method
        filtered_domain_flower_ids = flower_ids.filtered_domain([('name', '=', 'Test 2')])

        # Browse method
        flower_id = self.browse(22)
        flower_id.name = 'New Flower'
        flower_id.write({
            'name': 'New Flower'
        })
        flower_id.update({
            'name': 'Old Flower'
        })

        # Read method
        read_flower = filtered_flower_ids.read(['name', 'common_name', 'scientific_name'])

        # Search Read method
        search_read_flowers = self.search_read([('name', 'ilike', '%Test%')], fields=['common_name'])

        # Search Read method
        flower_count = self.search_count([('name', 'ilike', '%Test%')])

    def test_magic_numbers(self):
        flower_id = self.browse(22)

        # for flower in flower_ids:
        flower_id.write({
            'partner_ids': [

                # Unlink all partner_ids from the flower
                Command.clear(),
                # (5, 0, 0),

                # # Create a new res.partner record and link it to the flower
                Command.create({'name': 'Mohamed Ali', 'email': 'mohamed@smith.com'}),
                # (0, 0, {'name': 'Mohamed Ali', 'email': 'mohamed@smith.com'}),

                # Update partner with id 3 with then given dict of values
                Command.update(3, {'name': 'New Admin', 'email': 'ali@smith.com'}),
                # (1, 3, {'name': 'New Admin', 'email': 'ali@smith.com'}),
                #
                # # Deleting the partner with id 3 from the database
                Command.delete(24),
                # (2, 24, 0),
                #
                # Delete the relationship between the partner and the flower
                Command.unlink(7),
                # (3, 7, 0),
                #
                # # Link an existing res.partner record to the flower
                Command.link(7),
                # (4, 7, 0),
                #
                # # Unlink all existing records, then link a set of partners to the flower
                Command.set([7, 3]),
                # (6, 0, [7, 3])
            ]
        })

        # Create a new res.partner record and link it to the flower
        # flower.write({
        #     'partner_ids': [(1, 0, {'name': 'John Smith', 'email': 'john@smith.com'})]
        # })

    @api.model
    def default_get(self, fields):
        res = super(SallyFlower, self).default_get(fields)
        # res['name'] = 'Test 19'
        return res

    def _compute_watering_count(self):
        for flower in self:
            flower.watering_count = len(flower.watering_ids)

    def action_open_waterings(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Waterings',
            'res_model': 'sally.flower.water',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('id', 'in', self.watering_ids.ids)]
        }

    def water_flowers(self):
        for flower in self:
            flower.write({
                'watering_ids': [
                    # Empty our O2M field
                    Command.clear(),
                    (5, 0, 0),
                    # Create a new sally.flower.water record and link it to the O2M field
                    (0, 0, {'water_used': 10}),
                    Command.create({'water_used': 10}),
                    # Create a new sally.flower.water record and link it to the O2M field
                    (1, 10, {'water_used': 20}),
                    Command.update(10, {'water_used': 25}),
                    # Delete the water record completely from the DB
                    # (2, 10, 0),
                    # Command.delete(10),
                    # Remove the link to the water record from the flower's O2M field
                    (3, 10, 0),
                    Command.unlink(10),
                    # Add the link to the water record to the flower's O2M field
                    (4, 10, 0),
                    Command.link(10),
                    # Empty out the O2M field by removing the old references, and link a new set of waters
                    # (6, 0, [1, 2, 3]),
                    # Command.set([1, 2, 3]),
                ]
            })
    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         vals['common_name'] = 'OVERRIDDEN'
    #     return super(SallyFlower, self).create(vals_list)
    #
    # @api.model
    # def create(self, vals):
    #     vals['common_name'] = 'OVERRIDDEN'
    #     return super(SallyFlower, self).create(vals)
