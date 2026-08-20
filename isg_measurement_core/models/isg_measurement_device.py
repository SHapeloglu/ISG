# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgMeasurementDevice(models.Model):
    _name = 'isg.measurement.device'
    _description = 'Ölçüm Cihazı'
    _order = 'name'

    name = fields.Char(
        string='Cihaz Adı', required=True,
        help='Örn: Gürültü Ölçer #1, Toz Örneği Pompası #2',
    )
    code = fields.Char(
        string='Cihaz Kodu', required=True,
        help='Dahili benzersiz numarası',
    )
    device_type = fields.Selection(
        [
            ('sound_level_meter', 'Gürültü Ölçer'),
            ('dust_sampler', 'Toz Örneği Pompası'),
            ('gas_detector', 'Gaz Dedektörü'),
            ('vibration_meter', 'Titreşim Ölçer'),
            ('light_meter', 'Işık Ölçer (Luksometre)'),
            ('thermal_comfort', 'Isıl Konfor Ölçer'),
            ('other', 'Diğer'),
        ],
        string='Cihaz Türü', required=True,
    )
    manufacturer = fields.Char(string='Üretici')
    model = fields.Char(string='Model')
    serial_number = fields.Char(string='Seri Numarası')
    
    calibration_date = fields.Date(
        string='Son Kalibrasyon Tarihi', required=True,
        help='En son kalibrasyon tarihi',
    )
    calibration_certificate_id = fields.Many2one(
        'isg.document', string='Kalibrasyon Sertifikası',
        domain=[('document_type', '=', 'calibration')],
        help='e-imzalı kalibrasyon raporu',
    )
    calibration_valid_until = fields.Date(
        string='Kalibrasyon Geçerli (Son Gün)',
        compute='_compute_calibration_valid_until',
        store=True,
    )
    calibration_period_months = fields.Integer(
        string='Kalibrasyon Periyodu (ay)', default=12,
        help='Kaç ayda bir kalibre edilmesi gerekiyor',
    )
    
    measurement_unit = fields.Char(
        string='Ölçüm Birimi',
        help='dB, mg/m³, ppm, Lux, m/s², vb.',
    )
    measurement_range_min = fields.Float(string='Ölçüm Aralığı — Min')
    measurement_range_max = fields.Float(string='Ölçüm Aralığı — Max')
    
    location = fields.Char(
        string='Saklama Yeri',
        help='Laboratuvar, İSG ofisi, vb.',
    )
    notes = fields.Text(string='Notlar')
    
    company_id = fields.Many2one(
        'res.company', string='Şirket',
        default=lambda self: self.env.company,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri',
    )
    active = fields.Boolean(default=True)
    
    @api.depends('calibration_date', 'calibration_period_months')
    def _compute_calibration_valid_until(self):
        from dateutil.relativedelta import relativedelta
        for rec in self:
            if rec.calibration_date:
                rec.calibration_valid_until = (
                    rec.calibration_date + 
                    relativedelta(months=rec.calibration_period_months)
                )
            else:
                rec.calibration_valid_until = None

    def action_calibration_expired(self):
        """Kalibrasyonu süresi dolmuş cihazları filter"""
        today = fields.Date.today()
        return self.search([
            ('calibration_valid_until', '<', today),
            ('active', '=', True),
        ])
