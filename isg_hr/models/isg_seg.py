# -*- coding: utf-8 -*-
from odoo import models, fields


class IsgSeg(models.Model):
    _name = 'isg.seg'
    _description = 'Benzer Maruziyet Grubu (SEG)'
    _order = 'name'

    name = fields.Char(string='SEG Adı', required=True)
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri', required=True,
    )
    description = fields.Text(string='Açıklama')
    hazard_type = fields.Selection(
        selection=[
            ('chemical', 'Kimyasal'),
            ('physical', 'Fiziksel (Gürültü/Titreşim/Isı)'),
            ('biological', 'Biyolojik'),
            ('ergonomic', 'Ergonomik'),
            ('dust', 'Toz'),
            ('mixed', 'Karma'),
        ],
        string='Maruziyet Türü',
    )
    employee_ids = fields.One2many(
        'hr.employee', 'seg_id', string='Çalışanlar',
    )
    employee_count = fields.Integer(
        string='Çalışan Sayısı', compute='_compute_employee_count', store=True,
    )

    def _compute_employee_count(self):
        for seg in self:
            seg.employee_count = len(seg.employee_ids)
