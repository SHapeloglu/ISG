# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class IsgCapa(models.Model):
    _name = 'isg.capa'
    _description = 'DÖF / CAPA Kaydı'
    _inherit = ['mail.thread']
    _order = 'open_date desc'

    name = fields.Char(
        string='DÖF No', required=True, copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('isg.capa'),
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İşyeri',
        required=True, ondelete='cascade', tracking=True,
    )
    site_id = fields.Many2one(
        'isg.site', string='Alan / Lokasyon',
        domain="[('workplace_id', '=', workplace_id)]",
    )
    source = fields.Selection(
        selection=[
            ('incident', 'İş Kazası / Ramak Kala'),
            ('audit', 'Denetim Bulgusu'),
            ('inspection', 'Müfettiş Tespiti'),
            ('measurement', 'Ölçüm Aşımı'),
            ('employee', 'Çalışan Bildirimi'),
            ('board', 'İSG Kurulu Kararı'),
            ('other', 'Diğer'),
        ],
        string='Kaynak', required=True, tracking=True,
    )
    capa_type = fields.Selection(
        selection=[
            ('corrective', 'Düzeltici (DÖF)'),
            ('preventive', 'Önleyici (ÖF)'),
        ],
        string='Tür', required=True, default='corrective', tracking=True,
    )
    severity = fields.Selection(
        selection=[
            ('low', 'Düşük'),
            ('medium', 'Orta'),
            ('high', 'Yüksek'),
            ('critical', 'Kritik'),
        ],
        string='Önem Derecesi', required=True, default='medium', tracking=True,
    )
    state = fields.Selection(
        selection=[
            ('open', 'Açık'),
            ('analysis', 'Analiz'),
            ('action', 'Aksiyon'),
            ('verification', 'Doğrulama'),
            ('closed', 'Kapalı'),
            ('cancelled', 'İptal'),
        ],
        string='Durum', default='open', tracking=True,
    )
    open_date = fields.Date(
        string='Açılış Tarihi', required=True,
        default=fields.Date.today, tracking=True,
    )
    due_date = fields.Date(
        string='Kapanış Termin Tarihi', tracking=True,
    )
    close_date = fields.Date(
        string='Kapanış Tarihi', tracking=True,
    )
    is_overdue = fields.Boolean(
        string='Süresi Geçmiş', compute='_compute_is_overdue', store=True,
    )
    responsible_id = fields.Many2one(
        'hr.employee', string='Sorumlu Kişi', tracking=True,
    )
    opened_by_id = fields.Many2one(
        'hr.employee', string='Açan Kişi', tracking=True,
    )
    verified_by_id = fields.Many2one(
        'hr.employee', string='Doğrulayan Kişi', tracking=True,
    )
    description = fields.Text(
        string='Sorun Tanımı', required=True,
    )
    immediate_action = fields.Text(
        string='Acil / Anlık Aksiyon',
    )
    # Kök Neden Analizi
    root_cause_method = fields.Selection(
        selection=[
            ('5why', '5 Neden Analizi'),
            ('fishbone', 'Balık Kılçığı (Ishikawa)'),
            ('fault_tree', 'Hata Ağacı Analizi'),
            ('other', 'Diğer'),
        ],
        string='Kök Neden Yöntemi',
    )
    root_cause = fields.Text(string='Kök Neden')
    why_1 = fields.Char(string='1. Neden')
    why_2 = fields.Char(string='2. Neden')
    why_3 = fields.Char(string='3. Neden')
    why_4 = fields.Char(string='4. Neden')
    why_5 = fields.Char(string='5. Neden (Kök Neden)')
    # Balık Kılçığı Kategorileri
    cause_human = fields.Text(string='İnsan (Human)')
    cause_machine = fields.Text(string='Makine (Machine)')
    cause_method = fields.Text(string='Yöntem (Method)')
    cause_material = fields.Text(string='Malzeme (Material)')
    cause_environment = fields.Text(string='Çevre (Environment)')
    cause_management = fields.Text(string='Yönetim (Management)')
    # Doğrulama
    verification_result = fields.Selection(
        selection=[
            ('effective', 'Etkin — Sorun Tekrarlamadı'),
            ('partial', 'Kısmen Etkin — Takip Gerekiyor'),
            ('ineffective', 'Etkin Değil — Yeniden Aç'),
        ],
        string='Etkinlik Değerlendirmesi', tracking=True,
    )
    verification_notes = fields.Text(string='Doğrulama Notları')
    action_ids = fields.One2many(
        'isg.capa.action', 'capa_id', string='Aksiyonlar',
    )
    action_count = fields.Integer(
        string='Aksiyon Sayısı', compute='_compute_action_count',
    )
    isg_document_id = fields.Many2one(
        'isg.document', string='İlgili Belge',
    )

    @api.depends('due_date', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.today()
        for rec in self:
            if rec.due_date and rec.state not in ['closed', 'cancelled']:
                rec.is_overdue = rec.due_date < today
            else:
                rec.is_overdue = False

    @api.depends('action_ids')
    def _compute_action_count(self):
        for rec in self:
            rec.action_count = len(rec.action_ids)

    def action_to_analysis(self):
        self.write({'state': 'analysis'})

    def action_to_action(self):
        if not self.root_cause:
            raise ValidationError('Aksiyona geçmeden önce Kök Neden alanı doldurulmalıdır.')
        self.write({'state': 'action'})

    def action_to_verification(self):
        open_actions = self.action_ids.filtered(lambda a: a.state != 'done')
        if open_actions:
            raise ValidationError('Doğrulamaya geçmeden önce tüm aksiyonlar tamamlanmalıdır.')
        self.write({'state': 'verification'})

    def action_close(self):
        if not self.verification_result:
            raise ValidationError('Kapatmadan önce Etkinlik Değerlendirmesi yapılmalıdır.')
        if self.verification_result == 'ineffective':
            raise ValidationError('Etkin değil olarak değerlendirilen DÖF kapatılamaz. Yeniden açın.')
        self.write({
            'state': 'closed',
            'close_date': fields.Date.today(),
        })

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_reopen(self):
        self.write({'state': 'open', 'close_date': False})
