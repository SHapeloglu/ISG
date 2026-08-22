# TASKS.md — Görev Listesi

## Tamamlanan Görevler ✅

### FAZ 0 — Temel Mimari ✅ TAMAMLANDI (7/7)
- [x] F0-001 isg_core
- [x] F0-002 isg_security
- [x] F0-003 isg_party
- [x] F0-004 isg_location
- [x] F0-005 isg_document
- [x] F0-006 isg_hr
- [x] F0-007 isg_base

### FAZ 1 — Kurumsal Yönetişim (5/6) ✅ %83
- [x] F1-001 isg_contractor
- [x] F1-003 isg_training
- [x] F1-004 isg_visitor
- [x] F1-005 isg_board
- [x] F1-006 isg_correspondence
- [ ] F1-002 isg_health_basic (KVKK danışman onayı bekleniyor)

### FAZ 2 — Çekirdek ISG Operasyonları ✅ TAMAMLANDI (9/9)
- [x] F2-001 isg_capa
- [x] F2-002 isg_risk
- [x] F2-003 isg_incident
- [x] F2-004 isg_audit
- [x] F2-005 isg_ppe
- [x] F2-006 isg_emergency
- [x] F2-007 isg_chemical
- [x] F2-008 isg_equipment
- [x] F2-009 isg_ptw + isg_loto

### FAZ 3 — Ölçüm Yönetimi ✅ TAMAMLANDI (2/2)
- [x] **F3-001 isg_measurement_core** — Ölçüm altyapısı (kampanya, cihaz, numune, sonuç, limit)
- [x] **F3-002 isg_measurement_hygiene** — Gürültü parametreleri (LAeq, LCeq, Lpeak)

### FAZ 4 — Mevzuat Motoru (1/4)
- [x] **F4-001 isg_legislation** — Yükümlülük Altyapısı (kanun, yükümlülük, uygulanabilirlik)

### FAZ 5 — Raporlama (1/3)
- [x] F5-001 isg_reporting — TRIR/LWDR KPI

---

## Devam Eden / Sıradaki Görevler 🔄

### FAZ 4 — Devam (KRITIK)
- [ ] **F4-002** `isg_compliance` — Uygunluk Değerlendirmesi Motoru
      - İşyeri profili → hangi yükümlülükler geçerli?
      - Her yükümlülük için kanıt kontrol
      - Uygunluk snapshot (COMPLIANT / NON_COMPLIANT / PENDING)
      
- [ ] **F4-003** `isg_penalty` — İdari Para Cezaları (ÇSGB 2026)
      - Ceza tarifesi
      - Otomatik ceza hesaplama
      
- [ ] **F4-004** `isg_simulator` — Müfettiş Simülatörü / Uygunluk Raporu

### FAZ 3 — Opsiyonel Devam
- [ ] **F3-002 Devam** `isg_measurement_hygiene` — Diğer Parametreleri Ekle
      - Toz: solunum vs inhalasyon fraksiyonu
      - Titreşim: el-kol vs beden ayrımı
      - Aydınlatma: Lux ölçüm alanları
      - Isıl Konfor: PMV/PPD indeksleri
      - (Her bir parametre type için aynı inherit + invisible pattern)

### FAZ 1 — Bekleyen
- [ ] **F1-002** `isg_health_basic` — Temel Sağlık Gözetimi + KVKK Maskeleme
      ⚠️ KVKK mimarisi danışman onayı bekliyor — EN SONA BIRAK

---

## Bilinen Hatalar / Düzeltilecekler 🐛

- [ ] `isg_contractor.contractor_level` — recursive=True eklenmeli
- [ ] `isg_location.hazard_type` — unknown parameter 'invisible' WARNING
- [ ] Admin şifresi — kalıcı olarak belirlenmeli
- [ ] `isg_core` ACL — no group WARNING
- [ ] `html4css1.css` Permission denied WARNING (işlevsel değil)

---

## E1 Altyapı Kararları
- [ ] EX-001 `isg_assurance` iskeleti
- [ ] EX-002 Kanıt hash servisi
- [ ] EX-003 `isg_competency` iskeleti
- [ ] EX-004 Entegrasyon outbox/inbox
- [ ] EX-005 Dış UUID
- [ ] EX-006 `isg_moc` iskeleti

---

## İlerleme Özeti

| Faz | Toplam | Tamamlanan | % |
|-----|--------|------------|---|
| FAZ 0 | 7 | 7 | %100 |
| FAZ 1 | 6 | 5 | %83 |
| FAZ 2 | 9 | 9 | %100 |
| FAZ 3 | 2 | 2 | %100 |
| FAZ 4 | 4 | 1 | %25 |
| FAZ 5 | 3 | 1 | %33 |
| OSGB | 1 | 0 | %0 |
| **TOPLAM** | **32** | **24** | **%75** |

---

## Definition of Done (Her Modül İçin)

- [x] Odoo 18 uyumlu manifest
- [x] Model alanları ve constraint'ler
- [x] Liste, form, arama görünümleri
- [x] ACL (ir.model.access.csv) ve record rule
- [x] Türkçe alan metinleri
- [x] Mevzuat uygunluk notu
