# -*- coding: utf-8 -*-
from odoo import models, fields, api
class IsgPenaltyTariff(models.Model):
    _name = 'isg.penalty.tariff'
    _description = 'İSG Ceza Tarifesi (6331 md.26)'
    _order = 'valid_from desc, article'
    name = fields.Char(string='Tarife Adı', required=True)
    article = fields.Char(string='Kanun Maddesi', required=True,
                           help="Örn: 26/1-a")
    description = fields.Text(string='İhlal Tanımı', required=True)
    evidence_type = fields.Selection([
        ('risk_assessment', 'Risk Değerlendirmesi'),
        ('training_record', 'Eğitim Kaydı'),
        ('expert_assignment', 'Uzman Görevlendirme'),
        ('physician_assignment', 'Hekim Görevlendirme'),
        ('emergency_plan', 'Acil Durum Planı'),
        ('audit_checklist', 'Denetim Kontrol Listesi'),
        ('equipment_report', 'Ekipman Kontrol Raporu'),
        ('chemical_inventory', 'Kimyasal Envanter'),
        ('permit_to_work', 'İş İzni'),
        ('incident_report', 'Kaza Bildirimi'),
        ('other', 'Diğer'),
    ], string='İlgili Yükümlülük Türü', required=True,
       help="isg.obligation.evidence_type ile eşleşir")
    amount_2026 = fields.Monetary(string='2026 Tutarı (TL)', required=True,
                                   currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Para Birimi',
                                   default=lambda self: self.env.ref('base.TRY'))
    amount_per_employee = fields.Boolean(string='Çalışan Başına Uygulanır',
                                          default=False)
    repeat_multiplier = fields.Float(string='Tekrar İhlal Çarpanı', default=2.0)
    valid_from = fields.Date(string='Yürürlük Tarihi', required=True,
                              default=fields.Date.context_today, tracking=True,
                              help="Bu tarifenin hangi tarihten itibaren geçerli olduğu")
    effective_date = fields.Date(string='Eski Yürürlük Tarihi', 
                                  help="Geriye uyumluluk için — valid_from kullanın")
    active = fields.Boolean(string='Aktif', default=True)
    notes = fields.Text(string='Notlar')
