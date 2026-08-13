# -*- coding: utf-8 -*-
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class IsgRiskAssessment(models.Model):
    _name = 'isg.risk.assessment'
    _description = 'Risk Değerlendirmesi'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'assessment_date desc, id desc'

    name = fields.Char(
        string='Belge No', required=True, copy=False,
        readonly=True, default=lambda self: 'Yeni',
    )

    # --- İşyeri / Lokasyon ---
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri', required=True,
        tracking=True,
    )
    site_id = fields.Many2one(
        'isg.site', string='Lokasyon', required=True,
        domain="[('workplace_id', '=', workplace_id)]",
        tracking=True,
    )
    danger_class = fields.Selection(
        [('low', 'Az Tehlikeli'), ('medium', 'Tehlikeli'), ('high', 'Çok Tehlikeli')],
        string='Tehlike Sınıfı',
        compute='_compute_danger_class', store=True,
    )

    # --- Yöntem ve Ekip ---
    method = fields.Selection(
        [('l_matrix', 'L Matrisi (5x5)'), ('fine_kinney', 'Fine-Kinney')],
        string='Değerlendirme Yöntemi', required=True, default='l_matrix',
        tracking=True,
    )
    team_ids = fields.Many2many(
        'hr.employee', string='Risk Değerlendirme Ekibi',
    )
    assessment_date = fields.Date(
        string='Değerlendirme Tarihi', required=True,
        default=fields.Date.context_today, tracking=True,
    )

    # --- Yenileme ---
    next_review_date = fields.Date(
        string='Yenileme Tarihi', compute='_compute_next_review_date',
        store=True, tracking=True,
    )
    renewal_reason = fields.Selection(
        [
            ('period', 'Periyot Dolması'),
            ('accident', 'İş Kazası'),
            ('relocation', 'Taşınma'),
            ('new_equipment', 'Yeni Ekipman/Teknoloji'),
            ('legal_change', 'Yasal Değişiklik'),
            ('other', 'Diğer'),
        ],
        string='Yenileme Nedeni',
    )
    previous_assessment_id = fields.Many2one(
        'isg.risk.assessment', string='Önceki Değerlendirme',
        readonly=True, copy=False,
    )

    # --- Onay ---
    approver_id = fields.Many2one(
        'res.users', string='Onaylayan', readonly=True, copy=False,
    )
    approval_date = fields.Date(
        string='Onay Tarihi', readonly=True, copy=False,
    )
    document_id = fields.Many2one(
        'isg.document', string='Bağlı Belge',
    )
    notes = fields.Text(string='Notlar')

    # --- Durum ---
    state = fields.Selection(
        [
            ('draft', 'Taslak'),
            ('in_progress', 'Devam Ediyor'),
            ('done', 'Tamamlandı'),
            ('approved', 'Onaylandı'),
            ('renewal', 'Yenileme Gerekli'),
            ('archived', 'Arşivlendi'),
        ],
        string='Durum', default='draft', tracking=True, copy=False,
    )

    risk_line_ids = fields.One2many(
        'isg.risk.line', 'assessment_id', string='Tehlike/Risk Kayıtları',
    )
    total_hazards = fields.Integer(
        string='Toplam Tehlike Sayısı', compute='_compute_line_stats', store=True,
    )
    high_risk_count = fields.Integer(
        string='Yüksek Risk Sayısı', compute='_compute_line_stats', store=True,
    )
    open_capa_count = fields.Integer(
        string='Açık DÖF Sayısı', compute='_compute_line_stats', store=True,
    )

    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )

    @api.depends('risk_line_ids.risk_level', 'risk_line_ids.capa_id.state')
    def _compute_line_stats(self):
        for rec in self:
            lines = rec.risk_line_ids
            rec.total_hazards = len(lines)
            rec.high_risk_count = len(lines.filtered(
                lambda l: l.risk_level in ('high', 'intolerable')
            ))
            rec.open_capa_count = len(lines.filtered(
                lambda l: l.capa_id and l.capa_id.state not in ('closed', 'cancelled')
            ))

    @api.depends('site_id.danger_class', 'workplace_id.danger_class')
    def _compute_danger_class(self):
        for rec in self:
            rec.danger_class = (
                rec.site_id.danger_class or rec.workplace_id.danger_class
            )

    @api.depends('danger_class', 'assessment_date')
    def _compute_next_review_date(self):
        """
        Risk Değerlendirmesi Yönetmeliği — tehlike sınıfına göre
        yenileme periyodu:
        Az tehlikeli : +6 yıl
        Tehlikeli    : +4 yıl
        Çok tehlikeli: +2 yıl
        """
        yil = {'low': 6, 'medium': 4, 'high': 2}
        for rec in self:
            if rec.assessment_date and rec.danger_class:
                rec.next_review_date = rec.assessment_date + relativedelta(
                    years=yil.get(rec.danger_class, 4)
                )
            else:
                rec.next_review_date = False

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Yeni') == 'Yeni':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'isg.risk.assessment'
                ) or 'Yeni'
        return super().create(vals_list)

    def action_start(self):
        self.write({'state': 'in_progress'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_approve(self):
        self.write({
            'state': 'approved',
            'approver_id': self.env.user.id,
            'approval_date': fields.Date.context_today(self),
        })

    def action_reset_draft(self):
        self.write({'state': 'draft'})

    def action_renewal(self):
        """Yenileme periyodu doldu veya yenileme koşulu oluştu (kaza,
        taşınma, yeni ekipman vb.) — kayıt yenileme bekliyor olarak işaretlenir."""
        self.write({'state': 'renewal'})

    def action_archive_assessment(self):
        self.write({'state': 'archived'})

    def action_new_revision(self):
        """Onaylı/yenileme bekleyen bir değerlendirmeden, önceki kayda
        bağlı yeni bir taslak revizyon oluşturur ve formunu açar."""
        self.ensure_one()
        new_vals = {
            'workplace_id': self.workplace_id.id,
            'site_id': self.site_id.id,
            'method': self.method,
            'team_ids': [(6, 0, self.team_ids.ids)],
            'previous_assessment_id': self.id,
            'company_id': self.company_id.id,
        }
        new_assessment = self.create(new_vals)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'isg.risk.assessment',
            'res_id': new_assessment.id,
            'view_mode': 'form',
        }
