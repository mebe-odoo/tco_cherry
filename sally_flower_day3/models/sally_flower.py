# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_flower = fields.Boolean('Is Flower')


class SallyFlower(models.Model):
    _inherit = 'sally.flower'
    _inherits = {'product.product': 'product_id'}

    product_id = fields.Many2one('product.product', string="Product")
