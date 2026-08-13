from odoo import models, fields, api
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class IsgIncident(models.Model):
    _name = 'isg.incident'
    _description = 'İş Kazası / Ramak Kala'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'incident_date desc, id desc'

    name = fields.Char(
        string='Referans No',
        readonly=True,
        copy=False,
        default='Yeni',
    )
    incident_type = fields.Selection([
        ('accident', 'İş Kazası'),
        ('near_miss', 'Ramak Kala'),
        ('occupational_disease', 'Meslek Hastalığı'),
    ], string='Olay Türü', required=True, default='accident', tracking=True)

    company_id = fields.Many2one(
        'res.company',
        string='Şirket',
        required=True,
        default=lambda self: self.env.company,
        tracking=True,
    )
    workplace_id = fields.Many2one(
        'isg.workplace',
        string='İSG İşyeri',
        required=True,
        tracking=True,
    )
    site_id = fields.Many2one(
        'isg.site',
        string='Fiziksel Lokasyon',
        domain="[('workplace_id', '=', workplace_id)]",
        tracking=True,
    )
    incident_date = fields.Date(
        string='Olay Tarihi',
        required=True,
        default=fields.Date.today,
        tracking=True,
    )
    incident_time = fields.Float(
        string='Olay Saati',
        digits=(2, 2),
        help='Saat:Dakika formatında (örn. 14.30)',
    )
    location_description = fields.Char(
        string='Olay Yeri Tanımı',
    )
    description = fields.Text(
        string='Olay Tanımı',
        required=True,
    )

    # --- Etkilenen Kişi ---
    victim_id = fields.Many2one(
        'hr.employee',
        string='Kazaya Uğrayan / Etkilenen',
        tracking=True,
    )
    victim_job_title = fields.Char(
        string='Görevi',
        related='victim_id.job_title',
        store=True,
    )
    victim_tenure_days = fields.Integer(
        string='İşyerindeki Kıdem (Gün)',
    )
    witness_ids = fields.Many2many(
        'hr.employee',
        'isg_incident_witness_rel',
        'incident_id',
        'employee_id',
        string='Tanıklar',
    )

    # --- Yaralanma Bilgileri ---
    injury_type = fields.Selection([
        ('none', 'Yaralanma Yok'),
        ('cut', 'Kesik / Yara'),
        ('fracture', 'Kırık'),
        ('burn', 'Yanık'),
        ('crush', 'Ezilme / Burkulmak'),
        ('eye', 'Göz Yaralanması'),
        ('chemical', 'Kimyasal Maruziyet'),
        ('electrical', 'Elektrik Çarpması'),
        ('fall', 'Düşme'),
        ('death', 'Ölüm'),
        ('other', 'Diğer'),
    ], string='Yaralanma Türü', tracking=True)

    body_part = fields.Selection([
        ('head', 'Baş / Boyun'),
        ('eye', 'Göz'),
        ('hand', 'El / Parmak'),
        ('arm', 'Kol / Omuz'),
        ('leg', 'Bacak / Ayak'),
        ('back', 'Sırt / Bel'),
        ('trunk', 'Gövde'),
        ('multiple', 'Çoklu'),
        ('other', 'Diğer'),
    ], string='Vücut Bölgesi')

    first_aid_given = fields.Boolean(string='İlk Yardım Yapıldı mı?')
    hospitalized = fields.Boolean(string='Hastaneye Kaldırıldı mı?')
    lost_work_days = fields.Integer(
        string='Kayıp İş Günü',
        default=0,
        tracking=True,
    )

    # --- SGK Bildirimi (6331 md.14) ---
    sgk_notification_required = fields.Boolean(
        string='SGK Bildirimi Gerekli mi?',
        compute='_compute_sgk_notification',
        store=True,
    )
    sgk_notification_deadline = fields.Date(
        string='SGK Bildirim Son Tarihi',
        compute='_compute_sgk_notification',
        store=True,
        help='İş kazasında 3 iş günü içinde SGK\'ya bildirim zorunludur (6331 md.14)',
    )
    sgk_notification_done = fields.Boolean(
        string='SGK Bildirimi Yapıldı mı?',
        tracking=True,
    )
    sgk_notification_date = fields.Date(
        string='SGK Bildirim Tarihi',
        tracking=True,
    )
    sgk_reference_no = fields.Char(
        string='SGK Bildirim Referans No',
    )

    # --- Kök Neden ve DÖF ---
    immediate_cause = fields.Text(string='Anlık Neden')
    root_cause = fields.Text(string='Kök Neden (Özet)')
    capa_id = fields.Many2one(
        'isg.capa',
        string='İlgili DÖF',
        readonly=True,
        tracking=True,
    )

    # --- Belge ---
    document_id = fields.Many2one(
        'isg.document',
        string='İlgili Belge',
    )

    # --- Durum ---
    state = fields.Selection([
        ('draft', 'Taslak'),
        ('investigation', 'Araştırma'),
        ('sgk_pending', 'SGK Bildirimi Bekliyor'),
        ('closed', 'Kapalı'),
    ], string='Durum', default='draft', tracking=True)

    notes = fields.Html(string='Notlar')

    # -------------------------------------------------------------------------
    # Compute
    # -------------------------------------------------------------------------

    @api.depends('incident_type', 'incident_date')
    def _compute_sgk_notification(self):
        for rec in self:
            if rec.incident_type == 'accident' and rec.incident_date:
                rec.sgk_notification_required = True
                # 6331 md.14: 3 iş günü — basit hesaplama (takvim günü olarak +3)
                rec.sgk_notification_deadline = rec.incident_date + relativedelta(days=3)
            else:
                rec.sgk_notification_required = False
                rec.sgk_notification_deadline = False

    # -------------------------------------------------------------------------
    # Durum geçişleri
    # -------------------------------------------------------------------------

    def action_start_investigation(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError('Sadece Taslak durumdaki kayıtlar araştırmaya alınabilir.')
            rec.state = 'investigation'

    def action_sgk_pending(self):
        for rec in self:
            if rec.state != 'investigation':
                raise UserError('Önce araştırma aşamasına geçilmeli.')
            if rec.incident_type != 'accident':
                raise UserError('SGK bildirimi sadece iş kazaları için geçerlidir.')
            rec.state = 'sgk_pending'

    def action_close(self):
        for rec in self:
            if rec.state not in ('investigation', 'sgk_pending'):
                raise UserError('Kapatmak için önce araştırma aşamasında olmalı.')
            if rec.incident_type == 'accident' and rec.sgk_notification_required and not rec.sgk_notification_done:
                raise UserError('İş kazası kaydı kapatılmadan önce SGK bildirimi yapılmalıdır.')
            rec.state = 'closed'

    def action_reset_draft(self):
        for rec in self:
            if rec.state == 'closed':
                raise UserError('Kapalı kayıt taslağa alınamaz.')
            rec.state = 'draft'

    def action_create_capa(self):
        self.ensure_one()
        if self.capa_id:
            raise UserError('Bu kayıt için zaten bir DÖF mevcut: %s' % self.capa_id.name)
        type_label = dict(self._fields['incident_type'].selection).get(self.incident_type, '')
        capa = self.env['isg.capa'].create({
            'company_id': self.company_id.id,
            'workplace_id': self.workplace_id.id,
            'source': 'incident',
            'description': '%s — %s\nOlay: %s' % (
                type_label,
                self.name,
                self.description or '',
            ),
        })
        self.capa_id = capa.id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'isg.capa',
            'res_id': capa.id,
            'view_mode': 'form',
        }

    # -------------------------------------------------------------------------
    # ORM
    # -------------------------------------------------------------------------

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Yeni') == 'Yeni':
                vals['name'] = self.env['ir.sequence'].next_by_code('isg.incident') or 'Yeni'
        return super().create(vals_list)
