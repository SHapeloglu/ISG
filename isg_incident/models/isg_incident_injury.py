# -*- coding: utf-8 -*-
from odoo import models, fields, api

class IsgIncidentInjury(models.Model):
    _name = 'isg.incident.injury'
    _description = 'Yaralanma Detayı'
    _order = 'incident_id, sequence'

    incident_id = fields.Many2one(
        'isg.incident', string='Kaza', required=True, ondelete='cascade',
    )
    sequence = fields.Integer(default=10)

    # --- Yaralanma Türü ---
    injury_type = fields.Selection([
        ('none', 'Yaralanma Yok (Ramak Kala)'),
        ('first_aid', 'İlk Yardım'),
        ('lost_time', 'Kayıp Gün (Hastanelik)'),
        ('permanent_disability', 'Kalıcı İşlev Kaybı'),
        ('fatality', 'Ölüm'),
    ], string='Yaralanma Türü', required=True, default='first_aid',
    )

    # --- Beden Bölümü ---
    body_part = fields.Selection([
        ('head', 'Baş'),
        ('face', 'Yüz'),
        ('eye', 'Göz'),
        ('ear', 'Kulak'),
        ('neck', 'Boyun'),
        ('shoulder', 'Omuz'),
        ('arm', 'Kol'),
        ('elbow', 'Dirsek'),
        ('forearm', 'Ön Kol'),
        ('wrist', 'Bilek'),
        ('hand', 'El'),
        ('finger', 'Parmak'),
        ('chest', 'Göğüs'),
        ('back', 'Sırt'),
        ('abdomen', 'Karın'),
        ('hip', 'Kalça'),
        ('thigh', 'Uyluk'),
        ('knee', 'Diz'),
        ('leg', 'Bacak'),
        ('ankle', 'Ayak Bileği'),
        ('foot', 'Ayak'),
        ('toe', 'Ayak Parmağı'),
        ('multiple', 'Çoklu Bölgeler'),
        ('other', 'Diğer'),
    ], string='Yaralı Beden Bölümü',
    )

    # --- Açıklamalar ---
    injury_description = fields.Text(string='Yaralanma Açıklaması')
    medical_treatment = fields.Text(string='Tıbbi Müdahale')

    # --- Kayıp Gün ---
    days_lost = fields.Integer(
        string='Kayıp İş Günü',
        help='lost_time seçilirse doldur',
    )

    # --- Dönüş Eğitimi ---
    needs_return_training = fields.Boolean(
        string='Dönüş Eğitimi Gerekli',
        default=False,
    )

    # --- Kalıcı Sonuç ---
    permanent_consequence = fields.Text(
        string='Kalıcı Sonuç',
        help='permanent_disability seçilirse doldur',
    )

    _sql_constraints = [
        ('days_lost_positive', 'check(days_lost > 0 or injury_type != \'lost_time\')',
         'Kayıp gün pozitif olmalı veya yaralanma türü lost_time olmamalı.'),
    ]
