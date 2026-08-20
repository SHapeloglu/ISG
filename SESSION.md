# SESSION.md — Oturum Özeti (18 Ağustos 2026 — Session 2)

## 🎉 Mevcut Durum

**23/32 modül kurulu** | **FAZ 3-002 ✅ BAŞLANDI VE ÇALIŞIYOR**

### FAZ 0 — Temel Mimari (7/7 ✅)
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

### FAZ 1 — Kurumsal Yönetişim (5/6 ✅)
- isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- **Bekleyen:** F1-002 isg_health_basic (KVKK danışman onayı)

### FAZ 2 — Çekirdek ISG Operasyonları (9/9 ✅)
- isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw + isg_loto

### FAZ 3 — Ölçüm Yönetimi (2/2) — %100 ✅ TAMAMLANDI
- **F3-001 isg_measurement_core** ✅ (kampanya, cihaz, numune, sonuç, limit — snapshot mimarisi)
- **F3-002 isg_measurement_hygiene** ✅ (gürültü parametreleri: LAeq, LCeq, Lpeak)

### FAZ 5 — Raporlama (1/3)
- isg_reporting (TRIR/LWDR KPI) ✅

## Kurulu Modüller (23 toplam ISG)
isg_audit, isg_base, isg_board, isg_capa, isg_chemical,
isg_contractor, isg_core, isg_correspondence, isg_document,
isg_emergency, isg_equipment, isg_hr, isg_incident, isg_location,
isg_measurement_core, **isg_measurement_hygiene (NEW)**, isg_party, isg_ppe, isg_ptw, isg_reporting,
isg_risk, isg_security, isg_training, isg_visitor

## Bu Oturumda Tamamlananlar (18 Ağustos 2026 — Session 2)

### F3-002 `isg_measurement_hygiene` — Hijyen Parametreleri Uzantısı
- **Model:** `isg.measurement.result`'u inherit ederek gürültüye özel alanlar ekledi
- **measurement_type seçim alanı:** Gürültü / Toz / Titreşim / Aydınlatma / Isıl Konfor (şimdilik Gürültü aktif)
- **Gürültü (Noise) alanları:**
  - `laeq_value` (dB) — A-ağırlıklı eşdeğer ses basınç seviyesi
  - `lceq_value` (dB) — C-ağırlıklı eşdeğer ses basınç seviyesi
  - `lpeak_value` (dB) — Tepe ses basınç seviyesi
  - `lpeak_reference` (dB, default 140) — ÇSGB tepe limit
- **View:** `isg_measurement_result_form_hygiene` — `invisible="measurement_type != 'noise'"` ile kontrol
- **Özel DÖF açıklaması:** `action_create_capa()` gürültü ölçümleri için parametreye özel mesaj üretir

**Teknik Özellikler:**
- 1 model (inherit), 1 view (extend)
- XML view inheritance — Odoo 18 native
- Parametre-türü dispatch pattern — toz/titreşim/aydınlatma/ısıl konfor için tekrarlanabilir
- Mevzuat uyumu: ÇSGB Lpeak 140 dB default limiti

**Mevzuat Uyumu:**
- Türkiye ÇSGB gürültü ölçüm standartları
- LAeq TWA (8 saat ağırlıklı ortalama) — isg_measurement_core limit'e karşılaştırma
- Lpeak STEL (15 dk kısa süreli) → 140 dB mevzuat limiti
- OEL/STEL limit aşımında otomatik DÖF (limit aşımında severity=high/medium)

**Bilinen Sınırlamalar:**
- Toz / Titreşim / Aydınlatma / Isıl Konfor alanları ileride eklenecek (aynı pattern kullanarak)
- Limit seçim otomasyonu ileride (measurement_type'a göre otomatik limit tıklanabilir)
- Laboratuvar raporu onay workflow'u ileride (F3-002 sonrası)

## İlerleme

| Faz | Toplam | Tamamlanan | % |
|-----|--------|------------|---|
| FAZ 0 | 7 | 7 | %100 |
| FAZ 1 | 6 | 5 | %83 |
| FAZ 2 | 9 | 9 | %100 |
| FAZ 3 | 2 | 2 | %100 |
| FAZ 4 | 4 | 0 | %0 |
| FAZ 5 | 3 | 1 | %33 |
| OSGB | 1 | 0 | %0 |
| **TOPLAM** | **32** | **23** | **%72** |

## Sıradaki İş (Seçenekler)

**A) F3-002 Devam:** Toz / Titreşim / Aydınlatma / Isıl Konfor parametrelerini ekle (aynı pattern)
- Her parametre 30 dk (örn: toz için solunum/inhalasyon fraksiyonu, titreşim için el-kol/beden seçim)
- Hızlı ve tekrarlı

**B) F4-001 Atla:** Mevzuat Motoru'na geç (35-50 AD)
- HSE Radar'ın gerçek DNA'sı — "uygunluk değerlendirmesi"
- Daha ağır, daha kritik
- Uzman onayı gerekli

**Önerim:** **A → B sırası**. Ölçüm modülü hava gibi davranıyorken tamamlarsak (5 parametre = ~3 gün), sonra FAZ 4 mevzuat motoruna hazırız ve HSE Radar'ın %90'ı biter.

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

**Next:** F3-002 Devam (Toz/Titreşim/Aydınlatma/Isıl Konfor) mi yoksa FAZ 4 Mevzuat Motoru'na geçelim mi?
