# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgMeasurementCampaign(models.Model):
    _name = 'isg.measurement.campaign'
    _description = 'Ölçüm Kampanyası (Yıllık Plan)'
    _order = 'year desc, name'

    name = fields.Char(
        string='Kampanya Adı', required=True,
        help='Örn: Gürültü Ölçümleri 2026 Q1',
    )
    year = fields.Integer(
        string='Yıl', required=True,
        default=lambda: fields.Date.today().year,
    )
    quarter = fields.Selection(
        [
            ('q1', 'Q1 (Oca-Mar)'),
            ('q2', 'Q2 (Nis-Haz)'),
            ('q3', 'Q3 (Tem-Eyl)'),
            ('q4', 'Q4 (Eki-Ara)'),
            ('full_year', 'Yıl Boyunca'),
        ],
        string='Çeyrek / Periyot',
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
            ('all', 'Tüm Parametreler'),
        ],
        string='Parametre Türü', required=True,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri', required=True,
        ondelete='cascade',
    )
    site_id = fields.Many2one(
        'isg.site', string='Lokasyon / Site',
        help='Hangi fiziksel alanda ölçüm yapılacak',
    )
    description = fields.Text(string='Amaç / Açıklama')
    
    planned_start_date = fields.Date(string='Planlanan Başlangıç Tarihi')
    planned_end_date = fields.Date(string='Planlanan Bitiş Tarihi')
    
    state = fields.Selection(
        [
            ('draft', 'Taslak'),
            ('approved', 'Onaylandı'),
            ('in_progress', 'Devam Ediyor'),
            ('completed', 'Tamamlandı'),
            ('cancelled', 'İptal Edildi'),
        ],
        string='Durum', default='draft',
    )
    
    sample_line_ids = fields.One2many(
        'isg.measurement.sample', 'campaign_id',
        string='Numune Noktaları',
    )
    result_count = fields.Integer(
        string='Toplam Sonuç Sayısı',
        compute='_compute_result_count', store=True,
    )
    
    notes = fields.Text(string='Notlar')
    
    company_id = fields.Many2one(
        'res.company', string='Şirket',
        default=lambda self: self.env.company,
    )
    
    @api.depends('sample_line_ids')
    def _compute_result_count(self):
        for rec in self:
            rec.result_count = sum(
                len(sample.result_ids) for sample in rec.sample_line_ids
            )
    
    def action_approve(self):
        """Kampanyadı onayla"""
        self.write({'state': 'approved'})
    
    def action_start(self):
        """Kampanyayı başlat"""
        self.write({'state': 'in_progress'})
    
    def action_complete(self):
        """Kampanyayı tamamla"""
        self.write({'state': 'completed'})
    
    def action_cancel(self):
        """Kampanyayı iptal et"""
        self.write({'state': 'cancelled'})
