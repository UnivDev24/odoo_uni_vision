# -*- coding: utf-8 -*-
{
    'name': "univision_contacts",

    'summary': """
        This module customizes module contacts for UniVision   """,

    'description': """
        For instance default values / translation
    """,

    'author': "Uni Vision",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'contacts',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}