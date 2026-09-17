# BACKLOG.md — Roadmap & Open Issues (Doğrulanmış: 17 Eylül 2026)

**Not:** Danışmanlık gerektiren tüm işler buradan çıkarılıp `DANISMANLIK_ISLERI_BEKLEMEDE.md`'ye taşındı. Bu dosya sadece bizim (dev ekip) bütçesiz yapabileceğimiz işleri içerir.

## 📅 Immediate Horizon

### 1. res.users.workplace_ids + Record Rule'lar (Öncelik #1)
**Amaç:** Holding→şirket→işyeri→site record rule zincirini tamamlamak

**Kapsam:**
- `res.users` veya `hr.employee` üzerinde `workplace_ids` (Many2many → isg.workplace)
- Record rule domain fonksiyonları: her kullanıcının erişimi company_id + workplace_id + site_id kesişimine göre
- isg_core, isg_hr, isg_health_basic üzerinde test

**Tahmin:** 1 gün
**Blocker:** Yok — tamamen dev ekibin elinde
**Risk:** Mevcut kayıtların workplace_id migration'ı gerekebilir

### 2. Bilinen Bug Temizliği
- [ ] `isg_contractor.contractor_level` — recursive=True eklenmeli
- [ ] `isg_location.hazard_type` — invisible parametresi WARNING (işlevsel değil, temizlik)
- [ ] `isg_visitor.ppe_notes` — model seviyesinde invisible parametresi WARNING
- [ ] `isg_security.isg_group_ids` — geçici çözüm, temiz implementasyon

**Tahmin:** 0.5 gün

### 3. F5-002/F5-003 Doğrulama
- [ ] QWeb PDF şablonları envanteri (risk, kaza, audit, denetim raporları)
- [ ] HSE Radar kabul test senaryoları (27 işlev × 5 = 135 test case) — mevcut mu, eksik mi
- [ ] Eksikleri tamamla

**Tahmin:** 0.5 gün
**Not:** Önceki Gap Analysis'te "F5-003 doğrulama pending" olarak işaretliydi — gerçek durumu kontrol etmemiz gerekiyor

### 4. MEV-008: Risk Bilgilendirmesi (2 Nisan 2026 Yönetmeliği)
- [ ] `isg_visitor.risk_briefing_given` (boolean, date)
- [ ] `isg_contractor` için aynı alan
- [ ] Workplace_id'ye göre oto-doldurma şablonu

**Tahmin:** 0.5 gün

### 5. isg_health_basic İyileştirmeleri (Opsiyonel)
- [ ] Encryption key rotation script (ir.cron)
- [ ] Audit log retention policy (30/90/365 gün)
- [ ] Batch audit log cleanup script

**Tahmin:** 1-1.5 gün
**Not:** Hukuki KVKK onayından bağımsız — bu saf teknik altyapı, danışman onayı bekleyen kısım ayrı (bkz. danışmanlık listesi)

### 6. OEL/STEL Karşılaştırma Script'i (Kod Hazırlığı)
- [ ] ÇSGB verisiyle otomatik karşılaştırma script'i (validate_ozone_exposure_limit.py tarzı)
- [ ] Delta/mismatch raporu formatı
- [ ] Git commit + dokümantasyon

**Tahmin:** 1 gün
**Not:** Script'i hazırlarız, resmi doğrulama/imza danışmanlık listesinde kalır — onay geldiğinde hemen devreye girer

## 🚨 Bilinen Sınırlamalar (Teknik Borç)

### isg_health_basic
- [x] Encryption implemented (Fernet) — Seans 12
- [x] Audit log implemented — Seans 12
- [ ] Key rotation script (yukarıda #5)
- [ ] Audit log archival (yukarıda #5)
- [ ] Record rules for workplace access (res.users.workplace_ids'e bağımlı, #1)

### Genel
- [ ] Contabo VPS github.com:443 egress whitelist (admin görevi, git push friction azaltır)
- [ ] Multi-database testing (şu an tek DB, dev ortamı)

## 📊 Açık Kararlar (teknik, bizim alabileceğimiz)

1. **Audit Log Retention:** Önerilen: 1 yıl sonra arşivleme (compliance + boyut dengesi)
2. **Encryption Key Yönetimi:** Şu an env var + dosya fallback yeterli (MVP); Vault/KMS entegrasyonu danışmanlık/enterprise aşamasında değerlendirilir
3. **Record Rule Stratejisi:** `res.users.workplace_ids` (org yapısıyla uyumlu) — kararlaştırıldı, uygulanacak

## 🔗 İlgili Dosyalar
- `SESSION.md` — Seans özeti
- `TASKS.md` — Aktif görev listesi (öncelik sıralı)
- `ARCHITECTURE.md` — Doğrulanmış modül mimarisi
- `DANISMANLIK_ISLERI_BEKLEMEDE.md` — Bütçe onayı bekleyen tüm danışmanlık işleri (AYRI TUTULUYOR)
