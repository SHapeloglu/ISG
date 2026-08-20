# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgMeasurementLimit(models.Model):
    _name = 'isg.measurement.limit'
    _description = 'Ölçüm Limiti (OEL/STEL)'
    _order = 'regulation_version, parameter_type, name'

    name = fields.Char(
        string='Limit Adı', required=True,
        help='Örn: Gürültü TWA (8-saat ağırlıklı ortalama)',
    )
    parameter_type = fields.Selection(
        [
            ('noise', 'Gürültü (dB)'),
            ('dust_inhalable', 'Toz — İnhalasyon (mg/m³)'),
            ('dust_respirable', 'Toz — Solunum (mg/m³)'),
            ('chemical_vapor', 'Kimyasal Buhar (ppm / mg/m³)'),
            ('vibration_hand', 'Titreşim — El (m/s²)'),
            ('vibration_body', 'Titreşim — Beden (m/s²)'),
            ('light_lux', 'Aydınlatma (Lux)'),
            ('thermal_pmv', 'Isıl Konfor — PMV'),
            ('thermal_ppd', 'Isıl Konfor — PPD (%)'),
            ('other', 'Diğer'),
        ],
        string='Parametre Türü', required=True,
    )
    chemical_id = fields.Many2one(
        'isg.chemical', string='Kimyasal (kimyasal parametreler için)',
        help='Kimyasal buhar limiti ise ilgili kimyasal seçin',
    )
    twa_value = fields.Float(
        string='TWA (8-saat ağırlıklı)',
        help='Time Weighted Average — örn: 85 dB, 5 mg/m³',
    )
    stel_value = fields.Float(
        string='STEL (15 dk kısa süreli)',
        help='Short Term Exposure Limit — örn: 90 dB, 10 mg/m³',
    )
    ceil_value = fields.Float(
        string='Tavana (CEIL)',
        help='Asla aşılmaması gereken üst limit',
    )
    unit = fields.Char(
        string='Birim', required=True,
        help='dB, mg/m³, ppm, Lux, m/s², vb.',
    )
    regulation_version = fields.Selection(
        [
            ('2024', 'ÇSGB 2024 Yönetmeliği'),
            ('2025', 'ÇSGB 2025 Yönetmeliği'),
            ('2026', 'ÇSGB 2026 Yönetmeliği'),
            ('ab_cls', 'AB CLP Tüzüğü'),
        ],
        string='Mevzuat Versiyonu', required=True,
        default='2026',
    )
    effective_date = fields.Date(
        string='Yürürlük Tarihi',
        help='Bu limit hangi tarihten itibaren geçerli',
    )
    notes = fields.Text(
        string='Notlar',
        help='Örn: Ek açıklamalar, kaynaklar, özel koşullar',
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket',
        default=lambda self: self.env.company,
    )
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_limit', 'UNIQUE(parameter_type, chemical_id, regulation_version)',
         'Bu parametre ve mevzuat kombinasyonu zaten mevcut'),
    ]
