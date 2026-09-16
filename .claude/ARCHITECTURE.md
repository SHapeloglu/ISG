# ARCHITECTURE.md — ISG Platform 31 Modülü Mimari Özeti

## 🏗️ Modül Layerları

### Layer 1: Foundation
- **isg_base** (1/31): Security groups, mixin (uuid), IR extensions
- **isg_hr** (2/31): hr.employee extensions (workplace_id, sağlık history)
- **isg_security** (embedded in isg_base): ACL framework

### Layer 2: Configuration & Location
- **isg_site_ext** (3/31): isg.workplace model, org hierarchy
- **isg_location** (4/31): Work locations, tehlike sınıfları, hazard matrix
- **isg_machinery** (5/31): Equipment/machinery registry (PTW domain)

### Layer 3: Core Health & Safety
- **isg_health_basic** (6/31): Employee health exams, physician notes (encrypted), audit logs [NEW in S12]
- **isg_chemical** (7/31): Chemical/substance inventory, OEL/STEL tracking
- **isg_incident** (8/31): Incident registry, DÖF/CAPA workflows
- **isg_occupational_disease** (9/31): Disease tracking, risk matrix

### Layer 4: Training & Compliance
- **isg_training** (10/31, TODO): Regulation-driven training, incident→return trigger
- **isg_legislation** (11/31): Mevzuat registry, obligation applicability matrix

### Layer 5+: Reporting & Admin (12-31/31)
- PDF reports (F5-002, F5-003)
- Dashboard/analytics
- Misc integration & helper modules

**Total:** 31 production + 1 pending legal review = 32 planned

## 🔐 Security Model (isg_security)

### Groups
group_isg_manager — Full access (create/write/unlink)
group_isg_expert — Read+write, no delete (except audit)
group_isg_readonly — Read-only, field-level encryption masking

### ACL Pattern
CSV: `ir.model.access.csv`
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_MODEL_manager,MODEL_manager,model_MODEL,isg_security.group_isg_manager,1,1,1,1
access_MODEL_expert,MODEL_expert,model_MODEL,isg_security.group_isg_expert,1,1,1,0
access_MODEL_readonly,MODEL_readonly,model_MODEL,isg_security.group_isg_readonly,1,0,0,0

### Record Rules (Workplace-Based, TODO)
Planned: `res.users.workplace_ids` attribute → domain filtering

## 🔄 Data Flow (Seans 12 Snapshot)

### Employee Health Exam Lifecycle

Create exam (manager/expert)
→ physician_notes auto-encrypt (create hook)
→ audit log: "write" action, "(encrypted)" value
→ compute field shows decrypted (if authorized) OR "[ENCRYPTED - ...]"
Read exam
→ Compute field checks user role
→ Manager/Expert: decrypted text
→ Readonly: masked text
→ Audit logging: Not automatic for reads (can add)
Write/update exam
→ physician_notes re-encrypt (write hook)
→ audit log: before_value "(encrypted)", after_value "(encrypted)"
Delete exam
→ unlink hook logs deletion
→ audit log: action='delete', before_value has ID+employee info

### Encryption Storage
DB Table: isg_employee_health
physician_notes_encrypted (Char): Base64(Fernet(plaintext))

ORM Level: isg_employee_health
physician_notes (Text, compute): Decrypted value OR mask
_compute_physician_notes(): Read & decrypt
_inverse_physician_notes(): Encrypt & write to _encrypted

## 📊 Field Type Standards

| Type | Usage | Example |
|------|-------|---------|
| Many2one | Linked record | employee_id → hr.employee |
| Char | Short text, indexed | tehlike_kodu, uuid_code |
| Text | Long text, not searchable | physician_notes (compute) |
| Selection | Fixed choices | result (fit/unfit/conditional) |
| Integer | Whole numbers | heart_rate (bpm) |
| Float | Decimals | weight_kg, bmi |
| Date | Date only | examination_date |
| Datetime | Timestamp | accessed_date |
| One2many | Reverse link | Not used yet (prefer Many2one + domain) |
| Binary | Encrypted storage | Not used; use Base64 Char instead |

## 🔗 Dependency Graph (Seans 12)
odoo/addons/base
↓
isg_base ←─────────────────────────────────┐
↓ │
isg_hr ← isg_site_ext │
↓ ↓ │
isg_health_basic (encrypt+audit) ← all others
↑
isg_training (B-10, TODO)

Circular dependencies: None (unidirectional enforced)

## 🛠️ Common Patterns

### Compute + Inverse (Field Encryption)
```python
@api.depends('field_encrypted')
def _compute_field(self):
    for rec in self:
        rec.field = decrypt(rec.field_encrypted) if authorized(rec) else "[ENCRYPTED]"

def _inverse_field(self):
    for rec in self:
        if rec.field and rec.field != "[ENCRYPTED]":
            rec.field_encrypted = encrypt(rec.field)
```

### Create/Write Hooks (Audit Logging)
```python
@api.model_create_multi
def create(self, vals_list):
    # Pre-process: encrypt sensitive fields
    records = super().create(vals_list)
    # Post-process: log audit
    for rec in records:
        AuditModel.log_access(rec.id, 'write', ...)
    return records

def write(self, vals):
    # Pre-process: capture before values
    before = {rec.id: rec.sensitive_field for rec in self}
    result = super().write(vals)
    # Post-process: log diffs
    for rec in self:
        AuditModel.log_access(rec.id, 'write', 
            before_value=before[rec.id], 
            after_value=rec.sensitive_field)
    return result
```

### Audit Model
```python
class AuditModel(models.Model):
    employee_health_id = Many2one(...)
    action = Selection([('read','Read'),('write','Write'),('delete','Delete')])
    accessed_by_id = Many2one('res.users')
    sensitive_field = Char()
    before_value = Char(truncated)
    after_value = Char(truncated)
    
    def log_access(self, emp_health_id, action, **kwargs):
        return self.create({
            'employee_health_id': emp_health_id,
            'action': action,
            'accessed_by_id': self.env.user.id,
            **kwargs
        })
```

## 📈 Performance Considerations

- **Compute fields stored?** Yes (`store=True`) if searchable
- **Encryption overhead?** ~5-10ms per field (Fernet)
- **Audit logging?** Async optional (currently sync, not problematic for 100s exams)
- **DB indexes?** Standard on many2one/selection fields; consider on workplace_id for filtering

## 🚀 Scaling (Future)

1. Audit log archival: Move old records to separate table/index (1yr+ retention)
2. Encryption key rotation: Re-encrypt all fields on key change (scheduled job)
3. Multi-workspace: Record rules on `workplace_id` (res.users.workplace_ids attribute pending)
4. API: REST endpoints for external HSE Radar sync

