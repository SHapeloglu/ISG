# -*- coding: utf-8 -*-
from odoo import fields, models


class IsgCapaRiskExtension(models.Model):
    _inherit = 'isg.capa'

    source = fields.Selection(
        selection_add=[('risk_assessment', 'Risk Değerlendirmesi')],
        ondelete={'risk_assessment': 'cascade'},
    )
    risk_line_id = fields.Many2one(
        'isg.risk.line', string='Kaynak Risk Satırı',
        readonly=True, copy=False,
    )
