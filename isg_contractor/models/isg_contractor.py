# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class IsgContractor(models.Model):
    _name = 'isg.contractor'
    _description = 'Alt İşveren'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'isg.uuid.mixin']
    _order = 'name'

    name = fields.Char(
        string='Alt İşveren Adı', required=True, tracking=True,
    )
    partner_id = fields.Many2one(
        'res.partner', string='Firma / Kişi',
        domain="[('isg_party_type', 'in', ['subcontractor', 'other'])]",
    )

    # --- Asıl işveren tarafı ---
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri', required=True, tracking=True,
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )
    site_id = fields.Many2one(
        'isg.site', string='Çalışma Lokasyonu',
        domain="[('workplace_id', '=', workplace_id)]",
    )

    # --- Üst alt işveren (zincir yapısı) ---
    parent_contractor_id = fields.Many2one(
        'isg.contractor', string='Üst Alt İşveren',
        help='Bu alt işveren başka bir alt işverenin altındaysa seçin (zincir yapısı).',
        ondelete='restrict',
    )
    child_contractor_ids = fields.One2many(
        'isg.contractor', 'parent_contractor_id', string='Alt Taşeronlar',
    )
    contractor_level = fields.Integer(
        string='Zincir Seviyesi', compute='_compute_contractor_level', store=True,
    )

    # --- Sözleşme ---
    contract_start = fields.Date(string='Sözleşme Başlangıcı', tracking=True)
    contract_end = fields.Date(string='Sözleşme Bitişi', tracking=True)
    contract_subject = fields.Char(string='Sözleşme Konusu')
    contract_no = fields.Char(string='Sözleşme No')

    # --- Çalışan bildirimi ---
    employee_count_declared = fields.Integer(
        string='Bildirilen Çalışan Sayısı', tracking=True,
    )
    employee_count_actual = fields.Integer(
        string='Fiili Çalışan Sayısı',
        compute='_compute_employee_count_actual', store=True,
    )
    danger_class = fields.Selection(
        related='workplace_id.danger_class',
        string='Tehlike Sınıfı', readonly=True, store=True,
    )

    # --- Durum ---
    state = fields.Selection(
        selection=[
            ('draft', 'Taslak'),
            ('active', 'Aktif'),
            ('expired', 'Süresi Dolmuş'),
            ('terminated', 'Feshedildi'),
        ],
        string='Durum', default='draft', tracking=True,
    )

    # --- Belge matrisi özeti ---
    document_ids = fields.One2many(
        'isg.contractor.document', 'contractor_id', string='Belgeler',
    )
    document_count = fields.Integer(
        string='Belge Sayısı', compute='_compute_document_count',
    )
    missing_document_count = fields.Integer(
        string='Eksik Belge Sayısı', compute='_compute_document_count',
    )

    notes = fields.Text(string='Notlar')

    @api.depends('parent_contractor_id', 'parent_contractor_id.contractor_level')
    def _compute_contractor_level(self):
        for rec in self:
            if rec.parent_contractor_id:
                rec.contractor_level = rec.parent_contractor_id.contractor_level + 1
            else:
                rec.contractor_level = 1

    def _compute_employee_count_actual(self):
        # İleride isg_hr entegrasyonu ile doldurulacak
        for rec in self:
            rec.employee_count_actual = 0

    def _compute_document_count(self):
        for rec in self:
            rec.document_count = len(rec.document_ids)
            rec.missing_document_count = len(
                rec.document_ids.filtered(lambda d: d.state == 'missing')
            )

    def action_activate(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError(_('Sadece taslak kayıtlar aktive edilebilir.'))
            rec.state = 'active'

    def action_terminate(self):
        self.write({'state': 'terminated'})

    def action_view_documents(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'isg.contractor.document',
            'view_mode': 'list,form',
            'domain': [('contractor_id', '=', self.id)],
            'context': {'default_contractor_id': self.id},
            'target': 'current',
        }
