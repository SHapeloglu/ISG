# -*- coding: utf-8 -*-
from odoo import models, fields, api


class IsgWorkplaceDangerClassHistory(models.Model):
    _name = 'isg.workplace.danger_class.history'
    _description = 'İşyeri Tehlike Sınıfı Değişim Geçmişi'
    _order = 'change_date desc'

    workplace_id = fields.Many2one(
        'isg.workplace',
        string='İşyeri',
        required=True,
        ondelete='cascade',
        readonly=True,
    )
    danger_class_old = fields.Selection([
        ('low', 'Az Tehlikeli'),
        ('medium', 'Tehlikeli'),
        ('high', 'Çok Tehlikeli'),
    ],
        string='Eski Tehlike Sınıfı',
        readonly=True,
    )
    danger_class_new = fields.Selection([
        ('low', 'Az Tehlikeli'),
        ('medium', 'Tehlikeli'),
        ('high', 'Çok Tehlikeli'),
    ],
        string='Yeni Tehlike Sınıfı',
        readonly=True,
        required=True,
    )
    change_date = fields.Date(
        string='Değişim Tarihi',
        readonly=True,
        default=fields.Date.context_today,
    )
    reason = fields.Text(
        string='Değişim Nedeni',
        readonly=True,
    )
    modified_by = fields.Many2one(
        'res.users',
        string='Değişiklik Yapan',
        readonly=True,
        default=lambda self: self.env.user,
    )
