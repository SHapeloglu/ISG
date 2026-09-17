# TASKS.md — Aktif Backlog (Doğrulanmış: 17 Eylül 2026)

**Durum:** 31/31 üretim modülü kurulu (%100). Proje modül bazında TAMAMLANDI.
**Not:** Danışmanlık gerektiren tüm işler `DANISMANLIK_ISLERI_BEKLEMEDE.md` dosyasına taşındı. Bütçe onayı gelene kadar bu listeye dokunulmuyor.

## 🎯 Öncelik Sırası (Bizim Yapabileceklerimiz — danışman gerekmiyor)

### 1. Dokümantasyon Düzeltmesi ✅ (17 Eylül 2026, bugün)
- [x] ARCHITECTURE.md — VPS gerçeğine göre yeniden yazıldı
- [ ] TASKS.md — devam ediyor (bu dosya)
- [ ] SESSION.md — güncellenecek
- [ ] BACKLOG.md — güncellenecek
- [ ] CONTEXT_FOR_CLAUDE.md — güncellenecek

### 2. res.users.workplace_ids + Record Rule'lar (Tahmini: 1 gün)
- [ ] hr.employee / res.users üzerinde workplace_ids (Many2many → isg.workplace) tanımla
- [ ] Record rule domain fonksiyonları yaz (holding→şirket→işyeri→site zinciri)
- [ ] isg_core, isg_hr, isg_health_basic üzerinde test et
- **Neden öncelikli:** Birçok modülün record rule'u bu attribute'a bağımlı, güvenlik modelinin eksik son parçası

### 3. Bilinen Bug Temizliği (Tahmini: 0.5 gün)
- [ ] isg_contractor.contractor_level → recursive=True eklenmeli
- [ ] isg_location.hazard_type → invisible parametresi WARNING (işlevsel değil ama temizlenmeli)
- [ ] isg_visitor.ppe_notes → model seviyesinde invisible parametresi WARNING
- [ ] isg_security.isg_group_ids → geçici çözüm, temiz implementasyon yapılabilir

### 4. F5-002/F5-003 Doğrulama (Tahmini: 0.5 gün)
- [ ] QWeb PDF şablonları mevcut mu kontrol et (risk, kaza, audit raporları)
- [ ] HSE Radar kabul test senaryoları (27 işlev × 5 senaryo = 135 test case) hazır mı doğrula
- [ ] Eksik varsa tamamla

### 5. MEV-008: Risk Bilgilendirmesi Alanı (Tahmini: 0.5 gün)
- [ ] isg_visitor'a risk_briefing_given (boolean, date) ekle
- [ ] isg_contractor'a aynı alan uygulanabilir
- [ ] İşyerine özgü risk bilgilendirmesi şablonu (workplace_id'ye göre oto-doldur)

### 6. isg_health_basic İyileştirmeleri — Opsiyonel (Tahmini: 1-1.5 gün)
- [ ] Encryption key rotation script (ir.cron ile)
- [ ] Audit log retention policy (30/90/365 gün arşivleme)
- [ ] Batch audit log cleanup script

### 7. OEL/STEL Karşılaştırma Script Hazırlığı (Tahmini: 1 gün)
- [ ] ÇSGB resmi verisiyle otomatik karşılaştırma script'i yaz (kod hazır, resmi imza danışmanlık listesinde kalır)
- [ ] Mismatch raporu formatı (delta document)

## 🔒 Danışmanlık Gerektiren İşler
→ Bkz. `DANISMANLIK_ISLERI_BEKLEMEDE.md` (bütçe onayı bekliyor, ayrı takip)

## 📊 Genel Proje Durumu
- **31/31 modül** kurulu (%100) — isg_tests hariç (ayrı, uninstalled)
- **Git:** main branch, HEAD: f74a5e7
- **VPS:** vmi3389964, isg.powerbi.com.tr
- **Son doğrulama:** 17 Eylül 2026 (git log + ls + psql çıktısı)
