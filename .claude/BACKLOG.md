# BACKLOG.md — Teknik Borç ve Referans (22 Ağustos 2026)

## HSE Radar Paritesi Hedefi

Hedefimiz HSE Radar'ın Türkiye ISG fonksiyonlarının %90+ kapsamını yapmak.

**Şu anki kapsama: ~78%** (25/32 modül)

## Tamamlanan HSE Radar Fonksiyonları ✅

- Risk Değerlendirmesi (L Matrisi + Fine-Kinney)
- İş Kazası / Ramak Kala Takibi
- Denetim & Bulgu Kaydı
- KKD Yönetimi (Zimmet, Envanter)
- Acil Durum Planı (Tatbikat)
- Kurumsal Yönetişim (Kurul, Eğitim, Yazışma, Ziyaretçi)
- Kimyasal Envanter + SDS
- Ekipman Periyodik Kontrol (EKİPNET)
- İş İzni (PTW) + LOTO
- Ölçüm Yönetimi — Çekirdek Altyapı + Gürültü Parametreleri (F3-001 + F3-002)
- **Mevzuat Motoru — Yükümlülük Altyapısı** (F4-001) ✅ TAMAMLANDI

## Planlanmış Fonksiyonlar (FAZ 4-5)

- **Uygunluk Değerlendirmesi** (F4-002) ⭐ KRITIK — İşyeri profile göre otomatik yükümlülük hesaplama + kanıt kontrol (HSE Radar DNA)
- İdari Para Cezaları (F4-003) — ÇSGB 2026 güncellemesi
- Müfettiş Simülatörü (F4-004) — "Müfettiş gelirse" raporu
- Ölçüm Orkestrasyonu Detayları (F3-002 devam) — Toz, Titreşim, Aydınlatma, Isıl Konfor
- Raporlama Detayları (PDF, Superset — F5-002/003)

---

## Bilinen Teknik Borçlar 🐛

### Model Seviyesi

- [ ] `isg_contractor.contractor_level` — `recursive=True` eklenmeli (self-referential)
- [ ] `isg_location.hazard_type` — model seviyesinde `invisible` parametresi (view'da olmalı)
- [ ] `isg_visitor.ppe_notes` — model seviyesinde `invisible` parametresi
- [ ] `isg_measurement_result.exceeding_percentage` — compute field, store=True gerekli (✅ yapıldı F3-001'de)

### Security / ACL

- [ ] `isg_core` modeline "no group" WARNING var
- [ ] Record rule eksikleri:
  - `isg_risk_line` (risk.hazard kayıtları)
  - `isg_audit_line` (audit bulguları)
  - `isg_ppe_issue` (KKD problemleri)
  - `isg_chemical_inventory` (stok takibi)
  - `isg_obligation` (mevzuat kuralları — F4-002 girilince gerekli)

### Veri Seti

- [ ] OEL/STEL limit değerleri dolu değil (ÇSGB/AB kaynaklarından uzman doğrulama gerekli)
- [ ] Kimyasal envanter örnek veri yok
- [ ] Ekipman örnek veri yok
- [ ] **Mevzuat seed data (kanunlar, yönetmelikler) başladı** — 7 mevzuat, 7 yükümlülük eklendi. Daha fazla eklenebilir.

### Sistem

- [ ] Admin şifresi NULL — kalıcı şifre belirlenmeli
- [ ] `html4css1.css` Permission denied WARNING (işlevsel değil, bilgi amaçlı)
- [ ] SSH key kurulumu deferred (şu an HTTPS auth kullanıyoruz)

---

## Modül Detayları (25/32)

### FAZ 0 — Temel Mimari (7/7 ✅)
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

### FAZ 1 — Kurumsal Yönetişim (5/6)
- isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- **Bekleyen:** isg_health_basic (KVKK maskeleme) — EN SONA

### FAZ 2 — Çekirdek ISG Operasyonları (9/9 ✅)
- isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw

### FAZ 3 — Ölçüm Yönetimi (2/2 ✅)
- **isg_measurement_core ✅** (campaign, device, sample, result, limit)
- **isg_measurement_hygiene ✅** (gürültü parametreleri: LAeq, LCeq, Lpeak)

### FAZ 4 — Mevzuat/Uygunluk Motoru (1/4)
- **isg_legislation ✅** (yükümlülük altyapısı: kanun, yükümlülük, uygulanabilirlik)
- isg_compliance (uygunluk değerlendirmesi — ⏳ KRITIK, sonraki modül)
- isg_penalty (idari cezalar — ⏳ planlandı)
- isg_simulator (müfettiş simülatörü — ⏳ planlandı)

### FAZ 5 — Raporlama (1/3)
- **isg_reporting ✅** (TRIR/LWDR)
- QWeb PDF şablonları (⏳ planlandı)
- Superset entegrasyonu (⏳ planlandı)

### OSGB Modülü
- isg_osgb (Uzman/hekim planlama)

---

## Kritik Yolda Olan (Critical Path)

1. ✅ **FAZ 4-001 isg_legislation** — Yükümlülük altyapısı TAMAMLANDI
2. ⏳ **FAZ 4-002 isg_compliance** — Uygunluk değerlendirmesi (KRITIK — bundan sonra HSE Radar DNA'sı aktif olur)
3. ⏳ **FAZ 4-003 isg_penalty** — Ceza tarifesi
4. ⏳ **FAZ 4-004 isg_simulator** — Müfettiş simülatörü

**100% Hedefine ulaşınca 50 kayıtlık entegrasyon testi yapılacak** (workplace → obligation → compliance → penalty → simulator zinciri)

---

## Performans Notları

- Record rule çokluğu (15 per modül) → test ortamında sorguları monitor etmek gerekebilir
- Snapshot fields (store=True) → veri tabanında disk kullanımı artabilir
- Compute field dependencies → O(n) sorgu riski (optimize edilebilir)
- View inheritance cascade (F3-002 gibi) — performansı minimal, inheritance depth kontrol
- **Mevzuat motoru (F4-002+)** — applicability rules nested evaluation → iterate over not recursive
- isg.obligation.applicability rules 1000+ kayda çıkırsa indexed olmalı

---

## Dokümantasyon Durumu

- SESSION.md ✅ güncel (F4-001 TAMAMLANDI)
- TASKS.md ✅ güncel (F4-001 tamamlandı, F4-002 planlama eklendi)
- CLAUDE.md ✅ güncel (FAZ 4-001 eklendi, Odoo 18 uyarıları eklendi)
- ARCHITECTURE.md ✅ güncel (Mevzuat altyapısı ve uygunluk mimarisi eklendi)
- BACKLOG.md ✅ güncel (bu dosya)
