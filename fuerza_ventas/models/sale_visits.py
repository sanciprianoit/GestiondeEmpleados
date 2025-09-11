# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleVisit(models.Model):
    _name = 'sale.visit'
    _description = 'Visita Comercial'

    name = fields.Char("Etiqueta", required=True)

    salesperson_id = fields.Many2one('hr.employee', string="Vendedor")
    partner_id = fields.Many2one('res.partner', string="Cliente")
    branch_id = fields.Many2one('res.company', string="Sucursal")

    visit_type = fields.Selection([
        ('commercial', 'Comercial'),
        ('client_intake', 'Toma de cliente'),
        ('collection', 'Cobranza'),
    ], string="Tipo de Visita", default="commercial")

    visit_date = fields.Date("Fecha de visita")
    repeat = fields.Boolean("Repetir")

    frequency = fields.Selection([
        ('weekly', 'Semanal'),
        ('biweekly', 'Quincenal'),
        ('monthly', 'Mensual'),
    ], string="Frecuencia")

    repeat_from = fields.Date("Repetir desde")

    priority_level = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Baja'),
        ('2', 'Media'),
        ('3', 'Alta')
    ], string="Prioridad", default='0', required=True, help="Prioridad de la visita")

    status = fields.Selection([
        ('to_visit', 'Por Visitar'),
        ('not_visited', 'No Visitado'),
        ('visiting', 'Visitando'),
        ('effective', 'Efectiva'),
        ('not_effective', 'No Efectiva'),
    ], string="Estatus", default="to_visit")

    line_ids = fields.One2many('sale.visit.line', 'visit_id', string="Líneas de la visita")
    parent_id = fields.Many2one('sale.visit.wrapper', string="Contenedor de Visitas")

    @api.model
    def get_kpis(self):
        result = {}
        for state in ['to_visit', 'not_visited', 'visiting', 'effective', 'not_effective']:
            result[state] = self.search_count([('status', '=', state)])
        return result

    @api.onchange('partner_id', 'salesperson_id')
    def _onchange_set_name(self):
        if self.partner_id and self.salesperson_id:
            self.name = f"Visita para {self.partner_id.name} por {self.salesperson_id.name}"

    # Métodos decorativos para los botones
    def action_button_map(self):
        """Botón decorativo: Mapa"""
        return True

    def action_button_summary(self):
        """Botón decorativo: Resumen"""
        return True

    def action_button_export(self):
        """Botón decorativo: Exportar"""
        return True

    def action_button_history(self):
        """Botón decorativo: Histórico"""
        return True


class SaleVisitLine(models.Model):
    _name = 'sale.visit.line'
    _description = 'Línea de Visita'

    name = fields.Char("Descripción", required=True)
    visit_id = fields.Many2one('sale.visit', string="Visita")

    priority_level = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Baja'),
        ('2', 'Media'),
        ('3', 'Alta'),
    ], string="Prioridad", default='0', required=True)

    status = fields.Selection([
        ('pending', 'Pendiente'),
        ('done', 'Hecho'),
    ], string="Estado", default="pending")
