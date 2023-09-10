# -*- coding: utf-8 -*-
{
    'name': "univision_account",

    'summary': """
        module containing account personnalisation for uni vision""",

    'description': """
        personnalisation for account module
    """,

    'author': "Uni Vision",
    'website': "http://uni-vision.fr/",
    'license':"LGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'account',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'views/account_report.xml',
        'views/report_invoice.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}