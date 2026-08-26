# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime


class IsgOsgbAssignment(models.Model):
    _name = 'isg.osgb.assignment'
    _description = 'OSGB İşyeri-Uzman Atama'
    _order = 'osgb_id, workplace_id, assignment_date desc'

    osgb_id = fields.Many2one(
        'isg.osgb', string='OSGB', required=True, ondelete='cascade',
    )
    company_id = fields.Many2one(
        related='osgb_id.company_id', string='Şirket', store=True, readonly=True,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İşyeri', required=True, ondelete='cascade',
    )
    expert_id = fields.Many2one(
        'isg.osgb.expert', string='Görevli Uzman', ondelete='set null',
        domain="[('osgb_id', '=', osgb_id)]",
    )
    role = fields.Selection([
        ('expert', 'İSG Uzmanı'),
        ('physician', 'İşyeri Hekimi'),
    ], string='Rol', required=True, default='expert',
    )

    # --- Sözleşme ---
    assignment_date = fields.Date(
        string='Atama Başlangıcı', required=True,
        default=lambda self: fields.Date.today(),
    )
    termination_date = fields.Date(string='Atama Bitişi')
    contract_no = fields.Char(string='Sözleşme No')

    # --- Süre (ay bazında) ---
    monthly_visit_days = fields.Integer(
        string='Aylık Ziyaret Günleri', default=1,
    )
    monthly_required_minutes = fields.Integer(
        string='Gereken Aylık Dakika (Hesaplı)', 
        compute='_compute_required_minutes', store=True,
    )
    monthly_actual_minutes = fields.Integer(
        string='Fiili Aylık Dakika', default=0,
    )
    compliance_status = fields.Selection(
        [('compliant', 'Uyumlu'), ('warning', 'Uyarı'), ('non_compliant', 'Uyumsuz')],
        string='Uygunluk Durumu',
        compute='_compute_compliance_status', store=True,
    )

    # --- İSG-KATİP ---
    katip_notification_sent = fields.Boolean(
        string='İSG-KATİP Bildirimi Gönderildi', default=False,
    )
    katip_notification_date = fields.Date(
        string='İSG-KATİP Bildirimi Tarihi',
    )

    active = fields.Boolean(default=True)
    notes = fields.Text(string='Notlar')

    @api.depends('workplace_id.danger_class', 'role')
    def _compute_required_minutes(self):
        """6331 s.K. md.6 — gereken aylık dakika."""
        for rec in self:
            rate_table = self.env['isg.rate.table']
            danger_class = rec.workplace_id.danger_class
            role_map = {'expert': 'expert', 'physician': 'physician'}
            role = role_map.get(rec.role)
            rate = rate_table.get_rate(danger_class, role) if role else 0
            rec.monthly_required_minutes = rec.workplace_id.employee_count * rate if rec.workplace_id else 0

    @api.depends('monthly_actual_minutes', 'monthly_required_minutes')
    def _compute_compliance_status(self):
        """Aylık dakika uygunluğu."""
        for rec in self:
            if rec.monthly_required_minutes == 0:
                rec.compliance_status = 'compliant'
            elif rec.monthly_actual_minutes >= rec.monthly_required_minutes * 0.9:  # %90 tolerans
                rec.compliance_status = 'compliant'
            elif rec.monthly_actual_minutes >= rec.monthly_required_minutes * 0.75:
                rec.compliance_status = 'warning'
            else:
                rec.compliance_status = 'non_compliant'

    def action_record_visit(self):
        """Ziyaret saati kaydet (action button)."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Ziyaret Kaydı',
            'res_model': 'isg.osgb.visit',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_assignment_id': self.id},
        }
