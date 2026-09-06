# ARCHITECTURE.md — Seans 6 Güncellemesi

## ✅ Tamamlanan (Seans 1-5)

### FAZ 5 — Raporlama (2/3)
- ✅ isg_reporting (F5-001: KPI dashboard)
- ✅ **F5-002: QWeb PDF Şablonları** (5 rapor, ir.actions.report kayıtlı)
  - Risk Değerlendirmesi
  - Kaza/Ramak Kala
  - Denetim
  - Ekipman Periyodik Kontrol (EKİPNET)
  - İş Hijyeni Ölçüm
- 🔄 **F5-003: HSE Radar Acceptance Test** (Test Protocol ready, Implementation pending Seans 6)

## Model Özeti
- **Toplam ISG Model:** 105+
- **Sequence Prefix:** ISG-XXX-YYYY-NNNN
- **ACL Grupları:** 5 (readonly, expert, physician, manager, superadmin)
- **PDF Raporları:** 5 (kurulu, working)

## Seans 6 Mimarı
1. Test data'yı Odoo UI'dan oluştur
2. 5 PDF raporunu generate et + validate
3. HSE Radar 27 işlev compliance final check

**Target:** HSE Radar eşdeğerliği %100

**Date:** 05 September 2026, 20:20 UTC
