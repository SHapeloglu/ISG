# -*- coding: utf-8 -*-
from odoo import api, fields, models

class IsgChemicalIncompatibility(models.Model):
    _name = 'isg.chemical.incompatibility'
    _description = 'Kimyasal Uyumsuzluk Matrisi'
    _order = 'chemical_id_a, chemical_id_b'

    # İki kimyasal arasındaki uyumsuzluk
    chemical_id_a = fields.Many2one(
        'isg.chemical', string='Kimyasal A', required=True,
        ondelete='cascade', tracking=True,
    )
    chemical_id_b = fields.Many2one(
        'isg.chemical', string='Kimyasal B', required=True,
        ondelete='cascade', tracking=True,
    )

    # Uyumsuzluk derecesi
    severity = fields.Selection(
        [
            ('critical', 'Kritik (Aynı ortamda YASAK)'),
            ('high', 'Yüksek (Ayrı bölmede, aralarında bariyerler)'),
            ('medium', 'Orta (Ayrı raf / Arası açık)'),
        ],
        string='Uyumsuzluk Derecesi', required=True, default='high',
    )

    reason = fields.Text(
        string='Neden',
        help='Neden uyumsuzdur? (Örn: "Asit + Baz reaksiyonu", "Oksidatif + Yanıcı")',
    )

    # Yapılması gerekenler
    mitigation_measures = fields.Text(
        string='Hafifletme Önlemleri',
        help='Zorunlu tutulursa nasıl saklanalı?',
    )

    company_id = fields.Many2one(
        'res.company', string='Şirket',
        default=lambda self: self.env.company,
    )

    # Constraint: A != B ve çift kayıt olmasın
    _sql_constraints = [
        ('different_chemicals', 'check(chemical_id_a != chemical_id_b)',
         'Aynı kimyasal kendi kendisiyle uyumsuzdur olamaz.'),
    ]

    @api.model
    def create(self, vals):
        # Ters kaydı otomatik kontrol et (A-B ve B-A çift sayılmasın)
        a_id = vals.get('chemical_id_a')
        b_id = vals.get('chemical_id_b')
        
        existing = self.search([
            ('chemical_id_a', '=', b_id),
            ('chemical_id_b', '=', a_id),
        ])
        
        if existing:
            raise ValidationError(
                'Bu uyumsuzluk zaten kaydedilmiş (ters yönde): %s ↔ %s' % (
                    existing.chemical_id_a.name,
                    existing.chemical_id_b.name,
                )
            )
        
        return super().create(vals)
