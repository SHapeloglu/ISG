# SESSION.md — Oturum Özeti (18 Ağustos 2026)

## 🎉 Mevcut Durum

**22/32 modül kurulu** | **FAZ 3-001 ✅ TAMAMLANDI**

### FAZ 0 — Temel Mimari (7/7 ✅)
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

### FAZ 1 — Kurumsal Yönetişim (5/6 ✅)
- isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- **Bekleyen:** F1-002 isg_health_basic (KVKK danışman onayı)

### FAZ 2 — Çekirdek ISG Operasyonları (9/9 ✅)
- isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw + isg_loto

### FAZ 3 — Ölçüm Yönetimi (1/2)
- **F3-001 isg_measurement_core ✅ TAMAMLANDI**
  - isg_measurement_campaign (Yıllık ölçüm planı)
  - isg_measurement_device (Cihazlar + kalibrasyon takibi)
  - isg_measurement_sample (Numune noktaları + SEG bağlantı)
  - isg_measurement_result (Ham sonuçlar, snapshot/dondurulmuş kalibrasyon + limit bilgisi, uygunluk hesaplama, otomatik DÖF tetikleme)
  - isg_measurement_limit (OEL/STEL limit değerleri, versiyonlu mevzuat)

### FAZ 5 — Raporlama (1/3)
- isg_reporting (TRIR/LWDR KPI) ✅

## Kurulu Modüller (22 toplam ISG)
isg_audit, isg_base, isg_board, isg_capa, isg_chemical,
isg_contractor, isg_core, isg_correspondence, isg_document,
isg_emergency, isg_equipment, isg_hr, isg_incident, isg_location,
isg_measurement_core (NEW), isg_party, isg_ppe, isg_ptw, isg_reporting,
isg_risk, isg_security, isg_training, isg_visitor

## İlerleme
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

## Bu Oturumda Tamamlananlar (18 Ağustos 2026)

### F3-001 `isg_measurement_core` — Ölçüm Yönetimi Çekirdeği
- **`isg.measurement.campaign`** — Yıllık ölçüm planı (yıl, parametre, lokasyon, periyot, durum makinesi)
- **`isg.measurement.device`** — Ölçüm cihazları + kalibrasyon yönetimi (cihaz türü, kalibrasyon tarihi/sertifika, geçerlilik son tarihi, kalibrasyonun süresi geçmiş check'i)
- **`isg.measurement.sample`** — Numune noktaları (kampanya içinde, SEG bağlantı, etkilenen çalışanlar, durum makinesi)
- **`isg.measurement.result`** — **SNAPSHOT MIMARISI** (EN KRİTİK):
  - Ham ölçüm değeri (read-only dondurulmuş)
  - Cihaz kalibrasyon snapshot (ölçüm anındaki durum → sonradan değişse bile kayıt bozulmaz)
  - Limit snapshot (OEL/STEL değerleri versiyonlu → "2024 mevzuatına göre uygundu ama 2026'da aşım" durumunu yönetebiliyor)
  - Uygunluk hesaplama: raw_value ≤ limit_twa_snapshot → COMPLIANT, yoksa EXCEEDING + yüzde
  - Otomatik DÖF tetikleme: limit aşımında action_create_capa() → isg_capa ile integrasyon
- **`isg.measurement.limit`** — OEL/STEL limit değerleri kataloğu (mevzuat versiyonlu: 2024/2025/2026/AB CLP)

**Teknik Özellikler:**
- 5 model, 15 security rule (readonly/expert/manager × 5 model)
- Snapshot pattern: create() sırasında cihaz/limit bilgileri dondurulur (@api.model_create_multi ile)
- Compute fields: compliance_status, exceeding_value, exceeding_percentage (store=True)
- Menu: Ölçüm Yönetimi (5 submenu) + isg_core.menu_isg_root'a bağlı

**Mevzuat Uyumu:**
- Türkiye ÇSGB ölçüm standardları (gürültü, toz, kimyasal, titreşim, aydınlatma, ısıl konfor)
- Yetkili laboratuvar raporu onay akışı (F3-001 altyapısı, tam onay ileride)
- EKİPNET hazırlık (equipment modülü ile entegrasyon hazır)

**Bilinen Sınırlamalar:**
- Limit veri seti henüz dolu değil (ÇSGB/AB kaynaklarından uzman doğrulaması gerekli)
- Ölçüm labortuvarı/yetki onay workflow'u F3-002'de (isg_measurement_hygiene + entegrasyon)
- Numune noktası duplicate/çakışma kontrolleri ileride

## Sıradaki İş
**FAZ 3 devam:**
- F3-002: `isg_measurement_hygiene` — Gürültü/toz/titreşim/aydınlatma/ısıl konfor parametrelerine özel alanlar + formüller
- F3-003: `isg_environment` — Çevre izleme (ambient gürültü, fabrika ortamı kalitesi)

**Ardından FAZ 4:**
- F4-001: `isg_legislation` + `isg_obligation` — Mevzuat motoru (HSE Radar'ın çekirdek özelliği)

## Bilinen Açık Konular (BACKLOG)
- `isg_contractor.contractor_level` — recursive=True eklenmeli
- `isg_location.hazard_type` — unknown parameter 'invisible' WARNING
- Admin şifresi — kalıcı olarak belirlenmeli
- `isg_health_basic` (F1-002) — KVKK danışman onayı bekliyor

## Komut Özeti (Hatırlatma)

```bash
# Modül güncelle
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" \
  -d isg -u MODUL_ADI --stop-after-init 2>&1 | grep -E "ERROR|loaded" | tail -10
sudo systemctl start odoo18-isg.service

# Durum kontrol
sudo systemctl status odoo18-isg.service
```

---

**Next Chat:** FAZ 3-002 isg_measurement_hygiene modülü — parametre-özel ölçüm alanları (gürültü level formülleri, toz fraction seçimi, vb.)
