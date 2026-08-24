# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import datetime, timedelta

class IsgRiskAssessment(models.Model):
    _name = 'isg.risk.assessment'
    _description = 'Risk Değerlendirmesi'
    _inherit = 'isg.uuid.mixin'
    _order = 'assessment_date desc'
    _rec_name = 'sequence'

    sequence = fields.Char(
        string='Değerlendirme No',
        default='/',
        readonly=True,
        copy=False,
        index=True
    )

    workplace_id = fields.Many2one(
        'isg.workplace',
        string='İşyeri',
        required=True,
        ondelete='cascade',
        readonly=False
    )

    company_id = fields.Many2one(
        'res.company',
        string='Şirket',
        related='workplace_id.company_id',
        store=True,
        readonly=True
    )

    assessment_date = fields.Date(
        string='Değerlendirme Tarihi',
        default=lambda self: fields.Date.today(),
        readonly=False
    )

    assessment_type = fields.Selection(
        [
            ('initial', 'Ön Değerlendirme'),
            ('periodic', 'Periyodik'),
            ('remediation', 'İyileştirme Sonrası'),
            ('change', 'Değişiklik Sonrası'),
        ],
        string='Değerlendirme Türü',
        default='initial',
        readonly=False
    )

    team_leader_id = fields.Many2one(
        'res.users',
        string='Ekip Lideri',
        default=lambda self: self.env.user,
        readonly=False
    )

    team_member_ids = fields.Many2many(
        'res.users',
        'risk_assessment_team_members_rel',
        'assessment_id',
        'user_id',
        string='Ekip Üyeleri',
        help='Risk değerlendirmesi yapan uzman ve hekimler'
    )

    state = fields.Selection(
        [
            ('draft', 'Taslak'),
            ('completed', 'Tamamlandı'),
            ('approved', 'Onaylı'),
        ],
        string='Durum',
        default='draft',
        readonly=True
    )

    assessment_line_ids = fields.One2many(
        'isg.risk.assessment.line',
        'assessment_id',
        string='Değerlendirme Satırları',
        readonly=False
    )

    notes = fields.Text(
        string='Notlar'
    )

    # Hesaplı Alanlar
    total_hazards = fields.Integer(
        string='Toplam Tehlike',
        compute='_compute_statistics',
        store=True,
        readonly=True
    )

    critical_risks = fields.Integer(
        string='Kritik Risk Sayısı',
        compute='_compute_statistics',
        store=True,
        readonly=True
    )

    high_risks = fields.Integer(
        string='Yüksek Risk Sayısı',
        compute='_compute_statistics',
        store=True,
        readonly=True
    )

    average_risk_score = fields.Float(
        string='Ort. Risk Puanı',
        compute='_compute_statistics',
        store=True,
        readonly=True
    )

    next_assessment_date = fields.Date(
        string='Sonraki Değerlendirme Tarihi',
        compute='_compute_next_assessment_date',
        store=True,
        readonly=True
    )

    @api.model
    def create(self, vals):
        if vals.get('sequence', '/') == '/':
            vals['sequence'] = self.env['ir.sequence'].next_by_code('isg.risk.assessment') or '/'
        return super().create(vals)

    @api.depends('assessment_line_ids.risk_level', 'assessment_line_ids.risk_score')
    def _compute_statistics(self):
        """İstatistikleri hesapla"""
        for record in self:
            lines = record.assessment_line_ids
            record.total_hazards = len(lines)
            
            # Risk seviyeleri sayısı
            record.critical_risks = len(lines.filtered(lambda l: l.risk_level == 'critical'))
            record.high_risks = len(lines.filtered(lambda l: l.risk_level == 'high'))
            
            # Ortalama risk puanı
            if lines:
                record.average_risk_score = sum(l.risk_score for l in lines) / len(lines)
            else:
                record.average_risk_score = 0.0

    @api.depends('assessment_date')
    def _compute_next_assessment_date(self):
        """Sonraki değerlendirme tarihi — 2 yıl sonra (Risk Değerlendirmesi Yönetmeliği)"""
        for record in self:
            if record.assessment_date:
                # Periyodik: 2 yıl, Ön: 1 yıl sonra
                days = 730 if record.assessment_type == 'periodic' else 365
                record.next_assessment_date = record.assessment_date + timedelta(days=days)
            else:
                record.next_assessment_date = None

    def action_complete_assessment(self):
        """Değerlendirmeyi tamamla"""
        self.ensure_one()
        if self.state != 'draft':
            raise models.ValidationError('Sadece taslak değerlendirmeler tamamlanabilir.')
        
        # Kritik riskler için otomatik CAPA oluştur
        critical_lines = self.assessment_line_ids.filtered(lambda l: l.risk_level == 'critical')
        for line in critical_lines:
            self.env['isg.capa'].create({
                'workplace_id': self.workplace_id.id,
                'subject': f'Kritik Risk: {line.hazard_id.name}',
                'description': f'Risk Puanı: {line.risk_score}, Tehlike: {line.hazard_id.description}',
                'state': 'open',
            })
        
        self.state = 'completed'

    def action_approve_assessment(self):
        """Değerlendirmeyi onayla"""
        self.ensure_one()
        if self.state != 'completed':
            raise models.ValidationError('Sadece tamamlanmış değerlendirmeler onaylanabilir.')
        self.state = 'approved'
