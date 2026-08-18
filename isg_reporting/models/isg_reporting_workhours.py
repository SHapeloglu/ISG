from odoo import models, fields, api
from odoo.exceptions import ValidationError


class IsgReportingWorkhours(models.Model):
    _name = 'isg.reporting.workhours'
    _description = 'İSG Aylık Çalışılan Saat Kaydı'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'period_date desc, workplace_id'

    workplace_id = fields.Many2one(
        'isg.workplace',
        string='İşyeri',
        required=True,
        tracking=True,
        index=True,
    )
    company_id = fields.Many2one(
        related='workplace_id.company_id',
        string='Şirket',
        store=True,
        readonly=True,
    )
    period_date = fields.Date(
        string='Dönem (Ayın İlk Günü)',
        required=True,
        tracking=True,
        help="Örn: 2026-08-01 (Ağustos 2026 dönemi için)",
    )
    period_display = fields.Char(
        string='Dönem',
        compute='_compute_period_display',
        store=True,
    )
    total_worked_hours = fields.Float(
        string='Toplam Çalışılan Saat',
        required=True,
        tracking=True,
        help="İşyerindeki tüm çalışanların o ay toplam çalıştığı saat",
    )
    employee_count_snapshot = fields.Integer(
        string='Çalışan Sayısı (O Dönem)',
        help="Referans amaçlı, KPI hesaplamasına dahil edilmez",
    )
    notes = fields.Text(string='Notlar')

    _sql_constraints = [
        (
            'workplace_period_unique',
            'unique(workplace_id, period_date)',
            'Bu işyeri için bu döneme ait kayıt zaten mevcut!',
        ),
    ]

    @api.depends('period_date')
    def _compute_period_display(self):
        for rec in self:
            if rec.period_date:
                rec.period_display = rec.period_date.strftime('%m/%Y')
            else:
                rec.period_display = ''

    @api.constrains('total_worked_hours')
    def _check_positive_hours(self):
        for rec in self:
            if rec.total_worked_hours <= 0:
                raise ValidationError('Toplam çalışılan saat sıfırdan büyük olmalıdır.')

    @api.constrains('period_date')
    def _check_period_is_first_day(self):
        for rec in self:
            if rec.period_date and rec.period_date.day != 1:
                raise ValidationError('Dönem tarihi ayın ilk günü olmalıdır (örn: 2026-08-01).')
