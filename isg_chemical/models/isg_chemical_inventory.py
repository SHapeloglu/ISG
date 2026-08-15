# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgChemicalInventory(models.Model):
    _name = 'isg.chemical.inventory'
    _description = 'Kimyasal Stok Takibi'
    _order = 'chemical_id, date desc'

    chemical_id = fields.Many2one(
        'isg.chemical', string='Kimyasal', required=True,
        ondelete='cascade',
    )
    date = fields.Date(
        string='Tarih', required=True,
        default=fields.Date.context_today,
    )
    transaction_type = fields.Selection(
        [
            ('in', 'Giriş'),
            ('out', 'Çıkış'),
            ('return', 'İade'),
            ('adjustment', 'Dengeleme'),
        ],
        string='İşlem Türü', required=True,
    )
    quantity = fields.Float(string='Miktar', required=True)
    unit = fields.Char(
        related='chemical_id.unit', readonly=True,
        string='Birim',
    )
    reference = fields.Char(
        string='Referans',
        help='Sevkiyat no, sipariş no vb.',
    )
    notes = fields.Text(string='Notlar')
    
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri',
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            chemical = self.env['isg.chemical'].browse(
                vals.get('chemical_id')
            )
            if vals.get('transaction_type') == 'in':
                chemical.quantity += vals.get('quantity', 0)
            elif vals.get('transaction_type') in ('out', 'return'):
                chemical.quantity -= vals.get('quantity', 0)
            elif vals.get('transaction_type') == 'adjustment':
                chemical.quantity = vals.get('quantity', 0)
        return super().create(vals_list)
