# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgChemical(models.Model):
    _name = 'isg.chemical'
    _description = 'Kimyasal Madde'
    _order = 'name'

    name = fields.Char(
        string='Kimyasal Adı', required=True,
        help='Ticari ad veya IUPAC adı',
    )
    code = fields.Char(string='Kod')
    cas_number = fields.Char(
        string='CAS Numarası',
        help='Örn: 7732-18-5 (su)',
    )
    supplier_id = fields.Many2one(
        'res.partner', string='Tedarikçi',
        domain=[('supplier_rank', '>', 0)],
    )
    brand = fields.Char(string='Marka / Model')

    ghs_class = fields.Selection(
        [
            ('flammable', 'Alevlenir'),
            ('toxic', 'Toksik'),
            ('corrosive', 'Aşındırıcı'),
            ('oxidizing', 'Oksidatif'),
            ('explosive', 'Patlayıcı'),
            ('carcinogenic', 'Kanserojenik'),
            ('mutagenic', 'Mutajenik'),
            ('environmental', 'Çevre Tehdidi'),
            ('health_hazard', 'Sağlık Tehdidi'),
            ('unknown', 'Bilinmiyor'),
        ],
        string='GHS Sınıfı',
        help='Tehlike sınıflaması',
    )
    
    hazard_statement = fields.Text(
        string='Tehlike Tanıtımı (H)',
        help='H cümleleri (örn: H225 Ateşe çok kolay alışır)',
    )
    precautionary_statement = fields.Text(
        string='Önlemlendirme (P)',
        help='P cümleleri (örn: P210 Isıdan, sıcaklıktan koruyun)',
    )

    quantity = fields.Float(string='Mevcut Miktar', default=0)
    unit = fields.Char(string='Birim', default='L', help='Örn: L, ML, KG, G, Adet')
    min_quantity = fields.Float(
        string='Minimum Stok',
        help='Bu seviyenin altında uyarı verilir',
    )

    preparation_date = fields.Date(
        string='Hazırlık Tarihi',
        help='Depo giriş tarihi',
    )
    location = fields.Char(
        string='Depo / Raf Konumu',
        help='Örn: Depo A - Raf 3 - Bölüm B',
    )

    sds_document_id = fields.Many2one(
        'isg.document', string='GBF / SDS Belgesi',
        domain=[('document_type', '=', 'gbf')],
    )
    notes = fields.Text(string='Notlar')

    company_id = fields.Many2one(
        'res.company', string='Şirket',
        default=lambda self: self.env.company,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri',
    )
    site_id = fields.Many2one(
        'isg.site', string='Lokasyon',
    )

    active = fields.Boolean(default=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('code'):
                vals['code'] = self.env['ir.sequence'].next_by_code(
                    'isg.chemical'
                ) or 'NEW'
        return super().create(vals_list)
