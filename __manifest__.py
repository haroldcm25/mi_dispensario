# -*- coding: utf-8 -*-
{
    'name': "Dispensario",

    'summary': """
        Resumen de qué hace el módulo de Dispensario
     """,

    'description': """
        Descripción de Módulo dispensario
    """,

    'author': "Harold Campo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': [

    ],
    'application': True,
    # mi_dispensario_extended  -> mi_dispensario
    'installable': True,
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        #'views/templates.xml',
    ]
}
