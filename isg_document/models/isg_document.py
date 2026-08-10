# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class IsgDocument(models.Model):
    _name = 'isg.document'
    _description = 'İSG Belge / Kanıt Kaydı'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(
        string='Belge Adı', required=True, tracking=True,
    )
    document_type = fields.Selection(
        selection=[
            ('risk_assessment', 'Risk Değerlendirmesi'),
            ('training_certificate', 'Eğitim Sertifikası'),
            ('measurement_report', 'Ölçüm Raporu'),
            ('inspection_report', 'Muayene/Kontrol Raporu'),
            ('health_report', 'Sağlık Raporu'),
            ('permit', 'İş İzni'),
            ('other', 'Diğer'),
        ],
        string='Belge Türü', required=True, tracking=True,
    )

    # --- Dosya bağlantısı ---
    attachment_id = fields.Many2one(
        'ir.attachment', string='Dosya', ondelete='restrict', readonly=True,
    )
    document_file = fields.Binary(
        string='Dosya Yükle', attachment=False,
        help='Dosyayı buradan yükleyin; sistem otomatik olarak İSG belgesine bağlar.',
    )
    document_filename = fields.Char(string='Dosya Adı')
    isg_sha256 = fields.Char(
        related='attachment_id.isg_sha256', string='SHA-256', store=True, readonly=True,
    )

    # --- Sürüm zinciri ---
    version = fields.Integer(string='Sürüm No', default=1, readonly=True)
    parent_document_id = fields.Many2one(
        'isg.document', string='Önceki Sürüm', readonly=True, ondelete='restrict',
    )
    child_document_ids = fields.One2many(
        'isg.document', 'parent_document_id', string='Sonraki Sürümler',
    )

    # --- Geçerlilik ---
    valid_from = fields.Date(string='Geçerlilik Başlangıcı')
    valid_until = fields.Date(string='Geçerlilik Bitişi')

    # --- Durum / kilit ---
    state = fields.Selection(
        selection=[
            ('draft', 'Taslak'),
            ('approved', 'Onaylı'),
            ('locked', 'Kilitli (Arşiv)'),
        ],
        string='Durum', default='draft', required=True, tracking=True,
    )

    # --- E-imza (5070 s.K.) ---
    signed_by_id = fields.Many2one(
        'res.users', string='İmzalayan', readonly=True,
    )
    signed_date = fields.Datetime(string='İmza Tarihi', readonly=True)
    signature_reference = fields.Char(
        string='E-İmza Referans No', readonly=True,
        help='5070 sayılı Elektronik İmza Kanunu kapsamında imza referansı.',
    )

    # --- Güvenlik zinciri (ALAN 4) ---
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri',
    )
    site_id = fields.Many2one(
        'isg.site', string='Site / Lokasyon',
    )

    # --- Kaynak kayıt (polymorphic) ---
    res_model = fields.Char(string='Kaynak Model')
    res_id = fields.Integer(string='Kaynak Kayıt ID')

    # ------------------------------------------------------------------
    # Kilit mekanizması: state == 'locked' olan kayıtlar değiştirilemez
    # ------------------------------------------------------------------
    @api.model_create_multi
    def create(self, vals_list):
        file_map = {}
        for i, vals in enumerate(vals_list):
            if vals.get('document_file'):
                file_map[i] = (vals.pop('document_file'), vals.pop('document_filename', None))
        records = super().create(vals_list)
        for i, rec in enumerate(records):
            if i in file_map:
                file_data, filename = file_map[i]
                attachment = self.env['ir.attachment'].create({
                    'name': filename or rec.name or 'document',
                    'datas': file_data,
                    'res_model': 'isg.document',
                    'res_id': rec.id,
                })
                rec.attachment_id = attachment.id
        return records

    def write(self, vals):
        for doc in self:
            if doc.state == 'locked':
                # Sadece chatter/activity alanlarına izin ver, geri kalanı engelle
                allowed_keys = {'message_follower_ids', 'activity_ids', 'message_ids'}
                if not set(vals.keys()).issubset(allowed_keys):
                    raise UserError(_(
                        'Bu belge kilitlenmiştir ve değiştirilemez. '
                        'Değişiklik yapmak için yeni bir sürüm oluşturun.'
                    ))
        file_data = vals.pop('document_file', None)
        filename = vals.pop('document_filename', None)
        result = super().write(vals)
        if file_data:
            for doc in self:
                attachment = self.env['ir.attachment'].create({
                    'name': filename or doc.name or 'document',
                    'datas': file_data,
                    'res_model': 'isg.document',
                    'res_id': doc.id,
                })
                super(IsgDocument, doc).write({'attachment_id': attachment.id})
        return result

    def unlink(self):
        for doc in self:
            if doc.state in ('approved', 'locked'):
                raise UserError(_(
                    'Onaylı veya kilitli belgeler silinemez.'
                ))
        return super().unlink()

    # ------------------------------------------------------------------
    # Durum geçiş butonları
    # ------------------------------------------------------------------
    def action_approve(self):
        for doc in self:
            if doc.state != 'draft':
                raise UserError(_('Sadece taslak belgeler onaylanabilir.'))
            doc.state = 'approved'

    def action_lock(self):
        for doc in self:
            if doc.state != 'approved':
                raise UserError(_('Sadece onaylı belgeler kilitlenebilir.'))
            doc.signed_by_id = self.env.user
            doc.signed_date = fields.Datetime.now()
            doc.state = 'locked'

    def action_new_version(self):
        """Kilitli/onaylı bir belgeden yeni taslak sürüm oluşturur."""
        self.ensure_one()
        new_doc = self.copy({
            'version': self.version + 1,
            'parent_document_id': self.id,
            'state': 'draft',
            'signed_by_id': False,
            'signed_date': False,
            'signature_reference': False,
            'attachment_id': False,
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'isg.document',
            'view_mode': 'form',
            'res_id': new_doc.id,
            'target': 'current',
        }
