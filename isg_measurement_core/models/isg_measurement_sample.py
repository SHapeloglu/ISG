# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgMeasurementSample(models.Model):
    _name = 'isg.measurement.sample'
    _description = 'Ölçüm Numune Noktası'
    _order = 'campaign_id, name'

    campaign_id = fields.Many2one(
        'isg.measurement.campaign', string='Kampanya',
        required=True, ondelete='cascade',
    )
    name = fields.Char(
        string='Numune Noktası Adı', required=True,
        help='Örn: Montaj Hattı #1, Lab Alanı',
    )
    code = fields.Char(string='Numune Kodu')
    
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
    
    site_id = fields.Many2one(
        'isg.site', string='Lokasyon',
        help='Numune noktasının fiziksel yeri',
    )
    seg_id = fields.Many2one(
        'isg.seg', string='SEG — Benzer Maruziyet Grubu',
        help='Bu numune hangi SEG grubunu temsil ediyor',
    )
    affected_employees = fields.Many2many(
        'hr.employee', string='Etkilenen Çalışanlar',
        help='Bu maruziyet noktasından etkilenen çalışanlar',
    )
    
    measurement_duration_hours = fields.Float(
        string='Ölçüm Süresi (saat)', default=8,
        help='Kaç saat ölçüm yapılacak (genelde 8 saatlik vardiya)',
    )
    measurement_date = fields.Date(
        string='Ölçüm Tarihi',
        help='Numune ne zaman alınacak',
    )
    
    device_id = fields.Many2one(
        'isg.measurement.device', string='Ölçüm Cihazı',
        help='Hangi cihaz kullanılacak',
    )
    operator_id = fields.Many2one(
        'hr.employee', string='Operatör',
        help='Ölçüm yapan kişi',
    )
    
    state = fields.Selection(
        [
            ('pending', 'Beklemede'),
            ('in_progress', 'Ölçüm Yapılıyor'),
            ('completed', 'Tamamlandı'),
            ('cancelled', 'İptal Edildi'),
        ],
        string='Durum', default='pending',
    )
    
    result_ids = fields.One2many(
        'isg.measurement.result', 'sample_id',
        string='Ölçüm Sonuçları',
    )
    
    notes = fields.Text(string='Notlar')
    
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri',
        related='campaign_id.workplace_id', store=True,
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket',
        related='campaign_id.company_id', store=True,
    )
