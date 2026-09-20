# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import AccessError
from .encryption_helper import get_encryption_helper


class IsgEmployeeHealth(models.Model):
    _name = 'isg.employee.health'
    _description = 'Çalışan Sağlık Muayenesi (KVKK Uyumlu)'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'examination_date desc'

    # ─── Temel Referanslar ───────────────────────────────────
    employee_id = fields.Many2one(
        'hr.employee', string='Çalışan', required=True, ondelete='restrict', tracking=True,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='Çalışma Yeri', compute='_compute_workplace_id',
        store=True, readonly=True,
    )

    # ─── Muayene Bilgileri ───────────────────────────────────
    examination_date = fields.Date(
        string='Muayene Tarihi', required=True, default=fields.Date.context_today, tracking=True,
    )
    examiner_id = fields.Many2one(
        'res.partner', string='Muayene Yapan Hekim', required=True, tracking=True,
        domain=[('is_occupational_physician', '=', True)],
    )

    # ─── Fiziksel Ölçümler ───────────────────────────────────
    systolic_bp = fields.Integer(string='Sistolik Basınç (mmHg)')
    diastolic_bp = fields.Integer(string='Diastolik Basınç (mmHg)')
    heart_rate = fields.Integer(string='Kalp Atışı (bpm)')
    weight_kg = fields.Float(string='Ağırlık (kg)')
    height_cm = fields.Integer(string='Boy (cm)')
    bmi = fields.Float(string='BMI', compute='_compute_bmi', store=True)

    # ─── Muayene Sonucu ─────────────────────────────────────
    result = fields.Selection([
        ('fit', 'Uygun'),
        ('unfit', 'Uygun Değil'),
        ('conditional', 'Şartlı Uygun'),
    ], string='Muayene Sonucu', required=True, tracking=True)

    restrictions = fields.Text(
        string='Çalışma Kısıtlamaları',
        help='Eğer "Şartlı Uygun" ise, işyerinde uygulanacak kısıtlamalar',
    )

    # ─── Hekim Notları (KVKK: Şifrelenmiş) ───────────────────
    # Storage: encrypted (hidden, readonly)
    physician_notes_encrypted = fields.Char(
        string='Hekim Notları (Encrypted)', readonly=True,
    )
    
    # Display: compute + role-based masking
    physician_notes = fields.Text(
        string='Hekim Notları',
        compute='_compute_physician_notes',
        inverse='_inverse_physician_notes',
        help='Sadece hekim ve yönetici tarafından görülebilir',
    )

    # ─── Sistem Alanları ────────────────────────────────────
    created_date = fields.Datetime(string='Oluşturma Tarihi', readonly=True)
    created_by_id = fields.Many2one('res.users', string='Oluşturan', readonly=True)

    # ─────────────────────────────────────────────────────────
    # COMPUTE & INVERSE METHODS
    # ─────────────────────────────────────────────────────────

    @api.depends('physician_notes_encrypted')
    def _compute_physician_notes(self):
        """Role-based masking: authorized users görsün, diğerleri 'ENCRYPTED'"""
        helper = get_encryption_helper()
        for rec in self:
            # Authorized roles: manager, expert (isg_security.group_isg_manager veya group_isg_expert)
            user = self.env.user
            is_manager = user.has_group('isg_security.group_isg_manager')
            is_expert = user.has_group('isg_security.group_isg_expert')
            
            if is_manager or is_expert:
                # Decrypt ve göster
                if rec.physician_notes_encrypted:
                    rec.physician_notes = helper.decrypt(rec.physician_notes_encrypted)
                else:
                    rec.physician_notes = False
            else:
                # Readonly users ve diğerleri
                rec.physician_notes = "[ENCRYPTED - Yetkiniz yok]"

    def _inverse_physician_notes(self):
        """physician_notes'e yazılan değeri encrypt edip _encrypted'a yaz"""
        helper = get_encryption_helper()
        for rec in self:
            if rec.physician_notes and rec.physician_notes != "[ENCRYPTED - Yetkiniz yok]":
                encrypted = helper.encrypt(rec.physician_notes)
                rec.physician_notes_encrypted = encrypted

    @api.depends('weight_kg', 'height_cm')
    def _compute_bmi(self):
        for rec in self:
            if rec.weight_kg and rec.height_cm:
                height_m = rec.height_cm / 100.0
                rec.bmi = rec.weight_kg / (height_m ** 2)
            else:
                rec.bmi = 0.0

    @api.depends('employee_id')
    def _compute_workplace_id(self):
        for rec in self:
            if rec.employee_id and hasattr(rec.employee_id, 'workplace_id'):
                rec.workplace_id = rec.employee_id.workplace_id
            else:
                rec.workplace_id = False

    # ─────────────────────────────────────────────────────────
    # CREATE & WRITE & UNLINK OVERRIDES (with Audit Logging)
    # ─────────────────────────────────────────────────────────

    @api.model_create_multi
    def create(self, vals_list):
        helper = get_encryption_helper()
        for vals in vals_list:
            vals['created_date'] = fields.Datetime.now()
            vals['created_by_id'] = self.env.user.id
            
            # physician_notes'i şifrele
            if 'physician_notes' in vals and vals['physician_notes']:
                encrypted = helper.encrypt(vals['physician_notes'])
                vals['physician_notes_encrypted'] = encrypted
                del vals['physician_notes']  # compute field'ı db'ye yazma
        
        records = super().create(vals_list)
        
        # Audit logging: CREATE
        audit_model = self.env['isg.employee.health.audit']
        for rec in records:
            audit_model.log_access(
                rec.id, 'write',
                sensitive_field='physician_notes',
                before_value=None,
                after_value='(encrypted)' if rec.physician_notes_encrypted else None,
                notes='Yeni muayene kaydı oluşturuldu'
            )
        
        return records

    def write(self, vals):
        helper = get_encryption_helper()
        audit_model = self.env['isg.employee.health.audit']
        
        # physician_notes'i şifrele ve audit log'la
        for rec in self:
            if 'physician_notes' in vals and vals['physician_notes']:
                encrypted = helper.encrypt(vals['physician_notes'])
                vals['physician_notes_encrypted'] = encrypted
                
                # Audit: before değer
                before_value = '(encrypted)' if rec.physician_notes_encrypted else None
                after_value = '(encrypted)'
                
                audit_model.log_access(
                    rec.id, 'write',
                    sensitive_field='physician_notes',
                    before_value=before_value,
                    after_value=after_value,
                    notes='Hekim notları güncellendi'
                )
                
                del vals['physician_notes']  # compute field'ı db'ye yazma
        
        return super().write(vals)

    def unlink(self):
        """Silme öncesi audit log kaydet"""
        audit_model = self.env['isg.employee.health.audit']
        
        for rec in self:
            audit_model.log_access(
                rec.id, 'delete',
                sensitive_field='all',
                before_value=f"ID: {rec.id}, Employee: {rec.employee_id.name}",
                after_value=None,
                notes='Muayene kaydı silindi'
            )
        
        return super().unlink()
