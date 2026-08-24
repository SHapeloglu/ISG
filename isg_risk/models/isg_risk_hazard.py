# -*- coding: utf-8 -*-
from odoo import api, fields, models

class IsgRiskHazard(models.Model):
    _name = 'isg.risk.hazard'
    _description = 'Tehlike Kataloğu'
    _order = 'category, name'
    _rec_name = 'name'

    name = fields.Char(
        string='Tehlike Adı',
        required=True,
        index=True
    )

    category = fields.Selection(
        [
            ('physical', 'Fiziksel'),
            ('chemical', 'Kimyasal'),
            ('biological', 'Biyolojik'),
            ('ergonomic', 'Ergonomik'),
            ('psychosocial', 'Psikososyal'),
            ('safety', 'Güvenlik'),
            ('electrical', 'Elektrik'),
            ('thermal', 'Isıl'),
            ('radiation', 'Radyasyon'),
            ('noise', 'Gürültü'),
            ('vibration', 'Titreşim'),
            ('other', 'Diğer'),
        ],
        string='Kategori',
        required=True,
        index=True
    )

    description = fields.Text(
        string='Açıklama',
        help='Tehlikenin detaylı açıklaması'
    )

    possible_consequences = fields.Text(
        string='Olası Sonuçlar',
        help='Bu tehlikenin neden olabileceği hasarlar'
    )

    affected_groups = fields.Many2many(
        'res.partner',
        'hazard_affected_groups_rel',
        'hazard_id',
        'partner_id',
        string='Etkilenen Gruplar',
        domain="[('is_company', '=', False)]",
        help='Bu tehlikiden etkilenebilecek çalışan grupları'
    )

    active = fields.Boolean(
        string='Aktif',
        default=True
    )

    _sql_constraints = [
        ('unique_hazard_name', 'unique(name)', 'Bu tehlike adı zaten tanımlanmış.'),
    ]
