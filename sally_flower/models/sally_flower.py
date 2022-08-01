# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SallyFlower(models.Model):
    _name = 'sally.flower'
    _description = 'Sally Flowers'
    _rec_name = 'common_name'

    common_name = fields.Char("Common Name")
    scientific_name = fields.Char("Scientific Name")

    season_start_date = fields.Date("Season Start Date")
    season_end_date = fields.Date("Season End Date")

    watering_frequency = fields.Integer("Watering Frequency")
    watering_amount = fields.Float("Watering Amount")

    variant_ids = fields.One2many('sally.flower.variant', 'flower_id')

    def _new_func(self):
        return self


# Class Inheritance - Just add features to an existing model


class SallyFlowerExtended(models.Model):
    _inherit = 'sally.flower'

    new_name = fields.Char('New Name')


class FlowerMixin(models.AbstractModel):
    _name = "flower.mixin"

    color = fields.Selection([('blue', 'Blue'), ('red', 'Red'), ('yellow', 'Yellow')])
    is_flower = fields.Boolean('Is Flower')
    caretaker_id = fields.Many2one('res.partner', string='Caretaker')
    length = fields.Float('Length of the Flower')


class SallyFlowerExtendedMixin(models.Model):
    _name = 'sally.flower'
    _inherit = ['sally.flower', 'image.mixin', 'flower.mixin', 'website.published.mixin']

    @api.depends_context('lang')
    def _compute_website_url(self):
        for record in self:
            record.website_url = '/flowers'


# Prototype Inheritance - Copy existing features to a new model


class SallyFlowerNew(models.Model):
    _name = 'sally.flower.new'
    _inherit = 'sally.flower'


# Delegation Inheritance - Copy existing features to a new model


class SallyFlowerVariant(models.Model):
    _name = 'sally.flower.variant'
    _inherits = {'sally.flower': 'flower_id'}

    flower_id = fields.Many2one('sally.flower', string="Flower", required=True)

    def _new_func_variant(self):
        # This will not work, because delegation inheritance will not copy over the functions, only the fields
        return self._new_func()
