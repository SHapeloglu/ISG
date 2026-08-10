from odoo import models, fields


class IsgCapaRiskExt(models.Model):
    _inherit = 'isg.capa'

    risk_assessment_id = fields.Many2one(
        'isg.risk.assessment',
        string='İlgili Risk Değerlendirmesi',
        ondelete='set null',
    )
