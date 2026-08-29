# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError


class IsgAudit(models.Model):
    _name = 'isg.audit'
    _description = 'Denetim Kaydı'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'audit_date desc, id desc'

    name = fields.Char(
        string='Denetim No', required=True, copy=False,
        readonly=True, default=lambda self: 'Yeni',
    )
    audit_type = fields.Selection(
        [
            ('internal', 'İç Denetim'),
            ('external', 'Dış Denetim'),
            ('inspection', 'Müfettiş Denetimi'),
            ('supplier', 'Tedarikçi/Alt İşveren Denetimi'),
        ],
        string='Denetim Türü', required=True, default='internal', tracking=True,
    )
    template_id = fields.Many2one(
        'isg.audit.template', string='Kontrol Listesi Şablonu',
        tracking=True,
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri', required=True, tracking=True,
    )
    site_id = fields.Many2one(
        'isg.site', string='Lokasyon',
        domain="[('workplace_id', '=', workplace_id)]",
    )
    contractor_id = fields.Many2one(
        'isg.contractor', string='Alt İşveren (Opsiyonel)',
        help='Eğer bu denetim bir alt işverenin denetimi ise burada seçin',
    )
    audit_date = fields.Date(
        string='Denetim Tarihi', required=True,
        default=fields.Date.context_today, tracking=True,
    )
    auditor_ids = fields.Many2many(
        'hr.employee', string='Denetçiler',
    )
    external_auditor = fields.Char(string='Dış Denetçi / Kurum')
    scope = fields.Text(string='Denetim Kapsamı')
    document_id = fields.Many2one('isg.document', string='Bağlı Belge')
    notes = fields.Text(string='Notlar')

    state = fields.Selection(
        [
            ('draft', 'Taslak'),
            ('in_progress', 'Devam Ediyor'),
            ('done', 'Tamamlandı'),
            ('closed', 'Kapalı'),
        ],
        string='Durum', default='draft', tracking=True, copy=False,
    )

    line_ids = fields.One2many(
        'isg.audit.line', 'audit_id', string='Bulgular',
    )
    total_questions = fields.Integer(
        string='Toplam Madde', compute='_compute_stats', store=True,
    )
    conformity_count = fields.Integer(
        string='Uygun', compute='_compute_stats', store=True,
    )
    nonconformity_count = fields.Integer(
        string='Uygunsuz', compute='_compute_stats', store=True,
    )
    open_capa_count = fields.Integer(
        string='Açık DÖF', compute='_compute_stats', store=True,
    )
    total_weight = fields.Integer(
        string='Toplam Ağırlık (Max Puan)', compute='_compute_scoring', store=True,
    )
    achieved_weight = fields.Integer(
        string='Elde Edilen Puan', compute='_compute_scoring', store=True,
    )
    compliance_percentage = fields.Float(
        string='Uyum %', compute='_compute_scoring', store=True,
    )
    compliance_status = fields.Selection(
        [
            ('red', 'RED - Uygunsuz'),
            ('yellow', 'YELLOW - Kısmi Uyum'),
            ('green', 'GREEN - Uyumlu'),
        ],
        string='Uyum Durumu', compute='_compute_scoring', store=True,
    )

    @api.depends('line_ids.result', 'line_ids.capa_id.state')
    def _compute_stats(self):
        for rec in self:
            lines = rec.line_ids
            rec.total_questions = len(lines)
            rec.conformity_count = len(lines.filtered(lambda l: l.result == 'ok'))
            rec.nonconformity_count = len(lines.filtered(lambda l: l.result == 'nok'))
            rec.open_capa_count = len(lines.filtered(
                lambda l: l.capa_id and l.capa_id.state not in ('closed', 'cancelled')
            ))

    @api.depends('line_ids.weight', 'line_ids.response_weight', 'line_ids.is_critical', 'line_ids.result')
    def _compute_scoring(self):
        for rec in self:
            lines = rec.line_ids
            rec.total_weight = sum(lines.mapped('weight'))
            rec.achieved_weight = sum(lines.mapped('response_weight'))
            
            if rec.total_weight > 0:
                rec.compliance_percentage = (rec.achieved_weight / rec.total_weight) * 100
            else:
                rec.compliance_percentage = 0
            
            # Kritik bulgu varsa RED, yoksa % bağlı
            has_critical_nok = any(l.is_critical and l.result == 'nok' for l in lines)
            if has_critical_nok:
                rec.compliance_status = 'red'
            elif rec.compliance_percentage >= 90:
                rec.compliance_status = 'green'
            elif rec.compliance_percentage >= 70:
                rec.compliance_status = 'yellow'
            else:
                rec.compliance_status = 'red'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Yeni') == 'Yeni':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'isg.audit'
                ) or 'Yeni'
        return super().create(vals_list)

    def action_load_template(self):
        """Şablondaki soruları denetim satırlarına yükle."""
        self.ensure_one()
        if not self.template_id:
            raise UserError('Önce bir kontrol listesi şablonu seçin.')
        if self.line_ids:
            raise UserError(
                'Denetimde zaten satırlar var. Şablon yüklemek için önce satırları silin.'
            )
        lines = []
        for q in self.template_id.question_ids:
            lines.append({
                'audit_id': self.id,
                'sequence': q.sequence,
                'question': q.question,
                'category': q.category,
                'legal_reference': q.legal_reference,
                'weight': q.weight,
                'is_critical': q.is_critical,
            })
        self.env['isg.audit.line'].create(lines)

    def action_start(self):
        self.write({'state': 'in_progress'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_close(self):
        for rec in self:
            if rec.open_capa_count > 0:
                raise UserError(
                    '%d açık DÖF kaydı var. Kapatmadan önce DÖF\'leri tamamlayın.' % rec.open_capa_count
                )
        self.write({'state': 'closed'})

    def action_reset_draft(self):
        self.write({'state': 'draft'})


class IsgAuditLine(models.Model):
    _name = 'isg.audit.line'
    _description = 'Denetim Bulgu Satırı'
    _order = 'sequence, id'

    audit_id = fields.Many2one(
        'isg.audit', string='Denetim',
        required=True, ondelete='cascade', index=True,
    )
    sequence = fields.Integer(string='Sıra', default=10)
    question = fields.Char(string='Kontrol Maddesi', required=True)
    category = fields.Selection(
        [
            ('risk', 'Risk Yönetimi'),
            ('emergency', 'Acil Durum'),
            ('ppe', 'KKD'),
            ('equipment', 'Ekipman / Makine'),
            ('chemical', 'Kimyasal'),
            ('training', 'Eğitim'),
            ('documentation', 'Dokümantasyon'),
            ('housekeeping', 'Düzen / Temizlik'),
            ('other', 'Diğer'),
        ],
        string='Kategori', default='other',
    )
    legal_reference = fields.Char(string='Yasal Dayanak')
    weight = fields.Integer(
        string='Ağırlık (Puan)', default=1,
        help='Template\'ten otomatik kopyalanır',
    )
    is_critical = fields.Boolean(string='Kritik Madde')
    result = fields.Selection(
        [
            ('ok', 'Uygun'),
            ('nok', 'Uygunsuz'),
            ('na', 'Uygulanamaz'),
            ('obs', 'Gözlem'),
        ],
        string='Sonuç',
    )
    response_weight = fields.Integer(
        string='Yanıt Puanı', compute='_compute_response_weight', store=True,
        help='Uygun ise weight, değilse 0',
    )
    finding = fields.Text(string='Bulgu / Açıklama')
    evidence = fields.Char(string='Kanıt / Referans')
    capa_id = fields.Many2one(
        'isg.capa', string='İlişkili DÖF', readonly=True, copy=False,
    )

    @api.depends('result', 'weight')
    def _compute_response_weight(self):
        for rec in self:
            if rec.result == 'ok':
                rec.response_weight = rec.weight
            else:
                rec.response_weight = 0

    def action_create_capa(self):
        self.ensure_one()
        if self.capa_id:
            raise UserError(
                'Bu satır için zaten bir DÖF mevcut: %s' % self.capa_id.name
            )
        if self.result != 'nok':
            raise UserError('DÖF sadece Uygunsuz sonuçlu maddeler için açılabilir.')
        capa = self.env['isg.capa'].create({
            'workplace_id': self.audit_id.workplace_id.id,
            'site_id': self.audit_id.site_id.id or False,
            'source': 'audit',
            'capa_type': 'corrective',
            'severity': 'critical' if self.is_critical else 'medium',
            'open_date': fields.Date.context_today(self),
            'description': 'Denetim Bulgusu — %s\nMadde: %s\nBulgu: %s' % (
                self.audit_id.name,
                self.question,
                self.finding or '',
            ),
        })
        self.capa_id = capa.id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'isg.capa',
            'res_id': capa.id,
            'view_mode': 'form',
        }

    @api.model_create_multi
    def create(self, vals_list):
        lines = super().create(vals_list)
        lines._auto_capa_for_critical()
        return lines

    def write(self, vals):
        res = super().write(vals)
        if 'result' in vals:
            self._auto_capa_for_critical()
        return res

    def _auto_capa_for_critical(self):
        """Kritik madde uygunsuz işaretlenince otomatik DÖF aç."""
        for rec in self:
            if rec.is_critical and rec.result == 'nok' and not rec.capa_id:
                rec.action_create_capa()
