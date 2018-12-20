# -*- coding: utf-8 -*-
{
    'name': "univision_reports",

    'summary': """
        module containing reports personnalisation for uni vision""",

    'description': """
        personnalisation for invoice / headers / etc
    """,

    'author': "Uni Vision",
    'website': "http://uni-vision.fr/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'reports',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account, web, sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        'views/tpl_report_invoice_univision.xml',
        'views/tpl_report_external_univision.xml',
        'views/tpl_report_saleorder_univision.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}