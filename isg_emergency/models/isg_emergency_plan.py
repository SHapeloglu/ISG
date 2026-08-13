# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgEmergencyPlan(models.Model):
    _name = 'isg.emergency.plan'
    _description = 'Acil Durum Planı'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'plan_date desc, id desc'

    name = fields.Char(
        string='Plan No', required=True, copy=False,
        readonly=True, default=lambda self: 'Yeni',
    )
    title = fields.Char(string='Plan Başlığı', required=True)
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri', required=True, tracking=True,
    )
    site_id = fields.Many2one(
        'isg.site', string='Lokasyon',
        domain="[('workplace_id', '=', workplace_id)]",
    )
    plan_date = fields.Date(
        string='Plan Tarihi', required=True,
        default=fields.Date.context_today,
    )
    review_date = fields.Date(string='Gözden Geçirme Tarihi')
    emergency_types = fields.Many2many(
        'isg.emergency.type', string='Acil Durum Türleri',
    )
    responsible_id = fields.Many2one(
        'hr.employee', string='Sorumlu', tracking=True,
    )
    team_ids = fields.Many2many(
        'hr.employee', 'isg_emergency_plan_team_rel',
        'plan_id', 'employee_id', string='Acil Durum Ekibi',
    )
    assembly_point_ids = fields.Many2many(
        'isg.assembly.point', string='Toplanma Noktaları',
    )
    document_id = fields.Many2one('isg.document', string='Plan Belgesi')
    description = fields.Html(string='Plan İçeriği')
    notes = fields.Text(string='Notlar')

    state = fields.Selection(
        [
            ('draft', 'Taslak'),
            ('active', 'Aktif'),
            ('review', 'Gözden Geçirme'),
            ('archived', 'Arşivlendi'),
        ],
        string='Durum', default='draft', tracking=True, copy=False,
    )
    drill_ids = fields.One2many(
        'isg.emergency.drill', 'plan_id', string='Tatbikatlar',
    )
    drill_count = fields.Integer(
        string='Tatbikat Sayısı', compute='_compute_drill_count',
    )

    @api.depends('drill_ids')
    def _compute_drill_count(self):
        for rec in self:
            rec.drill_count = len(rec.drill_ids)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Yeni') == 'Yeni':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'isg.emergency.plan'
                ) or 'Yeni'
        return super().create(vals_list)

    def action_activate(self):
        self.write({'state': 'active'})

    def action_review(self):
        self.write({'state': 'review'})

    def action_archive_plan(self):
        self.write({'state': 'archived'})

    def action_reset_draft(self):
        self.write({'state': 'draft'})


class IsgEmergencyType(models.Model):
    _name = 'isg.emergency.type'
    _description = 'Acil Durum Türü'
    _order = 'name'

    name = fields.Char(string='Acil Durum Türü', required=True)
    code = fields.Char(string='Kod')
    active = fields.Boolean(default=True)
