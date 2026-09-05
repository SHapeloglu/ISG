# ARCHITECTURE.md — Seans 4 Güncellemesi (05 Eylül 2026)

## ✅ Tamamlanan (Seans 4)

### FAZ 5 — Raporlama (2/3)
- ✅ isg_reporting (F5-001)
- ✅ **F5-002: QWeb PDF Şablonları** (5 rapor şablonu kurulu)
  - Risk Değerlendirmesi (isg.risk.assessment)
  - Kaza/Ramak Kala (isg.incident)
  - Denetim (isg.audit)
  - Ekipman Periyodik Kontrol (isg.equipment.inspection) — EKİPNET
  - İş Hijyeni Ölçüm (isg.measurement.hygiene)
- ⏳ F5-003: HSE Radar Kabul Testi (27 işlev × 5 senaryo)

## Model Özeti
- **Toplam ISG Model:** 105+
- **Sequence Prefix:** ISG-XXX-YYYY-NNNN
- **ACL Grupları:** 5 (readonly, expert, physician, manager, superadmin)
- **Record Rule:** workplace + site + company iç içe
- **PDF Raporları:** 5 (Risk, Incident, Audit, Equipment, Measurement)

## Sıradaki Mimarı Tasarım
1. **F5-003 Kabul Testi** — 27 işlev senaryosu
2. **isg_tests Cleanup** — Alan validasyon + TransactionCase
3. **E2/E3 Entegrasyon** — SGK API, EKİPNET, KVKK maskeleme

**Tarih:** 05 Eylül 2026, 19:35 UTC
