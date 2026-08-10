# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class IsgTrainingPlan(models.Model):
    _name = 'isg.training.plan'
    _description = 'İSG Eğitim Planı'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'isg.uuid.mixin']
    _order = 'year desc, workplace_id'

    name = fields.Char(
        string='Plan Adı', required=True, tracking=True,
    )
    year = fields.Integer(
        string='Yıl', required=True,
        default=lambda self: fields.Date.today().year,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri', required=True, tracking=True,
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Taslak'),
            ('approved', 'Onaylı'),
            ('done', 'Tamamlandı'),
            ('cancelled', 'İptal'),
        ],
        string='Durum', default='draft', tracking=True,
    )
    line_ids = fields.One2many(
        'isg.training.plan.line', 'plan_id', string='Eğitim Kalemleri',
    )
    total_planned = fields.Integer(
        string='Planlanan Eğitim Sayısı', compute='_compute_totals', store=True,
    )
    total_completed = fields.Integer(
        string='Tamamlanan Eğitim Sayısı', compute='_compute_totals', store=True,
    )
    notes = fields.Text(string='Notlar')

    @api.depends('line_ids', 'line_ids.state')
    def _compute_totals(self):
        for plan in self:
            plan.total_planned = len(plan.line_ids)
            plan.total_completed = len(plan.line_ids.filtered(
                lambda l: l.state == 'done'
            ))

    def action_approve(self):
        for plan in self:
            if plan.state != 'draft':
                raise UserError(_('Sadece taslak planlar onaylanabilir.'))
            plan.state = 'approved'

    def action_cancel(self):
        self.write({'state': 'cancelled'})


class IsgTrainingPlanLine(models.Model):
    _name = 'isg.training.plan.line'
    _description = 'İSG Eğitim Planı Kalemi'
    _order = 'planned_date'

    plan_id = fields.Many2one(
        'isg.training.plan', string='Eğitim Planı',
        required=True, ondelete='cascade',
    )
    training_type_id = fields.Many2one(
        'isg.training.type', string='Eğitim Türü', required=True,
    )
    planned_date = fields.Date(string='Planlanan Tarih')
    planned_duration_hours = fields.Float(string='Planlanan Süre (Saat)')
    target_employee_count = fields.Integer(string='Hedef Katılımcı Sayısı')
    trainer = fields.Char(string='Eğitmen / Kurum')
    state = fields.Selection(
        selection=[
            ('planned', 'Planlandı'),
            ('done', 'Tamamlandı'),
            ('cancelled', 'İptal'),
        ],
        string='Durum', default='planned',
    )
    training_record_id = fields.Many2one(
        'isg.training.record', string='Eğitim Kaydı',
    )
    notes = fields.Text(string='Notlar')
