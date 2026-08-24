# -*- coding: utf-8 -*-
from odoo import api, fields, models

class IsgSimulatorFinding(models.Model):
    _name = 'isg.simulator.finding'
    _description = 'İSG Simülasyon Bulgusu'
    _order = 'run_id, severity desc, estimated_penalty_amount desc'

    run_id = fields.Many2one(
        'isg.simulator.run',
        string='Simülasyon',
        required=True,
        ondelete='cascade',
        readonly=True
    )

    obligation_id = fields.Many2one(
        'isg.obligation',
        string='Yükümlülük',
        required=True,
        readonly=True
    )

    obligation_name = fields.Char(
        string='Yükümlülük Adı',
        related='obligation_id.name',
        store=True,
        readonly=True
    )

    compliance_status = fields.Selection(
        [
            ('compliant', 'Uyumlu'),
            ('pending', 'Beklemede'),
            ('overdue', 'Vadesi Geçmiş'),
            ('non_compliant', 'Uyumsuz'),
        ],
        string='Uygunluk Durumu',
        readonly=True
    )

    estimated_penalty_amount = fields.Float(
        string='Tahmini Ceza (TL)',
        readonly=True
    )

    severity = fields.Selection(
        [
            ('low', 'Düşük'),
            ('medium', 'Orta'),
            ('high', 'Yüksek'),
        ],
        string='Önem Seviyesi',
        readonly=True
    )

    recommendation = fields.Text(
        string='Öneri',
        readonly=True
    )

    created_date = fields.Datetime(
        string='Oluşturma Tarihi',
        default=lambda self: fields.Datetime.now(),
        readonly=True
    )
