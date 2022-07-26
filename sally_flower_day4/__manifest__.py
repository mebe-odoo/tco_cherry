# -*- coding: utf-8 -*-
{
    'name': "Sally Flower (Day 4)",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sally_flower_day3'],

    # always loaded
    'data': [
        # 'security/sally_flower_security.xml',
        'security/ir.model.access.csv',
        'views/sally_flower_views.xml',
        'report/report_sally_flower.xml',
        'data/ir_actions_server.xml',
        'data/report_paperformat.xml',
        'data/ir_actions_report.xml',
        'data/ir_cron.xml',
        'data/sally_flower.xml',
    ]
}
