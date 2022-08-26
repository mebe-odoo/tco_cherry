from odoo.http import Controller, route, request
from odoo.addons.http_routing.models.ir_http import slug

from odoo.addons.portal.controllers.portal import CustomerPortal

import json


class NewCustomerPortal(CustomerPortal):

    @route()
    def home(self, **kw):
        return request.make_response("Hello World", [('Content-Type', 'text/plain')])


class FlowerController(Controller):

    @route('/flowers/json/<int:flower_id>', auth='public', type='json')
    def flower_json(self, flower_id, **kwargs):
        flower = request.env['sally.flower'].sudo().browse(flower_id)
        return flower.read()[0]

    @route('/flowers/http/<int:flower_id>', auth='public', type='http')
    def flower_http(self, flower_id, **kwargs):
        flower = request.env['sally.flower'].sudo().browse(flower_id)
        return request.make_response(
            flower.read()[0],
            [('Content-Type', 'application/json')]
        )

    @route([
        '/flowers/<model("sally.flower"):flower>',
        '/f/<model("sally.flower"):flower>'
    ], auth='public', type='http', website=True, methods=["GET"])
    def flower_render(self, flower, **kwargs):
        return request.render("sally_flower_day7.flower_page", {'flower': flower})

    @route('/flowers/create', auth='public', type='http', methods=["POST"])
    def flower_create(self, **kwargs):
        flower_id = request.env['sally.flower'].create(kwargs)
        return request.redirect('/flowers/%s' % slug(flower_id))

