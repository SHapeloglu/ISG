# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class IsgWorkplace(models.Model):
    _name = 'isg.workplace'
    _description = 'İSG İşyeri'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    # ── Temel Bilgiler ──────────────────────────────────────
    name = fields.Char(
        string='İşyeri Adı',
        required=True,
        tracking=True,
    )
    company_id = fields.Many2one(
        'res.company',
        string='Şirket',
        required=True,
        default=lambda self: self.env.company,
        tracking=True,
    )
    active = fields.Boolean(default=True)

    # ── SGK / Mevzuat Bilgileri ─────────────────────────────
    sgk_workplace_code = fields.Char(
        string='SGK İşyeri Sicil No',
        tracking=True,
    )
    nace_code = fields.Char(
        string='NACE Kodu',
        tracking=True,
    )
    danger_class = fields.Selection([
        ('low',      'Az Tehlikeli'),
        ('medium',   'Tehlikeli'),
        ('high',     'Çok Tehlikeli'),
    ],
        string='Tehlike Sınıfı',
        required=True,
        tracking=True,
    )
    employee_count = fields.Integer(
        string='Çalışan Sayısı',
        tracking=True,
    )
    sector = fields.Char(
        string='Sektör',
        tracking=True,
    )
    is_public = fields.Boolean(
        string='Kamu İşyeri mi?',
        tracking=True,
    )

    # ── İletişim ────────────────────────────────────────────
    address = fields.Text(string='Adres')
    city = fields.Char(string='İl')
    district = fields.Char(string='İlçe')
    phone = fields.Char(string='Telefon')
    email = fields.Char(string='E-posta')

    # ── İlişkiler ───────────────────────────────────────────
    site_ids = fields.One2many(
        'isg.site',
        'workplace_id',
        string='Fiziksel Siteler',
    )
    site_count = fields.Integer(
        string='Site Sayısı',
        compute='_compute_site_count',
    )
    danger_class_history_ids = fields.One2many(
        'isg.workplace.danger_class.history',
        'workplace_id',
        string='Tehlike Sınıfı Değişim Geçmişi',
        readonly=True,
    )

    # ── Hesaplama ───────────────────────────────────────────
    @api.depends('site_ids')
    def _compute_site_count(self):
        for rec in self:
            rec.site_count = len(rec.site_ids)

    # ── Kısıtlar ────────────────────────────────────────────
    @api.constrains('employee_count')
    def _check_employee_count(self):
        for rec in self:
            if rec.employee_count < 0:
                raise ValidationError('Çalışan sayısı negatif olamaz.')

    # ── Tehlike Sınıfı Değişim Geçmişi (B-9) ─────────────────
    @api.onchange('danger_class')
    def _onchange_danger_class(self):
        """Tehlike sınıfı değiştiğinde, history kaydı oluştur"""
        if self.id and self.danger_class:
            # Veritabanından mevcut değeri oku
            old_record = self.env['isg.workplace'].browse(self.id)
            old_danger_class = old_record.danger_class
            
            # Değişim varsa history kaydı oluştur
            if old_danger_class and old_danger_class != self.danger_class:
                self.env['isg.workplace.danger_class.history'].create({
                    'workplace_id': self.id,
                    'danger_class_old': old_danger_class,
                    'danger_class_new': self.danger_class,
                    'change_date': fields.Date.context_today(self),
                    'reason': f'Tehlike sınıfı {old_danger_class} → {self.danger_class} olarak değiştirildi',
                })

    # ── Uzman/Hekim Süre Hesabı (6331 s.K. md.6) ───────────
    # NOT: Katsayılar artık isg.rate.table modelinden okunuyor (versiyonlu).
    # Eskiden burada hardcoded dict vardı; isg_osgb da aynı tabloyu kullanacağı
    # için tek kaynağa taşındı (bkz. BACKLOG.md B-1).
    @api.depends('danger_class', 'employee_count')
    def _compute_required_expert_minutes(self):
        RateTable = self.env['isg.rate.table']
        for rec in self:
            rate = RateTable.get_rate(rec.danger_class, 'expert')
            rec.required_expert_minutes = rec.employee_count * rate

    required_expert_minutes = fields.Integer(
        string='Gereken Uzman Süresi (dk/ay)',
        compute='_compute_required_expert_minutes',
        store=True,
    )

    @api.depends('danger_class', 'employee_count')
    def _compute_required_physician_minutes(self):
        RateTable = self.env['isg.rate.table']
        for rec in self:
            rate = RateTable.get_rate(rec.danger_class, 'physician')
            rec.required_physician_minutes = rec.employee_count * rate

    required_physician_minutes = fields.Integer(
        string='Gereken Hekim Süresi (dk/ay)',
        compute='_compute_required_physician_minutes',
        store=True,
    )

    def name_get(self):
        result = []
        for rec in self:
            name = f'[{rec.company_id.name}] {rec.name}' if rec.company_id else rec.name
            result.append((rec.id, name))
        return result

    def action_open_sites(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Fiziksel Siteler',
            'res_model': 'isg.site',
            'view_mode': 'list,form',
            'domain': [('workplace_id', '=', self.id)],
            'context': {'default_workplace_id': self.id},
        }
