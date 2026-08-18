from dateutil.relativedelta import relativedelta
from datetime import timedelta

from odoo import models, fields, api


class IsgReportingWorkhoursKpi(models.Model):
    _inherit = 'isg.reporting.workhours'

    period_end_date = fields.Date(
        string='Dönem Bitiş',
        compute='_compute_period_end_date',
        store=True,
    )
    recordable_incident_count = fields.Integer(
        string='Kayıt Edilebilir Olay Sayısı',
        compute='_compute_kpi',
        store=True,
        help="incident_type in (Kaza, Meslek Hastalığı) ve yaralanma var (injury_type != Yok)",
    )
    near_miss_count = fields.Integer(
        string='Ramak Kala Sayısı',
        compute='_compute_kpi',
        store=True,
        help="Öncü gösterge, TRIR hesabına dahil edilmez",
    )
    lost_work_days_total = fields.Integer(
        string='Toplam Kayıp İş Günü',
        compute='_compute_kpi',
        store=True,
    )
    trir = fields.Float(
        string='TRIR',
        compute='_compute_kpi',
        store=True,
        digits=(6, 2),
        help="(Kayıt Edilebilir Olay x 200.000) / Toplam Çalışılan Saat",
    )
    lwdr = fields.Float(
        string='LWDR',
        compute='_compute_kpi',
        store=True,
        digits=(6, 2),
        help="(Kayıp İş Günü x 200.000) / Toplam Çalışılan Saat",
    )

    @api.depends('period_date')
    def _compute_period_end_date(self):
        for rec in self:
            if rec.period_date:
                rec.period_end_date = (
                    rec.period_date + relativedelta(months=1) - timedelta(days=1)
                )
            else:
                rec.period_end_date = False

    @api.depends('workplace_id', 'period_date', 'period_end_date', 'total_worked_hours')
    def _compute_kpi(self):
        Incident = self.env['isg.incident']
        for rec in self:
            if not (rec.workplace_id and rec.period_date and rec.period_end_date):
                rec.recordable_incident_count = 0
                rec.near_miss_count = 0
                rec.lost_work_days_total = 0
                rec.trir = 0.0
                rec.lwdr = 0.0
                continue

            base_domain = [
                ('workplace_id', '=', rec.workplace_id.id),
                ('incident_date', '>=', rec.period_date),
                ('incident_date', '<=', rec.period_end_date),
            ]

            recordable_domain = base_domain + [
                ('incident_type', 'in', ['accident', 'occupational_disease']),
                ('injury_type', '!=', 'none'),
            ]
            recordable = Incident.search(recordable_domain)
            rec.recordable_incident_count = len(recordable)
            rec.lost_work_days_total = sum(recordable.mapped('lost_work_days'))

            near_miss_domain = base_domain + [('incident_type', '=', 'near_miss')]
            rec.near_miss_count = Incident.search_count(near_miss_domain)

            if rec.total_worked_hours:
                rec.trir = (rec.recordable_incident_count * 200000) / rec.total_worked_hours
                rec.lwdr = (rec.lost_work_days_total * 200000) / rec.total_worked_hours
            else:
                rec.trir = 0.0
                rec.lwdr = 0.0
