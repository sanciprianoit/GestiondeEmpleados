{
    'name': 'Partner Branch Extension',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Agrega campo Sucursal al formulario de Contactos',
    'author': 'Rafael',
    'depends': ['base'],
    'data': [
   'security/ir.model.access.csv',
    'views/res_partner_view.xml',
    ],
    'installable': True,
    'application': False,
}
