# SEANS 12 — isg_health_basic Encryption & Audit Log Sistemi (16 Eylül 2026)

## Hedef & Tamamlanan İş
**Amaç:** isg_health_basic modülüne KVKK-uyumlu şifreleme ve audit log sistemi eklemek.

### ✅ Tamamlanan (3/3)

#### 1. Encryption Helper Class
- `encryption_helper.py`: Fernet symmetric encryption implementation
- Key management: ISG_ENCRYPTION_KEY env var → ~/.isg_encryption_key → fallback Fernet.generate_key()
- `_encrypt(plaintext)` / `decrypt(ciphertext)` methods
- Singleton pattern: `get_encryption_helper()`
- Base64 encoding for storage

#### 2. Field-Level Encryption (physician_notes)
- Storage split: `physician_notes_encrypted` (Char, hidden) ← real storage
- Display: `physician_notes` (Text, compute + inverse)
- Role-based masking:
  - Manager/Expert: Decrypted value görürler
  - Readonly/Others: "[ENCRYPTED - Yetkiniz yok]"
- Create/write hooks: Otomatik encrypt before save
- Fixed: `invisible=True` parametresi Python field'dan kaldırıldı (XML-only)

#### 3. Audit Log Sistemi
- Model: `isg.employee.health.audit` (13 column, fully created)
  - `employee_health_id` (Many2one)
  - `action` (read/write/delete selection)
  - `accessed_by_id` (res.users, auto-populated)
  - `accessed_date` (Datetime, auto-populated)
  - `sensitive_field` (physician_notes / all)
  - `before_value`, `after_value` (truncated to 255 chars, encrypted masked)
  - `notes` (freeform)
- Create/write/unlink hooks: Full tracking
  - Create: Logs "write" action + "(encrypted)" placeholder
  - Write: Logs before/after values (or "(encrypted)")
  - Unlink: Logs delete action before removal
- `log_access()` helper method for manual logging
- ACL: Manager (1,1,1,1), Expert (1,1,1,0), Readonly (1,0,0,0)
- Views: List (5 field), Form (tabbed), Search (3 filters: Okuma/Yazma/Silme)

### 📊 Durum
- **Modül:** isg_health_basic (still counted in 31/32 total)
- **Tablo:** isg_employee_health_audit başarıyla oluşturuldu
- **Dependencies:** cryptography>=41.0.0, packaging (both installed)
- **Git commits:** 35fdc77 (feat), 39a27e4 (fix)

## Teknik Notlar

### Odoo 18 Kuralları (Yenilenenler)
- `invisible=True` sadece XML view'lerde geçerli; Python field definition'da invalid parameter error
- XML ref'lerde full module path kullan: `ref="module.record_id"` (module omit edilirse scope error)
- Record order matters: search/filter views action'dan önce tanımlanmalı (ref resolution için)

### Açık Konular
- `res.users.workplace_ids` attribute henüz tanımlanmadı → record rule'lar TODO
- Encryption key format: Base64 Fernet key; fallback dev-only (üretimde env var required)
- Audit log'lar şifreli değil, sadece erişim kaydı (ayrı security policy gerekli KVKK compliance için)

### Dosya Değişiklikleri
isg_health_basic/
├── models/
│ ├── encryption_helper.py (NEW)
│ ├── isg_employee_health_audit.py (NEW)
│ ├── isg_employee_health.py (MODIFIED: compute/inverse/hooks)
│ └── init.py (MODIFIED: added audit import)
├── views/
│ └── isg_employee_health_audit_views.xml (NEW)
├── security/
│ └── ir.model.access.csv (MODIFIED: added 3 audit ACL rows)
└── manifest.py (MODIFIED: cryptography dep, audit views)

## Seans 11→12 Delta
- Seans 11: Scaffold hazır (model, 2 view, ACL)
- Seans 12: Encryption + audit log tüm implantasyonu tamamlandı
- Total dev time: ~3 saat (estimate 3-3.5, başında hata çözümleri ile)

## Sonraki Seans (13)
- **Başlangıç:** isg_training B-10 (April 2, 2026 Regulation Compliance)
  - Estimated: 2-3 days
  - Scope: Full training module + incident→return training trigger
- **Ya da:** isg_health_basic enhancements (encryption key rotation, audit retention policy)
  - Estimated: 1-1.5 days

Bütçe bloke: Faz 1 ₺300K onayı bekleniyor.
