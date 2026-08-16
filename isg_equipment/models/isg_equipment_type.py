# -*- coding: utf-8 -*-
from odoo import fields, models

class IsgEquipmentType(models.Model):
    _name = 'isg.equipment.type'
    _description = 'Ekipman Türü (EK-II)'
    _order = 'name'

    name = fields.Char(
        string='Ekipman Türü',
        required=True,
        help='Örn: Kompresör, Vinç, Asansör',
    )
    code = fields.Char(string='Kod')
    description = fields.Text(string='Açıklama')
    
    # EK-II kaynağı
    ekii_category = fields.Char(
        string='EK-II Kategorisi',
        help='Örn: 1, 2, 3 — İş Ekipmanları Yönetmeliği EK-II',
    )
    
    # Periyodik kontrol periyodu (ay)
    inspection_period_months = fields.Integer(
        string='Kontrol Periyodu (Ay)',
        default=12,
        help='Periyodik kontrol araç (örn: 12 = 1 yıl)',
    )
    
    # Yetkili kuruluş türü
    authorized_body_type = fields.Selection(
        [
            ('a', 'A Tipi Muayene Kuruluşu'),
            ('b', 'B Tipi Muayene Kuruluşu'),
            ('both', 'Her İkisi'),
        ],
        string='Yetkili Muayene Kuruluşu',
        default='both',
    )
    
    # Kontrol yöntemi
    inspection_method = fields.Char(
        string='Kontrol Yöntemi',
        help='Periyodik kontrol standarı (örn: TS EN 4413)',
    )
    
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Ekipman kodu benzersiz olmalı'),
    ]
