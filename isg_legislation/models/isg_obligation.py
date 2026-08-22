# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgObligation(models.Model):
    _name = 'isg.obligation'
    _description = 'İSG Yükümlülüğü'
    _order = 'legislation_id, sequence, name'

    name = fields.Char(
        string='Yükümlülük Adı', required=True,
        help='Örn: Risk değerlendirmesi yapılmalı, Uzman görevlendirilmeli',
    )
    sequence = fields.Integer(
        string='Sıra', default=10,
    )

    legislation_id = fields.Many2one(
        'isg.legislation', string='Mevzuat',
        required=True, ondelete='cascade',
    )
    article_reference = fields.Char(
        string='Madde Referansı',
        help='Örn: Md. 10, Md. 4',
    )

    evidence_type = fields.Selection(
        [
            ('risk_assessment', 'Risk Değerlendirmesi Raporu'),
            ('training_record', 'Eğitim Kaydı'),
            ('expert_appointment', 'Uzman Atama Belgesi'),
            ('physician_appointment', 'Hekim Atama Belgesi'),
            ('emergency_plan', 'Acil Durum Planı'),
            ('audit_checklist', 'Denetim Kontrolü'),
            ('equipment_inspection', 'Ekipman İnceleme Raporu'),
            ('chemical_inventory', 'Kimyasal Envanter'),
            ('ptw_permit', 'İzinli Çalışma İzni'),
            ('incident_report', 'Kaza Raporu'),
            ('other', 'Diğer'),
        ],
        string='Kanıt Türü', required=True,
        help='Bu yükümlülük için ne tür kanıt gerekli?',
    )

    retention_days = fields.Integer(
        string='Saklama Süresi (gün)',
        help='Kanıtın kaç gün saklanması gerekli? Örn: 730 (2 yıl), 1825 (5 yıl)',
    )

    is_periodic = fields.Boolean(
        string='Periyodik mi?',
        help='Yükümlülük periyodik olarak tekrarlanmalı mı? (Örn: eğitim yıllık)',
    )
    periodic_days = fields.Integer(
        string='Periyot (gün)',
        help='Periyodik ise kaç günde bir yapılmalı?',
    )

    # Uygulanabilirlik kuralları
    applicability_ids = fields.One2many(
        'isg.obligation.applicability', 'obligation_id',
        string='Uygulanabilirlik Kuralları',
    )

    description = fields.Text(
        string='Açıklama',
    )

    state = fields.Selection(
        [
            ('active', 'Aktif'),
            ('inactive', 'Pasif'),
        ],
        string='Durum', default='active',
    )

    company_id = fields.Many2one(
        'res.company', string='Şirket',
        default=lambda self: self.env.company,
    )


class IsgObligationApplicability(models.Model):
    _name = 'isg.obligation.applicability'
    _description = 'Yükümlülük Uygulanabilirlik Kuralı'
    _order = 'obligation_id, sequence'

    name = fields.Char(
        string='Adı', required=True,
        help='Kural açıklaması',
    )

    obligation_id = fields.Many2one(
        'isg.obligation', string='Yükümlülük',
        required=True, ondelete='cascade',
    )
    sequence = fields.Integer(
        string='Sıra', default=10,
    )

    # Kural: İşyeri hangi profile girerse bu yükümlülük geçerli?
    danger_class = fields.Selection(
        [
            ('low', 'Az Tehlikeli'),
            ('medium', 'Tehlikeli'),
            ('high', 'Çok Tehlikeli'),
        ],
        string='Tehlike Sınıfı',
        help='Boş bırakılırsa tüm sınıflara uygulanır',
    )
    min_employee_count = fields.Integer(
        string='Minimum Çalışan Sayısı',
        help='Bu yükümlülük kaç çalışandan itibaren geçerli?',
    )
    is_public_sector = fields.Boolean(
        string='Kamu Sektörü',
        help='Sadece kamu işyerleri için mi?',
    )
    sector_codes = fields.Char(
        string='NACE Kodları',
        help='Virgülle ayrılmış NACE kodları (örn: 86.10, 86.20)',
    )

    description = fields.Text(
        string='Açıklama',
    )

    company_id = fields.Many2one(
        'res.company', string='Şirket',
        related='obligation_id.company_id', store=True,
    )
