# -*- coding: utf-8 -*-
from odoo import models, fields, api


class IsgOsgb(models.Model):
    _name = 'isg.osgb'
    _description = 'Ortak Sağlık ve Güvenlik Birliği (OSGB)'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'isg.uuid.mixin']
    _order = 'name'

    name = fields.Char(
        string='OSGB Adı', required=True, tracking=True,
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )

    # --- Yetki Belgesi (Bakanlık) ---
    ministry_certificate_no = fields.Char(
        string='Bakanlık Yetki Belgesi No', tracking=True,
    )
    ministry_certificate_date = fields.Date(
        string='Belge Tarihi', tracking=True,
    )
    ministry_certificate_expiry = fields.Date(
        string='Belge Geçerlilik Bitiş', tracking=True,
    )

    # --- İletişim ---
    address = fields.Text(string='Adres')
    phone = fields.Char(string='Telefon')
    email = fields.Char(string='E-posta')
    website = fields.Char(string='Web Sitesi')

    # --- Kadro ---
    expert_ids = fields.One2many(
        'isg.osgb.expert', 'osgb_id', string='İSG Uzmanları',
    )
    expert_count = fields.Integer(
        string='Uzman Sayısı', compute='_compute_expert_count', store=True,
    )

    physician_ids = fields.One2many(
        'isg.osgb.physician', 'osgb_id', string='İşyeri Hekimleri',
    )
    physician_count = fields.Integer(
        string='Hekim Sayısı', compute='_compute_physician_count', store=True,
    )

    # --- Atamalar ---
    assignment_ids = fields.One2many(
        'isg.osgb.assignment', 'osgb_id', string='İşyeri Atamaları',
    )
    assignment_count = fields.Integer(
        string='Atama Sayısı', compute='_compute_assignment_count', store=True,
    )

    # --- Not ---
    notes = fields.Text(string='Notlar')

    # --- Durum ---
    active = fields.Boolean(default=True)

    @api.depends('expert_ids')
    def _compute_expert_count(self):
        for rec in self:
            rec.expert_count = len(rec.expert_ids)

    @api.depends('physician_ids')
    def _compute_physician_count(self):
        for rec in self:
            rec.physician_count = len(rec.physician_ids)

    @api.depends('assignment_ids')
    def _compute_assignment_count(self):
        for rec in self:
            rec.assignment_count = len(rec.assignment_ids)

    def name_get(self):
        result = []
        for rec in self:
            name = f'[{rec.company_id.name}] {rec.name}' if rec.company_id else rec.name
            result.append((rec.id, name))
        return result
