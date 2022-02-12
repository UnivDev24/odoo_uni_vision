# -*- coding: utf-8 -*-
{
    'name': "univision_calendar",

    'summary': """
        Ce module personnalise le calendrier pour uni vision""",

    'description': """
        Il s'appuie sur le module de base du calendrier
    """,

    'author': "Uni Vision",
    'website': "http://www.yourcompany.com",
    'license':"LGPL-3"

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'calendar',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['calendar'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/calendar_view_univision.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}