# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
class IsgVisitor(models.Model):
    _name = 'isg.visitor'
    _description = 'İSG Ziyaretçi Kaydı'
    _inherit = ['mail.thread']
    _order = 'entry_datetime desc'
    name = fields.Char(
        string='Ziyaretçi No', required=True, copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('isg.visitor'),
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İşyeri',
        required=True, ondelete='cascade', tracking=True,
    )
    visitor_name = fields.Char(string='Ad Soyad', required=True)
    visitor_company = fields.Char(string='Kurum / Firma')
    visitor_tc = fields.Char(string='TC Kimlik No')
    visitor_phone = fields.Char(string='Telefon')
    purpose = fields.Selection(
        selection=[
            ('meeting', 'Toplantı'),
            ('inspection', 'Denetim / Müfettiş'),
            ('contractor', 'Alt İşveren / Taşeron'),
            ('delivery', 'Teslimat'),
            ('maintenance', 'Bakım / Onarım'),
            ('other', 'Diğer'),
        ],
        string='Ziyaret Amacı', required=True, default='meeting', tracking=True,
    )
    host_employee_id = fields.Many2one(
        'hr.employee', string='Karşılayan Kişi', tracking=True,
    )
    entry_datetime = fields.Datetime(
        string='Giriş Zamanı', required=True,
        default=fields.Datetime.now, tracking=True,
    )
    exit_datetime = fields.Datetime(
        string='Çıkış Zamanı', tracking=True,
    )
    state = fields.Selection(
        selection=[
            ('inside', 'İçeride'),
            ('exited', 'Çıktı'),
        ],
        string='Durum', default='inside', tracking=True,
    )
    ppe_required = fields.Boolean(
        string='KKD Gerekiyor', default=False, tracking=True,
    )
    ppe_given = fields.Boolean(
        string='KKD Verildi', default=False, tracking=True,
    )
    ppe_notes = fields.Char(
        string='Verilen KKD',
    )
    induction_done = fields.Boolean(
        string='Güvenlik Brifing Verildi', default=False, tracking=True,
    )
    # ─── Risk Bilgilendirmesi (2 Nisan 2026 Yönetmeliği) ─────
    risk_briefing_ack = fields.Boolean(
        string='İşyerine Özgü Risk Bilgilendirmesi Verildi',
        default=False, tracking=True,
    )
    risk_briefing_date = fields.Date(
        string='Risk Bilgilendirmesi Tarihi', tracking=True,
    )
    risk_briefing_attachment_ids = fields.Many2many(
        'ir.attachment', string='Risk Bilgilendirmesi Tutanakları',
    )
    site_id = fields.Many2one(
        'isg.site', string='Gidilen Alan',
        domain="[('workplace_id', '=', workplace_id)]",
    )
    notes = fields.Text(string='Notlar')
    duration_hours = fields.Float(
        string='Ziyaret Süresi (Saat)',
        compute='_compute_duration', store=True,
    )
    @api.depends('entry_datetime', 'exit_datetime')
    def _compute_duration(self):
        for rec in self:
            if rec.entry_datetime and rec.exit_datetime:
                delta = rec.exit_datetime - rec.entry_datetime
                rec.duration_hours = delta.total_seconds() / 3600
            else:
                rec.duration_hours = 0.0
    @api.constrains('entry_datetime', 'exit_datetime')
    def _check_exit_after_entry(self):
        for rec in self:
            if rec.exit_datetime and rec.entry_datetime:
                if rec.exit_datetime < rec.entry_datetime:
                    raise ValidationError(
                        'Çıkış zamanı giriş zamanından önce olamaz.'
                    )
    def action_exit(self):
        self.write({
            'state': 'exited',
            'exit_datetime': fields.Datetime.now(),
        })
