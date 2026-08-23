# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api, _

class ISGComplianceEvidence(models.Model):
    _name = 'isg.compliance.evidence'
    _description = 'Uygunluk Değerlendirmesi Kanıtı'
    _order = 'id desc'

    obligation_id = fields.Many2one(
        'isg.obligation',
        string='Yükümlülük',
        required=True,
        ondelete='cascade'
    )
    workplace_id = fields.Many2one(
        'isg.workplace',
        string='İşyeri',
        required=True,
        ondelete='cascade'
    )
    evidence_type = fields.Selection(
        [
            ('risk_assessment', 'Risk Değerlendirmesi'),
            ('training_record', 'Eğitim Kaydı'),
            ('expert_assignment', 'Uzman Görevlendirilmesi'),
            ('physician_assignment', 'Hekim Görevlendirilmesi'),
            ('emergency_plan', 'Acil Durum Planı'),
            ('audit_checklist', 'Denetim Kontrol Listesi'),
            ('equipment_report', 'Ekipman Raporu'),
            ('chemical_inventory', 'Kimyasal Envanter'),
            ('permit_to_work', 'İş İzni'),
            ('incident_report', 'Kaza Raporu'),
            ('other', 'Diğer'),
        ],
        string='Kanıt Türü',
        required=True
    )
    document_id = fields.Many2one(
        'ir.attachment',
        string='Dosya/Belge',
        ondelete='set null'
    )
    source_model = fields.Char(
        string='Kaynak Model',
        help='Kanıtın geldiği model adı (ör: isg.training.record, isg.capa, isg.measurement.result)'
    )
    source_res_id = fields.Integer(
        string='Kaynak Kayıt ID'
    )
    valid_from = fields.Date(
        string='Geçerlilik Başlangıcı',
        default=fields.Date.today
    )
    valid_until = fields.Date(
        string='Geçerlilik Sonu'
    )
    is_valid = fields.Boolean(
        string='Şu Anda Geçerli mi?',
        compute='_compute_is_valid',
        store=True
    )
    notes = fields.Text(string='Notlar')

    @api.depends('valid_until')
    def _compute_is_valid(self):
        """
        Kanıt geçerli mi kontrol et: valid_until >= bugün ve valid_from <= bugün
        """
        today = fields.Date.today()
        for record in self:
            if record.valid_from and record.valid_until:
                record.is_valid = record.valid_from <= today <= record.valid_until
            elif record.valid_until:
                record.is_valid = today <= record.valid_until
            elif record.valid_from:
                record.is_valid = record.valid_from <= today
            else:
                record.is_valid = True

    @api.model_create_multi
    def create(self, vals_list):
        """
        Kanıt oluşturulurken, valid_until eksikse obligation.retention_days'ten hesapla.
        """
        for vals in vals_list:
            if not vals.get('valid_until') and vals.get('obligation_id'):
                obligation = self.env['isg.obligation'].browse(vals['obligation_id'])
                if obligation.retention_days:
                    valid_from = vals.get('valid_from') or fields.Date.today()
                    if isinstance(valid_from, str):
                        valid_from = fields.Date.from_string(valid_from)
                    vals['valid_until'] = valid_from + timedelta(days=obligation.retention_days)
        
        return super().create(vals_list)

    _sql_constraints = [
        ('unique_evidence', 'unique(obligation_id, workplace_id, source_model, source_res_id)',
         'Aynı yükümlülük, işyeri ve kaynak için birden fazla kanıt kaydı olamaz.'),
    ]
