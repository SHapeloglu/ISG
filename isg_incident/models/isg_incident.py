# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, timedelta

class IsgIncident(models.Model):
    _name = 'isg.incident'
    _description = 'İş Kazası / Ramak Kala / Meslek Hastalığı'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'isg.uuid.mixin']
    _order = 'incident_date desc, id desc'

    # --- Temel Bilgiler ---
    name = fields.Char(
        string='Kaza No', readonly=True, tracking=True,
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company, tracking=True,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İşyeri', required=True, ondelete='restrict',
        tracking=True,
    )
    site_id = fields.Many2one(
        'isg.site', string='Fiziksel Lokasyon',
    )

    # --- Kaza Tarihi/Saati ---
    incident_date = fields.Datetime(
        string='Kaza Tarihi/Saati', required=True,
        default=lambda self: fields.Datetime.now(), tracking=True,
    )

    # --- Kaza Türü ---
    incident_type = fields.Selection([
        ('accident', 'İş Kazası'),
        ('near_miss', 'Ramak Kala'),
        ('occupational_disease', 'Meslek Hastalığı'),
    ], string='Kaza Türü', required=True, default='accident', tracking=True,
    )

    # --- Şiddet ---
    severity = fields.Selection([
        ('minor', 'Hafif (İlk Yardım)'),
        ('serious', 'Ciddi (Hastanelik)'),
        ('fatal', 'Ölümcül'),
    ], string='Şiddet', required=True, default='minor', tracking=True,
    )

    # --- Açıklamalar ---
    description = fields.Text(
        string='Kaza Açıklaması', required=True, tracking=True,
    )
    location_description = fields.Text(
        string='Kazanın Meydana Geldiği Yer',
    )

    # --- Yaralanan Kişi ---
    injured_employee_id = fields.Many2one(
        'hr.employee', string='Yaralanan Çalışan',
    )
    injured_person_name = fields.Char(
        string='Yaralanan Adı (Kontraktor/Ziyaretçi ise)',
    )

    # --- Yaralanma Detayları ---
    injury_ids = fields.One2many(
        'isg.incident.injury', 'incident_id', string='Yaralanma Detayları',
    )

    # --- Tanıklar ---
    witnesses = fields.Text(string='Tanık Adları')

    # --- Acil İşlemler ---
    immediate_action = fields.Text(string='Alınan Acil İşlemler')

    # --- Soruşturma ---
    investigation_date = fields.Date(string='Soruşturma Tarihi')
    investigation_notes = fields.Text(string='Soruşturma Bulguları')

    # --- Koku Analizi (CAPA) ---
    root_cause_analysis_id = fields.Many2one(
        'isg.capa', string='Koku Analizi (DÖF)',
    )

    # --- Durum ---
    state = fields.Selection([
        ('reported', 'Bildirildi'),
        ('investigating', 'Soruşturma Devam Ediyor'),
        ('analyzed', 'Analiz Tamamlandı'),
        ('resolved', 'Kapalı'),
    ], string='Durum', required=True, default='reported', tracking=True,
    )

    # --- SGK Bildirimi ---
    sgk_notification_required = fields.Boolean(
        string='SGK Bildirimi Gerekli',
        compute='_compute_sgk_notification_required', store=True, tracking=True,
    )
    sgk_notification_date = fields.Date(
        string='SGK Bildirimi Tarihi', tracking=True,
    )
    sgk_notification_deadline = fields.Date(
        string='SGK Bildirim Süresi (3 İş Günü)',
        compute='_compute_sgk_notification_deadline', store=True,
    )
    sgk_days_remaining = fields.Integer(
        string='Kalan Gün',
        compute='_compute_sgk_days_remaining', store=True,
    )

    # --- Dönüş Eğitimi ---
    return_to_work_required = fields.Boolean(
        string='Dönüş Eğitimi Gerekli',
        compute='_compute_return_to_work_required', store=True,
    )
    return_to_work_training_id = fields.Many2one(
        'isg.training.record', string='Dönüş Eğitimi',
    )

    # --- TRIR ---
    trir_eligible = fields.Boolean(
        string='TRIR\'a Dahil',
        compute='_compute_trir_eligible', store=True,
    )

    # --- Sistem ---
    created_date = fields.Datetime(readonly=True, tracking=True)
    created_by_id = fields.Many2one('res.users', readonly=True)
    notes = fields.Text(string='Ek Notlar')
    active = fields.Boolean(default=True)

    @api.model
    def create(self, vals):
        if 'name' not in vals:
            vals['name'] = self.env['ir.sequence'].next_by_code('isg.incident') or '/'
        vals['created_date'] = fields.Datetime.now()
        vals['created_by_id'] = self.env.user.id
        return super().create(vals)

    @api.depends('incident_type', 'severity')
    def _compute_sgk_notification_required(self):
        """SGK bildirimi gerekli mi?"""
        for rec in self:
            rec.sgk_notification_required = (
                rec.incident_type in ['accident', 'occupational_disease']
                and rec.severity in ['serious', 'fatal']
            )

    @api.depends('incident_date', 'sgk_notification_required')
    def _compute_sgk_notification_deadline(self):
        """SGK bildirimi süresi: incident_date + 3 iş günü (basit: +4 takvim günü)"""
        for rec in self:
            if rec.sgk_notification_required and rec.incident_date:
                # Basit hesaplama: 3 iş günü ≈ 4 takvim günü (hafta sonu kurtarma)
                deadline = rec.incident_date + timedelta(days=4)
                rec.sgk_notification_deadline = deadline.date()
            else:
                rec.sgk_notification_deadline = None

    @api.depends('sgk_notification_deadline')
    def _compute_sgk_days_remaining(self):
        """Kalan gün (uyarı için)"""
        for rec in self:
            if rec.sgk_notification_deadline:
                remaining = (rec.sgk_notification_deadline - fields.Date.today()).days
                rec.sgk_days_remaining = remaining
            else:
                rec.sgk_days_remaining = None

    @api.depends('state', 'injury_ids')
    def _compute_return_to_work_required(self):
        """Dönüş eğitimi gerekli mi?"""
        for rec in self:
            rec.return_to_work_required = (
                rec.state == 'resolved'
                and any(inj.needs_return_training for inj in rec.injury_ids)
            )

    @api.depends('incident_type', 'injury_ids')
    def _compute_trir_eligible(self):
        """TRIR'a dahil mi?"""
        for rec in self:
            has_lost_time = any(
                inj.injury_type in ['lost_time', 'permanent_disability', 'fatality']
                for inj in rec.injury_ids
            )
            rec.trir_eligible = (
                rec.incident_type in ['accident', 'occupational_disease']
                and has_lost_time
            )

    def action_start_investigation(self):
        """Soruşturma başla"""
        self.ensure_one()
        self.state = 'investigating'
        self.investigation_date = fields.Date.today()

    def action_add_root_cause(self):
        """Koku analizi oluştur (CAPA)"""
        self.ensure_one()
        capa = self.env['isg.capa'].create({
            'name': f'Kuka Analizi: {self.name}',
            'workplace_id': self.workplace_id.id,
            'incident_id': self.id,
            'description': f'Kaza: {self.description}',
        })
        self.root_cause_analysis_id = capa.id
        self.state = 'analyzed'
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'isg.capa',
            'res_id': capa.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_create_return_training(self):
        """Dönüş eğitimi oluştur (RG 33212 Md 14)"""
        self.ensure_one()
        if not self.return_to_work_required:
            raise UserError(_('Bu kaza için dönüş eğitimi gerekli değil.'))
        training_record = self.env['isg.training.record'].create({
            'name': f'Dönüş Eğitimi: {self.name}',
            'training_type_id': self.env.ref('isg_training.training_type_return').id,
            'training_date': fields.Date.today() + timedelta(days=5),
            'workplace_id': self.workplace_id.id,
            'duration_hours': 8.0,
            'company_id': self.company_id.id,
            'attendee_ids': [(0, 0, {'employee_id': self.injured_employee_id.id})],
        })
        self.return_to_work_training_id = training_record.id

    def action_close(self):
        """Kazayı kapat"""
        self.ensure_one()
        self.state = 'resolved'
        # Dönüş eğitimi gerekli ise otomatik oluştur
        if self.return_to_work_required and not self.return_to_work_training_id:
            self.action_create_return_training()

    def name_get(self):
        result = []
        for rec in self:
            name = f'{rec.name} - {rec.workplace_id.name}' if rec.workplace_id else rec.name
            result.append((rec.id, name))
        return result
