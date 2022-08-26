from odoo import api, fields, models, _


class SallyFlower(models.Model):
    _inherit = 'sally.flower'
    _rec_name = 'flower_sequence'

    flower_sequence = fields.Char("Flower Sequence", default="Draft FLower", readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['flower_sequence'] = self.env['ir.sequence'].next_by_code('sally.flower.year') or _('New')
        return super(SallyFlower, self).create(vals_list)
