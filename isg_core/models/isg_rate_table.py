from odoo import models, fields, api


class IsgRateTable(models.Model):
    _name = 'isg.rate.table'
    _description = 'İSG Uzman/Hekim Süre Katsayı Tablosu (6331 s.K. md.6)'
    _order = 'valid_from desc, danger_class, role'
    _rec_name = 'display_name'

    danger_class = fields.Selection([
        ('low',    'Az Tehlikeli'),
        ('medium', 'Tehlikeli'),
        ('high',   'Çok Tehlikeli'),
    ],
        string='Tehlike Sınıfı',
        required=True,
    )
    role = fields.Selection([
        ('expert',    'İSG Uzmanı'),
        ('physician', 'İşyeri Hekimi'),
    ],
        string='Rol',
        required=True,
    )
    minutes_per_employee = fields.Integer(
        string='Dakika / Çalışan / Ay',
        required=True,
    )
    valid_from = fields.Date(
        string='Geçerlilik Başlangıcı',
        required=True,
        default=lambda self: fields.Date.today(),
    )
    active = fields.Boolean(default=True)
    note = fields.Char(string='Not / Kaynak')

    display_name = fields.Char(
        string='Görünen Ad',
        compute='_compute_display_name',
        store=True,
    )

    @api.depends('danger_class', 'role', 'minutes_per_employee', 'valid_from')
    def _compute_display_name(self):
        danger_labels = dict(self._fields['danger_class'].selection)
        role_labels = dict(self._fields['role'].selection)
        for rec in self:
            rec.display_name = '%s / %s — %s dk (%s itibarıyla)' % (
                danger_labels.get(rec.danger_class, ''),
                role_labels.get(rec.role, ''),
                rec.minutes_per_employee,
                rec.valid_from,
            )

    @api.model
    def get_rate(self, danger_class, role, on_date=None):
        """Verilen tarihte (varsayılan: bugün) geçerli olan dakika/çalışan katsayısını döndürür.
        on_date <= valid_from olan en güncel kaydı bulur. Kayıt yoksa 0 döner.
        """
        if not danger_class or not role:
            return 0
        on_date = on_date or fields.Date.today()
        rate = self.search([
            ('danger_class', '=', danger_class),
            ('role', '=', role),
            ('valid_from', '<=', on_date),
            ('active', '=', True),
        ], order='valid_from desc', limit=1)
        return rate.minutes_per_employee if rate else 0
