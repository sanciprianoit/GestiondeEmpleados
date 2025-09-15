# -*- coding: utf-8 -*-
{
    'name': "Fuerza de Ventas",
    'summary': "Fuerzas de Ventas",
    'description': """
        Módulo para gestionar visitas comerciales: programación, estatus, clientes, vendedores y métricas.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Sales',
    'version': '0.1',

    # 🔗 Dependencias necesarias
    'depends': ['base', 'sale', 'crm', 'sales_team', 'contacts', 'hr'],

    # 📂 Archivos que siempre se cargan
    'data': [
        'security/ir.model.access.csv',
        'views/sale_visit_views.xml',
        'views/sale_visit_menu.xml',
        # ← Vista heredada para agregar campo Sucursal
    ],

    # 📦 Archivos demo (opcional)
    'demo': [
        'demo/demo.xml',
    ],

    # 🖼️ Ícono institucional para el dashboard
    'images': ['static/description/icon.png'],

    # ⚙️ Configuración de aplicación
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
