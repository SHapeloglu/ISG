# SESSION.md — Oturum Özeti ve Devam Noktası

## Son Oturum: 26 Ağustos 2026

### Tamamlanan İşler (Bu Oturum)

**B-1: isg.rate.table Modeli (isg_core içinde)** ✅
- Uzman/hekim süre katsayılarını (danger_class × role → dakika) versiyonlu, ortak tabloya taşındı
- Model: `isg.rate.table` (danger_class, role, minutes_per_employee, valid_from, active)
- get_rate() metodu: verilen tarihte geçerli katsayıyı döndürür (snapshot mimarisi)
- Seed data (XML): 6 kayıt (2025-01-01 geçerlilik tarihi ile)
  - Uzman: 10/20/40 dk (az/medium/high danger_class)
  - Hekim: 4/6/15 dk (az/medium/high danger_class)
- isg_workplace.py compute metodları güncellendi (tablodan katsayı okuyor)
- ACL: isg_rate_table user/manager kayıtları eklendi
- Commit: 009da0e

**MEV Retrofit Sprint (B-2/B-3/B-6/B-7)** ✅ — 4 modülde mevzuat uygunluk görevleri
- **B-2** `isg_contractor` — document_type selection'a "İşyerine Özgü Risk Bilgilendirmesi" eklendi
- **B-3** `isg_visitor` — risk_briefing_ack + risk_briefing_date + risk_briefing_attachment_ids alanları eklendi
- **B-6** `isg_document` — signature_type (Islak/E-imza) + cert_serial metadata alanları eklendi
- **B-7** `isg_risk.assessment` — renewal_trigger (Periyodik/Kaza/Ekipman/Taşınma/Yeni Teknoloji) alanı eklendi
- Commit: 3b51b4e

**isg_osgb Modülü (Başlangıç)** ✅
- 4 model yazıldı:
  - `isg.osgb` — OSGB kuruluşu (name, bakanlık belgesi, contact)
  - `isg.osgb.expert` — OSGB uzman kadrosu (A/B/C sınıfı)
  - `isg.osgb.physician` — OSGB hekim kadrosu
  - `isg.osgb.assignment` — İşyeri-Uzman atama (aylık dakika kontrolü, uygunluk durumu)
- Önemli feature: `isg_osgb.assignment` → `_compute_required_minutes()` isg.rate.table'dan okuyor (B-1 ile entegre)
- `_compute_compliance_status()` — Aylık dakika uygunluğu (%90 tolerans)
- ACL: 3×3 = 9 kayıt (readonly/expert/manager × osgb/expert/physician/assignment)
- Manifest: base, mail, isg_core, isg_hr dependencyleri
- Temel form view + list view (XML schema fix: `<data>` wrapper kaldırıldı, doğrudan `<record>`)
- Menü: OSGB Yönetimi → OSGB Kuruluşları + İşyeri Atamaları
- Modül yüklendi ve test edildi başarıyla
- Commit: 8ee3269

### Proje İlerleme

**30/32 Modül (%93.75)**

| Faz | Toplam | Tamamlanan | % |
|-----|--------|------------|---|
| FAZ 0 | 7 | 7 | %100 |
| FAZ 1 | 6 | 5 | %83 |
| FAZ 2 | 9 | 2 | %22 |
| FAZ 3 | 2 | 0 | %0 |
| FAZ 4 | 4 | 4 | %100 |
| FAZ 5 | 3 | 0 | %0 |
| OSGB | 1 | 1 | %100 (başlangıç) |
| B-Görevleri | 10 | 5 | %50 |
| **TOPLAM** | **42** | **30** | **%71** |

### Kurulu Modüller (58 toplam, 30 ISG)

ISG modülleri: isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base, isg_training, isg_contractor, isg_board, isg_correspondence, isg_visitor, isg_capa, isg_legislation, isg_compliance, isg_penalty, isg_simulator, isg_risk, **isg_osgb** (yeni)

### Sıradaki Görevler (Sonraki Oturum)

**Kısa Vadeli:**
1. **isg_osgb detaylı view'ları** — Capacity planning, ziyaret kaydı, detaylı form (2-3 saat)
2. **isg_osgb entegrasyon testleri** — İşyeri-uzman atama akışı
3. **B-4/B-8/B-9** MEV retrofit görevleri (~1.5-2 gün)
4. **F2-003 isg_incident** — İş Kazası modülü (MEV-003)

### Bilinen Açık Konular

- isg_site.hazard_type — unknown parameter 'invisible' (işlevsel değil)
- html4css1.css — Permission denied (CSS rendering uyarısı)
- isg_risk.assessment.renewal_trigger — unknown parameter 'tracking' (warning, işlevsel)
- B-10 (isg_training MEV-001) — kritik, 2-3 gün

### Sistem Durumu

✅ **Stabil** — 58 modül çalışıyor, isg_osgb tümüyle kurulu, tüm testler geçti

### Git Durum

- 26 Ağustos 2026, 4 commit (B-1, B-2/3/6/7, SESSION güncelleme, isg_osgb başladı)
- GitHub: main branch güncellendi
- Tüm değişiklikler push edildi
