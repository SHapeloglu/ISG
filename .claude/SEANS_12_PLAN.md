# SEANS 12 PLAN — isg_health_basic Enhancements

## Hedef
isg_health_basic modülüne KVKK-uyumlu şifreleme ve audit log sistemi eklemek

## Teknik Tasarım

### 1. Field-Level Encryption (physician_notes)
**Kütüphane:** cryptography >= 41.0.0 (Fernet symmetric encryption)

**Implantasyon:**
- `_encrypt(plaintext)` ve `_decrypt(ciphertext)` helper methods
- physician_notes computed field değil, real field
- Encryption key: Django SECRET_KEY veya custom `ISG_ENCRYPTION_KEY` env var
- Before save: encrypt
- After load: decrypt (sadece authorized roles için)

**Access Control:**
Manager/Expert: sees decrypted value
Readonly/Others: sees "ENCRYPTED"

### 2. Audit Log Sistemi
**Model:** `isg.employee.health.audit`
- `employee_health_id` (Many2one)
- `action` (read/write/delete)
- `accessed_by_id` (res.users)
- `accessed_date` (Datetime, auto)
- `sensitive_field` (physician_notes / all fields)
- `before_value` / `after_value` (Char, truncated)

**Trigger:** Odoo's `@api.model_create_multi`, `write()`, `unlink()`

### 3. Record Rules (TODO)
Henüz implementasyon yok — `res.users.workplace_ids` attribute'i tanımlanırsa devam edilecek

## Adım Adım Iş Akışı

### Adım 1: Encryption Helper Class (30 min)
- Fernet setup
- `_encrypt()`, `_decrypt()` methods
- Test: basit encrypt/decrypt

### Adım 2: physician_notes Field Encryption (45 min)
- `physician_notes` storage format değiştir (LargeBinary?)
- Property/compute pattern ile transparent decryption
- Role-based masking

### Adım 3: Audit Log Model (45 min)
- `isg.employee.health.audit` scaffold
- ACL
- Basic views

### Adım 4: Create/Write/Unlink Hooks (30 min)
- `create()` override
- `write()` override
- `unlink()` override
- Audit record oluşturma

### Adım 5: Test & Commit (30 min)
- Manual test (Web UI'da encrypt/decrypt test)
- Git commit

**Tahmini Süre:** 3-3.5 saat

## Önemli Notlar
- encryption_key'i `.env` veya hardcode'dan oku (üretimde SECRET_KEY)
- Audit log'lar encrypted değil, sadece erişim kaydı tutulacak (KVKK uyumu: ayrı güvenlik policy gerekli)
- physician_notes şu anda Text, encryption sonrası LargeBinary/Char olacak

