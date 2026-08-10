# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class IsgBoardMeeting(models.Model):
    _name = 'isg.board.meeting'
    _description = 'İSG Kurulu Toplantısı'
    _inherit = ['mail.thread']
    _order = 'meeting_date desc'

    name = fields.Char(
        string='Toplantı No', required=True, copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('isg.board.meeting'),
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İşyeri',
        required=True, ondelete='cascade', tracking=True,
    )
    meeting_date = fields.Date(
        string='Toplantı Tarihi', required=True, tracking=True,
    )
    meeting_type = fields.Selection(
        selection=[
            ('ordinary', 'Olağan'),
            ('extraordinary', 'Olağanüstü'),
        ],
        string='Toplantı Türü', required=True,
        default='ordinary', tracking=True,
    )
    state = fields.Selection(
        selection=[
            ('planned', 'Planlandı'),
            ('held', 'Gerçekleşti'),
            ('cancelled', 'İptal Edildi'),
        ],
        string='Durum', default='planned', tracking=True,
    )
    quorum_met = fields.Boolean(
        string='Yeter Sayı Sağlandı', tracking=True,
    )
    attendee_ids = fields.Many2many(
        'isg.board.member',
        'isg_board_meeting_attendee_rel',
        'meeting_id', 'member_id',
        string='Katılanlar',
        domain="[('workplace_id', '=', workplace_id), ('is_active', '=', True)]",
    )
    attendee_count = fields.Integer(
        string='Katılımcı Sayısı', compute='_compute_attendee_count',
    )
    agenda = fields.Text(string='Gündem')
    minutes = fields.Html(string='Toplantı Tutanağı')
    decision_ids = fields.One2many(
        'isg.board.decision', 'meeting_id', string='Kararlar',
    )
    decision_count = fields.Integer(
        string='Karar Sayısı', compute='_compute_decision_count',
    )
    next_meeting_date = fields.Date(
        string='Sonraki Toplantı Tarihi', compute='_compute_next_meeting_date',
        store=True,
    )
    isg_document_id = fields.Many2one(
        'isg.document', string='Tutanak Belgesi',
    )

    @api.depends('attendee_ids')
    def _compute_attendee_count(self):
        for rec in self:
            rec.attendee_count = len(rec.attendee_ids)

    @api.depends('decision_ids')
    def _compute_decision_count(self):
        for rec in self:
            rec.decision_count = len(rec.decision_ids)

    @api.depends('meeting_date', 'workplace_id')
    def _compute_next_meeting_date(self):
        for rec in self:
            if rec.meeting_date and rec.workplace_id:
                danger = rec.workplace_id.danger_class
                if danger == 'very_dangerous':
                    rec.next_meeting_date = rec.meeting_date + relativedelta(days=15)
                else:
                    rec.next_meeting_date = rec.meeting_date + relativedelta(months=1)
            else:
                rec.next_meeting_date = False

    def action_held(self):
        self.write({'state': 'held'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})


class IsgBoardDecision(models.Model):
    _name = 'isg.board.decision'
    _description = 'İSG Kurulu Kararı'
    _inherit = ['mail.thread']
    _order = 'meeting_id desc, sequence'

    meeting_id = fields.Many2one(
        'isg.board.meeting', string='Toplantı',
        required=True, ondelete='cascade',
    )
    workplace_id = fields.Many2one(
        related='meeting_id.workplace_id',
        string='İşyeri', store=True, readonly=True,
    )
    sequence = fields.Integer(string='Sıra', default=10)
    name = fields.Char(string='Karar Özeti', required=True)
    description = fields.Text(string='Karar Detayı')
    responsible_id = fields.Many2one(
        'hr.employee', string='Sorumlu',
    )
    due_date = fields.Date(string='Termin Tarihi', tracking=True)
    state = fields.Selection(
        selection=[
            ('open', 'Açık'),
            ('done', 'Tamamlandı'),
            ('delayed', 'Gecikmiş'),
        ],
        string='Durum', default='open', tracking=True,
    )
    is_delayed = fields.Boolean(
        string='Gecikmiş', compute='_compute_is_delayed', store=True,
    )
    notes = fields.Text(string='Notlar')

    @api.depends('due_date', 'state')
    def _compute_is_delayed(self):
        today = fields.Date.today()
        for rec in self:
            if rec.due_date and rec.state == 'open' and rec.due_date < today:
                rec.is_delayed = True
                rec.state = 'delayed'
            else:
                rec.is_delayed = False

    def action_done(self):
        self.write({'state': 'done'})

    def action_reopen(self):
        self.write({'state': 'open', 'is_delayed': False})
