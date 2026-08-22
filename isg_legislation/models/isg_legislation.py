# -*- coding: utf-8 -*-
from odoo import models, fields
from datetime import datetime

class ISGLegislation(models.Model):
    _name = 'isg.legislation'
    _description = 'ISG Mevzuatı (Kanun, Yönetmelik, Tebliğ)'
    _order = 'name'

    name = fields.Char('Mevzuat Adı', required=True)
    legislation_type = fields.Selection([
        ('law', 'Kanun'),
        ('regulation', 'Yönetmelik'),
        ('communique', 'Tebliğ'),
        ('directive', 'Yönerge'),
        ('guide', 'Rehber'),
    ], string='Türü', required=True, default='regulation')
    
    number = fields.Char('Kanun/Yönetmelik No', required=True)
    effective_date = fields.Date('Yürürlük Tarihi', required=True)
    amendment_date = fields.Date('Son Değişiklik Tarihi')
    
    source_url = fields.Char('Resmi Kaynak URL')
    notes = fields.Text('Açıklamalar')
    
    # Bağlantılar
    obligation_ids = fields.One2many('isg.obligation', 'legislation_id', 'Yükümlülükler')
    
    _sql_constraints = [
        ('unique_number', 'unique(number)', 'Mevzuat No benzersiz olmalı'),
    ]
