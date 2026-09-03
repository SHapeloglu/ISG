# -*- coding: utf-8 -*-
from odoo import api, fields, models

class IsgChemicalOel(models.Model):
    _name = 'isg.chemical.oel'
    _description = 'Kimyasal Maruziyet Sınırı (OEL/STEL)'
    _order = 'chemical_id, valid_from desc'

    chemical_id = fields.Many2one(
        'isg.chemical', string='Kimyasal', required=True,
        ondelete='cascade',
    )

    # TWA (8 saatlik ağırlıklı ortalama)
    twa_value = fields.Float(
        string='TWA (8h) Değeri',
        help='Türkiye ÇSGB belirlediği değer',
    )
    twa_unit = fields.Selection(
        [
            ('ppm', 'ppm (Hacim Yüzdesi)'),
            ('mg_m3', 'mg/m³ (Kütle Yoğunluğu)'),
        ],
        string='TWA Birimi', default='mg_m3',
    )

    # STEL (15 dakika kısa süreli limit)
    stel_value = fields.Float(
        string='STEL (15min) Değeri',
        help='Türkiye ÇSGB belirlediği değer (opsiyonel)',
    )
    stel_unit = fields.Selection(
        [
            ('ppm', 'ppm'),
            ('mg_m3', 'mg/m³'),
        ],
        string='STEL Birimi', default='mg_m3',
    )

    # Geçerlilik
    valid_from = fields.Date(
        string='Geçerlilik Başlangıcı',
        help='Yönetmelik yürürlük tarihi',
        default=fields.Date.context_today,
    )
    regulation_reference = fields.Char(
        string='Mevzuat Kaynağı',
        help='Örn: "ÇSGB İSG Yönetmeliği Ek-I (2025-01-15)"',
    )

    # Notlar
    notes = fields.Text(
        string='Notlar',
        help='Özel uyarılar, karşılaştırmalar (AB CLP vs TR), vb.',
    )

    company_id = fields.Many2one(
        'res.company', string='Şirket',
        default=lambda self: self.env.company,
    )

    _sql_constraints = [
        ('twa_positive', 'check(twa_value > 0 or twa_value IS NULL)',
         'TWA değeri pozitif olmalıdır.'),
        ('stel_positive', 'check(stel_value > 0 or stel_value IS NULL)',
         'STEL değeri pozitif olmalıdır.'),
    ]
