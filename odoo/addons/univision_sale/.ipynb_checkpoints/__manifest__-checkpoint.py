# -*- coding: utf-8 -*-
{
    'name': "univision_sale",

    'summary': """
         module containing sale personnalisation for uni vision""",

    'description': """
        personnalisation for sale module
    """,

    'author': "Uni Vision",
    'website': "http://uni-vision.fr/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [        
        'report/sale_report_univision_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}