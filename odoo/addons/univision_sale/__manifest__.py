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
    'license':"LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': [''],

    # always loaded
    'data': [        
        'report/sale_report_templates.xml',
        'report/sale_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}