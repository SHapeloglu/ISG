# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgPpeStock(models.Model):
    _name = 'isg.ppe.stock'
    _description = 'KKD Stok Kaydı'
    _order = 'ppe_type_id, id'

    ppe_type_id = fields.Many2one(
        'isg.ppe.type', string='KKD Türü', required=True, ondelete='restrict',
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri', required=True,
    )
    size = fields.Char(string='Beden / Numara')
    brand = fields.Char(string='Marka / Model')
    quantity = fields.Integer(string='Mevcut Stok', default=0)
    min_quantity = fields.Integer(
        string='Minimum Stok',
        help='Bu seviyenin altına düşünce uyarı verilir',
    )
    is_low_stock = fields.Boolean(
        string='Stok Kritik mi?',
        compute='_compute_is_low_stock', store=True,
    )
    location = fields.Char(string='Depo / Raf Konumu')
    notes = fields.Text(string='Notlar')

    @api.depends('quantity', 'min_quantity')
    def _compute_is_low_stock(self):
        for rec in self:
            rec.is_low_stock = (
                rec.min_quantity > 0 and rec.quantity <= rec.min_quantity
            )
