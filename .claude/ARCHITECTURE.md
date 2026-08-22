# ARCHITECTURE.md — ISG Platform Mimarisi (22 Ağustos 2026)

## Genel Bakış

ISG Platform, Odoo 18 üzerine kurulu, Türkiye'nin 6331 Kanunu ve ilgili yönetmeliklere uyumlu, kurumsal ISG yönetim sistemidir.

**Platform:** Odoo 18.0 | **DB:** PostgreSQL | **VPS:** Contabo | **Version:** GitHub SHapeloglu/ISG | **25/32 Modül (%78)**

---

## Modül Hiyerarşisi

### FAZ 0 — Foundation (7/7 ✅)
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

### FAZ 1 — Governance (5/6, %83)
- isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- Bekleyen: isg_health_basic (KVKK onayı)

### FAZ 2 — Core Operations (9/9 ✅)
- isg_capa, isg_risk, isg_incident, isg_audit, isg_emergency, isg_ppe, isg_chemical, isg_equipment, isg_ptw+isg_loto

### FAZ 3 — Measurement (2/2 ✅)
- isg_measurement_core ✅
- isg_measurement_hygiene ✅

### FAZ 4 — Legislation (1/4)
- **isg_legislation ✅**
  * isg.legislation: Kanun/yönetmelik metadata
  * isg.obligation: Yükümlülük tanımı + kanıt türü + saklama süresi
  * isg.obligation.applicability: Uygulanabilirlik kuralları (danger_class, min_employee, sector_type, NACE)
- Planlanan: isg_compliance, isg_penalty, isg_simulator

### FAZ 5 — Reporting (1/3)
- isg_reporting ✅ (TRIR/LWDR KPI)
- Planlanan: QWeb PDF şablonları, Superset BI

### OSGB — Uzman Planlama (0/1)

---

## Kritik Mimariler

### 1. Snapshot Mimarisi (F3-001)
Ölçüm kaydedildiginde:
1. Cihaz kalibrasyon bilgileri (tarih, sertifika, gecerlilik) DONDURULUR
2. Limit degerleri (OEL/STEL) versiyonlu tutulur
3. Ham sonuc asla degismez
4. Uygunluk hesaplamasi snapshot limite göre yapilir
5. Sonradan limit degisse bile eski olcum kaydı korunur

### 2. Parametre Dispatch Mimarisi (F3-002)
Ölçüm sonucu model'e inherit ile parametre-özel alanları eklenir:
1. measurement_type seçim alanı (gürültü / toz / titreşim / aydınlatma / ısıl konfor)
2. Her parametre türüne özel alanlar ekle (LAeq/LCeq/Lpeak for noise, etc)
3. View'da invisible="measurement_type != 'TYPE'" ile kontrol
4. Aynı pattern beş parametre için tekrarlanabilir
5. action_create_capa() override ile parametreye özel DÖF açıklaması

### 3. Mevzuat Altyapısı (F4-001) — NEW!
Türkiye İSG mevzuatının merkezi kaydı:

1. **isg.legislation**: Kanun/yönetmelik metadata
   - name, legislation_type, number, effective_date, amendment_date
   - source_url, notes
   - One2many: obligation_ids

2. **isg.obligation**: Yükümlülük tanımı
   - name, legislation_id, article, description
   - evidence_type: risk_assessment, training_record, expert_assignment, physician_assignment, emergency_plan, audit_checklist, equipment_report, chemical_inventory, permit_to_work, incident_report, other
   - is_periodic, periodic_days (tekrarlanan görevler)
   - retention_days (kanıt saklama süresi)
   - One2many: applicability_ids

3. **isg.obligation.applicability**: Uygulanabilirlik kuralları
   - obligation_id, danger_class, min_employee, max_employee
   - sector_type (public/private/both), nace_code, description
   - "Bu yükümlülük kime uygulanır?" kuralları

**Veri Tabanı (7 mevzuat, 7 yükümlülük):**
- 6331 Sayılı İSG Kanunu
- İSG Hizmetleri Yönetmeliği
- Risk Değerlendirmesi Yönetmeliği
- Çalışan Eğitimi Yönetmeliği (2 Nisan 2026 güncellemesi)
- + 3 temel yükümlülük türü ve uygulanabilirlik kuralları

### 4. Uygunluk Değerlendirmesi Motoru (F4-002 — PLANLANAN)
İşyeri profili → Otomatik yükümlülük hesaplama → Kanıt kontrolü → Uygunluk snapshot

1. İşyeri profili girilir (NACE, danger_class, employee_count, sector_type)
2. isg.obligation.applicability kurallarına göre geçerli yükümlülükler otomatik hesaplanır
3. Her yükümlülük için kanıt taraması yapılır (ir.attachment, isg.document)
4. Uygunluk snapshot: COMPLIANT / NON_COMPLIANT / PENDING / EXPIRED
5. Kanıt eksik → DÖF otomatik oluştur

**Bu mimarinin sorgu kompleksitesi O(n) olmaması için indexed yapmak gerekir.**

---

## Sunucu Yapısında

Klasör: /opt/odoo/isg_addons/
Database: isg (PostgreSQL)
Modüller: 25 kurulu
Service: sudo systemctl status odoo18-isg.service

---

## Teknik Borclar

- isg_contractor.contractor_level — recursive=True eklenmeli
- isg_location.hazard_type — invisible parameter warning
- Record rule eksikleri
- Admin sifresi NULL
- SSH key setup deferred

---

Son Güncelleme: 22 Ağustos 2026
Sürüm: 5.0 (25/32 modül, FAZ 4-001 tamamlandı, %78 ilerleme)
GitHub: https://github.com/SHapeloglu/ISG
