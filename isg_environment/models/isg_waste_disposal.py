# -*- coding: utf-8 -*-
from odoo import fields, models, api


class WasteDisposal(models.Model):
    _name = 'isg.waste.disposal'
    _description = 'Atık Bertaraf Kaydı'
    _inherit = ['isg.uuid.mixin', 'mail.thread']
    _order = 'disposal_date desc'

    workplace_id = fields.Many2one('isg.workplace', 'İşyeri', required=True, ondelete='cascade')
    
    waste_code_id = fields.Many2one('isg.waste.code', 'Atık Kodu', required=True)
    waste_storage_id = fields.Many2one('isg.waste.storage', 'Depolama Alanı')
    
    disposal_date = fields.Date('Bertaraf Tarihi', required=True, default=fields.Date.context_today)
    quantity_m3 = fields.Float('Miktar (m³)', required=True)
    quantity_kg = fields.Float('Miktar (kg)', help='Ağırlık bilgisi')
    
    disposal_method = fields.Selection([
        ('landfill', 'Depo (Landfill)'),
        ('incineration', 'Yakma (Incineration)'),
        ('recycling', 'Geri Dönüşüm'),
        ('composting', 'Kompostlama'),
        ('hazmat', 'Tehlikeli Atık Bertarafı'),
        ('other', 'Diğer'),
    ], string='Bertaraf Yöntemi', required=True)
    
    # Bertaraf Kuruluşu
    disposal_company_id = fields.Many2one('res.partner', 'Bertaraf Kuruluşu',
                                         domain=[('is_waste_contractor', '=', True)])
    disposal_license_no = fields.Char('Bertaraf Lisans No')
    disposal_cert_date = fields.Date('Bertaraf Sertifikası Tarihi')
    
    # Maliyet
    cost = fields.Float('Bertaraf Maliyeti (TL)')
    cost_per_unit = fields.Float('Birim Maliyet (TL/m³)', compute='_compute_cost_per_unit')
    
    @api.depends('cost', 'quantity_m3')
    def _compute_cost_per_unit(self):
        for rec in self:
            if rec.quantity_m3 > 0:
                rec.cost_per_unit = rec.cost / rec.quantity_m3
            else:
                rec.cost_per_unit = 0
    
    # Belgelendirme
    disposal_certificate = fields.Many2one('ir.attachment', 'Bertaraf Sertifikası')
    manifest_document = fields.Many2one('ir.attachment', 'Atık Yönetim Bilgi Formu (AYBF)')
    
    responsible_person_id = fields.Many2one('res.users', 'Sorumlu Kişi', default=lambda self: self.env.user)
    notes = fields.Text('Notlar', tracking=True)
    
    state = fields.Selection([
        ('draft', 'Taslak'),
        ('confirmed', 'Onaylandı'),
        ('disposed', 'Bertaraf Yapıldı'),
        ('archived', 'Arşivlendi'),
    ], default='draft', tracking=True)
    
    @api.constrains('quantity_m3', 'quantity_kg')
    def _check_quantities(self):
        for rec in self:
            if rec.quantity_m3 < 0 or rec.quantity_kg < 0:
                raise ValueError('Miktar sıfırdan küçük olamaz!')
    
    def action_confirm(self):
        """Bertaraf kaydını onayla"""
        self.state = 'confirmed'
        # İlgili storage'dan hacim düş
        if self.waste_storage_id:
            self.waste_storage_id.current_volume_m3 -= self.quantity_m3
    
    def action_dispose(self):
        """Bertaraf tamamlandı"""
        self.state = 'disposed'
    
    def action_archive(self):
        """Arşivle"""
        self.state = 'archived'
