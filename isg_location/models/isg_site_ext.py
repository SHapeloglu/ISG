from odoo import models, fields, api


class IsgSiteExt(models.Model):
    """
    isg_core'daki isg.site modelini genişletir.
    GPS, kapasite, toplanma noktası ve tehlikeli alan bilgileri eklenir.
    """
    _inherit = 'isg.site'

    # ── GPS Koordinatları ────────────────────────────────────
    latitude = fields.Float(
        string='Enlem (Latitude)',
        digits=(10, 7),
    )
    longitude = fields.Float(
        string='Boylam (Longitude)',
        digits=(10, 7),
    )

    # ── Kapasite ve Sorumlu ──────────────────────────────────
    capacity = fields.Integer(
        string='Kapasite (Kişi)',
        help='Bu alanda aynı anda çalışabilecek maksimum kişi sayısı.',
    )
    responsible_id = fields.Many2one(
        'res.partner',
        string='Sorumlu Kişi',
        domain=[('is_company', '=', False)],
    )

    # ── Tehlikeli Alan Bilgileri ─────────────────────────────
    is_hazardous = fields.Boolean(
        string='Tehlikeli Alan mı?',
        tracking=True,
        help='ATEX, kapalı alan, yüksek gerilim vb. özel tehlike barındıran alanlar.',
    )
    hazard_type = fields.Selection([
        ('atex',        'ATEX / Patlayıcı Ortam'),
        ('confined',    'Kapalı Alan'),
        ('electrical',  'Yüksek Gerilim'),
        ('radiation',   'Radyasyon'),
        ('chemical',    'Kimyasal Madde'),
        ('height',      'Yüksekte Çalışma'),
        ('noise',       'Yüksek Gürültü'),
        ('other',       'Diğer'),
    ],
        string='Tehlike Türü',
        invisible=True,
    )
    hazard_description = fields.Text(
        string='Tehlike Açıklaması',
    )

    # ── Toplanma Noktası ─────────────────────────────────────
    is_assembly_point = fields.Boolean(
        string='Toplanma Noktası mı?',
        tracking=True,
        help='Acil durum tahliyesinde toplanma noktası olarak kullanılan alan.',
    )
    assembly_point_ids = fields.One2many(
        'isg.assembly.point',
        'site_id',
        string='Toplanma Noktaları',
    )
    assembly_point_count = fields.Integer(
        string='Toplanma Noktası Sayısı',
        compute='_compute_assembly_point_count',
    )

    @api.depends('assembly_point_ids')
    def _compute_assembly_point_count(self):
        for rec in self:
            rec.assembly_point_count = len(rec.assembly_point_ids)
