# -*- coding: utf-8 -*-
from odoo import api, fields, models

class IsgRiskControl(models.Model):
    _name = 'isg.risk.control'
    _description = 'Kontrol Önlemi'
    _order = 'assessment_line_id, hierarchy, sequence'

    assessment_line_id = fields.Many2one(
        'isg.risk.assessment.line',
        string='Değerlendirme Satırı',
        required=True,
        ondelete='cascade',
        readonly=True
    )

    sequence = fields.Integer(
        string='Sıra',
        default=10
    )

    name = fields.Char(
        string='Kontrol Önlemi',
        required=True
    )

    hierarchy = fields.Selection(
        [
            ('1_elimination', '1. Eleme (Tehlikeyi Ortadan Kaldırma)'),
            ('2_substitution', '2. Değiştirme'),
            ('3_engineering', '3. Teknik Kontrol'),
            ('4_administrative', '4. İdari Kontrol'),
            ('5_ppe', '5. Kişisel Koruyucu Donanım (KKD)'),
        ],
        string='Hiyerarşi Seviyesi',
        required=True,
        default='3_engineering'
    )

    description = fields.Text(
        string='Açıklama',
        help='Kontrol önleminin detaylı açıklaması'
    )

    responsible_id = fields.Many2one(
        'res.users',
        string='Sorumlu',
        readonly=False
    )

    planned_date = fields.Date(
        string='Planlanan Tarih',
        readonly=False
    )

    implementation_date = fields.Date(
        string='Uygulanma Tarihi',
        readonly=False
    )

    state = fields.Selection(
        [
            ('planned', 'Planlandı'),
            ('in_progress', 'Devam Ediyor'),
            ('implemented', 'Uygulandı'),
            ('verified', 'Doğrulandı'),
        ],
        string='Durum',
        default='planned',
        readonly=False
    )

    effectiveness = fields.Selection(
        [
            ('not_verified', 'Doğrulanmadı'),
            ('not_effective', 'Etkin Değil'),
            ('partially_effective', 'Kısmen Etkin'),
            ('effective', 'Etkin'),
        ],
        string='Etkinlik',
        default='not_verified'
    )

    risk_reduction_percentage = fields.Integer(
        string='Risk İndirimi (%)',
        help='Bu kontrol önleminin riski ne kadar azalttığı',
        default=50
    )

    notes = fields.Text(
        string='Notlar'
    )

    @api.onchange('hierarchy')
    def _onchange_hierarchy(self):
        """Hiyerarşi değiştiğinde varsayılan yüzdeyi güncelle"""
        hierarchy_defaults = {
            '1_elimination': 100,
            '2_substitution': 90,
            '3_engineering': 75,
            '4_administrative': 50,
            '5_ppe': 30,
        }
        if self.hierarchy:
            self.risk_reduction_percentage = hierarchy_defaults.get(self.hierarchy, 50)
