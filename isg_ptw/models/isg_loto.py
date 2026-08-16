# -*- coding: utf-8 -*-
from odoo import api, fields, models

class IsgLoto(models.Model):
    _name = 'isg.loto'
    _description = 'LOTO - Kilit ve Etiket Prosedürü'
    _order = 'lockout_date desc'

    ptw_id = fields.Many2one(
        'isg.ptw',
        string='İş İzni',
        required=True,
        ondelete='cascade',
    )
    
    # Enerji kaynağı
    energy_source = fields.Char(
        string='Enerji Kaynağı',
        required=True,
        help='Örn: Elektrik Panosu X, Vana Y, Kompresör Z',
    )
    
    energy_type = fields.Selection(
        [
            ('electrical', 'Elektrik'),
            ('pneumatic', 'Pnömatik (Hava)'),
            ('hydraulic', 'Hidrolik (Yağ Basıncı)'),
            ('mechanical', 'Mekanik'),
            ('thermal', 'Termal (Isı)'),
            ('chemical', 'Kimyasal'),
            ('radiation', 'Radyasyon'),
            ('other', 'Diğer'),
        ],
        string='Enerji Türü',
        required=True,
    )
    
    # Kilit bilgileri
    lockout_date = fields.Datetime(
        string='Kilit Tarihi',
        required=True,
        default=fields.Datetime.now,
    )
    
    lock_number = fields.Char(
        string='Kilit Numarası',
        help='Fiziksel kilit etiketi numarası',
    )
    
    locked_by = fields.Many2one(
        'res.users',
        string='Kilitleyen',
        required=True,
        default=lambda self: self.env.user,
    )
    
    # Ortak kilit (birden fazla kişi aynı noktayı kilitleyebilir)
    is_group_lockout = fields.Boolean(
        string='Ortak Kilit mi?',
        default=False,
        help='Bu noktayı birden fazla kişi mi kilitledi?',
    )
    
    additional_lockers = fields.Many2many(
        'res.users',
        'isg_loto_user_rel',
        'loto_id',
        'user_id',
        string='Diğer Kilitleyen Kişiler',
    )
    
    # Kilit açma
    unlock_date = fields.Datetime(
        string='Kilit Açma Tarihi',
    )
    
    unlocked_by = fields.Many2one(
        'res.users',
        string='Kilit Açan',
    )
    
    # Durum
    state = fields.Selection(
        [
            ('locked', 'Kilitli'),
            ('unlocked', 'Kilit Açıldı'),
            ('failed', 'Kilit Başarısız'),
        ],
        string='Durum',
        default='locked',
    )
    
    # Notlar
    notes = fields.Text(string='Notlar')
    
    def action_unlock(self):
        """Kilidi aç"""
        for record in self:
            record.write({
                'state': 'unlocked',
                'unlock_date': fields.Datetime.now(),
                'unlocked_by': self.env.user.id,
            })
            # PTW kontrol: tüm LOTO'lar açıldı mı?
            ptw = record.ptw_id
            remaining_locks = ptw.loto_ids.filtered(
                lambda l: l.state == 'locked'
            )
            if not remaining_locks:
                # Tüm kilitler açıldı, enerji verilebilir
                ptw.message_post(
                    body="Tüm LOTO kilitler açıldı. Enerji geri verilebilir.",
                    message_type='notification',
                )
