# -*- coding: utf-8 -*-
from odoo import fields, models

class IsgPtwType(models.Model):
    _name = 'isg.ptw.type'
    _description = 'İş İzni Türü'
    _order = 'name'

    name = fields.Char(
        string='İzin Türü',
        required=True,
        help='Örn: Sıcak İş, Kapalı Alan, Elektrik',
    )
    
    code = fields.Char(string='Kod')
    
    description = fields.Text(string='Açıklama')
    
    # Onay zinciri
    approval_sequence = fields.Char(
        string='Onay Sırası',
        help='Hangi roller bu türü onaylamak zorunda (virgülle ayrılmış)',
    )
    
    # Varsayılan geçerlilik süresi (saat)
    default_validity_hours = fields.Integer(
        string='Varsayılan Geçerlilik (Saat)',
        default=8,
        help='İzin kaç saat boyunca geçerli olur',
    )
    
    # Ön koşullar
    precondition_ids = fields.One2many(
        'isg.ptw.precondition',
        'ptw_type_id',
        string='Ön Koşul Kontrol Listeleri',
    )
    
    # Tehlike seviyesi
    hazard_level = fields.Selection(
        [
            ('low', 'Düşük Tehlike'),
            ('medium', 'Orta Tehlike'),
            ('high', 'Yüksek Tehlike'),
            ('critical', 'Kritik Tehlike'),
        ],
        string='Tehlike Seviyesi',
        default='medium',
    )
    
    active = fields.Boolean(default=True)
    
    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'İzin kodu benzersiz olmalı'),
    ]
