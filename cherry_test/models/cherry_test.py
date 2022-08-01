from odoo import models, fields


class CherryTest(models.Model):
    _name = 'cherry.test'
    _description = 'Cherry Test'

    name = fields.Char(string="Name New", default='Mohamed')
    age = fields.Integer(default=28)

    is_blue = fields.Boolean()

    birth_date = fields.Date()
    birth_time = fields.Datetime()

    partner_id = fields.Many2one('res.partner', readonly=True,
                                 domain=['|', ('name', 'ilike', 'M%'), ('name', 'ilike', 'A%')],
                                 default=lambda self: self.env['res.partner'].browse(3))
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)

    amount_float = fields.Float()
    amount_monetary = fields.Monetary(currency_field='currency_id')

    def action_test_transactions(self):
        res = self._test_transactions_1()
        return res

    def _test_transactions_1(self):
        self = self.with_context(lang='fr_FR')
        return self._test_transactions_2()

    def _test_transactions_2(self):
        return True
