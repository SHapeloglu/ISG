# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import datetime, timedelta

class IsgPtw(models.Model):
    _name = 'isg.ptw'
    _description = 'İş İzni (Permit to Work)'
    _order = 'issue_date desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Temel bilgiler
    name = fields.Char(
        string='İzin Numarası',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('isg.ptw'),
    )
    
    ptw_type_id = fields.Many2one(
        'isg.ptw.type',
        string='İzin Türü',
        required=True,
        ondelete='restrict',
    )
    
    # Tarihler
    issue_date = fields.Datetime(
        string='İzin Tarihi',
        required=True,
        default=fields.Datetime.now,
    )
    
    validity_hours = fields.Integer(
        string='Geçerlilik (Saat)',
        required=True,
        related='ptw_type_id.default_validity_hours',
    )
    
    expiry_datetime = fields.Datetime(
        string='Son Geçerlilik Zamanı',
        compute='_compute_expiry_datetime',
        store=True,
    )
    
    # Talep eden ve onaylayan
    requester_id = fields.Many2one(
        'res.users',
        string='Talep Eden',
        required=True,
        default=lambda self: self.env.user,
    )
    
    requester_employee_id = fields.Many2one(
        'hr.employee',
        string='Talep Eden Çalışan',
    )
    
    work_location = fields.Char(
        string='Çalışma Yeri',
        help='Hangi yerde çalışılacak?',
    )
    
    work_description = fields.Text(
        string='Yapılacak İşin Açıklaması',
        required=True,
    )
    
    # Durum
    state = fields.Selection(
        [
            ('draft', 'Taslak'),
            ('submitted', 'Gönderildi - Bekleyen'),
            ('approved', 'Onaylandı'),
            ('rejected', 'Reddedildi'),
            ('active', 'Aktif - Çalışma Yapılıyor'),
            ('completed', 'Tamamlandı'),
            ('cancelled', 'İptal Edildi'),
            ('expired', 'Süresi Doldu'),
        ],
        string='Durum',
        default='draft',
        tracking=True,
    )
    
    # Onay zinciri
    approval_ids = fields.One2many(
        'isg.ptw.approval',
        'ptw_id',
        string='Onay Adımları',
    )
    
    # Ön koşul kontroller
    precondition_check_ids = fields.One2many(
        'isg.ptw.precondition.check',
        'ptw_id',
        string='Ön Koşul Kontroller',
    )
    
    # LOTO
    loto_ids = fields.One2many(
        'isg.loto',
        'ptw_id',
        string='LOTO Kayıtları',
    )
    
    # Kurumsal
    company_id = fields.Many2one(
        'res.company',
        string='Şirket',
        default=lambda self: self.env.company,
    )
    
    workplace_id = fields.Many2one(
        'isg.workplace',
        string='İSG İşyeri',
    )
    
    site_id = fields.Many2one(
        'isg.site',
        string='Lokasyon',
    )
    
    # Notlar ve belgeler
    notes = fields.Text(string='Notlar')
    document_id = fields.Many2one(
        'isg.document',
        string='İmzalı İzin Belgesi',
    )
    
    @api.depends('issue_date', 'validity_hours')
    def _compute_expiry_datetime(self):
        for record in self:
            if record.issue_date and record.validity_hours:
                record.expiry_datetime = record.issue_date + timedelta(
                    hours=record.validity_hours
                )
            else:
                record.expiry_datetime = None
    
    def action_submit(self):
        """İzni gönder (ilk onay adımına)"""
        for record in self:
            record.write({'state': 'submitted'})
            # İlk onaylayana bildirim gönder
            record.message_post(
                body="İş izni onay için gönderildi",
                message_type='notification',
            )
    
    def action_approve(self):
        """İzni onayla (bu adımdaki onaylayana ait)"""
        for record in self:
            record.write({'state': 'approved'})
            record.message_post(
                body="İş izni onaylandı",
                message_type='notification',
            )
    
    def action_reject(self):
        """İzni reddet"""
        for record in self:
            record.write({'state': 'rejected'})
            record.message_post(
                body="İş izni reddedildi",
                message_type='notification',
            )
    
    def action_activate(self):
        """Çalışmaya başla"""
        for record in self:
            record.write({'state': 'active'})
    
    def action_complete(self):
        """Çalışmayı tamamla"""
        for record in self:
            record.write({'state': 'completed'})
            record.message_post(
                body="İş izni tamamlandı",
                message_type='notification',
            )
