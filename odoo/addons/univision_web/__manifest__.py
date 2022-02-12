# -*- coding: utf-8 -*-
{
    'name': "univision_web",

    'summary': """
         module containing web personnalisation for uni vision""",

    'description': """
        personnalisation for web module
    """,

    'author': "Uni Vision",
    'website': "http://uni-vision.fr/",
    'license':"LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'web',
    'version': '0.2',
    'assets' : {
        'web.report_assets_common': [
            'static/scss/layout_background.scss',
            'static/scss/report.scss'
        ],
    },
    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [        
       'views/report_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}