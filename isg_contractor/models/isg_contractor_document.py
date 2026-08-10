# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class IsgContractorDocument(models.Model):
    _name = 'isg.contractor.document'
    _description = 'Alt İşveren Belge Matrisi'
    _inherit = ['mail.thread']
    _order = 'document_type, expiry_date'

    contractor_id = fields.Many2one(
        'isg.contractor', string='Alt İşveren',
        required=True, ondelete='cascade',
    )
    workplace_id = fields.Many2one(
        related='contractor_id.workplace_id',
        string='İşyeri', store=True, readonly=True,
    )
    document_type = fields.Selection(
        selection=[
            ('sgk_declaration', 'SGK İşyeri Tescil Belgesi'),
            ('sgk_debt', 'SGK Borcu Yoktur Yazısı'),
            ('tax_debt', 'Vergi Borcu Yoktur Yazısı'),
            ('trade_registry', 'Ticaret Sicil Gazetesi'),
            ('signature_circular', 'İmza Sirküleri'),
            ('isg_policy', 'İSG Politikası'),
            ('risk_assessment', 'Risk Değerlendirmesi'),
            ('emergency_plan', 'Acil Durum Planı'),
            ('isg_expert', 'İSG Uzmanı Görevlendirme'),
            ('physician', 'İşyeri Hekimi Görevlendirme'),
            ('ppe_list', 'KKD Listesi'),
            ('training_records', 'Eğitim Kayıtları'),
            ('insurance', 'İş Kazası Sigortası'),
            ('other', 'Diğer'),
        ],
        string='Belge Türü', required=True, tracking=True,
    )
    name = fields.Char(string='Belge Adı', required=True)
    is_mandatory = fields.Boolean(string='Zorunlu', default=True)
    state = fields.Selection(
        selection=[
            ('missing', 'Eksik'),
            ('submitted', 'Teslim Edildi'),
            ('approved', 'Onaylandı'),
            ('expired', 'Süresi Dolmuş'),
            ('rejected', 'Reddedildi'),
        ],
        string='Durum', default='missing', tracking=True,
    )
    submission_date = fields.Date(string='Teslim Tarihi')
    expiry_date = fields.Date(string='Geçerlilik Bitiş Tarihi', tracking=True)
    is_expired = fields.Boolean(
        string='Süresi Dolmuş', compute='_compute_is_expired', store=True,
    )
    isg_document_id = fields.Many2one(
        'isg.document', string='İSG Belgesi',
    )
    attachment_ids = fields.Many2many(
        'ir.attachment', string='Dosyalar',
    )
    notes = fields.Text(string='Notlar')

    @api.depends('expiry_date')
    def _compute_is_expired(self):
        today = fields.Date.today()
        for rec in self:
            if rec.expiry_date and rec.expiry_date < today:
                rec.is_expired = True
                if rec.state == 'approved':
                    rec.state = 'expired'
            else:
                rec.is_expired = False

    def action_submit(self):
        self.write({
            'state': 'submitted',
            'submission_date': fields.Date.today(),
        })

    def action_approve(self):
        for rec in self:
            if not rec.isg_document_id and not rec.attachment_ids:
                raise UserError(_(
                    'Onaylamadan önce "İSG Belgesi" veya "Dosyalar" '
                    'alanlarından en az biri doldurulmalıdır.'
                ))
        self.write({'state': 'approved'})

    def action_reject(self):
        self.write({'state': 'rejected'})
