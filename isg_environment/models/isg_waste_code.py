# -*- coding: utf-8 -*-
from odoo import fields, models


class WasteCode(models.Model):
    _name = 'isg.waste.code'
    _description = 'Atık Kodu Kataloğu'
    _inherit = ['isg.uuid.mixin']
    _order = 'code asc'

    code = fields.Char('Atık Kodu', required=True)
    name = fields.Char('Atık Açıklaması', required=True)
    waste_category = fields.Selection([
        ('general', 'Genel Atık'),
        ('hazardous', 'Tehlikeli Atık'),
        ('biomedical', 'Biyomedikal Atık'),
        ('electronic', 'Elektronik Atık'),
        ('construction', 'İnşaat Atığı'),
        ('agricultural', 'Tarımsal Atık'),
        ('other', 'Diğer'),
    ], string='Atık Kategorisi', required=True)
    
    is_hazardous = fields.Boolean('Tehlikeli Atık mı?', default=False)
    hazard_characteristics = fields.Text('Tehlike Özellikleri')
    
    storage_requirements = fields.Text('Depolama Gereksinimleri', 
                                       help='Hangi koşullarda depolanmalı?')
    disposal_method = fields.Selection([
        ('landfill', 'Depo (Landfill)'),
        ('incineration', 'Yakma (Incineration)'),
        ('recycling', 'Geri Dönüşüm'),
        ('composting', 'Kompostlama'),
        ('hazmat', 'Tehlikeli Atık Bertarafı'),
        ('other', 'Diğer'),
    ], string='Bertaraf Yöntemi', required=True)
    
    is_active = fields.Boolean('Aktif', default=True)
    notes = fields.Text('Notlar')
    
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Atık kodu benzersiz olmalıdır'),
    ]

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.code}] {record.name}"
            result.append((record.id, name))
        return result
