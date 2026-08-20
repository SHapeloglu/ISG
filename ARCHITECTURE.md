# ARCHITECTURE.md — ISG Platform Mimarisi (18 Ağustos 2026)

## Genel Bakış

ISG Platform, Odoo 18 üzerine kurulu, Türkiye'nin 6331 Kanunu ve ilgili yönetmeliklere uyumlu, kurumsal ISG yönetim sistemidir.

**Platform:** Odoo 18.0 | **DB:** PostgreSQL | **VPS:** Contabo | **Version:** GitHub SHapeloglu/ISG

---

## Modül Hiyerarşisi

FAZ 0 — Foundation (7/7 TAMAMLANDI)
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

FAZ 1 — Governance (5/6 TAMAMLANDI, %83)
- isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- Bekleyen: isg_health_basic (KVKK onayı)

FAZ 2 — Core Operations (9/9 TAMAMLANDI, %100)
- isg_capa, isg_risk, isg_incident, isg_audit, isg_emergency, isg_ppe, isg_chemical, isg_equipment, isg_ptw+isg_loto

FAZ 3 — Measurement (2/2 TAMAMLANDI, %100)
- isg_measurement_core ✅
  * isg_measurement_campaign (yillik olcum plani)
  * isg_measurement_device (cihazlar, kalibrasyon)
  * isg_measurement_sample (numune noktalari, SEG)
  * isg_measurement_result (snapshot: ham veri + kalibrasyon + limit dondurulmus)
  * isg_measurement_limit (OEL/STEL, versiyonlu)
  * Uygunluk hesaplama: raw_value <= limit → COMPLIANT, else EXCEEDING
  * DÖF entegrasyonu: limit asiminda otomatik isg_capa

- isg_measurement_hygiene ✅
  * isg.measurement.result inherit — measurement_type seçim
  * Gürültü parametreleri: LAeq, LCeq, Lpeak, Lpeak Referans (140 dB ÇSGB)
  * View invisible pattern: invisible="measurement_type != 'noise'"
  * Özel DÖF mesajlaşması (action_create_capa override)

FAZ 4 — Legislation (0/4, %0)
- Planlanan: isg_legislation, isg_obligation, isg_compliance, isg_penalty, isg_simulator

FAZ 5 — Reporting (1/3, %33)
- TAMAMLANDI: isg_reporting (TRIR/LWDR KPI)
- Planlanan: QWeb PDF sablonlari, Superset BI

OSGB — Uzman Planlama (0/1)

---

## Sunucu Yapisinda

Klasor: /opt/odoo/isg_addons/
Database: isg (PostgreSQL)
Modüller: 23 kurulu
Service: sudo systemctl status odoo18-isg.service

---

## Teknik Borclar

- isg_contractor.contractor_level — recursive=True eklenmeli
- isg_location.hazard_type — invisible parameter warning
- Record rule eksikleri
- Admin sifresi NULL
- SSH key setup deferred

---

## Snapshot Mimarisi (F3-001 Kritik Fikir)

Ölcüm kaydedildiginde:
1. Cihaz kalibrasyon bilgileri (tarih, sertifika, gecerlilik) DONDURULUR
2. Limit degerleri (OEL/STEL) versiyonlu tutulur
3. Ham sonuc asla degismez
4. Uygunluk hesaplamasi snapshot limite göre yapilir
5. Sonradan limit degisse bile eski olcum kaydı korunur

## Parametre Dispatch Mimarisi (F3-002 Kririk Fikir)

Ölçüm sonucu model'e inherit ile parametre-özel alanları eklenir:
1. measurement_type seçim alanı (gürültü / toz / titreşim / aydınlatma / ısıl konfor)
2. Her parametre türüne özel alanlar ekle (LAeq/LCeq/Lpeak for noise, etc)
3. View'da invisible="measurement_type != 'TYPE'" ile kontrol
4. Aynı pattern beş parametre için tekrarlanabilir
5. action_create_capa() override ile parametreye özel DÖF açıklaması

---

Son Güncelleme: 18 Ağustos 2026
Sürüm: 3.1 (23/32 modül, FAZ 3 %100)
GitHub: https://github.com/SHapeloglu/ISG
