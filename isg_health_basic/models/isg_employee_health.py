# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import AccessError


class IsgEmployeeHealth(models.Model):
    _name = 'isg.employee.health'
    _description = 'Çalışan Sağlık Muayenesi (KVKK Uyumlu)'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'examination_date desc'

    # ─── Temel Referanslar ───────────────────────────────────
    employee_id = fields.Many2one(
        'hr.employee', string='Çalışan', required=True, ondelete='restrict', tracking=True,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='Çalışma Yeri', compute='_compute_workplace_id', readonly=True,
    )

    # ─── Muayene Bilgileri ───────────────────────────────────
    examination_date = fields.Date(
        string='Muayene Tarihi', required=True, default=fields.Date.context_today, tracking=True,
    )
    examiner_id = fields.Many2one(
        'res.partner', string='Muayene Yapan Hekim', required=True, tracking=True,
        domain=[('is_occupational_physician', '=', True)],
    )

    # ─── Fiziksel Ölçümler ───────────────────────────────────
    systolic_bp = fields.Integer(string='Sistolik Basınç (mmHg)')
    diastolic_bp = fields.Integer(string='Diastolik Basınç (mmHg)')
    heart_rate = fields.Integer(string='Kalp Atışı (bpm)')
    weight_kg = fields.Float(string='Ağırlık (kg)')
    height_cm = fields.Integer(string='Boy (cm)')
    bmi = fields.Float(string='BMI', compute='_compute_bmi', store=True)

    # ─── Muayene Sonucu ─────────────────────────────────────
    result = fields.Selection([
        ('fit', 'Uygun'),
        ('unfit', 'Uygun Değil'),
        ('conditional', 'Şartlı Uygun'),
    ], string='Muayene Sonucu', required=True, tracking=True)

    restrictions = fields.Text(
        string='Çalışma Kısıtlamaları',
        help='Eğer "Şartlı Uygun" ise, işyerinde uygulanacak kısıtlamalar',
    )

    # ─── Hekim Notları (KVKK: Şifrelenmiş) ───────────────────
    physician_notes = fields.Text(
        string='Hekim Notları',
        help='Sadece hekim ve yönetici tarafından görülebilir',
    )

    # ─── Sistem Alanları ────────────────────────────────────
    created_date = fields.Datetime(string='Oluşturma Tarihi', readonly=True)
    created_by_id = fields.Many2one('res.users', string='Oluşturan', readonly=True)

    @api.depends('weight_kg', 'height_cm')
    def _compute_bmi(self):
        for rec in self:
            if rec.weight_kg and rec.height_cm:
                height_m = rec.height_cm / 100.0
                rec.bmi = rec.weight_kg / (height_m ** 2)
            else:
                rec.bmi = 0.0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['created_date'] = fields.Datetime.now()
            vals['created_by_id'] = self.env.user.id
        return super().create(vals_list)

    @api.depends('employee_id')
    def _compute_workplace_id(self):
        for rec in self:
            if rec.employee_id and hasattr(rec.employee_id, 'workplace_id'):
                rec.workplace_id = rec.employee_id.workplace_id
            else:
                rec.workplace_id = False
