from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # ── İSG Rol Tipi ────────────────────────────────────────
    isg_party_type = fields.Selection([
        ('osgb',        'OSGB (Ortak Sağlık ve Güvenlik Birimi)'),
        ('isgb',        'İSGB (İşyeri Sağlık ve Güvenlik Birimi)'),
        ('laboratory',  'Yetkili Laboratuvar / Ölçüm Kuruluşu'),
        ('inspection',  'Yetkili Muayene Kuruluşu (EKİPNET)'),
        ('contractor',  'Alt İşveren / Yüklenici'),
        ('supplier',    'Tedarikçi (İSG Malzeme/Hizmet)'),
        ('insurance',   'Sigorta Şirketi'),
        ('public',      'Kamu Kurumu (ÇSGB, SGK, vb.)'),
        ('other',       'Diğer'),
    ],
        string='İSG Rol Tipi',
        tracking=True,
        index=True,
    )

    is_isg_party = fields.Boolean(
        string='İSG Tarafı mı?',
        compute='_compute_is_isg_party',
        store=True,
        index=True,
    )

    # ── OSGB / İSGB Alanları ────────────────────────────────
    osgb_license_no = fields.Char(
        string='Yetki Belgesi No',
        tracking=True,
        help='ÇSGB tarafından verilen OSGB/İSGB yetki belgesi numarası.',
    )
    osgb_license_date = fields.Date(
        string='Yetki Belgesi Tarihi',
        tracking=True,
    )
    osgb_license_expiry = fields.Date(
        string='Yetki Belgesi Bitiş Tarihi',
        tracking=True,
    )
    osgb_license_expired = fields.Boolean(
        string='Yetki Belgesi Süresi Dolmuş',
        compute='_compute_osgb_license_expired',
        store=True,
    )

    # ── Laboratuvar / Muayene Kuruluşu Alanları ─────────────
    accreditation_no = fields.Char(
        string='Akreditasyon No',
        tracking=True,
        help='TÜRKAK akreditasyon numarası.',
    )
    accreditation_scope = fields.Text(
        string='Akreditasyon Kapsamı',
        tracking=True,
    )
    accreditation_expiry = fields.Date(
        string='Akreditasyon Bitiş Tarihi',
        tracking=True,
    )

    # ── Genel ───────────────────────────────────────────────
    isg_note = fields.Text(
        string='İSG Notu',
    )

    # ── Tarihsel Rol Kaydı ──────────────────────────────────
    isg_role_history_ids = fields.One2many(
        'isg.party.role.history',
        'partner_id',
        string='Rol Geçmişi',
    )

    # ── Hesaplamalar ─────────────────────────────────────────
    @api.depends('isg_party_type')
    def _compute_is_isg_party(self):
        for rec in self:
            rec.is_isg_party = bool(rec.isg_party_type)

    @api.depends('osgb_license_expiry')
    def _compute_osgb_license_expired(self):
        today = fields.Date.today()
        for rec in self:
            if rec.osgb_license_expiry:
                rec.osgb_license_expired = rec.osgb_license_expiry < today
            else:
                rec.osgb_license_expired = False


class IsgPartyRoleHistory(models.Model):
    """
    Bir partnerın zaman içinde üstlendiği İSG rollerinin geçmişi.
    Örn: Bir firma önce tedarikçiyken sonra OSGB olabilir.
    """
    _name = 'isg.party.role.history'
    _description = 'İSG Taraf Rol Geçmişi'
    _order = 'date_start desc'

    partner_id = fields.Many2one(
        'res.partner',
        string='Firma / Kişi',
        required=True,
        ondelete='cascade',
    )
    isg_party_type = fields.Selection([
        ('osgb',        'OSGB'),
        ('isgb',        'İSGB'),
        ('laboratory',  'Yetkili Laboratuvar'),
        ('inspection',  'Yetkili Muayene Kuruluşu'),
        ('contractor',  'Alt İşveren / Yüklenici'),
        ('supplier',    'Tedarikçi'),
        ('insurance',   'Sigorta Şirketi'),
        ('public',      'Kamu Kurumu'),
        ('other',       'Diğer'),
    ],
        string='Rol',
        required=True,
    )
    date_start = fields.Date(string='Başlangıç Tarihi', required=True)
    date_end = fields.Date(string='Bitiş Tarihi')
    note = fields.Char(string='Not')
