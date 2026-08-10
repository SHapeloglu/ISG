# -*- coding: utf-8 -*-
from odoo import models, fields, api


class IsgCapaAction(models.Model):
    _name = 'isg.capa.action'
    _description = 'DÖF Aksiyonu'
    _inherit = ['mail.thread']
    _order = 'sequence, id'

    capa_id = fields.Many2one(
        'isg.capa', string='DÖF', required=True, ondelete='cascade',
    )
    sequence = fields.Integer(string='Sıra', default=10)
    name = fields.Char(string='Aksiyon', required=True)
    description = fields.Text(string='Açıklama')
    action_type = fields.Selection(
        selection=[
            ('corrective', 'Düzeltici'),
            ('preventive', 'Önleyici'),
            ('immediate', 'Anlık'),
        ],
        string='Tür', required=True, default='corrective',
    )
    responsible_id = fields.Many2one(
        'hr.employee', string='Sorumlu', tracking=True,
    )
    due_date = fields.Date(string='Termin', tracking=True)
    completion_date = fields.Date(string='Tamamlanma Tarihi')
    state = fields.Selection(
        selection=[
            ('open', 'Açık'),
            ('done', 'Tamamlandı'),
            ('cancelled', 'İptal'),
        ],
        string='Durum', default='open', tracking=True,
    )
    is_overdue = fields.Boolean(
        string='Gecikmiş', compute='_compute_is_overdue', store=True,
    )
    effectiveness = fields.Text(string='Etkinlik Notu')

    @api.depends('due_date', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.today()
        for rec in self:
            if rec.due_date and rec.state == 'open':
                rec.is_overdue = rec.due_date < today
            else:
                rec.is_overdue = False

    def action_done(self):
        self.write({
            'state': 'done',
            'completion_date': fields.Date.today(),
        })

    def action_cancel(self):
        self.write({'state': 'cancelled'})
