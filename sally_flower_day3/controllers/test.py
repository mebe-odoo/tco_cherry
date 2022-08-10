from odoo.http import Controller, route, request


class TestController(Controller):

    @route('/test', auth='public', type='http')
    def test(self, name=None, **kwargs):
        return request.render('sally_flower_day3.test', {
            'partner_ids': request.env['res.partner'].search([('name', 'ilike', '%' + name + '%')] if name else []),
            'show_header': True
        })
