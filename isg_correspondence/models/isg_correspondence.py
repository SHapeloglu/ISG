# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class IsgCorrespondence(models.Model):
    _name = 'isg.correspondence'
    _description = 'İSG Yazışma Kaydı'
    _inherit = ['mail.thread']
    _order = 'correspondence_date desc'

    name = fields.Char(
        string='Yazışma No', required=True, copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('isg.correspondence'),
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İşyeri',
        required=True, ondelete='cascade', tracking=True,
    )
    direction = fields.Selection(
        selection=[
            ('incoming', 'Gelen'),
            ('outgoing', 'Giden'),
        ],
        string='Yön', required=True, default='incoming', tracking=True,
    )
    correspondence_date = fields.Date(
        string='Yazışma Tarihi', required=True,
        default=fields.Date.today, tracking=True,
    )
    subject = fields.Char(string='Konu', required=True)
    reference_no = fields.Char(string='Referans No / Evrak No')
    institution = fields.Char(
        string='Kurum / Kişi', required=True,
    )
    category = fields.Selection(
        selection=[
            ('inspection', 'Denetim / Müfettiş Yazısı'),
            ('sgk', 'SGK Yazışması'),
            ('csgb', 'ÇSGB Yazışması'),
            ('municipality', 'Belediye / İdare'),
            ('court', 'Mahkeme / Hukuki'),
            ('internal', 'İç Yazışma'),
            ('other', 'Diğer'),
        ],
        string='Kategori', required=True, default='other', tracking=True,
    )
    state = fields.Selection(
        selection=[
            ('open', 'Açık'),
            ('replied', 'Cevaplandı'),
            ('closed', 'Kapatıldı'),
            ('overdue', 'Süresi Geçmiş'),
        ],
        string='Durum', default='open', tracking=True,
    )
    requires_reply = fields.Boolean(
        string='Cevap Gerekiyor', default=False, tracking=True,
    )
    reply_deadline = fields.Date(
        string='Cevap Termin Tarihi', tracking=True,
    )
    reply_date = fields.Date(
        string='Cevaplandığı Tarih', tracking=True,
    )
    is_overdue = fields.Boolean(
        string='Süresi Geçmiş', compute='_compute_is_overdue', store=True,
    )
    days_remaining = fields.Integer(
        string='Kalan Gün', compute='_compute_is_overdue', store=True,
    )
    isg_document_id = fields.Many2one(
        'isg.document', string='İlgili Belge',
    )
    attachment_ids = fields.Many2many(
        'ir.attachment', string='Ekler',
    )
    related_correspondence_id = fields.Many2one(
        'isg.correspondence', string='İlgili Yazışma',
    )
    notes = fields.Text(string='Notlar')

    @api.depends('reply_deadline', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.today()
        for rec in self:
            if rec.reply_deadline and rec.state == 'open':
                delta = (rec.reply_deadline - today).days
                rec.days_remaining = delta
                if delta < 0:
                    rec.is_overdue = True
                    rec.state = 'overdue'
                else:
                    rec.is_overdue = False
            else:
                rec.is_overdue = False
                rec.days_remaining = 0

    @api.onchange('requires_reply', 'correspondence_date')
    def _onchange_reply_deadline(self):
        if self.requires_reply and self.correspondence_date and not self.reply_deadline:
            self.reply_deadline = self.correspondence_date + relativedelta(days=30)

    def action_reply(self):
        self.write({
            'state': 'replied',
            'reply_date': fields.Date.today(),
        })

    def action_close(self):
        self.write({'state': 'closed'})

    def action_reopen(self):
        self.write({'state': 'open', 'is_overdue': False})
