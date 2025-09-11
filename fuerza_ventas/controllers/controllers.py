# -*- coding: utf-8 -*-
# from odoo import http


# class FuerzaVentas(http.Controller):
#     @http.route('/fuerza_ventas/fuerza_ventas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fuerza_ventas/fuerza_ventas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fuerza_ventas.listing', {
#             'root': '/fuerza_ventas/fuerza_ventas',
#             'objects': http.request.env['fuerza_ventas.fuerza_ventas'].search([]),
#         })

#     @http.route('/fuerza_ventas/fuerza_ventas/objects/<model("fuerza_ventas.fuerza_ventas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fuerza_ventas.object', {
#             'object': obj
#         })

