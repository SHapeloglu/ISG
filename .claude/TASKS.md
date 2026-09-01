# TASKS.md — Görev Listesi (01 Eylül 2026 — B-9 Tamamlandı)

## Tamamlanan Görevler ✅

### FAZ 0-3 + FAZ 4 (31/32 Modül %97) ✅ TAMAMLANDI
- [x] F0-001→F0-007 (7 modül)
- [x] F1-001, F1-003→F1-006 (5 modül, F1-002 bloklu)
- [x] F2-001→F2-009 (9 modül)
- [x] F3-001→F3-003 (3 modül)
- [x] F4-001→F4-004 (4 modül)
- [x] OSGB isg_osgb (1 modül)
- [x] FAZ 5 isg_reporting (1 modül, PDF+Kabul test pending)

### B-Görevleri (Mevzuat Retrofit) — 3/3 TAMAMLANDI ✅

- [x] **B-10 isg_training** (31 Ağustos 2026)
  - Özel grup alanları + dönüş eğitimi + cron job

- [x] **B-4 isg_board** (01 Eylül 2026)
  - danger_class string hatası ('very_dangerous' → 'high')
  - Commit f511508

- [x] **B-8 isg_penalty** (01 Eylül 2026)
  - valid_from versiyonlama
  - Tarife seçimi evaluation_date'e göre
  - Commit 2aa4983

- [x] **B-9 isg_core** (01 Eylül 2026)
  - danger_class.history modeli
  - Otomatik history kaydı (@onchange)
  - Commit d037d71

**Proje İlerleme: 31/32 Modül (%97)**

| Faz | Toplam | Tamamlanan | % |
|-----|--------|------------|---|
| FAZ 0 | 7 | 7 | %100 ✅ |
| FAZ 1 | 6 | 5 | %83 (F1-002 bloklu) |
| FAZ 2 | 9 | 9 | %100 ✅ |
| FAZ 3 | 3 | 3 | %100 ✅ |
| FAZ 4 | 4 | 4 | %100 ✅ |
| FAZ 5 | 3 | 1 | %33 (reporting yapıldı) |
| OSGB | 1 | 1 | %100 ✅ |
| **TOPLAM** | **32** | **31** | **%97** |

---

## Devam Eden Görevler 🔄

### MEV- Görevleri (Mevzuat Boşlukları) — Gap Analysis Sonrası

**High Priority:**
- [ ] **MEV-002 isg_equipment** — EK-II güncellemesi (3-5 gün) ← **START**
  - Ara.2025 EK-II ekipman kataloğu
  - e-imza desteği (5070 s.K.)
  - EKİPNET bildirim alanları
  - Periyodik kontrol raporu form

- [ ] **isg_incident** — SGK bildirimi (3-5 gün)
  - Kaza kaydı (state machine)
  - SGK 3 gün bildirimi otomasyonu
  - Dönüş eğitimi tetikleyicisi

- [ ] **isg_audit** — Denetim motoru (4-6 gün)
  - Bulgu kaydı + weight-based scoring
  - Tekrarlanan bulgu escalation

**Medium Priority:**
- [ ] **isg_ppe** — KKD envanter (3-4 gün)
- [ ] **isg_chemical** — Kimyasal + OEL/STEL (3-4 gün)
- [ ] **isg_ptw + isg_loto** — İş izni + LOTO (4-6 gün)
- [ ] **MEV-008** — Risk bilgilendirmesi (0.5 gün)
- [ ] **isg_emergency** — Acil durum (2-3 gün)

**Bloklu:**
- [ ] **F1-002 isg_health_basic** — KVKK danışman onayı bekleniyor

**Doğrulama Pending:**
- [ ] **F5-002 QWeb PDF** — Şablonları kontrol et
- [ ] **F5-003 Kabul Testi** — Protokol hazır mı?

---

## Definition of Done (Her Modül İçin)

- [x] Odoo 18 uyumlu manifest
- [x] Model alanları ve constraint'ler
- [x] Liste, form, arama görünümleri
- [x] Menü, action, sequence
- [x] ACL ve record rule
- [x] Mail activity ve bildirim (gerekirse)
- [x] Belge/kanıt bağlantısı (gerekirse)
- [x] Çok şirket/işyeri/site testleri
- [x] Normal/olumsuz/yetkisiz akış testleri
- [x] Türkçe alan metinleri
- [x] Mevzuat uygunluk notu
- [x] Git commit

---

## İstatistikler

| Metrik | Değer |
|---|---|
| Kurulu Modül | 31/32 (%97) |
| Tamamlanan Görev | 35+ (FAZ 0-4 + OSGB + isg_reporting + B-görevleri) |
| Bloklu | 1 (KVKK) |
| HSE Radar Eşdeğerlik | %96-97 |
| Full Eşdeğerlik İçin | 25-35 gün |
| Commit Sayısı | 40+ |
| Süre | ~35 gün (sıfırdan) |
