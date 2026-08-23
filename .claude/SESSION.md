# SESSION.md — Oturum Özeti (23 Ağustos 2026 — Session 5)

## 🎉 Mevcut Durum

**26/32 modül kurulu** | **FAZ 4-002 ✅ TAMAMLANDI**

### FAZ 0 — Temel Mimari (7/7 ✅)
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

### FAZ 1 — Kurumsal Yönetişim (5/6 ✅)
- isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- **Bekleyen:** F1-002 isg_health_basic (KVKK danışman onayı)

### FAZ 2 — Çekirdek ISG Operasyonları (9/9 ✅)
- isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw + isg_loto

### FAZ 3 — Ölçüm Yönetimi (2/2 ✅)
- F3-001 isg_measurement_core ✅ (snapshot mimarisi)
- F3-002 isg_measurement_hygiene ✅ (gürültü parametreleri)

### FAZ 4 — Mevzuat Motoru (2/4 → 3/4 ✅)
- **F4-001 isg_legislation ✅** (Yükümlülük altyapısı)
- **F4-002 isg_compliance ✅ TAMAMLANDI** (Uygunluk Değerlendirmesi Motoru — HSE Radar DNA)
- F4-003 isg_penalty (planlandı)
- F4-004 isg_simulator (planlandı)

### FAZ 5 — Raporlama (1/3)
- isg_reporting (TRIR/LWDR KPI) ✅

## Kurulu Modüller (26 toplam ISG)
isg_audit, isg_base, isg_board, isg_capa, isg_chemical,
isg_compliance **(NEW)**, isg_contractor, isg_core, isg_correspondence, isg_document,
isg_emergency, isg_equipment, isg_hr, isg_incident, 
isg_legislation, isg_location,
isg_measurement_core, isg_measurement_hygiene, isg_party, isg_ppe, isg_ptw, isg_reporting,
isg_risk, isg_security, isg_training, isg_visitor

## Bu Oturumda Tamamlananlar (23 Ağustos 2026 — Session 5)

### F4-002 `isg_compliance` — Uygunluk Değerlendirmesi Motoru ✅ TAMAMLANDI

**2 Model:**
1. `isg.compliance` — İşyeri uygunluk değerlendirmesi snapshot'ı
   - workplace_id, obligation_id, evaluation_date (donmuş), status, evidence_id, due_date, capa_id, evaluator_id
   - 4 durum: uygun / eksik / beklemede / vadesi_geçmiş
   - @api.model _compute_applicable_obligations(workplace_id) — isg.obligation.applicability kurallarına göre filtreleme
   - action_evaluate_compliance() — tüm uygulanabilir yükümlülükleri değerlendir, DÖF otomatik oluştur

2. `isg.compliance.evidence` — Kanıt kaydı
   - obligation_id, workplace_id, evidence_type, document_id
   - source_model / source_res_id — hangi modelden geldi
   - valid_from / valid_until (compute ile _compute_is_valid)
   - obligation.retention_days'ten valid_until otomatik hesapla

**Teknik Notlar:**
- Snapshot mimarisi: her değerlendirme yeni kayıt, üzerine yazma yok
- Evidence geçerlilik süresi: obligation.retention_days'ten hesaplanır
- Otomatik DÖF: eksik/vadesi_geçmiş kanıt → isg_capa oluştur
- ACL: readonly/expert/manager (3 seviye)
- Record rules: company_id bazında erişim kontrolü
- Views: list (badge widget), form, search (durum filtreleri, groupby)

**GitHub Commit:** f54bcc6

---

## İlerleme Özeti

| Faz | Toplam | Tamamlanan | % |
|-----|--------|------------|---|
| FAZ 0 | 7 | 7 | %100 |
| FAZ 1 | 6 | 5 | %83 |
| FAZ 2 | 9 | 9 | %100 |
| FAZ 3 | 2 | 2 | %100 |
| FAZ 4 | 4 | 2 | %50 |
| FAZ 5 | 3 | 1 | %33 |
| OSGB | 1 | 0 | %0 |
| **TOPLAM** | **32** | **26** | **%81** |

---

## Sıradaki İş

**A) F4-003 `isg_penalty` — İdari Para Cezaları (ÇSGB 2026)**
- Model: isg.penalty (yükümlülük → ceza miktarı)
- 2026 güncellemeleri ile ceza tarifeleri
- Otomatik ceza hesaplama (uyumsuzluk × tutar)

**B) F4-004 `isg_simulator` — Müfettiş Simülatörü**
- Kapsamlı uygunluk raporu (tüm yükümlülükler kontrol listesi)
- "Müfettiş gelirse ne bulur?" simülasyonu
- Denetim preparedness skorlaması

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

**Next:** F4-003 İdari Para Cezaları
