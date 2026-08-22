# SESSION.md — Oturum Özeti (22 Ağustos 2026 — Session 3)

## 🎉 Mevcut Durum

**24/32 modül kurulu** | **FAZ 4-001 ✅ BAŞLANDI**

### FAZ 0 — Temel Mimari (7/7 ✅)
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

### FAZ 1 — Kurumsal Yönetişim (5/6 ✅)
- isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- **Bekleyen:** F1-002 isg_health_basic (KVKK danışman onayı)

### FAZ 2 — Çekirdek ISG Operasyonları (9/9 ✅)
- isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw + isg_loto

### FAZ 3 — Ölçüm Yönetimi (2/2 ✅)
- **F3-001 isg_measurement_core** ✅ (kampanya, cihaz, numune, sonuç, limit — snapshot mimarisi)
- **F3-002 isg_measurement_hygiene** ✅ (gürültü parametreleri: LAeq, LCeq, Lpeak)

### FAZ 4 — Mevzuat Motoru (1/4)
- **F4-001 isg_legislation** ✅ (Yükümlülük altyapısı: kanun, yükümlülük, uygulanabilirlik)

### FAZ 5 — Raporlama (1/3)
- isg_reporting (TRIR/LWDR KPI) ✅

## Kurulu Modüller (24 toplam ISG)
isg_audit, isg_base, isg_board, isg_capa, isg_chemical,
isg_contractor, isg_core, isg_correspondence, isg_document,
isg_emergency, isg_equipment, isg_hr, isg_incident, isg_legislation **(NEW)**, isg_location,
isg_measurement_core, isg_measurement_hygiene, isg_party, isg_ppe, isg_ptw, isg_reporting,
isg_risk, isg_security, isg_training, isg_visitor

## Bu Oturumda Tamamlananlar (22 Ağustos 2026 — Session 3)

### F4-001 `isg_legislation` — Mevzuat Motoru Başladı
- **3 model tasarımı:**
  1. `isg.legislation` — Kanun/yönetmelik metadata (ad, tür, no, yürürlük tarihi, kaynak URL)
  2. `isg.obligation` — Yükümlülük (ad, kanıt türü, saklama süresi, periyotluk)
  3. `isg.obligation.applicability` — Uygulanabilirlik kuralları (danger_class, min_employee, sektor, NACE)

- **Kanıt türleri (Evidence Types):**
  - Risk Değerlendirmesi Raporu
  - Eğitim Kaydı
  - Uzman Atama Belgesi
  - Hekim Atama Belgesi
  - Acil Durum Planı
  - Denetim Kontrolü
  - Ekipman İnceleme Raporu
  - Kimyasal Envanter
  - İzinli Çalışma İzni
  - Kaza Raporu
  - Diğer

- **View Architecture:**
  - List views (Mevzuat listesi, Yükümlülükler listesi)
  - Form views (detaylı edit)
  - Search views (filtreleme)
  - Menu structure: Mevzuat → Yükümlülükler (submenu)

- **Security (3-level ACL):**
  - readonly: sadece okunabilir
  - expert: okuma + yazma (oluşturma yok)
  - manager: tam kontrol (silme dahil)

**Mevzuat Uyumu:**
- Türkiye 6331 Kanunu temel yapısı
- Yönetmelik, Tebliğ, Yönerge, Rehber türleri
- Periyodik yükümlülükler (eğitim = 365 gün, vb.)
- NACE sektör kodları desteği

**Teknik Özellikler:**
- `retention_days`: Kanıt saklama süresi (2 yıl = 730, 5 yıl = 1825)
- `is_periodic` + `periodic_days`: Tekrarlanan görevler
- `applicability_ids` One2many: Her yükümlülüğe birden fazla kural
- `danger_class` seçim: Az Tehlikeli / Tehlikeli / Çok Tehlikeli

**Sıradaki (F4-002+):**
- İşyeri profili "uygulanabilir yükümlülükler" otomatik hesaplama motoru
- Kanıt kontrolü ve uygunluk değerlendirmesi
- İdari para cezaları (2026 ÇSGB güncellemesi)
- Müfettiş simülatörü (HSE Radar'ın "danışman" haline getirme)

## İlerleme

| Faz | Toplam | Tamamlanan | % |
|-----|--------|------------|---|
| FAZ 0 | 7 | 7 | %100 |
| FAZ 1 | 6 | 5 | %83 |
| FAZ 2 | 9 | 9 | %100 |
| FAZ 3 | 2 | 2 | %100 |
| FAZ 4 | 4 | 1 | %25 |
| FAZ 5 | 3 | 1 | %33 |
| OSGB | 1 | 0 | %0 |
| **TOPLAM** | **32** | **24** | **%75** |

## Sıradaki İş

**A) F4-002 `isg_compliance` — Uygunluk Değerlendirmesi**
- Her yükümlülük için "kanıt bulunuyor mu?" kontrol motoru
- İşyeri profile göre "hangi yükümlülükler geçerli?" otomatik hesaplama
- Uygunluk snapshot (tarih, kanıt, uygun/uyumsuz)

**B) F4-003 `isg_penalty` — İdari Para Cezaları**
- ÇSGB 2026 güncellenmiş ceza tarifesi
- Yükümlülük aşımında otomatik ceza hesapla

**C) F4-004 `isg_simulator` — Müfettiş Simülatörü**
- HSE Radar'ın ruh: "Eğer böyle bir denetim olsa, hangi sonuç alır?"
- Tüm yükümlülükler kontrol raporu

**Önerim:** **A → B → C** sırası. Uygunluk motoru olmadan cezalar ve simülatör çalışmaz.

## Komut Özeti

```bash
# Modül kurulum akışı
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" \
  -d isg -i MODUL_ADI --stop-after-init 2>&1 | grep -E "ERROR|loaded" | tail -10
sudo systemctl start odoo18-isg.service
```

---

**Next:** F4-002 Uygunluk Değerlendirmesi mi yoksa F3-002 Devam (Toz/Titreşim/Aydınlatma/Isıl Konfor) mi?
