# TASKS.md — Görev Listesi (14 Ağustos 2026 Güncellemesi)

## Tamamlanan Görevler ✅

### FAZ 0 — Temel Mimari ✅ TAMAMLANDI
- [x] F0-001 `isg_core`
- [x] F0-002 `isg_security`
- [x] F0-003 `isg_party`
- [x] F0-004 `isg_location`
- [x] F0-005 `isg_document`
- [x] F0-006 `isg_hr`
- [x] F0-007 `isg_base`

### FAZ 1 — Kurumsal Yönetişim ✅ TAMAMLANDI (F1-002 hariç)
- [x] F1-001 `isg_contractor`
- [x] F1-003 `isg_training`
- [x] F1-004 `isg_visitor`
- [x] F1-005 `isg_board`
- [x] F1-006 `isg_correspondence`

### FAZ 2 — Çekirdek İSG Operasyonları ✅ 6/9 TAMAMLANDI
- [x] F2-001 `isg_capa` — DÖF/CAPA
- [x] F2-002 `isg_risk` — Risk değerlendirmesi
- [x] F2-003 `isg_incident` — İş kazası
- [x] F2-004 `isg_audit` — Denetim
- [x] F2-005 `isg_ppe` — KKD yönetimi
- [x] F2-006 `isg_emergency` — Acil durum

---

## Devam Eden / Sıradaki Görevler 🔄

### FAZ 2 — Devam (Öncelik Sırası)

- [ ] **F2-007** `isg_chemical` — Kimyasal envanter ve SDS/GBF
      - Kimyasal envanter (marka, hazırlık tarihi, SDS dosyası)
      - GBF/SDS yönetimi (ir.attachment bağlantısı)
      - GHS sınıflama kategorileri
      - Depolama uyumluluk matrisi (temel)
      - Mevzuat: Kimyasal Maddeler Yönetmeliği

- [ ] **F2-008** `isg_equipment` — Ekipman ve periyodik kontrol (EKİPNET)
      - EK-II ekipman kataloğu (Ara.2025 güncellemesi)
      - Periyodik kontrol takvimi
      - EKİPNET hazırlık raporu
      - Yetkili muayene kuruluşu kaydı
      - Kontrol sonuç ve rapor

- [ ] **F2-009** `isg_ptw` + `isg_loto` — İş izni ve LOTO
      - İzin türleri (sıcak iş, kapalı alan, elektrik, yüksekte)
      - Ön koşul kontrol listeleri
      - Çok aşamalı onay zinciri
      - LOTO izolasyon nokta yönetimi
      - Süre ve uzatma kontrolleri

### FAZ 1 — Bekleyen
- [ ] **F1-002** `isg_health_basic` — Temel sağlık gözetimi + KVKK maskeleme
      ⚠️ KVKK mimarisi için danışman onayı bekliyor — EN SONA BIRAK

### FAZ 3 — Ölçüm ve Çevre (Planlanıyor)
- [ ] F3-001 `isg_measurement_core` + `isg_measurement_hygiene`
      - Ölçüm kampanyası ve numune yönetimi
      - Kalibrasyon snapshot ve sürüm yönetimi
      - Limit profili ve uygunluk değerlendirmesi
      - Yetkili laboratuvar onay akışı
      - Gürültü, toz, kimyasal, titreşim, ısıl, aydınlatma

- [ ] F3-002 `isg_environment` — Çevre etkileri analizi

### FAZ 4 — Sanal Müfettiş (Planlanıyor)
- [ ] F4-001 `isg_legislation` + `isg_obligation`
      - Mevzuat kaydı ve sürüm yönetimi
      - Yükümlülük tanımlama (kural motoru)
      - Uygulanabilirlik motoru (işyeri profili bazlı)
      - Mevzuat güncelleme akışı

- [ ] F4-002 `isg_compliance` — Uygunluk değerlendirmesi
      - Kanıt yönetimi
      - Snapshot (tarihi dondurma)
      - Uygunluk raporu

- [ ] F4-003 `isg_penalty` — Ceza ve yaptırımlar (2026 güncellemesi)
- [ ] F4-004 `isg_simulator` — Sanal müfettiş simülasyonu

### FAZ 5 — Raporlama (Planlanıyor)
- [ ] F5-001 `isg_reporting` + Superset entegrasyonu
- [ ] F5-002 QWeb PDF şablonları
- [ ] F5-003 HSE Radar kabul testi

### OSGB Modülü (Özel)
- [ ] `isg_osgb` — OSGB planlama ve görevlendirme motoru
      - Uzman/hekim atama
      - Kapasite planlama (6331 md.6 hesaplaması)
      - Ziyaret takvimi
      - İSG-KATİP bildirimi hazırlığı

---

## Bilinen Hatalar / Düzeltilecekler 🐛

- [ ] `isg_contractor` contractor_level — recursive=True eklenmeli
- [ ] `isg_location` hazard_type — unknown parameter 'invisible' WARNING
- [ ] `isg_visitor` ppe_notes — model seviyesinde invisible
- [ ] `isg_risk` site_id — NOT NULL constraint warning
- [ ] Admin şifresi — kalıcı şifre belirlenmeli

---

## İlerleme Özeti (14 Ağustos 2026)

| Faz | Toplam | Tamamlanan | % |
|-----|--------|------------|---|
| FAZ 0 | 7 | 7 | %100 |
| FAZ 1 | 6 | 5 | %83 |
| FAZ 2 | 9 | 6 | %67 |
| FAZ 3 | 2 | 0 | %0 |
| FAZ 4 | 4 | 0 | %0 |
| FAZ 5 | 3 | 0 | %0 |
| OSGB | 1 | 0 | %0 |
| **TOPLAM** | **32** | **18** | **%56** |

**Adam-gün**: ~65-75 / 200 (harcanmış) = %32-37 tamamlandı

---

## Definition of Done (Her Modül İçin)

- [ ] Odoo 18 uyumlu manifest
- [ ] Model alanları ve constraint'ler
- [ ] Liste, form, arama görünümleri
- [ ] Menü, action, sequence
- [ ] ACL ve record rule
- [ ] Mail activity ve bildirim
- [ ] Belge/kanıt bağlantısı (gerekiyorsa)
- [ ] Çok şirket/işyeri/site testleri
- [ ] Normal/olumsuz/yetkisiz akış testleri
- [ ] Türkçe alan metinleri
- [ ] Mevzuat uygunluk notu
