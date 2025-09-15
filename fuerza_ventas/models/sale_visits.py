# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleVisit(models.Model):
    _name = 'sale.visit'
    _description = 'Visita Comercial'

    name = fields.Char("Etiqueta", required=True)
    salesperson_id = fields.Many2one('hr.employee', string="Vendedor")
    partner_id = fields.Many2one('res.partner', string="Cliente")
    branch_id = fields.Many2one('res.company', string="Sucursal")

    direccion_cliente = fields.Char("Dirección del Cliente", readonly=True, store=True)

    visit_type = fields.Selection([
        ('commercial', 'Comercial'),
        ('client_intake', 'Toma de cliente'),
        ('collection', 'Cobranza'),
    ], string="Tipo de Visita", default="commercial")

    visit_date = fields.Date("Fecha de visita", default=fields.Date.context_today)
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
    ], string="Prioridad", default='0', required=True)

    status = fields.Selection([
        ('to_visit', 'Por Visitar'),
        ('not_visited', 'No Visitado'),
        ('visiting', 'Visitando'),
        ('effective', 'Efectiva'),
        ('not_effective', 'No Efectiva'),
    ], string="Estatus", default="to_visit")

    line_ids = fields.One2many('sale.visit.line', 'visit_id', string="Líneas de la visita")
    parent_id = fields.Many2one('sale.visit.wrapper', string="Contenedor de Visitas")

    # 🔒 Control de edición
    can_edit = fields.Boolean(string="¿Puede editar?", default=False)

    def action_enable_edit(self):
        for record in self:
            record.can_edit = True

    def action_cancel_edit(self):
        for record in self:
            record.can_edit = False

    def write(self, vals):
        res = super().write(vals)
        if 'can_edit' not in vals:
            self.sudo().write({'can_edit': False})
        return res

    @api.constrains('can_edit')
    def _check_edit_permission(self):
        for record in self:
            if not record.can_edit and self.env.context.get('edit_attempt'):
                raise ValidationError("Debe presionar el botón 'Editar' antes de modificar este registro.")

    @api.model
    def get_kpis(self):
        return {state: self.search_count([('status', '=', state)])
                for state in ['to_visit', 'not_visited', 'visiting', 'effective', 'not_effective']}

    @api.onchange('partner_id')
    def _onchange_partner_info(self):
        if self.partner_id:
            if self.partner_id.user_id and self.partner_id.user_id.employee_ids:
                self.salesperson_id = self.partner_id.user_id.employee_ids[0]
            self.direccion_cliente = self.partner_id.contact_address
            self.name = f"Visita para {self.partner_id.name}" + (
                f" por {self.salesperson_id.name}" if self.salesperson_id else "")
            if self.partner_id.branch_id:
                self.branch_id = self.partner_id.branch_id  # 🏢 Hereda sucursal del contacto

    @api.onchange('repeat')
    def _onchange_repeat_toggle(self):
        if not self.repeat:
            self.frequency = False
            self.repeat_from = False

    @api.constrains('repeat', 'frequency', 'repeat_from')
    def _check_repeat_consistency(self):
        for record in self:
            if not record.repeat and (record.frequency or record.repeat_from):
                raise ValidationError("Los campos de frecuencia solo pueden llenarse si 'Repetir' está activado.")

    def action_button_map(self): return True
    def action_button_summary(self): return True
    def action_button_export(self): return True
    def action_button_history(self): return True


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
