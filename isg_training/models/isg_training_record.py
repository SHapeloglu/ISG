# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class IsgTrainingRecord(models.Model):
    _name = 'isg.training.record'
    _description = 'İSG Eğitim Kaydı'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'isg.uuid.mixin']
    _order = 'training_date desc'

    name = fields.Char(
        string='Eğitim Adı', required=True, tracking=True,
    )
    training_type_id = fields.Many2one(
        'isg.training.type', string='Eğitim Türü', required=True,
    )
    training_category = fields.Selection(
        related='training_type_id.training_category',
        string='Kategori', store=True, readonly=True,
    )
    delivery_method = fields.Selection(
        related='training_type_id.delivery_method',
        string='Yöntem', store=True, readonly=True,
    )

    # --- Tarih ve süre ---
    training_date = fields.Date(
        string='Eğitim Tarihi', required=True, tracking=True,
    )
    duration_hours = fields.Float(
        string='Süre (Saat)', required=True,
    )

    # --- Kapsam ---
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri', required=True,
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )
    site_id = fields.Many2one(
        'isg.site', string='Lokasyon',
    )

    # --- Eğitmen ---
    trainer_name = fields.Char(string='Eğitmen Adı')
    trainer_institution = fields.Char(string='Eğitmen Kurumu')
    trainer_certificate = fields.Char(string='Eğitmen Sertifika No')

    # --- Katılımcılar ---
    attendee_ids = fields.One2many(
        'isg.training.attendee', 'record_id', string='Katılımcılar',
    )
    attendee_count = fields.Integer(
        string='Katılımcı Sayısı',
        compute='_compute_attendee_count', store=True,
    )

    # --- 2 Nisan 2026 yönetmelik uygunluk ---
    regulation_compliant = fields.Boolean(
        string='Yönetmelik Uyumlu',
        compute='_compute_regulation_compliant', store=True,
        help='2 Nisan 2026 Çalışan Eğitimi Yönetmeliğine uygunluk.',
    )
    compliance_notes = fields.Text(
        string='Uygunluk Notları', readonly=True,
    )

    # --- Belge ---
    document_id = fields.Many2one(
        'isg.document', string='Eğitim Belgesi / Sertifika',
    )

    # --- Durum ---
    state = fields.Selection(
        selection=[
            ('draft', 'Taslak'),
            ('confirmed', 'Onaylandı'),
            ('cancelled', 'İptal'),
        ],
        string='Durum', default='draft', tracking=True,
    )

    @api.depends('attendee_ids')
    def _compute_attendee_count(self):
        for rec in self:
            rec.attendee_count = len(rec.attendee_ids)

    @api.depends(
        'training_type_id', 'duration_hours',
        'delivery_method', 'training_category',
    )
    def _compute_regulation_compliant(self):
        for rec in self:
            notes = []
            compliant = True

            # İşe başlama eğitimi: min 2 saat, yüz yüze zorunlu
            if rec.training_category == 'onboarding':
                if rec.duration_hours < 2.0:
                    compliant = False
                    notes.append(
                        'İşe başlama eğitimi min 2 saat olmalıdır '
                        '(2 Nisan 2026 Yönetmeliği md.5).'
                    )
                if rec.delivery_method != 'face_to_face':
                    compliant = False
                    notes.append(
                        'İşe başlama eğitimi yüz yüze yapılmalıdır '
                        '(2 Nisan 2026 Yönetmeliği md.5).'
                    )

            # Minimum süre kontrolü (eğitim türü tanımından)
            if rec.training_type_id and rec.training_type_id.min_duration_hours:
                if rec.duration_hours < rec.training_type_id.min_duration_hours:
                    compliant = False
                    notes.append(
                        f'Bu eğitim türü için minimum süre '
                        f'{rec.training_type_id.min_duration_hours} saattir.'
                    )

            rec.regulation_compliant = compliant
            rec.compliance_notes = '\n'.join(notes) if notes else 'Uygun'

    def action_confirm(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError(_('Sadece taslak kayıtlar onaylanabilir.'))
            rec.state = 'confirmed'

    def action_cancel(self):
        self.write({'state': 'cancelled'})


class IsgTrainingAttendee(models.Model):
    _name = 'isg.training.attendee'
    _description = 'İSG Eğitim Katılımcısı'

    record_id = fields.Many2one(
        'isg.training.record', string='Eğitim Kaydı',
        required=True, ondelete='cascade',
    )
    employee_id = fields.Many2one(
        'hr.employee', string='Çalışan', required=True,
    )
    workplace_id = fields.Many2one(
        related='employee_id.isg_workplace_id',
        string='İSG İşyeri', store=True, readonly=True,
    )
    attended = fields.Boolean(string='Katıldı', default=True)
    score = fields.Float(string='Sınav Puanı')
    passed = fields.Boolean(string='Geçti', default=True)
    certificate_no = fields.Char(string='Sertifika No')

    # --- Sonraki eğitim tarihi (tehlike sınıfına göre otomatik) ---
    next_training_date = fields.Date(
        string='Sonraki Eğitim Tarihi',
        compute='_compute_next_training_date', store=True,
    )

    @api.depends(
        'record_id.training_date',
        'record_id.training_type_id',
        'employee_id.isg_workplace_id.danger_class',
    )
    def _compute_next_training_date(self):
        for att in self:
            if not att.record_id.training_date or not att.record_id.training_type_id:
                att.next_training_date = False
                continue
            t_type = att.record_id.training_type_id
            danger = att.employee_id.isg_workplace_id.danger_class
            period_map = {
                'low': t_type.period_low,
                'medium': t_type.period_medium,
                'high': t_type.period_high,
            }
            months = period_map.get(danger, t_type.period_medium)
            if months:
                att.next_training_date = (
                    att.record_id.training_date
                    + relativedelta(months=months)
                )
            else:
                att.next_training_date = False
