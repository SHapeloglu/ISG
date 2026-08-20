# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgMeasurementResult(models.Model):
    _name = 'isg.measurement.result'
    _description = 'Ölçüm Sonucu (Ham Veri — Snapshot)'
    _order = 'measurement_date desc, id desc'

    sample_id = fields.Many2one(
        'isg.measurement.sample', string='Numune Noktası',
        required=True, ondelete='cascade',
    )
    campaign_id = fields.Many2one(
        'isg.measurement.campaign', string='Kampanya',
        related='sample_id.campaign_id', store=True,
    )
    
    measurement_date = fields.Date(
        string='Ölçüm Tarihi', required=True,
        default=fields.Date.today,
    )
    measurement_time_start = fields.Datetime(
        string='Ölçüm Başlama Saati',
    )
    measurement_time_end = fields.Datetime(
        string='Ölçüm Bitiş Saati',
    )
    measurement_duration_hours = fields.Float(
        string='Ölçüm Süresi (saat)',
        help='Başlama-Bitiş saatinden otomatik hesaplanabilir',
    )
    
    # === HAM SONUÇ (SNAPSHOT — DEĞİŞMEZ) ===
    raw_value = fields.Float(
        string='Ham Ölçüm Değeri', required=True,
        help='Cihazdan okunan ham değer — ASLA DEĞIŞTIRILMEZ',
    )
    unit = fields.Char(
        string='Birim', required=True,
        help='dB, mg/m³, ppm, Lux, m/s², vb.',
    )
    
    # === CIHAZ & KALIBRASYON SNAPSHOT ===
    device_id = fields.Many2one(
        'isg.measurement.device', string='Cihaz',
        help='Ölçümü yapan cihaz',
    )
    device_calibration_date_snapshot = fields.Date(
        string='Cihaz Kalibrasyon Tarihi (snapshot)',
        help='Ölçüm anındaki cihaz kalibrasyon tarihi — bu ölçümün kaydedildiği anki durumu yansıtır',
    )
    device_calibration_certificate_snapshot = fields.Char(
        string='Kalibrasyon Sertifikası No (snapshot)',
        help='Ölçüm sırasında geçerli olan sertifika no',
    )
    device_calibration_valid_until_snapshot = fields.Date(
        string='Kalibrasyon Geçerli (snapshot)',
        help='Ölçüm anındaki kalibrasyonun son geçerli tarihi',
    )
    
    # === LIMIT SNAPSHOT (VERSİYONLÜ) ===
    limit_id = fields.Many2one(
        'isg.measurement.limit', string='Uygulanan Limit (snapshot)',
        help='Bu ölçüm hangi limit profiline göre değerlendirildi',
    )
    limit_regulation_version = fields.Char(
        string='Mevzuat Versiyonu (snapshot)',
        help='Örn: ÇSGB 2026, AB CLP — ölçüm sırasındaki mevzuat versiyonu',
    )
    limit_twa_snapshot = fields.Float(
        string='Limit TWA (snapshot)',
        help='Ölçüm sırasında geçerli TWA limit değeri — sonradan değişse bile bu değer aynı kalır',
    )
    limit_stel_snapshot = fields.Float(
        string='Limit STEL (snapshot)',
        help='Ölçüm sırasında geçerli STEL limit değeri',
    )
    
    # === UYGUNLUK HESAPLAMA ===
    compliance_status = fields.Selection(
        [
            ('compliant', 'Uyumlu'),
            ('exceeding', 'Limit Aşımı'),
            ('not_evaluated', 'Değerlendirilmedi'),
        ],
        string='Uygunluk Durumu',
        compute='_compute_compliance_status', store=True,
    )
    exceeding_value = fields.Float(
        string='Aşım Miktarı',
        compute='_compute_exceeding_value', store=True,
        help='Sonuç — Limit (negatif = uyumlu)',
    )
    exceeding_percentage = fields.Float(
        string='Aşım Yüzdesi',
        compute='_compute_exceeding_percentage', store=True,
        help='(Sonuç / Limit) × 100',
    )
    
    # === DÖF BAĞLANTISI ===
    capa_id = fields.Many2one(
        'isg.capa', string='Oluşturulan DÖF',
        help='Bu ölçüm limit aşımı durumunda otomatik DÖF oluşturursa buraya linklenecek',
    )
    
    # === META ===
    notes = fields.Text(string='Notlar')
    operator_id = fields.Many2one(
        'hr.employee', string='Operatör',
        help='Ölçüm yapan kişi',
    )
    reviewed_by_id = fields.Many2one(
        'hr.employee', string='Doğrulayan',
        help='Sonucu doğrulayan İSG uzmanı',
    )
    reviewed_date = fields.Date(string='Doğrulama Tarihi')
    
    state = fields.Selection(
        [
            ('draft', 'Taslak'),
            ('recorded', 'Kaydedildi'),
            ('reviewed', 'Doğrulandı'),
            ('closed', 'Kapalı'),
        ],
        string='Durum', default='draft',
    )
    
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri',
        related='campaign_id.workplace_id', store=True,
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket',
        related='campaign_id.company_id', store=True,
    )
    
    # === SNAPSHOT DONDURMA (create sırasında) ===
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            sample = self.env['isg.measurement.sample'].browse(vals.get('sample_id'))
            
            # Cihaz snapshot
            if vals.get('device_id'):
                device = self.env['isg.measurement.device'].browse(vals.get('device_id'))
                vals['device_calibration_date_snapshot'] = device.calibration_date
                vals['device_calibration_valid_until_snapshot'] = device.calibration_valid_until
            
            # Limit snapshot
            if vals.get('limit_id'):
                limit = self.env['isg.measurement.limit'].browse(vals.get('limit_id'))
                vals['limit_regulation_version'] = limit.regulation_version
                vals['limit_twa_snapshot'] = limit.twa_value
                vals['limit_stel_snapshot'] = limit.stel_value
        
        return super().create(vals_list)
    
    @api.depends('raw_value', 'limit_twa_snapshot')
    def _compute_compliance_status(self):
        for rec in self:
            if not rec.limit_twa_snapshot:
                rec.compliance_status = 'not_evaluated'
            elif rec.raw_value <= rec.limit_twa_snapshot:
                rec.compliance_status = 'compliant'
            else:
                rec.compliance_status = 'exceeding'
    
    @api.depends('raw_value', 'limit_twa_snapshot')
    def _compute_exceeding_value(self):
        for rec in self:
            if rec.limit_twa_snapshot:
                rec.exceeding_value = max(0, rec.raw_value - rec.limit_twa_snapshot)
            else:
                rec.exceeding_value = 0
    
    @api.depends('raw_value', 'limit_twa_snapshot')
    def _compute_exceeding_percentage(self):
        for rec in self:
            if rec.limit_twa_snapshot and rec.limit_twa_snapshot > 0:
                rec.exceeding_percentage = (rec.raw_value / rec.limit_twa_snapshot) * 100
            else:
                rec.exceeding_percentage = 0
    
    def action_create_capa(self):
        """Limit aşımı durumunda otomatik DÖF oluştur"""
        self.ensure_one()
        if self.compliance_status != 'exceeding':
            return False
        
        capa_vals = {
            'name': f'Ölçüm Aşımı: {self.sample_id.name} ({self.measurement_date})',
            'source': 'measurement',
            'description': f'Parameter: {self.sample_id.parameter_type}\nSonuç: {self.raw_value} {self.unit}\nLimit: {self.limit_twa_snapshot} {self.unit}\nAşım: {self.exceeding_percentage:.1f}%',
            'workplace_id': self.workplace_id.id,
            'severity': 'high' if self.exceeding_percentage > 150 else 'medium',
        }
        capa = self.env['isg.capa'].create(capa_vals)
        self.write({'capa_id': capa.id})
        return capa
