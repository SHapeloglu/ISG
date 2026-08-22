# -*- coding: utf-8 -*-
from odoo import models, fields

class ISGObligation(models.Model):
    _name = 'isg.obligation'
    _description = 'ISG Yükümlülüğü'
    _order = 'name'

    name = fields.Char('Yükümlülük Adı', required=True)
    legislation_id = fields.Many2one('isg.legislation', 'Mevzuat', required=True, ondelete='cascade')
    article = fields.Char('Madde/Kısım')
    
    description = fields.Text('Yükümlülük Tanımı')
    
    evidence_type = fields.Selection([
        ('risk_assessment', 'Risk Değerlendirmesi Raporu'),
        ('training_record', 'Eğitim Kaydı'),
        ('expert_assignment', 'Uzman Atama Belgesi'),
        ('physician_assignment', 'Hekim Atama Belgesi'),
        ('emergency_plan', 'Acil Durum Planı'),
        ('audit_checklist', 'Denetim Kontrolü'),
        ('equipment_report', 'Ekipman İnceleme Raporu'),
        ('chemical_inventory', 'Kimyasal Envanter'),
        ('permit_to_work', 'İzinli Çalışma İzni'),
        ('incident_report', 'Kaza Raporu'),
        ('other', 'Diğer'),
    ], string='Kanıt Türü', required=True)
    
    is_periodic = fields.Boolean('Periyodik mi?', default=False)
    periodic_days = fields.Integer('Periyot (gün)', help='0 ise periyodik değil')
    retention_days = fields.Integer('Kanıt Saklama Süresi (gün)', default=730)
    
    # Uygulanabilirlik kuralları (One2many)
    applicability_ids = fields.One2many('isg.obligation.applicability', 'obligation_id', 'Uygulanabilirlik Kuralları')
    
    _sql_constraints = [
        ('unique_name_legislation', 'unique(name, legislation_id)', 'Aynı mevzuatta yükümlülük adı benzersiz olmalı'),
    ]


class ISGObligationApplicability(models.Model):
    _name = 'isg.obligation.applicability'
    _description = 'ISG Yükümlülüğü - Uygulanabilirlik Kuralı'
    
    obligation_id = fields.Many2one('isg.obligation', 'Yükümlülük', required=True, ondelete='cascade')
    
    # Uygulanabilirlik kriterleri
    danger_class = fields.Selection([
        ('low', 'Az Tehlikeli'),
        ('medium', 'Tehlikeli'),
        ('high', 'Çok Tehlikeli'),
    ], string='Tehlike Sınıfı')
    
    min_employee = fields.Integer('Minimum Çalışan Sayısı', default=1)
    max_employee = fields.Integer('Maksimum Çalışan Sayısı', default=999999)
    
    sector_type = fields.Selection([
        ('public', 'Kamu'),
        ('private', 'Özel'),
        ('both', 'Her İkisi'),
    ], string='Sektör', default='both')
    
    nace_code = fields.Char('NACE Kodu', help='Boş = tümüne uygulanır')
    
    description = fields.Text('Kurallı Açıklama')
    
    _sql_constraints = [
        ('valid_employee_range', 'check(min_employee <= max_employee)', 'Min çalışan sayısı max değerini aşamaz'),
    ]
