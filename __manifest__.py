# -*- coding: utf-8 -*-
{
    'name': "Dispensario",

    'summary': """
        Resumen de qué hace el módulo de Dispensario
     """,

    'license': 'LGPL-3',


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
        'security/mi_dispensario_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/principio_views.xml',
        'views/bodega_views.xml',
        'views/clasifica_producto_views.xml',
        'views/cliente_views.xml',
        'views/forma_views.xml',
        'views/proveedor_views.xml',
        'views/laboratorio_views.xml',
        'views/movimiento_views.xml',
        'views/presentacion_views.xml',
        'views/orden_compra_views.xml'
        #'views/templates.xml',
    ]
}
