# -*- coding: utf-8 -*-
from odoo import models, fields, api


class IsgOsgbExpert(models.Model):
    _name = 'isg.osgb.expert'
    _description = 'OSGB İSG Uzmanı'
    _order = 'osgb_id, expert_class, name'

    name = fields.Char(string='Adı Soyadı', required=True)
    osgb_id = fields.Many2one(
        'isg.osgb', string='OSGB', required=True, ondelete='cascade',
    )
    company_id = fields.Many2one(
        related='osgb_id.company_id', string='Şirket', store=True, readonly=True,
    )

    # --- Sınıflandırma (6331 s.K. md.6) ---
    expert_class = fields.Selection([
        ('A', 'Sınıf A (500+ çalışan)'),
        ('B', 'Sınıf B (250-500 çalışan)'),
        ('C', 'Sınıf C (50-250 çalışan)'),
    ],
        string='Uzman Sınıfı', required=True,
    )

    # --- Kayıt ---
    registration_date = fields.Date(string='İstihdam Tarihi')
    active = fields.Boolean(default=True)

    notes = fields.Text(string='Notlar')

    _sql_constraints = [
        ('name_osgb_unique', 'unique(name, osgb_id)', 'Uzman adı OSGB içinde benzersiz olmalıdır.'),
    ]

    def name_get(self):
        result = []
        for rec in self:
            class_label = dict(rec._fields['expert_class'].selection).get(rec.expert_class, '')
            name = f'{rec.name} ({class_label})'
            result.append((rec.id, name))
        return result
