# CONTEXT_FOR_CLAUDE.md — Hızlı Seans Başlangıç Snapshot (Seans 12 Sonrası)

**Geçerlilik:** Sep 16, 2026  
**HEAD:** 39a27e4  
**Modüller:** 31/32 kurulu (%97)

## 🏁 Hızlı Başlangıç (Yeni Seans)

### 1. VPS Doğrulama (5 dakika)
```bash
cd /opt/odoo/isg_addons
git log --oneline -3
sudo -u postgres psql -d isg -c "SELECT COUNT(*) FROM ir_module_module WHERE state='installed';"
sudo systemctl status odoo18-isg.service | head -5
```

### 2. Dosyaları Oku (3 dakika)
```bash
cat .claude/SESSION.md        # Seans 12 neler yaptı
cat .claude/TASKS.md          # Next tasks
cat .claude/CLAUDE.md         # Kurallar
```

### 3. Seans Başla (Ne yapılacak?)
**Seans 13 Plan:** isg_training B-10 (April 2, 2026 regulation training module)

---

## 📦 Seans 12 Çıktısı (Snapshot)

### Yeni Dosyalar
isg_health_basic/models/encryption_helper.py
isg_health_basic/models/isg_employee_health_audit.py
isg_health_basic/views/isg_employee_health_audit_views.xml

### Değiştirilen Dosyalar
isg_health_basic/models/isg_employee_health.py (compute/inverse/hooks)
isg_health_basic/models/init.py (added audit import)
isg_health_basic/security/ir.model.access.csv (added 3 audit ACL)
isg_health_basic/manifest.py (added cryptography dep + audit views)

### DB Tablosu
- `isg_employee_health_audit` ✅ (13 column, fully functional)

### Dependencies
- `cryptography>=41.0.0` ✅
- `packaging` ✅

### Git History
39a27e4 (HEAD) fix(isg_health_basic): Field parameter ve XML reference düzeltmeleri
35fdc77 feat(isg_health_basic): Encryption ve audit log sistemi eklendi
3cce1f6 SEANS 12 PLAN: ...

---

## 🔑 Seans 12 Teknolojisi

### Encryption
- **Library:** Fernet (symmetric, AES-128)
- **Key source:** `ISG_ENCRYPTION_KEY` env var (fallback: ~/.isg_encryption_key → generated)
- **Storage:** Base64-encoded ciphertext in `physician_notes_encrypted` Char field
- **Helper:** `encryption_helper.py` singleton

### Audit Log
- **Model:** `isg.employee.health.audit`
- **Actions:** read/write/delete
- **Triggers:** create() / write() / unlink() hooks
- **Storage:** Plaintext (not encrypted; separate security policy)

### Field Pattern
```python
# Storage (hidden)
physician_notes_encrypted = fields.Char(readonly=True)

# Display (compute + inverse)
physician_notes = fields.Text(
    compute='_compute_physician_notes',
    inverse='_inverse_physician_notes'
)

# Compute: Decrypt + role-based masking
@api.depends('physician_notes_encrypted')
def _compute_physician_notes(self):
    for rec in self:
        if user.has_group('manager') or user.has_group('expert'):
            rec.physician_notes = decrypt(rec.physician_notes_encrypted)
        else:
            rec.physician_notes = "[ENCRYPTED - Yetkiniz yok]"

# Inverse: Encrypt on write
def _inverse_physician_notes(self):
    for rec in self:
        if rec.physician_notes and rec.physician_notes != "[ENCRYPTED...]":
            rec.physician_notes_encrypted = encrypt(rec.physician_notes)
```

---

## ⚠️ Bilinen Sorunlar

### Açık
- [ ] `res.users.workplace_ids` henüz tanımlanmadı (record rules için)
- [ ] Encryption key rotation script yok
- [ ] Audit log archival policy yok

### Çözülen (Seans 12)
- [x] `invisible=True` Python field'da → kaldırıldı
- [x] XML ref scope error → full path eklendi
- [x] `packaging` missing → kuruldu
- [x] Table creation failed → fixed and verified

---

## 📊 İstatistikler

| Metric | Value |
|--------|-------|
| Total Modules | 31/32 (97%) |
| Code Lines (S12) | +340 lines |
| DB Tables (new) | 1 (audit) |
| Git Commits (S12) | 2 |
| Estimated Dev Hours | 3 |
| Estimated Next (S13) | 2-3 days (training B-10) |

---

## 🚀 Kontrol Listesi (Seans Başında)

- [ ] VPS bağlantısı OK
- [ ] git log HEAD: 39a27e4
- [ ] psql module count: 31
- [ ] systemctl status: running
- [ ] .claude/ dosyalar güncel
- [ ] GitHub push successful
- [ ] Seans 13 plan okudun mu?

