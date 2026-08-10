from odoo import models, fields, api
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class IsgRiskAssessment(models.Model):
    _name = 'isg.risk.assessment'
    _description = 'Risk Değerlendirmesi'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'assessment_date desc, id desc'

    name = fields.Char(
        string='Referans No',
        readonly=True,
        copy=False,
        default='Yeni',
    )
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
    danger_class = fields.Selection(
        related='workplace_id.danger_class',
        string='Tehlike Sınıfı',
        store=True,
    )
    assessment_date = fields.Date(
        string='Değerlendirme Tarihi',
        required=True,
        default=fields.Date.today,
        tracking=True,
    )
    method = fields.Selection([
        ('l_matrix', 'L Matrisi (5×5)'),
        ('fine_kinney', 'Fine-Kinney'),
    ], string='Puanlama Yöntemi', required=True, default='l_matrix', tracking=True)

    state = fields.Selection([
        ('draft', 'Taslak'),
        ('in_progress', 'Devam Ediyor'),
        ('done', 'Tamamlandı'),
        ('approved', 'Onaylandı'),
        ('renewal', 'Yenileme Gerekli'),
        ('archived', 'Arşiv'),
    ], string='Durum', default='draft', tracking=True)

    team_ids = fields.Many2many(
        'hr.employee',
        'isg_risk_assessment_team_rel',
        'assessment_id',
        'employee_id',
        string='Risk Değerlendirme Ekibi',
    )
    approver_id = fields.Many2one(
        'res.users',
        string='Onaylayan',
        tracking=True,
    )
    approval_date = fields.Date(string='Onay Tarihi', tracking=True)

    previous_assessment_id = fields.Many2one(
        'isg.risk.assessment',
        string='Önceki Risk Değerlendirmesi',
        domain="[('workplace_id', '=', workplace_id), ('state', '=', 'archived')]",
    )
    renewal_reason = fields.Selection([
        ('periodic', 'Periyodik'),
        ('accident', 'İş Kazası'),
        ('near_miss', 'Ramak Kala'),
        ('relocation', 'Taşınma'),
        ('new_equipment', 'Yeni Ekipman'),
        ('new_chemical', 'Yeni Kimyasal'),
        ('legislation', 'Mevzuat Değişikliği'),
        ('other', 'Diğer'),
    ], string='Yenileme Nedeni', tracking=True)

    next_review_date = fields.Date(
        string='Sonraki Yenileme Tarihi',
        compute='_compute_next_review_date',
        store=True,
        tracking=True,
    )

    risk_line_ids = fields.One2many(
        'isg.risk.line',
        'assessment_id',
        string='Tehlike / Risk Kayıtları',
    )

    document_id = fields.Many2one(
        'isg.document',
        string='İlgili Belge',
    )

    # Özet sayaçlar
    total_hazards = fields.Integer(
        string='Toplam Tehlike',
        compute='_compute_risk_summary',
        store=True,
    )
    high_risk_count = fields.Integer(
        string='Yüksek/Tolerans Gösterilemez Risk',
        compute='_compute_risk_summary',
        store=True,
    )
    open_capa_count = fields.Integer(
        string='Açık DÖF',
        compute='_compute_open_capa_count',
    )

    notes = fields.Html(string='Notlar')

    # -------------------------------------------------------------------------
    # Compute
    # -------------------------------------------------------------------------

    @api.depends('assessment_date', 'danger_class', 'state')
    def _compute_next_review_date(self):
        # Risk Değerlendirmesi Yönetmeliği md.12
        # Çok tehlikeli: en geç 2 yıl, Tehlikeli: 4 yıl, Az tehlikeli: 6 yıl
        period_map = {
            'very_dangerous': 2,
            'dangerous': 4,
            'less_dangerous': 6,
        }
        for rec in self:
            if rec.assessment_date and rec.danger_class:
                years = period_map.get(rec.danger_class, 6)
                rec.next_review_date = rec.assessment_date + relativedelta(years=years)
            else:
                rec.next_review_date = False

    @api.depends('risk_line_ids', 'risk_line_ids.risk_level')
    def _compute_risk_summary(self):
        for rec in self:
            lines = rec.risk_line_ids
            rec.total_hazards = len(lines)
            rec.high_risk_count = len(lines.filtered(
                lambda l: l.risk_level in ('high', 'intolerable')
            ))

    def _compute_open_capa_count(self):
        for rec in self:
            capas = self.env['isg.capa'].search([
                ('risk_assessment_id', '=', rec.id),
                ('state', 'not in', ('closed',)),
            ])
            rec.open_capa_count = len(capas)

    # -------------------------------------------------------------------------
    # Durum geçişleri
    # -------------------------------------------------------------------------

    def action_start(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError('Sadece Taslak durumdaki kayıtlar başlatılabilir.')
            rec.state = 'in_progress'

    def action_done(self):
        for rec in self:
            if rec.state != 'in_progress':
                raise UserError('Sadece Devam Ediyor durumdaki kayıtlar tamamlanabilir.')
            if not rec.risk_line_ids:
                raise UserError('En az bir tehlike/risk satırı girilmeden tamamlanamaz.')
            rec.state = 'done'

    def action_approve(self):
        for rec in self:
            if rec.state != 'done':
                raise UserError('Sadece Tamamlandı durumdaki kayıtlar onaylanabilir.')
            rec.write({
                'state': 'approved',
                'approver_id': self.env.user.id,
                'approval_date': fields.Date.today(),
            })

    def action_renewal(self):
        for rec in self:
            if rec.state != 'approved':
                raise UserError('Sadece Onaylandı durumdaki kayıtlar yenileme moduna alınabilir.')
            rec.state = 'renewal'

    def action_archive_assessment(self):
        for rec in self:
            rec.state = 'archived'

    def action_new_revision(self):
        """Mevcut değerlendirmeyi arşivle, yeni taslak aç."""
        self.ensure_one()
        if self.state not in ('approved', 'renewal'):
            raise UserError('Yeni revizyon sadece Onaylandı veya Yenileme Gerekli durumundan açılabilir.')
        self.action_archive_assessment()
        new = self.copy({
            'name': 'Yeni',
            'state': 'draft',
            'previous_assessment_id': self.id,
            'assessment_date': fields.Date.today(),
            'approval_date': False,
            'approver_id': False,
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'isg.risk.assessment',
            'res_id': new.id,
            'view_mode': 'form',
        }

    # -------------------------------------------------------------------------
    # ORM
    # -------------------------------------------------------------------------

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Yeni') == 'Yeni':
                vals['name'] = self.env['ir.sequence'].next_by_code('isg.risk.assessment') or 'Yeni'
        return super().create(vals_list)
