# -*- coding: utf-8 -*-
from odoo import fields, models

class IsgPtwPrecondition(models.Model):
    _name = 'isg.ptw.precondition'
    _description = 'Ön Koşul Kontrol Maddesi'
    _order = 'sequence, id'

    sequence = fields.Integer(string='Sıra', default=10)
    
    ptw_type_id = fields.Many2one(
        'isg.ptw.type',
        string='İzin Türü',
        required=True,
        ondelete='cascade',
    )
    
    description = fields.Char(
        string='Kontrol Maddesi',
        required=True,
        help='Örn: "Yangın söndürücü hazır mı?"',
    )
    
    help_text = fields.Text(
        string='Rehber Metin',
        help='Bu madde hakkında ek bilgi',
    )
    
    is_mandatory = fields.Boolean(
        string='Zorunlu mu?',
        default=True,
        help='Bu kontrol yapılmak zorunda mı?',
    )

class IsgPtwPreconditionCheck(models.Model):
    _name = 'isg.ptw.precondition.check'
    _description = 'Ön Koşul Kontrol Sonucu'
    _order = 'precondition_id, id'

    ptw_id = fields.Many2one(
        'isg.ptw',
        string='İş İzni',
        required=True,
        ondelete='cascade',
    )
    
    precondition_id = fields.Many2one(
        'isg.ptw.precondition',
        string='Kontrol Maddesi',
        required=True,
        ondelete='cascade',
    )
    
    is_checked = fields.Boolean(
        string='Kontrol Edildi mi?',
        default=False,
    )
    
    result = fields.Selection(
        [
            ('ok', 'Uygun'),
            ('not_ok', 'Uygun Değil'),
            ('na', 'Uygulanabilir Değil'),
        ],
        string='Sonuç',
    )
    
    notes = fields.Text(string='Notlar')
    
    checked_by = fields.Many2one(
        'res.users',
        string='Kontrol Eden',
    )
    
    checked_date = fields.Datetime(
        string='Kontrol Tarihi',
    )
