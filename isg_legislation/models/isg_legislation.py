# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgLegislation(models.Model):
    _name = 'isg.legislation'
    _description = 'Mevzuat (Kanun/Yönetmelik)'
    _order = 'effective_date desc, name'

    name = fields.Char(
        string='Adı', required=True,
        help='Örn: 6331 sayılı İSG Kanunu, Risk Değerlendirmesi Yönetmeliği',
    )
    regulation_type = fields.Selection(
        [
            ('law', 'Kanun'),
            ('regulation', 'Yönetmelik'),
            ('circular', 'Tebliğ'),
            ('directive', 'Yönerge'),
            ('guideline', 'Rehber'),
        ],
        string='Mevzuat Türü', required=True,
    )
    regulation_number = fields.Char(
        string='Kanun/Yönetmelik No',
        help='Örn: 6331, 2019/1147',
    )

    effective_date = fields.Date(
        string='Yürürlük Tarihi', required=True,
        help='Mevzuatın yürürlüğe girdiği tarih',
    )
    last_amendment_date = fields.Date(
        string='Son Değişiklik Tarihi',
        help='Mevzuatın son kez değiştirildiği tarih',
    )

    source_url = fields.Char(
        string='Kaynak URL',
        help='Resmi Gazete veya ÇSGB sayfası linki',
    )
    description = fields.Text(
        string='Açıklama',
    )

    # Yükümlülükler bu mevzuattan gelir
    obligation_ids = fields.One2many(
        'isg.obligation', 'legislation_id',
        string='Yükümlülükler',
        help='Bu mevzuattan türeyen yükümlülükler',
    )

    state = fields.Selection(
        [
            ('draft', 'Taslak'),
            ('active', 'Aktif'),
            ('amended', 'Değiştirildi'),
            ('repealed', 'Yürürlükten Kaldırıldı'),
        ],
        string='Durum', default='draft',
    )

    company_id = fields.Many2one(
        'res.company', string='Şirket',
        default=lambda self: self.env.company,
    )

    def action_activate(self):
        """Mevzuatı aktif et"""
        self.write({'state': 'active'})
