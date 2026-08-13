# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgEmergencyDrill(models.Model):
    _name = 'isg.emergency.drill'
    _description = 'Acil Durum Tatbikatı'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'drill_date desc, id desc'

    name = fields.Char(
        string='Tatbikat No', required=True, copy=False,
        readonly=True, default=lambda self: 'Yeni',
    )
    plan_id = fields.Many2one(
        'isg.emergency.plan', string='Acil Durum Planı',
        required=True, ondelete='cascade', tracking=True,
    )
    company_id = fields.Many2one(
        related='plan_id.company_id', store=True,
    )
    workplace_id = fields.Many2one(
        related='plan_id.workplace_id', store=True,
    )
    drill_type = fields.Selection(
        [
            ('evacuation', 'Tahliye'),
            ('fire', 'Yangın'),
            ('earthquake', 'Deprem'),
            ('chemical', 'Kimyasal Sızıntı'),
            ('medical', 'Tıbbi Acil'),
            ('full', 'Tam Tatbikat'),
            ('other', 'Diğer'),
        ],
        string='Tatbikat Türü', required=True, default='evacuation', tracking=True,
    )
    drill_date = fields.Date(
        string='Tatbikat Tarihi', required=True,
        default=fields.Date.context_today, tracking=True,
    )
    drill_time = fields.Float(
        string='Tatbikat Saati', digits=(2, 2),
        help='Saat:Dakika formatında (örn. 10.30)',
    )
    duration_minutes = fields.Integer(string='Süre (Dakika)')
    participant_count = fields.Integer(string='Katılımcı Sayısı')
    responsible_id = fields.Many2one(
        'hr.employee', string='Tatbikat Sorumlusu', tracking=True,
    )
    observer_ids = fields.Many2many(
        'hr.employee', 'isg_drill_observer_rel',
        'drill_id', 'employee_id', string='Gözlemciler',
    )
    result = fields.Selection(
        [
            ('successful', 'Başarılı'),
            ('partial', 'Kısmen Başarılı'),
            ('failed', 'Başarısız'),
        ],
        string='Tatbikat Sonucu', tracking=True,
    )
    evacuation_time_minutes = fields.Integer(
        string='Tahliye Süresi (Dakika)',
        help='Tüm personelin tahliye edilme süresi',
    )
    findings = fields.Text(string='Tatbikat Bulguları')
    improvements = fields.Text(string='İyileştirme Önerileri')
    document_id = fields.Many2one('isg.document', string='Tatbikat Raporu')
    next_drill_date = fields.Date(string='Sonraki Tatbikat Tarihi')
    notes = fields.Text(string='Notlar')

    state = fields.Selection(
        [
            ('planned', 'Planlandı'),
            ('done', 'Gerçekleşti'),
            ('cancelled', 'İptal'),
        ],
        string='Durum', default='planned', tracking=True, copy=False,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Yeni') == 'Yeni':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'isg.emergency.drill'
                ) or 'Yeni'
        return super().create(vals_list)

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_reset_planned(self):
        self.write({'state': 'planned'})
