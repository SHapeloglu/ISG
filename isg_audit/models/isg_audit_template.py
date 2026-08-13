# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgAuditTemplate(models.Model):
    _name = 'isg.audit.template'
    _description = 'Denetim Kontrol Listesi Şablonu'
    _order = 'name'

    name = fields.Char(string='Şablon Adı', required=True)
    audit_type = fields.Selection(
        [
            ('internal', 'İç Denetim'),
            ('external', 'Dış Denetim'),
            ('inspection', 'Müfettiş Denetimi'),
            ('supplier', 'Tedarikçi/Alt İşveren Denetimi'),
        ],
        string='Denetim Türü', required=True, default='internal',
    )
    description = fields.Text(string='Açıklama')
    active = fields.Boolean(string='Aktif', default=True)
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )
    question_ids = fields.One2many(
        'isg.audit.template.question', 'template_id', string='Sorular',
    )
    question_count = fields.Integer(
        string='Soru Sayısı', compute='_compute_question_count',
    )

    @api.depends('question_ids')
    def _compute_question_count(self):
        for rec in self:
            rec.question_count = len(rec.question_ids)


class IsgAuditTemplateQuestion(models.Model):
    _name = 'isg.audit.template.question'
    _description = 'Denetim Şablonu Sorusu'
    _order = 'sequence, id'

    template_id = fields.Many2one(
        'isg.audit.template', string='Şablon',
        required=True, ondelete='cascade',
    )
    sequence = fields.Integer(string='Sıra', default=10)
    question = fields.Char(string='Soru / Kontrol Maddesi', required=True)
    category = fields.Selection(
        [
            ('risk', 'Risk Yönetimi'),
            ('emergency', 'Acil Durum'),
            ('ppe', 'KKD'),
            ('equipment', 'Ekipman / Makine'),
            ('chemical', 'Kimyasal'),
            ('training', 'Eğitim'),
            ('documentation', 'Dokümantasyon'),
            ('housekeeping', 'Düzen / Temizlik'),
            ('other', 'Diğer'),
        ],
        string='Kategori', default='other',
    )
    legal_reference = fields.Char(string='Yasal Dayanak')
    is_critical = fields.Boolean(
        string='Kritik Madde',
        help='İşaretlenirse uygunsuz bulgu otomatik DÖF açar',
    )
