# ARCHITECTURE.md — Mimarı (Seans 4 Güncel)

## ✅ Tamamlanan (Seans 1-3)

### FAZ 0 — Temel Mimari (7/7)
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

### FAZ 1 — Kurumsal Yönetişim (5/6)
- isg_contractor, isg_training, isg_board, isg_correspondence, isg_visitor
- ⏳ isg_health_basic (KVKK bloklu)

### FAZ 2 — Operasyonel (9/9)
- isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_chemical, isg_equipment, isg_ptw, isg_emergency

### FAZ 3 — Ölçüm (3/3)
- isg_measurement_core, isg_measurement_hygiene, isg_environment

### FAZ 4 — Mevzuat (4/4)
- isg_legislation, isg_compliance, isg_penalty, isg_simulator

### OSGB (1/1)
- isg_osgb

### FAZ 5 — Raporlama (1/3)
- isg_reporting ✅
- ⏳ F5-002 (QWeb PDF şablonları)
- ⏳ F5-003 (HSE Radar Kabul Testi)

## Model Özeti
- **Toplam ISG Model:** 105+
- **Sequence Prefix:** ISG-XXX-YYYY-NNNN
- **ACL Grupları:** 5 (readonly, expert, physician, manager, superadmin)
- **Record Rule:** workplace + site + company iç içe

## Sıradaki Mimarı Tasarım
1. PDF şablonları (F5-002) — QWeb, Jinja2, dil desteği
2. Kabul testi (F5-003) — 27 işlev senaryosu
3. E2/E3 (isteğe bağlı) — API, maskeleme, entegrasyon

**Tarih:** 03 Eylül 2026, 08:40 UTC
