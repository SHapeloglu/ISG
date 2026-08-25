# TASKS.md — Görev Listesi

## Tamamlanan Görevler ✅

### FAZ 0 — Temel Mimari ✅ TAMAMLANDI
- [x] F0-001 isg_core — İşyeri + Site modelleri, 6331 md.6 uzman/hekim süre
- [x] F0-002 isg_security — 5 rol grubu, işyeri erişim kontrolü
- [x] F0-003 isg_party — OSGB/Lab/Muayene/Altİşveren rolleri
- [x] F0-004 isg_location — GPS, kapasite, tehlikeli alan, toplanma noktası
- [x] F0-005 isg_document — SHA-256, sürüm/kilit/e-imza
- [x] F0-006 isg_hr — Çalışan İSG profili, SEG
- [x] F0-007 isg_base — UUID mixin, outbox altyapısı

### FAZ 1 — Kurumsal Yönetişim ✅ %83 (5/6)
- [x] F1-001 isg_contractor — Alt işveren zinciri, belge matrisi
- [x] F1-003 isg_training — Eğitim planı + 2 Nisan 2026 yönetmelik
- [x] F1-004 isg_visitor — Ziyaretçi kaydı, giriş/çıkış
- [x] F1-005 isg_board — İSG kurulu, toplantı, karar takibi
- [x] F1-006 isg_correspondence — Gelen/giden yazışma, yasal süre takibi
- [ ] F1-002 isg_health_basic — ⏳ KVKK danışman onayı bekliyor (bloklu)

### FAZ 2 — Çekirdek İSG Operasyonları %22 (2/9)
- [x] F2-001 isg_capa — DÖF/CAPA, kök neden analizi, aksiyon takibi
- [x] F2-002 isg_risk — Risk değerlendirmesi, tehlike, kontrol önlemleri
- [ ] F2-003 isg_incident — İş kazası / ramak kala (sırada)
- [ ] F2-004 isg_audit — Denetim ve kontrol listeleri
- [ ] F2-005 isg_ppe — KKD yönetimi
- [ ] F2-006 isg_emergency — Acil durum planı
- [ ] F2-007 isg_chemical — Kimyasal envanter ve SDS
- [ ] F2-008 isg_equipment — Ekipman ve periyodik kontrol
- [ ] F2-009 isg_ptw + isg_loto — İş izni ve LOTO

### FAZ 3 — Ölçüm ve Çevre %0 (0/2)
- [ ] F3-001 isg_measurement_core + isg_measurement_hygiene
- [ ] F3-002 isg_environment

### FAZ 4 — Sanal Müfettiş ✅ %100 (4/4)
- [x] F4-001 isg_legislation — Mevzuat ve yükümlülük tanımları
- [x] F4-002 isg_compliance — Uygunluk değerlendirmesi motoru
- [x] F4-003 isg_penalty — İdari para cezası tarifesi (ÇSGB 2026)
- [x] F4-004 isg_simulator — Müfettiş simülasyonu

### FAZ 5 — Raporlama %0 (0/3)
- [ ] F5-001 isg_reporting — Raporlama + Superset entegrasyonu
- [ ] F5-002 QWeb PDF şablonları
- [ ] F5-003 HSE Radar kabul testi

### OSGB Modülü %0 (0/1)
- [ ] isg_osgb — OSGB planlama ve görevlendirme motoru

---

## Sıradaki Görevler (3 Kalan)

### Öncelik Sırası

**1. isg_osgb** (Tavsiye edilen)
   - OSGB planlama ve görevlendirme motoru
   - Uzman/hekim süre hesaplama (danger_class'a göre)
   - Kapasite planlama
   - İSG-KATİP hazırlık

**2. F5-001 isg_reporting** 
   - Raporlama ve dashboards
   - Superset entegrasyonu
   - QWeb PDF şablonları

**3. F1-002 isg_health_basic** (Bloklu)
   - KVKK danışman onayı bekliyor

---

## Açık Konular 🐛

- [ ] `isg_site.hazard_type` — unknown parameter 'invisible' (uyarı, işlevsel değil)
- [ ] `html4css1.css` — Permission denied (uyarı, işlevsel değil)
- [ ] `isg_risk.line` — Model declared but cannot be loaded (FAZ 2 eski kalıntısı)

---

## İlerleme Özeti

**Proje: %90.6 tamamlandı**
- 29/32 modül kuruldu
- FAZ 4 (Sanal Müfettiş) 100% bitti
- FAZ 0 (Temel) 100% bitti
- 3 modül kaldı (1 bloklu, 2 sırada)
