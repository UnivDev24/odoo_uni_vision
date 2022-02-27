# -*- coding: utf-8 -*-
{
    'name': "univision_contacts",

    'summary': """
        This module customizes module contacts for UniVision   """,

    'description': """
        For instance default values / translation
        version 0.3 : companies' contact not opened as a popup but as a form
    """,

    'author': "Uni Vision",
    'website': "http://www.yourcompany.com",
    'license':"LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'contacts',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        'views/partner_view.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}