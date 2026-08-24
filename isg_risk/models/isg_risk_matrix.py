# -*- coding: utf-8 -*-
from odoo import api, fields, models

class IsgRiskMatrix(models.Model):
    _name = 'isg.risk.matrix'
    _description = 'Risk Matrisi (Olasılık × Şiddet)'
    _order = 'probability, severity'

    probability = fields.Selection(
        [
            ('1', '1 - Çok Düşük'),
            ('2', '2 - Düşük'),
            ('3', '3 - Orta'),
            ('4', '4 - Yüksek'),
            ('5', '5 - Çok Yüksek'),
        ],
        string='Olasılık',
        required=True
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
        required=True
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

    color = fields.Char(
        string='Renk',
        compute='_compute_color',
        store=True,
        readonly=True
    )

    description = fields.Text(
        string='Açıklama'
    )

    @api.depends('probability', 'severity')
    def _compute_risk_score(self):
        """Risk puanı = olasılık (1-5) × şiddet (1-5)"""
        for record in self:
            prob = int(record.probability) if record.probability else 1
            sev = int(record.severity) if record.severity else 1
            record.risk_score = prob * sev

    @api.depends('risk_score')
    def _compute_risk_level(self):
        """Risk seviyesi puan aralığına göre"""
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

    @api.depends('risk_level')
    def _compute_color(self):
        """Risk seviyesine göre renk"""
        color_map = {
            'trivial': '#00AA00',      # Yeşil
            'low': '#77DD77',          # Açık Yeşil
            'medium': '#FFDD00',       # Sarı
            'high': '#FF8800',         # Turuncu
            'critical': '#FF0000',     # Kırmızı
        }
        for record in self:
            record.color = color_map.get(record.risk_level, '#FFFFFF')

    _sql_constraints = [
        ('unique_matrix', 'unique(probability, severity)', 'Bu olasılık-şiddet kombinasyonu zaten tanımlanmış.'),
    ]
