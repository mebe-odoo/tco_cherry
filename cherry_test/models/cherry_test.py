from odoo import models, fields


class CherryTest(models.Model):
    _name = 'cherry.test'
    _description = 'Cherry Test'

    name = fields.Char(string="Name", default='Mohamed')
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
        current_user = self.env.user
        current_company = self.env.company

        query = "SELECT name FROM cherry_table"
        self.env.cr.execute(query)
        results = self.env.cr.fetchdict()

        partner_ids = self.env['res.partner'].search([])
        # line 1 - returns all cherry.test records
        cherry_test_ids = self.search([], order='age DESC')
        first_name = cherry_test_ids[0]['name']
        # line 2 - return the first record it accesses
        cherry_test_id = self.search([], limit=1)
        first_name = cherry_test_id['name']

        # Context
        self._test_transactions_2()

    def _test_transactions_2(self):
        self = self.with_context({'return_value': True})
        cherry_test_id = self.search([], limit=1)
        cherry_test_id.name = 'Alaa'
        cherry_test_id.write({'name': 'Alaa'})
        raise Exception("Undo Changes")
        return True
