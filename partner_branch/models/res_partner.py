from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    branch_id = fields.Many2one(
        'res.company',
        string='Sucursal',
        ondelete='set null'
    )

    @api.constrains('branch_id', 'company_id')
    def _check_branch_company_consistency(self):
        for rec in self:
            if rec.branch_id and rec.company_id:
                if rec.branch_id not in rec.company_id.child_ids:
                    raise ValidationError("La sucursal debe ser una compañía hija de la compañía asignada.")
