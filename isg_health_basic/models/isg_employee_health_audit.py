# -*- coding: utf-8 -*-
from odoo import models, fields, api


class IsgEmployeeHealthAudit(models.Model):
    _name = 'isg.employee.health.audit'
    _description = 'Çalışan Sağlık Muayenesi Denetim Günlüğü'
    _order = 'accessed_date desc'

    # ─── İlişkiler ──────────────────────────────────────────
    employee_health_id = fields.Many2one(
        'isg.employee.health', string='Sağlık Muayenesi', required=True, ondelete='cascade',
    )

    # ─── Denetim Bilgileri ──────────────────────────────────
    action = fields.Selection([
        ('read', 'Okuma'),
        ('write', 'Yazma'),
        ('delete', 'Silme'),
    ], string='İşlem', required=True)

    accessed_by_id = fields.Many2one(
        'res.users', string='Erişim Yapan', required=True, readonly=True, ondelete='restrict',
    )

    accessed_date = fields.Datetime(
        string='Erişim Tarihi', required=True, readonly=True, default=fields.Datetime.now,
    )

    # ─── Değişim Kaydı ──────────────────────────────────────
    sensitive_field = fields.Char(
        string='Duyarlı Alan',
        help='physician_notes veya tüm alanlar',
    )

    before_value = fields.Char(
        string='Önceki Değer (Truncated)',
        help='Max 255 karakter, şifreleme durumunda "(encrypted)"',
    )

    after_value = fields.Char(
        string='Sonraki Değer (Truncated)',
        help='Max 255 karakter, şifreleme durumunda "(encrypted)"',
    )

    # ─── Sistem Alanları ────────────────────────────────────
    notes = fields.Text(string='Notlar', help='İşlem hakkında açıklamalar')

    @staticmethod
    def _truncate_value(value, max_length=255):
        """Değeri truncate et (encrypted varsa "(encrypted)" yaz)"""
        if not value:
            return False
        if isinstance(value, str):
            value_str = value
            if len(value_str) > max_length:
                return value_str[:max_length] + "..."
            return value_str
        return str(value)[:max_length]

    def log_access(self, employee_health_id, action, sensitive_field=None, before_value=None, after_value=None, notes=None):
        """
        Audit log kaydı oluştur (helper method)
        
        Örnek:
            audit_model = self.env['isg.employee.health.audit']
            audit_model.log_access(
                health_record.id, 'write',
                sensitive_field='physician_notes',
                before_value=old_notes,
                after_value=new_notes,
                notes='Hekim tarafından güncellendi'
            )
        """
        return self.create({
            'employee_health_id': employee_health_id,
            'action': action,
            'accessed_by_id': self.env.user.id,
            'accessed_date': fields.Datetime.now(),
            'sensitive_field': sensitive_field,
            'before_value': self._truncate_value(before_value),
            'after_value': self._truncate_value(after_value),
            'notes': notes,
        })
