{
    'name': "Gestión de Inducciones para Empleados",
    'summary': "Módulo para gestionar indicaciones e inducciones a empleados",
    'description': """
        Este módulo permite llevar registro de las indicaciones dadas a empleados,
        con tipos de inducción y items específicos.
    """,
    'author': "Tu Nombre",
    'website': "https://www.tusitio.com",
    'category': 'Human Resources',
    'version': '1.0',
    'depends': ['base', 'hr', 'web'],

    'data': [
    'security/ir.model.access.csv',
    'data/ir_sequence_data.xml',
    'views/tipo_induccion_views.xml',  
    'views/tipo_capacitacion_views.xml',
    'views/capacitador_views.xml', 
    'views/acta.xml',                  # 👉 Primero la vista
    'views/action_asignacion.xml',     # 👉 Después la acción que la usa
    'views/asignacion_views.xml',
    'views/asignacion_capacitacion_views.xml',
    'views/acta_capacitacion_views.xml',
    'views/menu.xml',
    'views/asignacion_report_button.xml',
    'reports/asignacion_report.xml',
    'views/report_acta_induccion.xml',
    'views/actas_participantes.xml',
    'views/reporte_acta_individual_template.xml',
],


    'assets': {
        'web.report_assets_common': [
            'induccion_emple/static/src/img/logo.png',
        ],
    },

    'images': ['static/description/icon.png'],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
