# -*- coding: utf-8 -*-
import hashlib
import base64
import os

from odoo import models, fields, api


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    isg_sha256 = fields.Char(
        string='SHA-256 Hash',
        compute='_compute_isg_sha256',
        store=True,
        help='Dosya içeriğinin SHA-256 özeti. Dosya değişirse hash de değişir; '
             'bu sayede belge bütünlüğü doğrulanabilir.',
    )

    @api.depends('store_fname', 'db_datas')
    def _compute_isg_sha256(self):
        for attachment in self:
            try:
                if attachment.store_fname:
                    # Dosya sisteminde saklı — tam yolu al ve oku
                    full_path = attachment._full_path(attachment.store_fname)
                    if os.path.exists(full_path):
                        with open(full_path, 'rb') as f:
                            attachment.isg_sha256 = hashlib.sha256(f.read()).hexdigest()
                    else:
                        attachment.isg_sha256 = False
                elif attachment.db_datas:
                    # Veritabanında saklı (küçük dosyalar)
                    raw = base64.b64decode(attachment.db_datas)
                    attachment.isg_sha256 = hashlib.sha256(raw).hexdigest()
                else:
                    attachment.isg_sha256 = False
            except Exception:
                attachment.isg_sha256 = False
