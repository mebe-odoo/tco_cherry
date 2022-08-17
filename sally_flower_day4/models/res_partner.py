from odoo import models, fields, api
from odoo.osv import expression


class ResPartner(models.Model):
    _inherit = 'res.partner'


    # Use the name_get function to display the labels of the partners rendered in a many2one field or a many2many field
    # using the many2many_tags widget
    def name_get(self):
        """
            Override
        """
        result = []
        for partner in self:
            name = '%s - %s' % (partner.name, partner.email)
            result.append((partner.id, name))
        return result

    # Use the _name_search to customize what fields/logic is used to filter partners depending on what you write
    # in a many2one field widget
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        """
            Override
        """
        args = args or []
        domain = ['|', '|', ('name', operator, name), ('email', operator, name), ('phone', operator, name)]
        return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)

    """
        DOMAIN 1:   [('name', '=', 'Mohamed')]
        DOMAIN 2:   [('email', '=', 'moh@test.com')]
        
        DOMAIN: DOMAIN 1 AND DOMAIN 2  ||  DOMAIN 1 OR DOMAIN 2
        DOMAIN: ['&', ('name', '=', 'Mohamed'), ('email', '=', 'moh@test.com')]  ||  ['|', ('name', '=', 'Mohamed'), ('email', '=', 'moh@test.com')]
        
        
        
        ['|', ('name', '=', 'Mohamed'), '&', ('email', '=', 'moh@test.com'), '&', ('phone', '=', 'moh@test.com'), '|', ('mobile', '=', 'moh@test.com'), ('street', '=', 'moh@test.com')]
        
        OR, AND
        
        DOMAIN = expression.AND([DOMAIN 1, DOMAIN 2])
        DOMAIN = expression.OR([ expression.AND([DOMAIN 1, DOMAIN 2]), [('phone', '=', 'moh@test.com')]])
    """