# SESSION.md — Oturum Özeti (22 Ağustos 2026 — Session 4)

## 🎉 Mevcut Durum

**25/32 modül kurulu** | **FAZ 4-001 ✅ TAMAMLANDI**

### FAZ 0 — Temel Mimari (7/7 ✅)
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

### FAZ 1 — Kurumsal Yönetişim (5/6 ✅)
- isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- **Bekleyen:** F1-002 isg_health_basic (KVKK danışman onayı)

### FAZ 2 — Çekirdek ISG Operasyonları (9/9 ✅)
- isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw + isg_loto

### FAZ 3 — Ölçüm Yönetimi (2/2 ✅)
- F3-001 isg_measurement_core ✅ (kampanya, cihaz, numune, sonuç, limit — snapshot mimarisi)
- F3-002 isg_measurement_hygiene ✅ (gürültü parametreleri: LAeq, LCeq, Lpeak)

### FAZ 4 — Mevzuat Motoru (1/4 → 2/4 ✅)
- **F4-001 isg_legislation ✅ TAMAMLANDI** (Yükümlülük altyapısı: kanun, yükümlülük, uygulanabilirlik)
  - 3 model: isg.legislation, isg.obligation, isg.obligation.applicability
  - 7 mevzuat: 6331 Kanunu, İSG Hizmetleri YÖN, Risk Değerlendirmesi YÖN, Eğitim YÖN
  - 7 yükümlülük: Risk Değerlendirmesi, İşe Başlama Eğitimi, Uzman/Hekim Görevlendirilmesi, İSG Kurulu, Acil Durum Planı
  - Uygulanabilirlik kuralları: tehlike_sınıfı, min/max_employee, sector_type, NACE_kodu
  - Data dosyası: 7 legislation + 7 obligation + 7 applicability rules

### FAZ 5 — Raporlama (1/3)
- isg_reporting (TRIR/LWDR KPI) ✅

## Kurulu Modüller (25 toplam ISG)
isg_audit, isg_base, isg_board, isg_capa, isg_chemical,
isg_contractor, isg_core, isg_correspondence, isg_document,
isg_emergency, isg_equipment, isg_hr, isg_incident, 
isg_legislation **(NEW)**, isg_location,
isg_measurement_core, isg_measurement_hygiene, isg_party, isg_ppe, isg_ptw, isg_reporting,
isg_risk, isg_security, isg_training, isg_visitor

## Bu Oturumda Tamamlananlar (22 Ağustos 2026 — Session 4)

### F4-001 `isg_legislation` — Mevzuat ve Yükümlülük Motoru ✅ TAMAMLANDI

**3 Model:**
1. `isg.legislation` — Kanun/yönetmelik metadata
   - name, legislation_type, number, effective_date, amendment_date, source_url, notes
   - One2many: obligation_ids

2. `isg.obligation` — Yükümlülük
   - name, legislation_id, article, description
   - evidence_type (risk_assessment, training_record, expert_assignment, etc.)
   - is_periodic, periodic_days, retention_days
   - One2many: applicability_ids

3. `isg.obligation.applicability` — Uygulanabilirlik kuralları
   - obligation_id, danger_class, min_employee, max_employee
   - sector_type (public/private/both), nace_code, description

**Data (7 mevzuat, 7 yükümlülük):**
- 6331 Sayılı İSG Kanunu
- İSG Hizmetleri Yönetmeliği
- Risk Değerlendirmesi Yönetmeliği
- Çalışan Eğitimi Yönetmeliği (2 Nisan 2026 güncellemesi)
- + yükümlülükler ve uygulanabilirlik kuralları

**Technical Notes:**
- Manifest'te `base` bağımlılığı eklendi (CSV import zamanı registry problemi)
- ACL dosyası `ir.model.access.csv` (noktalar önemli!)
- Views: Odoo 18'de `<tree>` → `<list>`, embedded list `<tree>` → `<list>`
- Encoding: `# -*- coding: utf-8 -*-` eklendi
- Record rules: global read-only (mevzuat verileri merkezi veri seti olmalı)

**GitHub Commit:** c13c6fe

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
| **TOPLAM** | **32** | **25** | **%78** |

---

## Sıradaki İş

**A) F4-002 `isg_compliance` — Uygunluk Değerlendirmesi Motoru** (KRITIK)
- İşyeri profili → hangi yükümlülükler geçerli?
- Her yükümlülük için kanıt kontrolü
- Uygunluk snapshot (COMPLIANT / NON_COMPLIANT / PENDING / EXPIRED)
- DÖF otomatik üretimi

Bu modül olmadan HSE Radar'ın çekirdek özelliği ("sanal müfettiş") çalışmaz.

**B) F4-003 `isg_penalty` — İdari Para Cezaları (ÇSGB 2026)

**C) F4-004 `isg_simulator` — Müfettiş Simülatörü

---

## Komut Özeti

```bash
# Modül kurulum/güncelleme
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" \
  -d isg -i MODUL_ADI --stop-after-init 2>&1 | grep -E "ERROR|loaded" | tail -10
sudo systemctl start odoo18-isg.service
```

---

**Next:** F4-002 Uygunluk Değerlendirmesi Motoru
