# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class IsgBoardMember(models.Model):
    _name = 'isg.board.member'
    _description = 'İSG Kurulu Üyesi'
    _inherit = ['mail.thread']
    _order = 'role, name'

    workplace_id = fields.Many2one(
        'isg.workplace', string='İşyeri',
        required=True, ondelete='cascade', tracking=True,
    )
    employee_id = fields.Many2one(
        'hr.employee', string='Çalışan',
        required=True, tracking=True,
    )
    name = fields.Char(
        related='employee_id.name', string='Ad Soyad', store=True,
    )
    role = fields.Selection(
        selection=[
            ('chair', 'Kurul Başkanı (İşveren/Vekili)'),
            ('secretary', 'Kurul Sekreteri (İSG Uzmanı)'),
            ('physician', 'İşyeri Hekimi'),
            ('hr_rep', 'İnsan Kaynakları Temsilcisi'),
            ('foreman', 'Formen veya Ustabaşı'),
            ('worker_rep', 'Çalışan Temsilcisi'),
            ('other', 'Diğer Üye'),
        ],
        string='Kurul Rolü', required=True, tracking=True,
    )
    start_date = fields.Date(
        string='Göreve Başlama', required=True, tracking=True,
    )
    end_date = fields.Date(
        string='Görev Bitiş', tracking=True,
    )
    is_active = fields.Boolean(
        string='Aktif', default=True, tracking=True,
    )
    notes = fields.Text(string='Notlar')

    @api.constrains('workplace_id', 'role', 'is_active')
    def _check_unique_chair(self):
        for rec in self:
            if rec.role == 'chair' and rec.is_active:
                count = self.search_count([
                    ('workplace_id', '=', rec.workplace_id.id),
                    ('role', '=', 'chair'),
                    ('is_active', '=', True),
                    ('id', '!=', rec.id),
                ])
                if count > 0:
                    raise ValidationError(
                        'Bir işyerinde yalnızca bir aktif Kurul Başkanı olabilir.'
                    )
