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

### FAZ 3 — Ölçüm Yönetimi (1/2)
- [x] **F3-001 isg_measurement_core** — Ölçüm altyapısı (kampanya, cihaz, numune, sonuç, limit)
- [ ] F3-002 isg_measurement_hygiene — Parametre-özel ölçümler (gürültü, toz, titreşim, vb.)

### FAZ 5 — Raporlama (1/3)
- [x] F5-001 isg_reporting — TRIR/LWDR KPI

---

## Devam Eden / Sıradaki Görevler 🔄

### FAZ 3 — Devam (Öncelik Sırası)

- [ ] **F3-002** `isg_measurement_hygiene` — Parametre-Özgü Ölçüm Alanları
      - Gürültü: LAeq, LCeq, Lpeak ölçüm formülleri
      - Toz: solunum vs inhalasyon fraksiyonu seçim
      - Titreşim: el-kol vs beden ayrımı
      - Aydınlatma: Lux ölçüm alanları
      - Isıl konfor: PMV/PPD indeksleri
      - Referans karşılaştırma fonksiyonları

- [ ] F3-003 `isg_environment` — Çevre İzleme
      - Ambient ölçümler (dış ortam kalitesi)
      - Fabrika ortamı monitoring
      - İndikatör parametreler

### FAZ 1 — Bekleyen
- [ ] **F1-002** `isg_health_basic` — Temel Sağlık Gözetimi + KVKK Maskeleme
      ⚠️ KVKK mimarisi danışman onayı bekliyor — EN SONA BIRAK

### FAZ 4 — Sanal Müfettiş / Mevzuat Motoru (EN KRİTİK, 35-50 AD)
- [ ] **F4-001** `isg_legislation` + `isg_obligation`
      - Mevzuat kaydı (6331, yönetmelikler, sürüm tarihleri)
      - Yükümlülük tanımlama (hangi kural neye uygulanıyor)
      - Uygulanabilirlik motoru (işyeri profili → hangi yükümlülükler)
      
- [ ] F4-002 `isg_compliance` — Uygunluk Değerlendirmesi
      - Her yükümlülük için kanıt kontrol (risk değerlendirmesi var mı, eğitim tamamlandı mı, vb.)
      - Uygunluk snapshot
      
- [ ] F4-003 `isg_penalty` — İdari Para Cezaları (2026 güncellenmiş)
      
- [ ] F4-004 `isg_simulator` — Müfettiş Simülatörü / Uygunluk Raporu

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
| FAZ 3 | 2 | 1 | %50 |
| FAZ 4 | 4 | 0 | %0 |
| FAZ 5 | 3 | 1 | %33 |
| OSGB | 1 | 0 | %0 |
| **TOPLAM** | **32** | **22** | **%69** |

---

## Definition of Done (Her Modül İçin)

- [ ] Odoo 18 uyumlu manifest
- [ ] Model alanları ve constraint'ler
- [ ] Liste, form, arama görünümleri
- [ ] Menü, action, sequence
- [ ] ACL (ir.model.access.csv) ve record rule
- [ ] Mail activity ve bildirim (gerekiyorsa)
- [ ] Belge/kanıt bağlantısı (gerekiyorsa)
- [ ] Çok şirket/işyeri/site testleri
- [ ] Normal/olumsuz/yetkisiz akış testleri
- [ ] Türkçe alan metinleri
- [ ] Mevzuat uygunluk notu
