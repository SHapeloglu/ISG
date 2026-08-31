# -*- coding: utf-8 -*-
from odoo import models, fields


class IsgTrainingType(models.Model):
    _name = 'isg.training.type'
    _description = 'İSG Eğitim Türü'
    _inherit = ['isg.uuid.mixin']
    _order = 'sequence, name'

    name = fields.Char(string='Eğitim Türü Adı', required=True)
    sequence = fields.Integer(string='Sıra', default=10)
    code = fields.Char(string='Kod', help='İç referans kodu.')

    # --- 2 Nisan 2026 Yönetmeliği ---
    training_category = fields.Selection(
        selection=[
            ('onboarding', 'İşe Başlama Eğitimi'),
            ('basic', 'Temel Eğitim'),
            ('periodic', 'Periyodik Eğitim'),
            ('return', 'Dönüş Eğitimi'),
            ('task_specific', 'Göreve Özgü Eğitim'),
            ('special_group', 'Özel Grup Eğitimi'),
            ('emergency', 'Acil Durum Eğitimi'),
            ('other', 'Diğer'),
        ],
        string='Eğitim Kategorisi', required=True,
    )
    delivery_method = fields.Selection(
        selection=[
            ('face_to_face', 'Yüz Yüze'),
            ('online', 'Çevrimiçi'),
            ('hybrid', 'Karma'),
        ],
        string='Eğitim Yöntemi', default='face_to_face',
    )

    # --- Süre zorunluluğu ---
    min_duration_hours = fields.Float(
        string='Minimum Süre (Saat)',
        help='2 Nisan 2026 yönetmeliğine göre: işe başlama eğitimi min 2 saat yüz yüze zorunlu.',
    )

    # --- Periyot (tehlike sınıfına göre) ---
    period_low = fields.Integer(
        string='Az Tehlikeli Periyot (Ay)',
        default=36,
        help='Az tehlikeli işyerleri için tekrar periyodu (ay). Yönetmelik: 3 yıl = 36 ay.',
    )
    period_medium = fields.Integer(
        string='Tehlikeli Periyot (Ay)',
        default=24,
        help='Tehlikeli işyerleri için tekrar periyodu (ay). Yönetmelik: 2 yıl = 24 ay.',
    )
    period_high = fields.Integer(
        string='Çok Tehlikeli Periyot (Ay)',
        default=12,
        help='Çok tehlikeli işyerleri için tekrar periyodu (ay). Yönetmelik: 1 yıl = 12 ay.',
    )

    # --- Hedef kitle ---
    target_all = fields.Boolean(
        string='Tüm Çalışanlar', default=True,
        help='Bu eğitim tüm çalışanlara zorunlu mu?',
    )
    target_new_employee = fields.Boolean(string='Yeni İşe Başlayanlar')
    target_pregnant = fields.Boolean(string='Gebe Çalışanlar')
    target_young = fields.Boolean(string='Genç Çalışanlar (18 yaş altı)')
    target_senior = fields.Boolean(string='Yaşlı Çalışanlar (55 yaş üstü)')
    target_disabled = fields.Boolean(string='Engelli Çalışanlar')

    description = fields.Text(string='Açıklama')
    active = fields.Boolean(default=True)
