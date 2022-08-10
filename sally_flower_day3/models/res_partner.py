from odoo import fields, api, models


class partner(models.Model):
    _inherit = 'res.partner'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if self._context.get('created_from_embedded_views'):
                vals['name'] += ' - Created from Embedded Views'
        return super(partner, self).create(vals_list)