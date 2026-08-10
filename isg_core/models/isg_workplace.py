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

    # ── Uzman/Hekim Süre Hesabı (6331 s.K. md.6) ───────────
    @api.depends('danger_class', 'employee_count')
    def _compute_required_expert_minutes(self):
        """
        6331 s.K. md.6 — Aylık gereken uzman çalışma süresi (dakika):
        Az tehlikeli : çalışan × 10 dk
        Tehlikeli    : çalışan × 20 dk
        Çok tehlikeli: çalışan × 40 dk
        """
        katsayi = {'low': 10, 'medium': 20, 'high': 40}
        for rec in self:
            rec.required_expert_minutes = (
                rec.employee_count * katsayi.get(rec.danger_class, 0)
            )

    required_expert_minutes = fields.Integer(
        string='Gereken Uzman Süresi (dk/ay)',
        compute='_compute_required_expert_minutes',
        store=True,
    )

    @api.depends('danger_class', 'employee_count')
    def _compute_required_physician_minutes(self):
        """
        6331 s.K. md.6 — Aylık gereken hekim çalışma süresi (dakika):
        Az tehlikeli : çalışan × 4 dk
        Tehlikeli    : çalışan × 6 dk
        Çok tehlikeli: çalışan × 15 dk
        """
        katsayi = {'low': 4, 'medium': 6, 'high': 15}
        for rec in self:
            rec.required_physician_minutes = (
                rec.employee_count * katsayi.get(rec.danger_class, 0)
            )

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
