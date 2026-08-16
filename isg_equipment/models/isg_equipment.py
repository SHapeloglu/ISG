# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import datetime, timedelta

class IsgEquipment(models.Model):
    _name = 'isg.equipment'
    _description = 'Ekipman (Örnek)'
    _order = 'name'

    name = fields.Char(string='Ekipman Adı', required=True)
    code = fields.Char(string='Envanterinde Kod')
    equipment_type_id = fields.Many2one(
        'isg.equipment.type',
        string='Ekipman Türü',
        required=True,
        ondelete='restrict',
    )
    
    # Teknik detaylar
    manufacturer = fields.Char(string='Üretici')
    model = fields.Char(string='Model')
    serial_number = fields.Char(string='Seri Numarası')
    manufacturing_date = fields.Date(string='Üretim Tarihi')
    put_in_service_date = fields.Date(
        string='Hizmete Alınma Tarihi',
        default=fields.Date.context_today,
    )
    
    # Muayene kuruluşu
    authorized_body_id = fields.Many2one(
        'res.partner',
        string='Yetkili Muayene Kuruluşu',
        domain=[('is_authorized_body', '=', True)],
    )
    
    # İşyeri ve lokasyon
    company_id = fields.Many2one(
        'res.company',
        string='Şirket',
        default=lambda self: self.env.company,
    )
    workplace_id = fields.Many2one(
        'isg.workplace',
        string='İSG İşyeri',
    )
    site_id = fields.Many2one(
        'isg.site',
        string='Fiziksel Lokasyon',
    )
    location_description = fields.Char(
        string='Konumu',
        help='Örn: Atölye A - Köşe 1',
    )
    
    # Periyodik kontrol planlama
    last_inspection_date = fields.Date(string='Son Kontrol Tarihi')
    next_inspection_date = fields.Date(
        string='Sonraki Kontrol Tarihi',
        compute='_compute_next_inspection_date',
        store=True,
    )
    inspection_period_months = fields.Integer(
        related='equipment_type_id.inspection_period_months',
        readonly=True,
    )
    
    # Durum
    status = fields.Selection(
        [
            ('active', 'Aktif - Kullanımda'),
            ('maintenance', 'Bakım Durumunda'),
            ('inactive', 'Pasif - Kullanım Dışı'),
            ('scrapped', 'Hurdaya Çıkartılmış'),
        ],
        string='Durum',
        default='active',
    )
    
    # Notlar ve belgeler
    notes = fields.Text(string='Notlar')
    inspection_ids = fields.One2many(
        'isg.equipment.inspection',
        'equipment_id',
        string='Periyodik Kontrol Kayıtları',
    )
    
    active = fields.Boolean(default=True)
    
    @api.depends('last_inspection_date', 'inspection_period_months')
    def _compute_next_inspection_date(self):
        for record in self:
            if record.last_inspection_date and record.inspection_period_months:
                next_date = record.last_inspection_date + timedelta(
                    days=record.inspection_period_months * 30
                )
                record.next_inspection_date = next_date
            else:
                record.next_inspection_date = None
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('code'):
                vals['code'] = self.env['ir.sequence'].next_by_code(
                    'isg.equipment'
                ) or 'NEW'
        return super().create(vals_list)
