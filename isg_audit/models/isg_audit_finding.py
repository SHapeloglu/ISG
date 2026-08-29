# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError


class IsgAuditFinding(models.Model):
    _name = 'isg.audit.finding'
    _description = 'Denetim Bulgusu'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc, id desc'

    name = fields.Char(
        string='Bulgu No', required=True, copy=False,
        readonly=True, default=lambda self: 'Yeni',
    )
    audit_id = fields.Many2one(
        'isg.audit', string='Denetim', required=True,
        ondelete='cascade', index=True, tracking=True,
    )
    audit_line_id = fields.Many2one(
        'isg.audit.line', string='Denetim Satırı',
        ondelete='set null', help='Uygunsuz satırdan geliyor',
    )
    
    # Bulgu Detayı
    finding_type = fields.Selection(
        [
            ('observation', 'Gözlem'),
            ('non_conformity', 'Uygunsuzluk'),
            ('major', 'Majör'),
            ('critical', 'Kritik'),
        ],
        string='Bulgu Türü', default='non_conformity', required=True, tracking=True,
    )
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
    question = fields.Char(string='Kontrol Maddesi')
    finding_description = fields.Text(string='Bulgu Açıklaması', required=True)
    root_cause = fields.Text(
        string='Kök Neden Analizi (Ön)',
        help='Ön kök neden analizi',
    )
    
    # Tekrarlanan Bulgu
    repeat_count = fields.Integer(
        string='Kaç Kez Tekrar Etmiş', default=0,
        help='Önceki denetimlerden kaç kez aynı bulgu vardı',
    )
    escalation_level = fields.Integer(
        string='Eskalasyon Seviyesi', compute='_compute_escalation_level',
        store=True, help='repeat_count >= 3 ise level 2',
    )
    previous_finding_ids = fields.Many2many(
        'isg.audit.finding', 'audit_finding_relation', 'finding_id', 'previous_finding_id',
        string='Önceki Benzer Bulgular',
        help='Aynı konuda daha önce kaydedilen bulgular',
    )
    
    # Sorumlu & Aksiyon
    responsible_person_id = fields.Many2one(
        'hr.employee', string='Sorumlu Kişi', tracking=True,
    )
    target_completion_date = fields.Date(
        string='Hedef Tamamlanma Tarihi', tracking=True,
    )
    
    # DÖF Bağlantısı
    capa_id = fields.Many2one(
        'isg.capa', string='İlişkili DÖF', readonly=True, copy=False,
    )
    is_capa_created = fields.Boolean(
        string='DÖF Oluşturuldu', compute='_compute_capa_created', store=True,
    )
    
    # Kanıt
    evidence_text = fields.Text(string='Kanıt / Gözlem Notları')
    evidence_attachment_ids = fields.Many2many(
        'ir.attachment', 'audit_finding_attachment_rel', 'finding_id', 'attachment_id',
        string='Kanıt Dosyaları (Fotoğraf, Belge)',
    )
    
    # Durum
    state = fields.Selection(
        [
            ('open', 'Açık'),
            ('in_review', 'İnceleniyor'),
            ('resolved', 'Çözüldü'),
            ('verified', 'Doğrulandı'),
            ('closed', 'Kapalı'),
        ],
        string='Durum', default='open', tracking=True, copy=False,
    )
    
    # İşyeri Context
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri',
        related='audit_id.workplace_id', store=True, readonly=True,
    )
    site_id = fields.Many2one(
        'isg.site', string='Lokasyon',
        related='audit_id.site_id', store=True, readonly=True,
    )

    @api.depends('repeat_count')
    def _compute_escalation_level(self):
        for rec in self:
            if rec.repeat_count >= 3:
                rec.escalation_level = 2
            elif rec.repeat_count >= 1:
                rec.escalation_level = 1
            else:
                rec.escalation_level = 0

    @api.depends('capa_id')
    def _compute_capa_created(self):
        for rec in self:
            rec.is_capa_created = bool(rec.capa_id)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Yeni') == 'Yeni':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'isg.audit.finding'
                ) or 'Yeni'
        return super().create(vals_list)

    def action_create_capa(self):
        """Bulgadan DÖF oluştur."""
        self.ensure_one()
        if self.capa_id:
            raise UserError(
                'Bu bulgu için zaten bir DÖF mevcut: %s' % self.capa_id.name
            )
        
        severity_map = {
            'observation': 'low',
            'non_conformity': 'medium',
            'major': 'high',
            'critical': 'critical',
        }
        
        capa = self.env['isg.capa'].create({
            'workplace_id': self.audit_id.workplace_id.id,
            'site_id': self.audit_id.site_id.id or False,
            'source': 'audit',
            'capa_type': 'corrective',
            'severity': severity_map.get(self.finding_type, 'medium'),
            'open_date': fields.Date.context_today(self),
            'description': 'Denetim Bulgusu — %s\nBulgu No: %s\nDenetim: %s\nAçıklama: %s' % (
                self.category,
                self.name,
                self.audit_id.name,
                self.finding_description,
            ),
            'assigned_to_id': self.responsible_person_id.id if self.responsible_person_id else False,
        })
        self.capa_id = capa.id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'isg.capa',
            'res_id': capa.id,
            'view_mode': 'form',
        }

    def action_mark_resolved(self):
        """Bulguyu Çözüldü olarak işaretle."""
        self.write({'state': 'resolved'})

    def action_verify(self):
        """Çözüm doğrulandı."""
        self.write({'state': 'verified'})

    def action_close(self):
        """Bulguyu kapat."""
        self.write({'state': 'closed'})

    def action_reopen(self):
        """Bulguyu tekrar aç."""
        self.write({'state': 'open'})
