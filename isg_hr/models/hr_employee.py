# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # --- İSG İşyeri Ataması ---
    isg_workplace_id = fields.Many2one(
        'isg.workplace',
        string='İSG İşyeri',
        help='Çalışanın bağlı olduğu SGK bildirimi yapılmış İSG işyeri.',
    )
    isg_site_id = fields.Many2one(
        'isg.site',
        string='Fiziksel Site / Lokasyon',
        domain="[('workplace_id', '=', isg_workplace_id)]",
        help='Çalışanın fiilen çalıştığı fiziksel lokasyon.',
    )

    # --- SEG (Benzer Maruziyet Grubu) ---
    seg_id = fields.Many2one(
        'isg.seg',
        string='SEG (Benzer Maruziyet Grubu)',
        help='Aynı tür ve düzeyde kimyasal/fiziksel/biyolojik maruziyete '
             'sahip çalışan grubu. Maruziyet ölçümlerinde örnekleme için kullanılır.',
    )

    # --- İSG Rolü ---
    isg_role = fields.Selection(
        selection=[
            ('worker', 'İşçi'),
            ('supervisor', 'Vardiya/Bölüm Amiri'),
            ('expert', 'İSG Uzmanı'),
            ('physician', 'İşyeri Hekimi'),
            ('manager', 'İSG Yöneticisi'),
            ('other_health', 'Diğer Sağlık Personeli'),
        ],
        string='İSG Rolü',
        default='worker',
    )

    # --- Tehlike Sınıfı (işyerinden otomatik) ---
    danger_class = fields.Selection(
        related='isg_workplace_id.danger_class',
        string='Tehlike Sınıfı',
        store=True,
        readonly=True,
    )

    # --- Uzman/Hekim Süre Bilgisi (bilgi amaçlı) ---
    required_expert_minutes = fields.Integer(
        related='isg_workplace_id.required_expert_minutes',
        string='Gereken Uzman Süresi (dk/ay)',
        readonly=True,
    )
    required_physician_minutes = fields.Integer(
        related='isg_workplace_id.required_physician_minutes',
        string='Gereken Hekim Süresi (dk/ay)',
        readonly=True,
    )

    # --- Vardiya ---
    isg_shift = fields.Selection(
        selection=[
            ('day', 'Gündüz'),
            ('evening', 'Akşam'),
            ('night', 'Gece'),
            ('rotating', 'Dönüşümlü'),
        ],
        string='Vardiya',
    )

    # --- KKD Beden Ölçüleri ---
    ppe_shoe_size = fields.Char(string='Ayakkabı Numarası')
    ppe_clothing_size = fields.Selection(
        selection=[
            ('xs', 'XS'), ('s', 'S'), ('m', 'M'),
            ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL'), ('xxxl', 'XXXL'),
        ],
        string='Kıyafet Bedeni',
    )
    ppe_glove_size = fields.Selection(
        selection=[('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')],
        string='Eldiven Bedeni',
    )

    # --- İSG Notları ---
    isg_notes = fields.Text(string='İSG Notları')
