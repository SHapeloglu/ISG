# -*- coding: utf-8 -*-
from odoo import api, fields, models

class IsgEquipmentInspection(models.Model):
    _name = 'isg.equipment.inspection'
    _description = 'Periyodik Kontrol Kaydı'
    _order = 'inspection_date desc'

    equipment_id = fields.Many2one(
        'isg.equipment',
        string='Ekipman',
        required=True,
        ondelete='cascade',
    )
    
    inspection_date = fields.Date(
        string='Kontrol Tarihi',
        required=True,
        default=fields.Date.context_today,
    )
    
    # Muayene kuruluşu bilgileri
    authorized_body_id = fields.Many2one(
        'res.partner',
        string='Yetkili Muayene Kuruluşu',
        required=True,
        domain=[('is_authorized_body', '=', True)],
    )
    
    # Kontrol sonuçları
    inspection_result = fields.Selection(
        [
            ('conforming', 'Uygun'),
            ('non_conforming', 'Uygun Değil'),
            ('conditional', 'Şartlı'),
        ],
        string='Kontrol Sonucu',
        required=True,
    )
    
    findings = fields.Text(
        string='Bulgular',
        help='Kontrol sırasında tespit edilen bulgular',
    )
    
    restrictions = fields.Text(
        string='Kısıtlamalar',
        help='Örn: "Maksimum 5 ton yük ile kullanılabilir"',
    )
    
    # Sonraki kontrol tarihi
    next_inspection_date = fields.Date(
        string='Sonraki Kontrol Tarihi',
        required=True,
    )
    
    # Belge ve e-imza
    report_document_id = fields.Many2one(
        'isg.document',
        string='Kontrol Raporu (Belge)',
        help='İmzalı kontrol raporu dosyası',
    )
    
    # EKİPNET hazırlığı
    ekipnet_ready = fields.Boolean(
        string='EKİPNET Hazır',
        default=False,
        help="Bu kayıt EKİPNET'e aktarılmaya hazır mı?",
    )
    
    ekipnet_submitted = fields.Boolean(
        string="EKİPNET'e Gönderildi",
        default=False,
    )
    
    ekipnet_reference = fields.Char(
        string='EKİPNET Referans No',
        help='EKİPNET tarafından oluşturulan referans numarası',
    )
    
    # Kurumsal
    company_id = fields.Many2one(
        'res.company',
        string='Şirket',
        default=lambda self: self.env.company,
    )
    
    workplace_id = fields.Many2one(
        related='equipment_id.workplace_id',
        readonly=True,
    )
    
    notes = fields.Text(string='Notlar')
    
    @api.onchange('inspection_result')
    def _onchange_inspection_result(self):
        """Sonuç değişince bildirimleri tetikle"""
        if self.inspection_result == 'non_conforming':
            # Uygun değilse CAPA otomatik oluşturulabilir
            pass
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            equipment = self.env['isg.equipment'].browse(
                vals.get('equipment_id')
            )
            # Son kontrol tarihini güncelle
            if vals.get('inspection_date'):
                equipment.last_inspection_date = vals.get('inspection_date')
        return super().create(vals_list)
