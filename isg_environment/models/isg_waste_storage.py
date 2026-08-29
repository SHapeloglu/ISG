# -*- coding: utf-8 -*-
from odoo import fields, models, api


class WasteStorage(models.Model):
    _name = 'isg.waste.storage'
    _description = 'Atık Depolama Alanı'
    _inherit = ['isg.uuid.mixin']
    _order = 'workplace_id, name'

    workplace_id = fields.Many2one('isg.workplace', 'İşyeri', required=True, ondelete='cascade')
    site_id = fields.Many2one('isg.site', 'Lokasyon', required=True, ondelete='cascade')
    
    name = fields.Char('Depolama Alanı Adı', required=True)
    storage_type = fields.Selection([
        ('indoor', 'Kapalı Alan'),
        ('outdoor', 'Açık Alan'),
        ('container', 'Konteyner'),
        ('tank', 'Depo Tankı'),
        ('other', 'Diğer'),
    ], string='Depolama Türü', required=True)
    
    waste_code_ids = fields.Many2many('isg.waste.code', string='Depolanan Atık Türleri')
    
    capacity_m3 = fields.Float('Kapasite (m³)', required=True, help='Deponun maksimum kapasitesi')
    current_volume_m3 = fields.Float('Mevcut Hacim (m³)', default=0)
    
    @api.depends('current_volume_m3', 'capacity_m3')
    def _compute_capacity_percentage(self):
        for rec in self:
            if rec.capacity_m3 > 0:
                rec.capacity_percentage = (rec.current_volume_m3 / rec.capacity_m3) * 100
            else:
                rec.capacity_percentage = 0
    
    capacity_percentage = fields.Float('Kapasite (%)', compute='_compute_capacity_percentage', store=True)
    
    @api.depends('capacity_percentage')
    def _compute_capacity_status(self):
        for rec in self:
            if rec.capacity_percentage >= 90:
                rec.capacity_status = 'full'
            elif rec.capacity_percentage >= 70:
                rec.capacity_status = 'warning'
            else:
                rec.capacity_status = 'ok'
    
    capacity_status = fields.Selection([
        ('ok', 'Normal'),
        ('warning', 'Uyarı (70%+)'),
        ('full', 'Dolu (90%+)'),
    ], compute='_compute_capacity_status', store=True)
    
    temperature_controlled = fields.Boolean('Sıcaklık Kontrollü')
    min_temperature = fields.Float('Min Sıcaklık (°C)')
    max_temperature = fields.Float('Max Sıcaklık (°C)')
    
    ventilated = fields.Boolean('Havalandırmalı')
    fire_extinguisher_count = fields.Integer('Yangın Söndürücü Sayısı', default=0)
    
    inspection_required = fields.Boolean('Periyodik İnceleme Gerekli', default=True)
    last_inspection_date = fields.Date('Son İnceleme Tarihi')
    next_inspection_date = fields.Date('Sonraki İnceleme Tarihi')
    
    compliance_notes = fields.Text('Uygunluk Notları')
    is_active = fields.Boolean('Aktif', default=True)
    
    state = fields.Selection([
        ('draft', 'Taslak'),
        ('active', 'Aktif'),
        ('suspended', 'Askıya Alındı'),
        ('closed', 'Kapalı'),
    ], default='draft')
