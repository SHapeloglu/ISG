# -*- coding: utf-8 -*-
from odoo import models, fields, api


class IsgOutbox(models.Model):
    """
    E3 entegrasyonları için olay kuyruğu.
    İSG-KATİP, EKİPNET, SGK gibi dış sistemlere
    gönderilecek olaylar burada birikir ve işlenir.
    """
    _name = 'isg.outbox'
    _description = 'İSG Entegrasyon Outbox'
    _order = 'create_date asc'

    # --- Kaynak kayıt ---
    res_model = fields.Char(string='Model', required=True)
    res_id = fields.Integer(string='Kayıt ID', required=True)
    res_uuid = fields.Char(string='Kayıt UUID')

    # --- Olay ---
    event_type = fields.Selection(
        selection=[
            ('create', 'Oluşturma'),
            ('update', 'Güncelleme'),
            ('delete', 'Silme'),
            ('assign', 'Atama'),
            ('revoke', 'İptal'),
        ],
        string='Olay Türü', required=True,
    )
    target_system = fields.Selection(
        selection=[
            ('isgkatip', 'İSG-KATİP'),
            ('ekipnet', 'EKİPNET'),
            ('sgk', 'SGK'),
            ('verbis', 'VERBİS'),
            ('other', 'Diğer'),
        ],
        string='Hedef Sistem', required=True,
    )
    payload = fields.Text(
        string='Payload (JSON)',
        help='Dış sisteme gönderilecek JSON verisi.',
    )

    # --- Durum ---
    state = fields.Selection(
        selection=[
            ('pending', 'Bekliyor'),
            ('processing', 'İşleniyor'),
            ('done', 'Gönderildi'),
            ('error', 'Hata'),
            ('cancelled', 'İptal'),
        ],
        string='Durum', default='pending', required=True, index=True,
    )

    # --- Retry ---
    retry_count = fields.Integer(string='Deneme Sayısı', default=0)
    max_retries = fields.Integer(string='Maksimum Deneme', default=3)
    next_retry = fields.Datetime(string='Sonraki Deneme')

    # --- Hata ---
    error_message = fields.Text(string='Hata Mesajı')
    last_attempt = fields.Datetime(string='Son Deneme')

    # --- Yanıt ---
    response_code = fields.Char(string='Yanıt Kodu')
    response_body = fields.Text(string='Yanıt İçeriği')

    def action_cancel(self):
        self.filtered(lambda r: r.state in ('pending', 'error')).write({
            'state': 'cancelled',
        })

    def action_retry(self):
        self.filtered(lambda r: r.state == 'error').write({
            'state': 'pending',
            'retry_count': 0,
            'error_message': False,
        })
