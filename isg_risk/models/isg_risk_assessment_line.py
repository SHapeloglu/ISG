# -*- coding: utf-8 -*-
from odoo import api, fields, models

class IsgRiskAssessmentLine(models.Model):
    _name = 'isg.risk.assessment.line'
    _description = 'Risk Değerlendirmesi Satırı'
    _order = 'assessment_id, risk_score desc'

    assessment_id = fields.Many2one(
        'isg.risk.assessment',
        string='Değerlendirme',
        required=True,
        ondelete='cascade',
        readonly=True
    )

    hazard_id = fields.Many2one(
        'isg.risk.hazard',
        string='Tehlike',
        required=True,
        ondelete='cascade',
        readonly=False
    )

    hazard_category = fields.Selection(
        related='hazard_id.category',
        store=True,
        readonly=True
    )

    probability = fields.Selection(
        [
            ('1', '1 - Çok Düşük'),
            ('2', '2 - Düşük'),
            ('3', '3 - Orta'),
            ('4', '4 - Yüksek'),
            ('5', '5 - Çok Yüksek'),
        ],
        string='Olasılık',
        required=True,
        readonly=False
    )

    severity = fields.Selection(
        [
            ('1', '1 - Hafif'),
            ('2', '2 - Orta'),
            ('3', '3 - Ağır'),
            ('4', '4 - Çok Ağır'),
            ('5', '5 - Ölümcül'),
        ],
        string='Şiddet',
        required=True,
        readonly=False
    )

    risk_score = fields.Integer(
        string='Risk Puanı',
        compute='_compute_risk_score',
        store=True,
        readonly=True
    )

    risk_level = fields.Selection(
        [
            ('trivial', 'Önemsiz'),
            ('low', 'Düşük'),
            ('medium', 'Orta'),
            ('high', 'Yüksek'),
            ('critical', 'Kritik'),
        ],
        string='Risk Seviyesi',
        compute='_compute_risk_level',
        store=True,
        readonly=True
    )

    residual_risk_score = fields.Integer(
        string='Kalıntı Risk Puanı',
        help='Kontrol önlemleri uygulandıktan sonra kalan risk'
    )

    residual_risk_level = fields.Selection(
        [
            ('trivial', 'Önemsiz'),
            ('low', 'Düşük'),
            ('medium', 'Orta'),
            ('high', 'Yüksek'),
            ('critical', 'Kritik'),
        ],
        string='Kalıntı Risk Seviyesi',
        compute='_compute_residual_risk_level',
        store=True,
        readonly=True
    )

    control_ids = fields.One2many(
        'isg.risk.control',
        'assessment_line_id',
        string='Kontrol Önlemleri',
        readonly=False
    )

    description = fields.Text(
        string='Açıklama',
        help='Bu tehlike hakkında ek bilgiler'
    )

    @api.depends('probability', 'severity')
    def _compute_risk_score(self):
        """Risk puanı = olasılık × şiddet"""
        for record in self:
            prob = int(record.probability) if record.probability else 1
            sev = int(record.severity) if record.severity else 1
            record.risk_score = prob * sev

    @api.depends('risk_score')
    def _compute_risk_level(self):
        """Risk seviyesi matristen"""
        for record in self:
            score = record.risk_score
            if score <= 3:
                record.risk_level = 'trivial'
            elif score <= 6:
                record.risk_level = 'low'
            elif score <= 12:
                record.risk_level = 'medium'
            elif score <= 20:
                record.risk_level = 'high'
            else:
                record.risk_level = 'critical'

    @api.depends('residual_risk_score')
    def _compute_residual_risk_level(self):
        """Kalıntı risk seviyesi"""
        for record in self:
            if not record.residual_risk_score:
                record.residual_risk_level = record.risk_level
            else:
                score = record.residual_risk_score
                if score <= 3:
                    record.residual_risk_level = 'trivial'
                elif score <= 6:
                    record.residual_risk_level = 'low'
                elif score <= 12:
                    record.residual_risk_level = 'medium'
                elif score <= 20:
                    record.residual_risk_level = 'high'
                else:
                    record.residual_risk_level = 'critical'
