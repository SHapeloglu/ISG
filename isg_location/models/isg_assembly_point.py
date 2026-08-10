from odoo import models, fields


class IsgAssemblyPoint(models.Model):
    """
    Acil durum toplanma noktaları.
    Bir site altında birden fazla toplanma noktası olabilir.
    """
    _name = 'isg.assembly.point'
    _description = 'Acil Durum Toplanma Noktası'
    _order = 'site_id, name'

    name = fields.Char(
        string='Toplanma Noktası Adı',
        required=True,
    )
    site_id = fields.Many2one(
        'isg.site',
        string='Bağlı Site / Lokasyon',
        required=True,
        ondelete='cascade',
    )
    workplace_id = fields.Many2one(
        'isg.workplace',
        related='site_id.workplace_id',
        store=True,
        string='İşyeri',
    )
    company_id = fields.Many2one(
        'res.company',
        related='site_id.company_id',
        store=True,
        string='Şirket',
    )
    capacity = fields.Integer(
        string='Kapasite (Kişi)',
        help='Bu toplanma noktasına tahliye edilebilecek maksimum kişi sayısı.',
    )
    latitude = fields.Float(string='Enlem', digits=(10, 7))
    longitude = fields.Float(string='Boylam', digits=(10, 7))
    description = fields.Text(string='Açıklama / Yol Tarifi')
    active = fields.Boolean(default=True)
