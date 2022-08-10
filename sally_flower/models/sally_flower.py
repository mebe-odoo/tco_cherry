# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SallyFlower(models.Model):
    _name = 'sally.flower'
    _description = 'Sally Flowers'
    _rec_name = 'common_name'
    _inherits = {'product.product': 'product_id'}

    product_id = fields.Many2one('product.product', string="Product")

    common_name = fields.Char("Common Name", required=True)
    scientific_name = fields.Char("Scientific Name", require=True)

    season_start_date = fields.Date("Season Start Date")
    season_end_date = fields.Date("Season End Date")

    watering_frequency = fields.Integer("Watering Frequency")
    watering_amount = fields.Float("Watering Amount")

    partner_id = fields.Many2one('res.partner', string='Caretaker', ondelete='restrict', domain=[('name', 'like', 'M%')], context={'default_email': 'test@test.com'})
    email = fields.Char(related="partner_id.email")

    partner_ids = fields.Many2many('res.partner', 'partner_flower_relation', 'flower_id', 'partner_id', limit=2)

    variant_ids = fields.One2many('sally.flower.variant', 'flower_id')

    def _new_func(self):
        return self


# region Class Inheritance - Just add features to an existing model

class SallyFlowerExtended(models.Model):
    _inherit = 'sally.flower'

    new_name = fields.Char('New Name')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    flower_ids = fields.One2many('sally.flower', 'partner_id', string="Flowers")

# endregion

# region Class Inheritance - Use Mixins to add features to an existing model


class FlowerMixin(models.AbstractModel):
    _name = "flower.mixin"

    color = fields.Selection([('blue', 'Blue'), ('red', 'Red'), ('yellow', 'Yellow')])
    is_flower = fields.Boolean('Is Flower')
    # caretaker_id = fields.Many2one('res.partner', string='Caretaker')
    length = fields.Float('Length of the Flower')


class SallyFlowerExtendedMixin(models.Model):
    _name = 'sally.flower'
    _inherit = ['sally.flower', 'image.mixin', 'flower.mixin', 'website.published.mixin']

    @api.depends_context('lang')
    def _compute_website_url(self):
        for record in self:
            record.website_url = '/flowers/' + record.common_name

# endregion

# region Prototype Inheritance - Copy existing features to a new model


class SallyFlowerNew(models.Model):
    _name = 'sally.flower.new'
    _inherit = ['sally.flower']

    partner_ids = fields.Many2many('res.partner', 'partner_flower_relation2', 'partner_id', 'flower_id')


# endregion

# region Delegation Inheritance - Copy existing features to a new model


class SallyFlowerVariant(models.Model):
    _name = 'sally.flower.variant'
    _inherits = {
        'sally.flower': 'flower_id',
    }

    flower_id = fields.Many2one('sally.flower', string="Flower", required=True)

    def _new_func_variant(self):
        # This will not work, because delegation inheritance will not copy over the functions, only the fields
        return self._new_func()

# endregion