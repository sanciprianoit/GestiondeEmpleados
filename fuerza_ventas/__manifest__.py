# -*- coding: utf-8 -*-
{
   
    'summary': "Fuerzas de Ventas",
    'description': """
        Módulo para gestionar visitas comerciales: programación, estatus, clientes, vendedores y métricas.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Sales',
    'version': '0.1',

    # Dependencias necesarias
    'depends': ['base', 'sale', 'crm', 'sales_team'],

    # Archivos que siempre se cargan
    'data': [
    'security/ir.model.access.csv',
    'views/sale_visit_views.xml', # ← debe ir antes
    'views/sale_visit_menu.xml',           # ← debe ir después
],


    # Archivos demo (opcional)
    'demo': [
        'demo/demo.xml',
    ],

    # Ícono institucional para el dashboard
    'images': ['static/description/icon.png'],

    # Configuración de aplicación
    'name': "Fuerza de Ventas",
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
