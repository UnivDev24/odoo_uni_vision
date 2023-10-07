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
    'license': "LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Web/Theme',
    'version': '16.0.1.0.0',
    'assets': {
        'web.assets_frontend': [
            'univision_web/static/src/scss/report.scss',
            'univision_web/static/src/scss/layout_background.scss',
            'univision_web/static/src/scss/form_controller.scss'
            ],
        'web.report_assets_common': [
            'univision_web/static/src/scss/report.scss',
            'univision_web/static/src/scss/layout_background.scss',
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
