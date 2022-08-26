from odoo import models, fields


class SallyFlowerWater(models.Model):
    _name = 'sally.flower.water'

    name = fields.Char("Name", compute="_compute_water_name")
    water_used = fields.Float("Amount of water used", default=1.0)
    flower_id = fields.Many2one('sally.flower', string="Flower")

    def _compute_water_name(self):
        for watering in self:
            watering.name = (watering.flower_id.name + ' - Water') if watering.flower_id else 'Watering'
