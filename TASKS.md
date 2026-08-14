# TASKS.md — Proje İş Planı ve İlerleme

## Proje Durumu: %60 FAZ 2 Tamamlandı

### FAZ 0 — Temel Mimari ✅ TAMAMLANDI
- [x] Veri modeli, sequence, security groups
- [x] İSG ana menü yapısı
- [x] Base model templates (mail.thread, record rule, ACL)

### FAZ 1 — Kurumsal Yönetişim (13 modül) ✅ TAMAMLANDI
- [x] F1-001 `isg_core` — İşyeri, lokasyon, işçi sağlığı uzmanı, OSGB
- [x] F1-002 `isg_security` — Güvenlik grupları, menü, API
- [x] F1-003 `isg_party` — Şirket, personel, iletişim bilgileri
- [x] F1-004 `isg_location` — Lokasyon/site, tehlike sınıfı, depo
- [x] F1-005 `isg_document` — Belge tabanı, yönetim sistemi
- [x] F1-006 `isg_hr` — Çalışan, KKD beden ölçüleri, eğitim saatleri, sağlık muayene
- [x] F1-007 `isg_base` — İstenmeyen etkinlik kuralları, uyarılar
- [x] F1-008 `isg_training` — Eğitim planı, periyodik takvim, muafiyet
- [x] F1-009 `isg_contractor` — Alt işveren, işçi kontrol, ihraç
- [x] F1-010 `isg_board` — İSG Kurulu, karar ve tutanaklar
- [x] F1-011 `isg_correspondence` — Müfettiş yazışması, resmi yazı
- [x] F1-012 `isg_visitor` — Ziyaretçi, KKD muhasebesi, iç prosedür
- [x] F1-013 `isg_health_basic` — Sağlık muayene, ruh sağlığı değerlendirmesi

### FAZ 2 — Çekirdek İSG Operasyonları (32 modül planlı, 5 tamamlandı)

**Tamamlanan:**
- [x] F2-001 `isg_capa` — DÖF (Düzeltici/Önleyici Faaliyet), takip, tutma belgesi
- [x] F2-002 `isg_risk` — Risk Değerlendirmesi, L Matrisi + Fine-Kinney, yenileme
- [x] F2-003 `isg_incident` — İş kazası, ramak kala, SGK 3 gün takibi
- [x] F2-004 `isg_audit` — Denetim, kontrol listesi, bulgu kaydı
- [x] F2-005 `isg_ppe` — KKD yönetimi, zimmet, envanter
- [x] F2-006 `isg_emergency` — Acil durum planı, tatbikat

**Devam Ediyor / Planlanıyor:**
- [ ] **F2-007 `isg_chemical`** (ÖNCELİK: Kimyasal envanter, OEL/STEL tablosu, MSDS, depolama matrisi) — BAŞLANACAK
- [ ] F2-008 `isg_equipment` — Ekipman periyodik kontrol, bakım takvimi
- [ ] F2-009 `isg_ptw` — İş İzni (PTW) sistemi
- [ ] F2-010 `isg_loto` — LOTO (Lockout Tagout) kaydı
- [ ] F2-011 `isg_confined_space` — Kapalı alan çalışması
- [ ] F2-012 `isg_hot_work` — Sıcak işler, ateşli işler
- [ ] F2-013 `isg_excavation` — Kazı / Hafriyat
- [ ] F2-014 `isg_scaffold` — İskele / Çatı Güvenliği
- [ ] F2-015 `isg_electrical` — Elektriksel çalışmalar, yüksek gerilim
- [ ] F2-016 `isg_noise` — Gürültü ölçümü, OEL
- [ ] F2-017 `isg_vibration` — Titreşim ölçümü
- [ ] F2-018 `isg_lighting` — Aydınlatma ölçümü (lux)
- [ ] F2-019 `isg_air_quality` — Hava kalitesi ölçümü, partikül
- [ ] F2-020 `isg_ergonomics` — Ergonomi değerlendirmesi
- [ ] F2-021 `isg_psychosocial` — Psikososyal risk değerlendirmesi, stres
- [ ] F2-022 `isg_biological` — Biyolojik tehlike, universal precautions
- [ ] F2-023 `isg_fire_safety` — Yangın güvenliği, söndürücü, acil çıkış
- [ ] F2-024 `isg_hazmat` — Tehlikeli madde taşıması
- [ ] F2-025 `isg_vehicle` — Araç güvenliği, telematics
- [ ] F2-026 `isg_contractor_supervision` — Alt işveren denetimi (işyeri ziyareti)
- [ ] F2-027 `isg_accident_investigation` — Kaza soruşturması (beş neden analizi)
- [ ] F2-028 `isg_near_miss_tracking` — Ramak kala analiz (opsiyonel, incident'te birleştirilebilir)
- [ ] F2-029 `isg_medical_removal` — Tıbbi çıkarma prosedürü
- [ ] F2-030 `isg_occupational_disease` — Mesleki hastalık kaydı
- [ ] F2-031 `isg_statistics` — İstatistik, raporlama (TRIR, LWDR, vb.)
- [ ] F2-032 `isg_audit_action_plan` — Denetim sonrası aksiyon planı ve izleme

### FAZ 3 — İleri Yönetim & Entegrasyon (İleriki)
- [ ] Muhasebe entegrasyonu (kaza masrafları, DÖF maliyeti)
- [ ] İş Emri (MRP) entegrasyonu (KKD yenileme, ekipman bakım)
- [ ] HR Özlük Dosyası (eğitim, muayene, iş geçmişi)
- [ ] Uyum Raporlaması (mevzuat matrix)
- [ ] İSG-KATİP sistemi (muvazzaf İSG sorumlusu yönetimi, aylık rapor)

### HSE Radar Paritesi Hedefi

Şu anda HSE Radar fonksiyonlarının ~60%'i kapsanmış durumda:
- ✅ Risk Değerlendirmesi
- ✅ İş Kazası Takibi
- ✅ Denetim & Bulgu
- ✅ KKD Yönetimi
- ✅ Acil Durum Planı
- ⏳ Kimyasal Envanter (devam ediyor)
- ⏳ Ekipman Güvenliği (planlanıyor)
- ⏳ İş İzni Sistemi (planlanıyor)

### Bilinen Açık Konular (BACKLOG)

**Teknik Borç:**
1. isg_contractor.contractor_level — recursive=True bug (önceki oturumda not düşüldü)
2. isg_location.hazard_type — unknown parameter 'invisible' (view yükselmesi gerekiyor)
3. isg_ppe.type.size_type — unknown parameter 'invisible' (view yükselmesi gerekiyor)
4. isg_health_basic — KVKK danışman yönetimi eksik
5. isg_risk_line + isg_audit_line — record rule eksik (cross-company isolation)

**Feature Borcu (HSE Radar'ın Ötesi):**
1. İstatistik paneli (TRIR, LWDR, frequency rate)
2. Muhasebe entegrasyonu (kaza masrafları)
3. Otomatik e-posta bildirimleri (kaza, DÖF gecikme, tatbikat hatırlatıcısı)
4. Excel/PDF rapor şablonları
5. Mobil uygulama (KKD zimmet, tatbikat kontrol)

### Sıradaki Geliştirmeler (Şimdiden Ola)

- **F2-007 `isg_chemical`** — OEL/STEL tablosu, MSDS bağlantısı, depolama uyarısı
- **F2-008 `isg_equipment`** — Periyodik kontrol planı, takvim entegrasyonu
- **F2-009 F2-010 `isg_ptw` + `isg_loto`** — İş İzni sistemi (PTW-LOTO entegrasyonu)
- **F2-026 `isg_contractor_supervision`** — Alt işveren denetim ziyareti

### Proje Metrikleri

| Metrik | Değer |
|--------|-------|
| Kurulu Toplam Modül | 47 |
| İSG Modülü | 20 |
| Tamamlanan FAZ | 1 + 2/5 |
| Tahmini Tamamlanma | %60 |
| Ortalama Modül Boyutu | 300-500 satır (model+view+security) |
| Toplam İSG Kodu | ~8000 satır Python + XML |

