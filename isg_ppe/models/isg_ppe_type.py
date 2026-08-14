# -*- coding: utf-8 -*-
from odoo import fields, models


class IsgPpeType(models.Model):
    _name = 'isg.ppe.type'
    _description = 'KKD Türü'
    _order = 'name'

    name = fields.Char(string='KKD Adı', required=True)
    code = fields.Char(string='Kod')
    category = fields.Selection(
        [
            ('head', 'Baş Koruma (Baret)'),
            ('eye', 'Göz / Yüz Koruma'),
            ('hearing', 'İşitme Koruma'),
            ('respiratory', 'Solunum Koruma'),
            ('hand', 'El Koruma (Eldiven)'),
            ('foot', 'Ayak Koruma (Bot/Ayakkabı)'),
            ('body', 'Vücut Koruma (Tulum/Yelek)'),
            ('fall', 'Düşme Koruma (Emniyet Kemeri)'),
            ('other', 'Diğer'),
        ],
        string='Kategori', required=True,
    )
    requires_size = fields.Boolean(
        string='Beden Ölçüsü Gerekli mi?',
        help='Eldiven, bot, tulum gibi beden gerektiren KKD türleri için işaretleyin',
    )
    size_type = fields.Selection(
        [
            ('clothing', 'Kıyafet Bedeni'),
            ('shoe', 'Ayakkabı Numarası'),
            ('glove', 'Eldiven Bedeni'),
        ],
        string='Beden Türü',

    )
    lifespan_months = fields.Integer(
        string='Kullanım Ömrü (Ay)',
        help='0 = süresiz',
    )
    standard = fields.Char(
        string='CE / Standart',
        help='Örn: EN 397, EN 388, EN ISO 20345',
    )
    description = fields.Text(string='Açıklama')
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        'res.company', string='Şirket',
        default=lambda self: self.env.company,
    )
