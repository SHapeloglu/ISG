# BÖLÜM C: EKSİKLİKLER & GELİŞTİRME ÖNERİLERİ

**27 HSE Radar İşlevi × Odoo ISG Feature Gap Analysis**

---

## ÖZET: GAP MATRIX

### Odoo ISG'nin HSE Radar'a Kıyasla Eksiklikleri

| Bölüm | İşlevler | Tam | Eksik | % Eksilik | Öncelik |
|-------|----------|-----|-------|-----------|---------|
| **BÖLÜM 1:** Kurumsal | 4 | 4 | 0 | %0 | ✅ |
| **BÖLÜM 2:** İK & Yönetişim | 8 | 7 | 1 | %12 | 🟡 |
| **BÖLÜM 3:** Operasyonel | 10 | 9 | 1 | %10 | 🟡 |
| **BÖLÜM 4:** Ölçüm & Çevre | 2 | 2 | 0 | %0 | ✅ |
| **BÖLÜM 5:** Mevzuat & Yönetim | 4 | 4 | 0 | %0 | ✅ |
| **TOPLAM** | **27** | **26** | **2** | **%7** | — |

**Sonuç:** Sadece 2 eksiklik (minor), %93 coverage.

---

## DETAYLI GAP ANALIZI (Bölüm Bölüm)

---

### BÖLÜM 1: KURUMSAL YAPILAR (4/4 TAM) ✅

| İşlev | Durum | Açıklama |
|-------|-------|----------|
| 1. Holding/Kurum Yapısı | ✅ Tam | Zaten rich (4 katman: holding→şirket→işyeri→site) |
| 2. Kullanıcı/Grup/Yetki | ✅ Tam | Zaten var (5+ rol, record rules) |
| 3. Kurum İletişim Bilgileri | ✅ Tam | OSGB, MKK, Lab profilleri |
| 4. Yerleşim/Lokasyon | ✅ Tam | Zaten var (tree, GPS) |

**Tavsiye:** Bu bölüm kapatılmış, bakım/monitoring mode.

---

### BÖLÜM 2: İNSAN KAYNAKLARI & YÖNETİŞİM (7/8)

#### İşlev 5: İK ve Çalışanlar ✅ TAM
- ✓ Çalışan profili
- ✓ İSG role atama
- ✓ SEG (Benzer Maruziyet Grubu)
- ✓ Özel grup alanları (genç/yaşlı/engelli/gebe)
- ✓ KKD ölçüleri

**Durum:** Tam, 2 Nisan 2026 uyumlu

---

#### İşlev 6: Alt İşverenler ✅ TAM
- ✓ Alt işveren profili
- ✓ Sözleşme takibi
- ✓ 14 belge matrisi
- ✓ Belirleme & bildirimi
- ✓ Zincir yapısı

**Durum:** Tam

---

#### İşlev 7: İSG Kurulu ✅ TAM
- ✓ Üye tanımı
- ✓ Toplantı takvimi
- ✓ Karar yönetimi
- ✓ Tutanak oluşturma
- ✓ Otomatik bildirimi

**Durum:** Tam

---

#### İşlev 8: Sağlık Gözetimi ⚠️ **BLOKLU** (KVKK)

**Durum:** `isg_health_basic` modülü **intentionally uninstalled** (KVKK danışman onayı bekliyor)

**Eksik Öğeler:**
- [ ] Muayene kaydı (hekim-only view)
- [ ] Tetkik sonuçları (maskelenmiş erişim)
- [ ] Hekim portal (separate access)
- [ ] Audit log (kim ne okudu)
- [ ] KVKK rıza takibi

**ÇÖZÜM ÖNERİSİ:** [Bkz. BÖLÜM D — Mevzuat İyileştirmeleri]

**Tavsiye:**
- Dış KVKK danışmanı ile net meeting (scope tanımlama)
- Field-level encryption design (PostgreSQL pgcrypto)
- Role-based maskeleme (nur hekim görebilir)
- Legal opinion (belgeli)

**Bütçe:** ₺20-30K (danışman + dev)  
**Timeline:** 4-6 hafta  
**Priority:** 🔴 HIGH (Kamu pazarı için kritik)

---

#### İşlev 9: Ziyaretçi Yönetimi ✅ TAM
- ✓ Giriş/çıkış kaydı
- ✓ KKD bildirimi
- ✓ Güvenlik brifing
- ✓ İşe özgü risk bildirimi

**Durum:** 2 Nisan 2026 uyumlu

---

#### İşlev 10: Dokümantasyon ✅ TAM
- ✓ Belge yönetimi
- ✓ Sürüm kontrol
- ✓ SHA-256 hash
- ✓ E-imza framework
- ✓ Kilitli arşiv

**Durum:** Tam

---

#### İşlev 11: İç/Dış Yazışmalar ✅ TAM
- ✓ Gelen/giden kaydı
- ✓ Yasal cevap terimi (30 gün)
- ✓ Kategori
- ✓ Süresi geçmiş uyarısı

**Durum:** Tam

---

### BÖLÜM 2 ÖZET
- **Tam:** 7/8 (%88)
- **Eksik:** 1 (Sağlık Gözetimi — KVKK bloklı)
- **Tavsiye:** KVKK çözümü hızlandır (Bölüm D)

---

### BÖLÜM 3: OPERASYONEL İSG (9/10)

#### İşlev 12: Risk Değerlendirmesi ✅ TAM

**Kontrol Noktaları:**
- ✓ Tehlike tanımlama
- ✓ Risk ekibi
- ✓ Olasılık × Şiddet matrisi
- ✓ Kontrol hiyerarşisi
- ✓ Kalıntı risk
- ✓ Yenileme tetikleyicileri
- ✓ 2 yıl periyot

**Durum:** Tam, HSE Radar parity

---

#### İşlev 13: İş Kazası / Ramak Kala ✅ TAM (Odoo üstün)

**Özellikler:**
- ✓ Kaza kaydı
- ✓ SGK bildirimi (3 gün otomatik)
- ✓ Ramak kala kaydı
- ✓ Yaralanma sınıflandırması
- ✓ DÖF bağlantısı
- ✓ **Dönüş eğitimi otomatik tetikleme** ← HSE Radar'dan üstün

**Durum:** Tam + automation kazanımı

---

#### İşlev 14: DÖF / CAPA ✅ TAM

- ✓ DÖF kaydı
- ✓ Kök neden analizi (5 Neden + 6M)
- ✓ Durum makinesi
- ✓ Aksiyon takibi
- ✓ Etkinlik değerlendirmesi

**Durum:** Tam

---

#### İşlev 15: Denetim & Kontrol Listeleri ✅ TAM

- ✓ Denetim planı
- ✓ Kontrol listesi şablonları
- ✓ Bulgu kaydı
- ✓ Puanlama
- ✓ Tekrarlanan bulgu escalation

**Durum:** Tam

**Geliştirme İmkanı:**
- Mobile offline denetim (Flutter app) — bkz. BÖLÜM B (Quick Win)

---

#### İşlev 16: Eğitim ✅ TAM (Odoo üstün)

- ✓ Eğitim planı
- ✓ 2 Nisan 2026 periyot türleri
- ✓ İşe başlama eğitimi (2+ saat, yüz yüze)
- ✓ **Dönüş eğitimi otomatik** ← Odoo automation
- ✓ Özel grup eğitimi (genç/yaşlı/engelli/gebe)

**Durum:** 2 Nisan 2026 uyumlu + automation

---

#### İşlev 17: KKD Yönetimi ✅ TAM

- ✓ KKD envanter
- ✓ Çalışana zimmet
- ✓ Yenileme takvimi
- ✓ Uygunluk kontrolü

**Durum:** Tam

**Geliştirme İmkanı:**
- QR kod scanning (zimmet hızlandırma)
- Mobile app integration

---

#### İşlev 18: Acil Durum Planı ✅ TAM

- ✓ Acil durum planı
- ✓ Tahliye planı
- ✓ Toplanma noktaları
- ✓ Tatbikat kaydı
- ✓ Müşterek çalışan rehberi

**Durum:** Tam

---

#### İşlev 19: Kimyasal Madde Yönetimi ⚠️ **KISMEN** (OEL TARAMASI PENDING)

**Durum:** 95% tam, OEL/STEL doğrulaması pending

**Durumu:**
- ✓ Kimyasal envanter
- ✓ GBF/SDS yönetimi (OCA module)
- ✓ GHS sınıflama
- ⚠️ **OEL/STEL limit tablosu** (Türk ÇSGB veri — doğrulama gerekli)
- ✓ Depolama uyumluluk matrisi
- ✓ Maruziyet kaydı

**Eksik Öğeler:**
- [ ] OEL/STEL tablosunun ÇSGB'nin resmi veriyle eşleştirilmesi
- [ ] Periyodik güncelleme prosedürü (ÇSGB ne zaman değiştirir?)
- [ ] Test cases (örn: "Benzol 5 ppm limit" check)

**ÇÖZÜM ÖNERİSİ:**

**Seçenek A: Manual Doğrulama (Hızlı, Low Cost)**
- ÇSGB'den resmi OEL/STEL liste çek (PDF/Excel)
- Odoo isg_chemical.ozone_exposure_limit comparison
- Fark bulunmadığını rapor et (danışman sign-off)
- **Bütçe:** ₺5K (araştırma + rapor)
- **Timeline:** 2 hafta

**Seçenek B: Otomatik Feed (Robust)**
- ÇSGB website'den feed scraping (PDF OCR → DB)
- Monthly cron job (zaman otomatik)
- Change log tracking (audit trail)
- **Bütçe:** ₺15-20K (dev)
- **Timeline:** 4 hafta

**Tavsiye:** **Seçenek A (immediate)** + Seçenek B (phase 2)

**Priority:** 🟡 MEDIUM (kimyasal işletmeler %10 müşteri)

---

#### İşlev 20: Ekipman / Periyodik Kontrol (EK-II) ✅ TAM (Ara.2025 Uyumlu)

- ✓ EK-II ekipman kataloğu (Ara.2025 updated)
- ✓ Periyodik kontrol takvimi
- ✓ Yetkili kuruluş (MKK) kaydı
- ✓ Kontrol raporu & e-imza
- ✓ EKİPNET hazırlık
- ✓ Süre sonu uyarısı

**Durum:** Tam (Ara.2025 uyumlu doğrulandı)

**Geliştirme İmkanı:**
- EKİPNET API integrasyonu (E3 veri akışı) — bkz. Backlog

---

#### İşlev 21: İş İzni (PTW) & LOTO ✅ TAM

- ✓ İzin türleri
- ✓ Ön koşul checklists
- ✓ Çok aşamalı onay
- ✓ LOTO izolasyon
- ✓ Ortak kilit prosedürü
- ✓ Kapanış & serbest bırakma

**Durum:** Tam

**Geliştirme İmkanı:**
- QR kod döngüsü (PTW → LOTO → Unlock tracking)
- Mobile app (işçi PTW onay confirmation)

---

### BÖLÜM 3 ÖZET
- **Tam:** 9/10 (%90)
- **Eksik:** 1 (OEL/STEL doğrulama pending)
- **Tavsiye:** OEL validation (Seçenek A, ₺5K, 2 hafta)

---

### BÖLÜM 4: ÖLÇÜM & ÇEVRE (2/2) ✅ TAM

#### İşlev 22: Ölçüm / İzleme (İş Hijyeni) ✅ TAM

- ✓ Ölçüm kampanyası planı
- ✓ Numune & cihaz kaydı
- ✓ Kalibrasyon snapshot'ı
- ✓ Ham sonuç & limit sürümü
- ✓ Uygunluk değerlendirmesi
- ✓ Yetkili lab onayı

**Durum:** Tam

---

#### İşlev 23: Çevre Yönetimi ✅ TAM

- ✓ Atık kodu kataloğu
- ✓ Atık kaydı
- ✓ Depolama yönetimi
- ✓ Bertaraf takibi

**Durum:** Tam

---

### BÖLÜM 5: MEVZUAT & YÖNETİM (4/4) ✅ TAM

#### İşlev 24: İdari Para Cezaları ✅ TAM (2026 Güncel)

- ✓ Ceza tarifeleri (ÇSGB 2026, %49 artış)
- ✓ Tarife sürümü yönetimi
- ✓ Geçmiş tarihli simülasyon
- ✓ Yıllık otomatik güncelleme

**Durum:** 2026 uyumlu, tested

---

#### İşlev 25: Sanal Müfettiş (Mevzuat + Uyum) ✅ TAM

- ✓ Mevzuat motoru (6331, yönetmelikler)
- ✓ Yükümlülük tanımlama
- ✓ Uygulanabilirlik filtreleme
- ✓ Uygunluk değerlendirmesi
- ✓ Snapshot kilitlemesi

**Durum:** Tam

**Ekstra Kazanım:** Odoo versiyonlama (HSE Radar'dan farklı)

---

#### İşlev 26: Simülatör (Senaryo Testi) ✅ TAM

- ✓ "Ya da..." senaryoları
- ✓ Geçmiş tarihli değerlendirme
- ✓ Uyum tahmini

**Durum:** Tam

---

#### İşlev 27: Yönetim Raporları ✅ TAM (Odoo üstün)

- ✓ KPI dashboard
- ✓ İş hijyeni raporları
- ✓ TRIR / LWDR hesaplama
- ✓ PDF şablonları
- ✓ **Superset SQL (sınırsız)** ← Odoo üstün

**Durum:** Tam + reporting power

---

## ÖZET: 27 İŞLEV STATUS

| Durum | Sayı | % | İşlevler |
|-------|------|---|----------|
| ✅ Tam | 24 | 89% | 1-7, 9-27 |
| ⚠️ Eksik/Bloklu | 2 | 7% | 8 (KVKK), 19 (OEL) |
| 🚧 Backlog | 2 | 7% | 19 (OEL) minor, future |
| **TOPLAM** | **27** | **100%** | — |

---

# TEKNIK BACKLOG: GELIŞTIRME ÖNERİLERİ

## PRİYORİTE HARITASI

```
         Impact
          ↑
    HIGH │ ⭐⭐⭐      ⭐⭐⭐⭐
         │ Sağlık   Mobile  
         │ KVKK     App
         │          
    MED  │ ⭐⭐      ⭐⭐⭐
         │ OEL      E2/E3
         │ Veri     API
         │
    LOW  │ ⭐       ⭐⭐
         │ KKD QR   Feature
         │ Mobile   Enhancements
         └─────────────────→ Effort
           EASY              HARD
```

---

## DETAYLI BACKLOG İÖ'LERİ

### TIER 1: MUST-HAVE (Seans 8-10 içinde yapılmalı)

#### 1.1 İSG Sağlık Gözetimi (isg_health_basic) KVKK Uyumlu

**Epic:** "KVKK-Compliant Health Management"

**User Story 1: Hekim-Only Muayene Kaydı**
```
STORY: "Hekim sağlık testlerini kaydedebilmeli"

AC1: Nur hekim login'e giriş yapabilir (unique role)
AC2: Diğer kullanıcılar muayene ayrıntısını göremez 
     (field-level maskeleme)
AC3: İK/Manager sadece "Uygun/Uygun Değil" boolean görebilir
AC4: Tüm erişim audit log'a kaydedilir
AC5: PDKS rızası takibi (checkbox + tarih)

Technical Implementation:
- Field-level encryption (PostgreSQL pgcrypto)
  * isg_employee_health.blood_pressure — encrypted
  * isg_employee_health.test_result — encrypted
- Role-based access (ir.model.access, record rule)
  * hekim_group: full access
  * manager_group: read-only, fields masked
- Audit trail (ir.logging)
  * user_id, timestamp, field_name, old_value → encrypted
```

**Story 2: Muayene Süresi Takibi & Notification**
```
AC1: Muayene süresi geçince alarm
AC2: Çalışan "Muayene gerekli" state'i
AC3: İSG müdürü report (muayene gecikmiş)
```

**Story 3: SGK VERBİS Export**
```
AC1: Hekim muayene verisi → SGK format
AC2: Monthly batch export
```

**Technical Estimate:** 40-50 dev-gün  
**Bütçe:** ₺20-25K (dev + testing)  
**Timeline:** 6 hafta  
**Blocker:** KVKK danışman onayı (document hazır)

**Status:** 🔴 CRITICAL (Kamu pazarı için blocker)

---

#### 1.2 OEL/STEL Doğrulaması & Automated Feed

**Epic:** "Türk ÇSGB OEL/STEL Data Sync"

**Story 1: ÇSGB Resmi OEL Tarafından Doğrulama**
```
STORY: "OEL/STEL tablosunu ÇSGB ile karşılaştırmalı"

AC1: Odoo isg_chemical.ozone_exposure_limit 
     ≈ ÇSGB official list (benzol 5ppm, etc)
AC2: Fark varsa report et (delta document)
AC3: Danışman sign-off (written tasdik)
AC4: Git commit (version control: ozone_ozone_limits_v20260915)

Manual Process:
- ÇSGB web sayfasından OEL PDF indir
- Odoo table ile excel match
- Diff document hazırla
- Danışman imzala
```

**Technical Estimate:** 10-15 dev-gün (research + validation)  
**Bütçe:** ₺5K  
**Timeline:** 2 hafta  
**Status:** 🟡 MEDIUM

**Story 2: Otomatik ÇSGB Feed (Phase 2)**
```
STORY: "ÇSGB OEL verisi otomatik update olsun"

AC1: Monthly cron job (ÇSGB website'i check)
AC2: PDF OCR → parse → DB compare
AC3: Change detected → notification + git branch
AC4: Change log table (date, old_val, new_val)
AC5: Slack alert (changes found)

Implementation:
- Python script (OCR: tesseract veya AWS Textract)
- Odoo cron (model.ir.cron)
- ir.logging (change history)
- Slack webhook
```

**Technical Estimate:** 30-40 dev-gün  
**Bütçe:** ₺15-20K  
**Timeline:** 4 hafta  
**Status:** 🟡 PHASE 2

---

### TIER 2: SHOULD-HAVE (Seans 10-15'e kadar)

#### 2.1 E2/E3 Entegrasyon (SGK/EKİPNET API)

**Epic:** "Regulatory Reporting to Turkish Authorities"

**Feature E2: SGK Bildirimi (İş Kazası)**
```
STORY: "3 gün içinde SGK'ya otomatik bildirimi göndersin"

AC1: Kaza kaydı → API endpoint (SGK credentials)
AC2: 3 gün timer (reminder, escalation)
AC3: Sent/Failed status tracking
AC4: Retry logic (failed attempts)
AC5: Audit log (batch ID, response code)

Technical:
- REST API client (requests library)
- Odoo model: isg_incident → ir.cron (daily check)
- State machine: draft → submitted → confirmed → acknowledged
- Batch processing (night job)
```

**Technical Estimate:** 50-60 dev-gün  
**Bütçe:** ₺25-30K (dev + SGK integration testing)  
**Timeline:** 8 hafta  
**Dependency:** SGK API credentials (müşteriden gerekli)

**Status:** 📋 BACKLOG (High Impact, but resource-heavy)

---

#### 2.2 Mobile App: Offline Denetim (Flutter)

**Epic:** "Field Inspection App - Offline First"

[Bkz. BÖLÜM B — Mobile App section]

**Technical Estimate:** 120-150 dev-gün  
**Timeline:** 16 hafta  
**Priority:** 🔴 HIGH (market differentiation)

---

#### 2.3 QR Code Tracking (PTW/LOTO/KKD)

**Epic:** "Supply Chain & Asset Tracking"

**Story 1: PTW → LOTO → Unlock Cycle**
```
STORY: "PTW'de QR scan → LOTO setup → Unlock"

Flow:
1. İşçi PTW QR scan (mobile app)
   → PTW details auto-fill
2. Risk checklist confirm
3. Manager approval (digital sign)
4. Energy isolation başlasın
   → LOTO QR generate (unique per energy source)
5. LOTO kayıtla
6. Work complete → LOTO QR scan
   → Unlock confirmation
```

**Technical Estimate:** 20-30 dev-gün  
**Bütçe:** ₺10-15K  
**Timeline:** 3 hafta  
**Priority:** 🟡 MEDIUM (nice-to-have, nice-to-measure)

---

#### 2.4 AI/ML Features

[Bkz. BÖLÜM B — AI/ML Section]

---

### TIER 3: NICE-TO-HAVE (Phase 2+, 6+ ay)

#### 3.1 Advanced Reporting (Superset Templates)

**Epic:** "ISG KPI Library"

```
Dashboard 1: "Executive Dashboard"
- TRIR (Total Recordable Incident Rate)
- LWDR (Lost Workday Rate)
- Incident trend (90 gün)
- Compliance score
- Top risks (bar chart)

Dashboard 2: "Operational Dashboard"
- Overdue training
- Equipment inspection status
- Open DÖF/CAPA
- Upcoming risk reviews

Dashboard 3: "Compliance Dashboard"
- Mevzuat uyum % (by area)
- Audit findings trend
- Penalty exposure
```

**Technical Estimate:** 40-50 dev-gün  
**Timeline:** 8 hafta (parallel with other work)

---

#### 3.2 Incident Analytics

**Epic:** "Advanced Root Cause Analysis"

```
- Incident heatmap (by department/location)
- Root cause clustering (5M analysis categorization)
- Near-miss to incident conversion rate
- Seasonal patterns
```

**Technical:** Python + Pandas analytics

---

## SPRINT PLANNING RECOMMENDATIONS

### FAZA 1: TIER 1 (Seans 8-9, 8 hafta)

```
HAFTA   | isg_health KVKK | OEL Validation | Integration | Testing
────────┼──────────────────┼───────────────┼─────────────┼─────────
1-2     | [Design]         | [Research]    | —           |
3-4     | [Dev]            | [Validation]  | —           |
5-6     | [Testing]        | [Danışman]    | —           |
7-8     | [Production]     | [Complete]    | [Prep E2]   | [QA]
────────┴──────────────────┴───────────────┴─────────────┴─────────
Result: isg_health_basic + OEL doğru ✅
        E2 design ready (dev'e pass)
```

**Bütçe:** ₺45-50K  
**Team:** 2 dev + 1 QA + external consultant (KVKK)

---

### FAZA 2: TIER 2 (Seans 10-15, 12 hafta paralel)

```
Workstream A: E2/E3 Integration (8 hafta)
Workstream B: Mobile App MVP (16 hafta — başladı Seans 8'de)
Workstream C: QR Tracking (3 hafta — sprint 3-5)
```

---

## RELEASE NOTES TEMPLATE (Her Sprint'de)

```markdown
## Odoo ISG v2026-10 Release Notes

### 🆕 New Features
- [ ] isg_health_basic: KVKK-compliant health records
- [ ] OEL/STEL: Validated Turkish ÇSGB data
- [ ] QR PTW Tracking: Unified chain-of-custody

### 🔧 Improvements
- [ ] Email notifications (training, equipment due)
- [ ] PDF reports: Better formatting

### 🐛 Bug Fixes
- [ ] Risk renewal calendar: Fixed edge case (Feb 29)
- [ ] LOTO state machine: Missing transition

### ⚠️ Breaking Changes
None

### 📚 Documentation
- [ ] Health Management Administrator Guide
- [ ] OEL Data Validation Procedure
```

---

## QUALITY ASSURANCE CHECKLIST

```
For each feature:
☐ Unit tests (pytest)
☐ Integration tests (Odoo model + views)
☐ UI tests (Selenium, smoke test)
☐ Security tests (field masking verification)
☐ Performance tests (1000+ records)
☐ Data migration (if schema change)
☐ UAT (user acceptance) — pilot customer
☐ Documentation (user + developer)
☐ Deployment runbook (staging → production)
```

---

## KNOWN ISSUES & TECHNICAL DEBT

| Issue | Severity | Status | Note |
|-------|----------|--------|------|
| PDF report routing (F5-003 404) | 🟡 Medium | 🔄 Next | Odoo 18 base routing |
| isg_tests ghost DB record | 🟡 Medium | ✅ Fixed | Cleaned Seans 7 |
| tracking param on selection fields | 🟡 Medium | ⏳ Odoo issue | Wait for Odoo 18 fix |
| Deprecated odoo.api.Environment | 🟠 Low | ⏳ Script cleanup | Refactor sys.path code |

---

## CONCLUSION: ROADMAP STATUS

**Fonksiyonel Eşdeğerlik:** 89% (24/27 işlev tam)  
**Critical Path:** isg_health_basic + OEL validation  
**Timeline to HSE Radar parity:** 8 hafta (Seans 9'un sonunda)  
**Competitive Differentiation:** Mobile app + AI/ML (12-16 hafta)

**Next Phase:** BÖLÜM D — Mevzuat İyileştirmeleri

---

**Belge Sürümü:** 1.0  
**Tarih:** 7 Eylül 2026  
**Durum:** 🚀 READY FOR SPRINT PLANNING

