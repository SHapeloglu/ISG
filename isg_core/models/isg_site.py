from odoo import models, fields, api


class IsgSite(models.Model):
    _name = 'isg.site'
    _description = 'Fiziksel Site / Lokasyon'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'workplace_id, name'
    _parent_name = 'parent_id'
    _parent_store = True

    name = fields.Char(
        string='Site / Lokasyon Adı',
        required=True,
        tracking=True,
    )
    workplace_id = fields.Many2one(
        'isg.workplace',
        string='İSG İşyeri',
        required=True,
        ondelete='cascade',
        tracking=True,
    )
    company_id = fields.Many2one(
        'res.company',
        related='workplace_id.company_id',
        store=True,
        string='Şirket',
    )
    parent_id = fields.Many2one(
        'isg.site',
        string='Üst Lokasyon',
        ondelete='cascade',
    )
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many(
        'isg.site',
        'parent_id',
        string='Alt Lokasyonlar',
    )
    site_type = fields.Selection([
        ('campus',   'Kampüs'),
        ('building', 'Bina'),
        ('floor',    'Kat'),
        ('area',     'Alan / Saha'),
        ('line',     'Hat'),
        ('other',    'Diğer'),
    ],
        string='Lokasyon Türü',
        default='area',
    )
    danger_class = fields.Selection([
        ('low',    'Az Tehlikeli'),
        ('medium', 'Tehlikeli'),
        ('high',   'Çok Tehlikeli'),
    ],
        string='Tehlike Sınıfı',
        help='Boş bırakılırsa işyerinin tehlike sınıfı geçerlidir.',
    )
    active = fields.Boolean(default=True)
    note = fields.Text(string='Notlar')

    def name_get(self):
        result = []
        for rec in self:
            name = rec.name
            if rec.parent_id:
                name = f'{rec.parent_id.name} / {name}'
            result.append((rec.id, name))
        return result
