# -*- coding: utf-8 -*-
from odoo import models, fields, api


class IsgPenalty(models.Model):
    _name = 'isg.penalty'
    _description = 'İSG Olası Ceza Kaydı'
    _order = 'create_date desc'

    name = fields.Char(string='Ceza No', required=True, copy=False,
                        default='Yeni', readonly=True)

    compliance_id = fields.Many2one('isg.compliance', string='Uygunluk Kaydı',
                                     required=True, ondelete='cascade')
    tariff_id = fields.Many2one('isg.penalty.tariff', string='Ceza Tarifesi',
                                 required=True)

    workplace_id = fields.Many2one('isg.workplace', string='İşyeri',
                                    related='compliance_id.workplace_id',
                                    store=True, readonly=True)
    obligation_id = fields.Many2one('isg.obligation', string='Yükümlülük',
                                     related='compliance_id.obligation_id',
                                     store=True, readonly=True)

    employee_count = fields.Integer(string='Çalışan Sayısı',
                                     help="Çalışan başına ceza hesaplaması için")
    is_repeat_violation = fields.Boolean(string='Tekrar İhlal', default=False)

    calculated_amount = fields.Monetary(string='Hesaplanan Tutar (TL)',
                                         compute='_compute_calculated_amount',
                                         store=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Para Birimi',
                                   related='tariff_id.currency_id', store=True)

    status = fields.Selection([
        ('draft', 'Taslak'),
        ('notified', 'Bildirildi'),
        ('appealed', 'İtiraz'),
        ('finalized', 'Kesinleşti'),
        ('paid', 'Ödendi'),
    ], string='Durum', default='draft', required=True)

    notification_date = fields.Date(string='Bildirim Tarihi')
    payment_due_date = fields.Date(string='Ödeme Vade Tarihi')

    evaluator_id = fields.Many2one('res.users', string='Hesaplayan',
                                    default=lambda self: self.env.user)
    notes = fields.Text(string='Notlar')

    @api.depends('tariff_id', 'tariff_id.amount_2026', 'tariff_id.amount_per_employee',
                 'employee_count', 'is_repeat_violation', 'tariff_id.repeat_multiplier')
    def _compute_calculated_amount(self):
        for rec in self:
            amount = rec.tariff_id.amount_2026 or 0.0
            if rec.tariff_id.amount_per_employee and rec.employee_count:
                amount = amount * rec.employee_count
            if rec.is_repeat_violation and rec.tariff_id.repeat_multiplier:
                amount = amount * rec.tariff_id.repeat_multiplier
            rec.calculated_amount = amount

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Yeni') == 'Yeni':
                vals['name'] = self.env['ir.sequence'].next_by_code('isg.penalty') or 'Yeni'
        return super().create(vals_list)
