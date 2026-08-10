# -*- coding: utf-8 -*-
import uuid as uuid_lib
from odoo import models, fields, api


class IsgUuidMixin(models.AbstractModel):
    """
    Tüm isg_* modellerin _inherit edeceği UUID mixin.
    E3 entegrasyonları (İSG-KATİP, EKİPNET vb.) için
    dış sistem ID'si sağlar.
    """
    _name = 'isg.uuid.mixin'
    _description = 'İSG UUID Mixin'

    isg_uuid = fields.Char(
        string='İSG UUID',
        readonly=True,
        copy=False,
        index=True,
        help='Dış sistem entegrasyonları için benzersiz tanımlayıcı (UUID4). '
             'Kayıt oluşturulduğunda otomatik atanır, değiştirilemez.',
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('isg_uuid'):
                vals['isg_uuid'] = str(uuid_lib.uuid4())
        return super().create(vals_list)
