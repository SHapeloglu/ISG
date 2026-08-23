# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ISGCompliance(models.Model):
    _name = 'isg.compliance'
    _description = 'İşyeri Uygunluk Değerlendirmesi'
    _order = 'evaluation_date desc, workplace_id'

    workplace_id = fields.Many2one(
        'isg.workplace',
        string='İşyeri',
        required=True,
        ondelete='cascade'
    )
    obligation_id = fields.Many2one(
        'isg.obligation',
        string='Yükümlülük',
        required=True,
        ondelete='cascade'
    )
    evaluation_date = fields.Datetime(
        string='Değerlendirme Tarihi',
        default=fields.Datetime.now,
        readonly=True
    )
    status = fields.Selection([
        ('uygun', 'Uygun'),
        ('eksik', 'Eksik'),
        ('beklemede', 'Beklemede'),
        ('vadesi_geçmiş', 'Vadesi Geçmiş'),
    ], string='Uygunluk Durumu', default='beklemede')
    
    evidence_id = fields.Many2one(
        'isg.compliance.evidence',
        string='Kanıt',
        ondelete='set null'
    )
    due_date = fields.Date(
        string='Bir Sonraki Değerlendirme Tarihi'
    )
    capa_id = fields.Many2one(
        'isg.capa',
        string='İlgili DÖF',
        ondelete='set null'
    )
    evaluator_id = fields.Many2one(
        'res.users',
        string='Değerlendiren',
        default=lambda self: self.env.user
    )
    notes = fields.Text(string='Notlar')
    
    _sql_constraints = [
        ('unique_workplace_obligation', 'unique(workplace_id, obligation_id, evaluation_date)', 
         'Aynı işyeri ve yükümlülük için aynı tarihte birden fazla değerlendirme olamaz.'),
    ]

    @api.model
    def _compute_applicable_obligations(self, workplace_id):
        """
        Verilen işyeri için uygulanabilir yükümlülükleri hesapla.
        isg.obligation.applicability kurallarına göre filtrele.
        """
        workplace = self.env['isg.workplace'].browse(workplace_id)
        
        domain = [
            ('obligation_id', '!=', False),
            '|', '|', '|',
            ('danger_class', '=', False),
            ('danger_class', '=', workplace.danger_class),
            '&',
            ('min_employee', '<=', workplace.employee_count),
            ('max_employee', '>=', workplace.employee_count),
        ]
        
        applicability_records = self.env['isg.obligation.applicability'].search(domain)
        return applicability_records.mapped('obligation_id')

    def action_evaluate_compliance(self):
        """
        İşyeri için tüm uygulanabilir yükümlülükleri değerlendir.
        Her yükümlülük için en son kanıt kaydını kontrol et.
        """
        if not self.workplace_id:
            raise UserError('Değerlendirme yapılacak işyeri seçiniz.')
        
        applicable_obligations = self._compute_applicable_obligations(self.workplace_id.id)
        
        for obligation in applicable_obligations:
            # Aynı tarihte değerlendirme varsa atla
            existing = self.search([
                ('workplace_id', '=', self.workplace_id.id),
                ('obligation_id', '=', obligation.id),
                ('evaluation_date', '>=', fields.Datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
            ], limit=1)
            
            if existing:
                continue
            
            # En son kanıt kaydını bul
            latest_evidence = self.env['isg.compliance.evidence'].search([
                ('workplace_id', '=', self.workplace_id.id),
                ('obligation_id', '=', obligation.id),
            ], order='id desc', limit=1)
            
            # Uygunluk durumunu belirle
            status = 'beklemede'
            if latest_evidence:
                if latest_evidence.is_valid:
                    status = 'uygun'
                else:
                    status = 'vadesi_geçmiş'
            else:
                status = 'eksik'
            
            # Due date hesapla
            due_date = None
            if obligation.is_periodic:
                due_date = (datetime.now() + timedelta(days=obligation.periodic_days)).date()
            
            # Yeni compliance kaydı oluştur
            compliance_record = self.create({
                'workplace_id': self.workplace_id.id,
                'obligation_id': obligation.id,
                'status': status,
                'evidence_id': latest_evidence.id if latest_evidence else None,
                'due_date': due_date,
                'notes': f'{obligation.name} otomatik değerlendirildi.',
            })
            
            # Eksik/vadesi geçmiş ise DÖF oluştur
            if status in ['eksik', 'vadesi_geçmiş']:
                capa_vals = {
                    'name': f'DÖF: {obligation.name} ({self.workplace_id.name})',
                    'description': f'Uygunluk değerlendirmesine göre {obligation.name} yükümlülüğü eksik.',
                    'workplace_id': self.workplace_id.id,
                    'state': 'open',
                }
                capa = self.env['isg.capa'].create(capa_vals)
                compliance_record.capa_id = capa.id
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Başarılı'),
                'message': _('Uygunluk değerlendirmesi tamamlandı.'),
                'type': 'success',
            }
        }
