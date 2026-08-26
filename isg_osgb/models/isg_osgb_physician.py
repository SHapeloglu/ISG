# -*- coding: utf-8 -*-
from odoo import models, fields, api


class IsgOsgbPhysician(models.Model):
    _name = 'isg.osgb.physician'
    _description = 'OSGB İşyeri Hekimi'
    _order = 'osgb_id, name'

    name = fields.Char(string='Adı Soyadı', required=True)
    osgb_id = fields.Many2one(
        'isg.osgb', string='OSGB', required=True, ondelete='cascade',
    )
    company_id = fields.Many2one(
        related='osgb_id.company_id', string='Şirket', store=True, readonly=True,
    )

    # --- Kimlik ---
    medical_license_no = fields.Char(string='Tıp Lisans No')

    # --- Kayıt ---
    registration_date = fields.Date(string='İstihdam Tarihi')
    active = fields.Boolean(default=True)

    notes = fields.Text(string='Notlar')

    _sql_constraints = [
        ('name_osgb_unique', 'unique(name, osgb_id)', 'Hekim adı OSGB içinde benzersiz olmalıdır.'),
    ]
