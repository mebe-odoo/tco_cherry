from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug


class SallyFlowerExtendedMixin(models.Model):
    _name = 'sally.flower'
    _inherit = ['sally.flower', 'website.published.mixin']

    @api.depends_context('lang')
    def _compute_website_url(self):
        for record in self:
            record.website_url = '/flowers/' + slug(record)