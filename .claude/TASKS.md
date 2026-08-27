# TASKS.md — Görev Listesi

## Tamamlanan Görevler ✅

### FAZ 0-4 + B-Görevleri (1-7) + İSG_OSGB Başlangıç
- [x] F0-001 ~ F0-007 (FAZ 0 — 7/7 %100)
- [x] F1-001, F1-003-006 (FAZ 1 — 5/6 %83, isg_health_basic bloklu)
- [x] F2-001, F2-002 (FAZ 2 — 2/9 %22)
- [x] F4-001 ~ F4-004 (FAZ 4 — 4/4 %100)
- [x] **B-1** isg.rate.table modeli (isg_osgb ön koşulu)
- [x] **B-2** isg_contractor — Risk Bilgilendirmesi belge türü
- [x] **B-3** isg_visitor — risk_briefing alanları
- [x] **B-6** isg_document — e-imza metadata
- [x] **B-7** isg_risk — renewal_trigger alanı
- [x] **isg_osgb başlandı** — 4 model, ACL, temel view (30/32 modül)

---

## Devam Eden / Sıradaki Görevler 🔄

### isg_osgb Tamamlama (Sonraki Oturum)

- [ ] **isg_osgb detaylı view'ları** — Capacity planning, ziyaret kaydı, detaylı form (~2-3 saat)
- [ ] **isg_osgb entegrasyon testleri** — İşyeri-uzman atama, kapasitelendirme simülasyonu
- [ ] **isg_osgb veri yükleme** — Seed data (örnek OSGB, uzmanlar, atamalar)

### Kalan MEV Görevleri (B-4, B-8, B-9, B-10)

- [ ] **B-4** isg_board — Toplantı sıklığı retrofit (~1 gün)
- [ ] **B-8** isg_penalty — Tarife versiyonlama (~0.5-1 gün)
- [ ] **B-9** isg_core — danger_class.history modeli (~0.5-1 gün, yüksek öncelik)
- [ ] **B-10** isg_training — 2 Nisan 2026 tam uyum (~2-3 gün, 🔴 kritik)

_B-5 (isg_board / 21 Oca 2026 Ulusal Konsey) harici hukuki teyit bekliyor._

### Ana Görevler — Yeni Modüller (FAZ 2 devam)

1. **F2-003 isg_incident** — İş Kazası (MEV-003, ~3-4 gün)
2. **F2-004 isg_audit** — Denetim ve kontrol listeleri (~2-3 gün)
3. **F2-005 isg_ppe** — KKD yönetimi (~2 gün)
4. **F2-006 isg_emergency** — Acil durum planı (~1.5 gün)
5. **F2-007 isg_chemical** — Kimyasal envanter (veri seti doğrulaması uzun, ~3-4 gün)
6. **F2-008 isg_equipment** — Ekipman ve periyodik kontrol (Ara.2025 EK-II, ~2-3 gün)
7. **F2-009 isg_ptw + isg_loto** — İş izni ve LOTO (~3-4 gün, en karmaşık)

### FAZ 3 — Ölçüm ve Çevre

- [ ] **F3-001** isg_measurement_core + isg_measurement_hygiene
- [ ] **F3-002** isg_environment

### FAZ 5 — Raporlama

- [ ] **F5-001** isg_reporting — Raporlama & Dashboards + Superset entegrasyonu

### Bloklu

- [ ] **F1-002** isg_health_basic — KVKK danışman onayı bekliyor

---

## İlerleme Özeti (26 Ağustos 2026)

| Faz | Toplam | Tamamlanan | % | Not |
|-----|--------|------------|---|-----|
| FAZ 0 | 7 | 7 | %100 | ✅ |
| FAZ 1 | 6 | 5 | %83 | isg_health_basic bloklu |
| FAZ 2 | 9 | 2 | %22 | 7 modül sırada (F2-003 ~ F2-009) |
| FAZ 3 | 2 | 0 | %0 | Ölçüm/çevre |
| FAZ 4 | 4 | 4 | %100 | ✅ Sanal Müfettiş |
| FAZ 5 | 3 | 0 | %0 | Raporlama |
| OSGB | 1 | 1 | %100 | Başlangıç (view'lar eksik) |
| B-Görevleri | 10 | 5 | %50 | 5 kaldı |
| **TOPLAM** | **42** | **30** | **%71** | **30/32 modül aktif** |

---

## Proje Hızı

- **Bu oturum (26 Ağustos):** 1 gün, 5+ görev (B-1, B-2/3/6/7, isg_osgb başlangıç)
- **Kumulatif:** 29+ gün, ~90% cekirdek modüller
- **Kalan iş:** MEV görevleri (5-6 gün), FAZ 2 (15-20 gün), FAZ 3/5 (5-10 gün)
- **ETA:** Tüm modüller %100 (32/32) → 3-4 hafta

---

## Definition of Done (Her Modül İçin)

- [ ] Odoo 18 uyumlu manifest + model dosyaları
- [ ] ACL (ir.model.access.csv)
- [ ] Liste, form, arama görünümleri (views)
- [ ] Menü ve action tanımları
- [ ] Sequence (varsa)
- [ ] Seed data (varsa)
- [ ] Temel test (kurulum, model oluşturma, view render)
- [ ] Git commit + push
- [ ] SESSION.md güncelleme
