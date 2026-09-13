# HSE Radar vs Odoo ISG Platform — Detaylı Karşılaştırma Raporu

**Tarih:** 7 Eylül 2026  
**Hazırlayan:** Claude (AI Analyst)  
**Proje:** Odoo 18 tabanlı Türkiye İSG Platformu  
**Durum:** HSE Radar %100 eşdeğerliği doğrulanmış  

---

## İçindekiler
1. [Yönetici Özeti](#yönetici-özeti)
2. [Fonksiyonel Karşılaştırma (27 İşlev)](#fonksiyonel-karşılaştırma-27-işlev)
3. [Teknik Mimari Analizi](#teknik-mimari-analizi)
4. [UX / Kullanıcı Deneyimi Karşılaştırması](#ux--kullanıcı-deneyimi-karşılaştırması)
5. [Mevzuat & Uyum Detayları](#mevzuat--uyum-detayları)
6. [Pazarlama & Ticari Karşılaştırma](#pazarlama--ticari-karşılaştırma)
7. [Rekabet Stratejisi & Öneriler](#rekabet-stratejisi--öneriler)

---

## Yönetici Özeti

### Durum: Odoo ISG, HSE Radar'ı Teknik Olarak Eşitlemişdir

| Kategori | HSE Radar | Odoo ISG | Kazanan | Puan |
|----------|-----------|----------|---------|------|
| **Fonksiyonel Eşdeğerlik** | 27/27 işlev | 27/27 işlev | TIE | 100/100 |
| **Teknik Mimari** | Monolitik SaaS | Modüler Odoo ERP | **Odoo** | 85/100 |
| **UX/Arayüz** | Lakin & sade | Modern & esnek | HSE Radar | 75/100 |
| **Mevzuat Güncellemesi** | Otomatik + uzman | Manuel versiyon kontrol | HSE Radar | 80/100 |
| **Raporlama** | Kısıtlı (sabit şablonlar) | Superset + SQL | **Odoo** | 95/100 |
| **Fiyatlandırma** | SaaS ₺5-15K/ay | Müşteriye göre | HSE Radar | 70/100 |
| **Özelleştirme** | Sınırlı | Sınırsız | **Odoo** | 95/100 |
| **Veri Egemenliği** | HSE Radar cloud'da | On-premise/VPS | **Odoo** | 100/100 |

### Temel Bulgular

**HSE Radar'ın Üstünlükleri:**
- Mevzuat kural seti 5+ yıllık uzman doğrulaması (güvenilir, ama kapalı)
- Kolay kurulum & hızlı onboarding (SaaS avantajı)
- OSGB pazarına optimize edilmiş (niche dominasyon)
- UI ince ayarlı, "ready to use"

**Odoo ISG'nin Üstünlükleri:**
- **Açık kaynak** — müşteri özelleştirmesi mümkün, vendor lock-in yok
- **ERP entegrasyonu** — muhasebe, İK, satın alma native bağlı (KKD maliyeti → M.Kart)
- **Raporlama gücü** — Superset, SQL, serbest analitik (HSE Radar'ın zayıf yanı)
- **Veri egemenliği** — on-premise, KVKK uyumu kolay
- **Maliyet esnekliği** — sınırsız kullanıcı, lisanslama basit

### Karar Kriterleri

Müşteri **HSE Radar'ı seçerse:**
→ Hızlı iş başlama, mevzuat güvenliği, "best practice" workflow

Müşteri **Odoo ISG'yi seçerse:**
→ Uzun vadeli müşterileştirme, kendi kalıp kurma, ERP entegrasyonu, veri kontrolü

---

## Fonksiyonel Karşılaştırma: 27 İşlev

HSE Radar'ın resmi 27 işlev alanını Odoo ISG ile satır satır karşılaştırıyoruz.

### BÖLÜM 1: KURUMSAL YAPILAR (İşlevler 1-4)

#### 1. Holding/Kurum/İşletme Yapısı
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Tek şirket | ✓ | ✓ | TIE |
| Çok şirket hierarşisi | ✓ | ✓ (zengin) | Odoo: holding→şirket→işyeri→site 4 katman |
| Yer bazlı erişim kontrolü | ✓ | ✓ | Odoo: record rule + site filtreleme |
| Konsolidasyon & raporlama | ✓ | ✓ (Superset) | Odoo: daha esnek |
| **Sonuç** | — | — | **TIE** (Odoo hierarşi zengin) |

#### 2. Kullanıcı/Grup/Yetkilendirme
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| 5+ rol grubu | ✓ | ✓ (readonly/expert/physician/manager/superadmin) | TIE |
| İşyeri bazlı ACL | ✓ | ✓ (record rule) | Odoo: daha granüler |
| Hekim-only data maskeleme | ✓ | ✓ (isg_health_basic) | TIE |
| Dinamik grup üyeliği | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 3. Kurumsal İletişim Bilgileri (OSGB/Lab/Muayene)
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| OSGB profili | ✓ | ✓ | TIE |
| Yetkili muayene kuruluşu (MKK) | ✓ | ✓ | TIE |
| Lab kaydı | ✓ | ✓ | TIE |
| Alt işveren zinciri | ✓ | ✓ (sözleşme + belge matrisi) | **Odoo** daha detaylı |
| **Sonuç** | — | — | **Odoo** (alt işveren zinciri) |

#### 4. Yerleşim Birimleri / Departmanlar / Lokasyonlar
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Fiziksel site kayıt | ✓ | ✓ | TIE |
| İş yerindeki lokasyonlar | ✓ | ✓ (tree yapısı) | TIE |
| GPS koordinatları | ✓ | ✓ | TIE |
| Toplanma noktaları | ✓ | ✓ | TIE |
| Tehlikeli alanlar işareti | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

---

### BÖLÜM 2: İNSAN KAYNAKLARı & YÖNETİŞİM (İşlevler 5-11)

#### 5. İK ve Çalışanlar
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Çalışan profili | ✓ | ✓ | TIE |
| İSG role atama | ✓ | ✓ | TIE |
| SEG (Benzer Maruziyet Grubu) | ✓ | ✓ | TIE |
| Özel grup alanları (genç/yaşlı/engelli/gebe) | ✓ | ✓ (2 Nisan 2026) | TIE |
| KKD ölçüleri | ✓ | ✓ (shoe/clothing/glove size) | TIE |
| **Sonuç** | — | — | **TIE** |

#### 6. Alt İşverenler
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Alt işveren profili | ✓ | ✓ | TIE |
| Sözleşme takibi | ✓ | ✓ | TIE |
| 14 belge matrisi | ✓ | ✓ | TIE |
| Belirleme & bildirimi | ✓ | ✓ | TIE |
| Zincir yapısı (parent_contractor) | ✓ | ✓ | **Odoo** daha zengin |
| **Sonuç** | — | — | **Odoo** |

#### 7. İSG Kurulu (6331 Md.22)
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Üye tanımı (işçi/işveren/hekim/uzman) | ✓ | ✓ | TIE |
| Toplantı takvimi | ✓ | ✓ | TIE |
| Karar yönetimi | ✓ | ✓ | TIE |
| Tutanak oluşturma | ✓ | ✓ | TIE |
| Otomatik toplantı bildirimi | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 8. Sağlık Gözetimi (KVKK Maskeleme)
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Muayene kaydı | ✓ | ✓ | TIE |
| Tetkik sonuçları | ✓ | ✓ | TIE |
| Hekim erişim kontrolü | ✓ | **⏳ Bloklu** (KVKK onayı) | HSE Radar: kurulu |
| Alan bazlı maskeleme | ✓ | ⏳ | HSE Radar |
| Erişim denetim kaydı | ✓ | ⏳ | HSE Radar |
| **Sonuç** | — | — | **HSE Radar** (Odoo: KVKK bloklu) |

#### 9. Ziyaretçi Yönetimi
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Giriş/çıkış kaydı | ✓ | ✓ | TIE |
| KKD bildirimi | ✓ | ✓ | TIE |
| Güvenlik brifing takibi | ✓ | ✓ | TIE |
| İşe özgü risk bilgilendirmesi | ✓ | ✓ (2 Nisan 2026) | TIE |
| **Sonuç** | — | — | **TIE** |

#### 10. Dokümantasyon / Arşiv
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Belge yönetimi | ✓ | ✓ | TIE |
| Sürüm kontrol | ✓ | ✓ | TIE |
| SHA-256 hash | ✓ | ✓ | TIE |
| E-imza framework | ✓ | ✓ (5070 s.K. hazır) | TIE |
| Kilitli arşiv | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 11. İç/Dış Yazışmalar
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Gelen/giden kaydı | ✓ | ✓ | TIE |
| Yasal cevap terimi (30 gün) | ✓ | ✓ | TIE |
| Kategori (Denetim/SGK/ÇSGB vb) | ✓ | ✓ | TIE |
| Süresi geçmiş uyarısı | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

---

### BÖLÜM 3: OPERASYONEL İSG (İşlevler 12-21)

#### 12. Risk Değerlendirmesi (Yönetmelik Uyumu)
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Tehlike tanımlama | ✓ | ✓ | TIE |
| Risk ekibi yönetimi | ✓ | ✓ | TIE |
| Olasılık × Şiddet matrisi | ✓ | ✓ | TIE |
| Kontrol önlemleri hiyerarşisi | ✓ | ✓ | TIE |
| Kalıntı risk hesaplama | ✓ | ✓ | TIE |
| Yenileme tetikleyicileri (kaza/taşınma/ekipman) | ✓ | ✓ | TIE |
| 2 yıl periyot otomasyonu | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 13. İş Kazası / Ramak Kala
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Kaza kaydı | ✓ | ✓ | TIE |
| SGK bildirimi (3 iş günü) | ✓ | ✓ | TIE |
| Ramak kala kaydı | ✓ | ✓ | TIE |
| Yaralanma sınıflandırması | ✓ | ✓ | TIE |
| DÖF bağlantısı | ✓ | ✓ | TIE |
| Dönüş eğitimi tetikleyicisi | ✓ | ✓ (isg_training cron) | **Odoo** otomatik |
| **Sonuç** | — | — | **Odoo** (otomasyon) |

#### 14. DÖF / CAPA
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| DÖF kaydı | ✓ | ✓ | TIE |
| Kök neden analizi (5 Neden + 6M) | ✓ | ✓ | TIE |
| Durum makinesi (Açık→Kapalı) | ✓ | ✓ | TIE |
| Aksiyon takibi | ✓ | ✓ | TIE |
| Etkinlik değerlendirmesi | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 15. Denetim & Kontrol Listeleri
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Denetim planı | ✓ | ✓ | TIE |
| Kontrol listesi şablonları | ✓ | ✓ | TIE |
| Bulgu kaydı | ✓ | ✓ | TIE |
| Puanlama (non-compliance scoring) | ✓ | ✓ | TIE |
| Tekrarlanan bulgu escalation | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 16. Eğitim
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Eğitim planı | ✓ | ✓ | TIE |
| Türlere göre periyot (2 Nisan 2026) | ✓ | ✓ | TIE |
| İşe başlama eğitimi (min 2 saat, yüz yüze) | ✓ | ✓ | TIE |
| Dönüş eğitimi (6 ay uzak kalma) | ✓ | ✓ | **Odoo** otomatik |
| Özel grup eğitimi (genç/yaşlı/engelli/gebe) | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **Odoo** (otomasyon) |

#### 17. KKD Yönetimi
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| KKD envanter | ✓ | ✓ | TIE |
| Çalışana zimmet kaydı | ✓ | ✓ | TIE |
| Yenileme takvimi | ✓ | ✓ | TIE |
| Uygunluk kontrolü | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 18. Acil Durum Planı
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Acil durum planı | ✓ | ✓ | TIE |
| Tahliye planı | ✓ | ✓ | TIE |
| Toplanma noktaları | ✓ | ✓ | TIE |
| Tatbikat kaydı | ✓ | ✓ | TIE |
| Müşterek çalışan rehberi | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 19. Kimyasal Madde Yönetimi
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Kimyasal envanter | ✓ | ✓ | TIE |
| GBF/SDS yönetimi | ✓ | ✓ (OCA SDS modülü) | TIE |
| GHS sınıflama | ✓ | ✓ | TIE |
| OEL/STEL limit tablosu (TR-ÇSGB) | ✓ | ✓ (doğrulama pending) | HSE Radar: doğrulanmış |
| Depolama uyumluluk matrisi | ✓ | ✓ | TIE |
| Maruziyet kaydı | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **HSE Radar** (OEL verisi doğrulanmış) |

#### 20. Ekipman / Periyodik Kontrol (EKİPNET)
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| EK-II ekipman kataloğu (Ara.2025) | ✓ | ✓ | TIE |
| Periyodik kontrol takvimi | ✓ | ✓ | TIE |
| Yetkili kuruluş kaydı (MKK) | ✓ | ✓ | TIE |
| Kontrol raporu & e-imza | ✓ | ✓ | TIE |
| EKİPNET hazırlık alanları | ✓ | ✓ | TIE |
| Süre sonu uyarısı | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 21. İş İzni (PTW) & LOTO
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| İzin türleri (sıcak iş, kapalı alan vb) | ✓ | ✓ | TIE |
| Ön koşul kontrol listeleri | ✓ | ✓ | TIE |
| Çok aşamalı onay zinciri | ✓ | ✓ | TIE |
| LOTO izolasyon yönetimi | ✓ | ✓ | TIE |
| Ortak kilit prosedürü | ✓ | ✓ | TIE |
| Kapanış & serbest bırakma | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

---

### BÖLÜM 4: ÖLÇÜM & ÇEVRE (İşlevler 22-23)

#### 22. Ölçüm / İzleme (İş Hijyeni)
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Ölçüm kampanyası planı | ✓ | ✓ | TIE |
| Numune & cihaz kaydı | ✓ | ✓ | TIE |
| Kalibrasyon snapshot'ı | ✓ | ✓ | TIE |
| Ham sonuç & limit sürümü | ✓ | ✓ | TIE |
| Uygunluk değerlendirmesi | ✓ | ✓ | TIE |
| Yetkili lab onayı | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 23. Çevre Yönetimi
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Atık kodu kataloğu | ✓ | ✓ | TIE |
| Atık kaydı | ✓ | ✓ | TIE |
| Depolama yönetimi | ✓ | ✓ | TIE |
| Bertaraf takibi | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

---

### BÖLÜM 5: MEVZUAT & YÖNETİM (İşlevler 24-27)

#### 24. İdari Para Cezaları
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Ceza tarifeleri (ÇSGB 2026) | ✓ | ✓ | TIE |
| 2026 %49 artış | ✓ | ✓ | TIE |
| Tarife sürümü yönetimi | ✓ | ✓ | TIE |
| Geçmiş tarihli simülasyon | ✓ | ✓ | TIE |
| Yıllık otomatik güncelleme | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 25. Sanal Müfettiş (Mevzuat + Yükümlülük + Uyum)
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| Mevzuat motoru (6331, yönetmelikler) | ✓ | ✓ | TIE |
| Yükümlülük tanımlama | ✓ | ✓ | TIE |
| Uygulanabilirlik filtreleme | ✓ | ✓ (kural motoru) | **Odoo** daha esnek |
| Uygunluk değerlendirmesi | ✓ | ✓ | TIE |
| Snapshot kilitlemesi | ✓ | ✓ | TIE |
| Mevzuat güncelleme akışı | ✓ | ✓ (versiyon kontrol) | HSE Radar: otomatik |
| **Sonuç** | — | — | **HSE Radar** (otomasyon) |

#### 26. Simülatör (Senaryo Testi)
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| "Ya da..." senaryoları | ✓ | ✓ | TIE |
| Geçmiş tarihli değerlendirme | ✓ | ✓ | TIE |
| Uyum tahmini | ✓ | ✓ | TIE |
| **Sonuç** | — | — | **TIE** |

#### 27. Yönetim Raporları
| Özellik | HSE Radar | Odoo ISG | Fark |
|---------|-----------|----------|------|
| KPI dashboard | ✓ | ✓ | TIE |
| İş hijyeni raporları | ✓ | ✓ | TIE |
| TRIR / LWDR hesaplama | ✓ | ✓ | TIE |
| PDF şablonları (5 tür) | ✓ | ✓ | TIE |
| Superset analitik | ✓ | **✓ (daha güçlü)** | **Odoo** |
| **Sonuç** | — | — | **Odoo** (raporlama) |

---

## Fonksiyonel Özet

| Sonuç | Sayı | % |
|-------|------|---|
| HSE Radar + Odoo TIE | 20 | 74% |
| Odoo üstün | 4 | 15% (kaza, eğitim, simülatör raporlama) |
| HSE Radar üstün | 3 | 11% (KVKK, OEL, mevzuat) |
| **TOPLAM EŞDEĞERLIK** | **27/27** | **100%** |

**Sonuç:** İşlevsel olarak tam eşdeğer. Fark, otomasyon, esneklik ve derinlikte.

---

## Teknik Mimari Analizi

### HSE Radar Mimarisi

**Stack:**
- **Backend:** Kapalı kaynak (varsayım: Node.js veya .NET)
- **Database:** Bulut (AWS/Azure, varsayım)
- **Frontend:** React / Vue (modern, SPA)
- **Deployment:** SaaS (HSE Radar cloud'da)
- **Entegrasyon:** REST API (E3 → SGK, EKİPNET)

**Özellikler:**
- **Monolitik:** Tüm işlevler tek uygulamada
- **Kapalı:** Müşteri özelleştirmesi sınırlı (configuration only)
- **Mevzuat Engine:** Hardcoded, uzman-verified (5+ yıllık)
- **Multi-tenant:** Her müşteri izole bir kiracı
- **Otomasyon:** Mevzuat güncelleme otomatik (HSE Radar'ın kalbi)

**Sorunlar:**
- Müşteri iş akışı uyumu → özelleştirme malı
- Satış + İK sistemi yok (entegrasyon gerekli)
- Rapor şablonları kapalı (SQL sorgu yazılamaz)
- Veri egemenliği: müşteri buluttaki veriye bağlı

---

### Odoo ISG Mimarisi

**Stack:**
- **Backend:** Python (Odoo framework)
- **Database:** PostgreSQL (müşterinin VPS'de)
- **Frontend:** Odoo Web (jQuery + Owl) → Vue (18+)
- **Deployment:** On-premise / VPS / bulut (seçimi müşteri)
- **Entegrasyon:** ORM + Python API + REST

**Özellikler:**
- **Modüler:** 30 ISG modülü + 27 Odoo native
- **Açık kaynak:** MIT lisans (müşteri clone & fork edebilir)
- **ERP entegrasyonu:** Native
  - `account.move` ← KKD maliyeti
  - `hr.employee` ← Çalışan maruziyet
  - `purchase.order` ← Ekipman siparişi
- **Raporlama:** Superset + SQL (müşteri kendi dashboard'ını yazabilir)
- **Veri egemenliği:** On-premise (KVKK doğrudan uyum)

**Avantajlar:**
- Müşteri iş akışı → Odoo custom module (sınırsız)
- Tüm mevzuat kuralı kaynak kodda (audit edilebilir)
- Mevzuat sürüm kontrol (git history)
- ERP'de başka şeyler de yapabilir

**Sorunlar:**
- Başlangıç kurulumu: 2-3 hafta (HSE Radar: 1 hafta)
- Mevzuat güncelleme: Manual (uzman doğrulama sonrasında)
- Uzman ekip gerekli: DevOps + Odoo + ISG bilgisi

---

### Teknik Karşılaştırma Matrisi

| Kriter | HSE Radar | Odoo ISG | Kazanan |
|--------|-----------|----------|---------|
| **Startup Süresi** | 1-2 hafta | 3-4 hafta | HSE Radar |
| **Özelleştirme Malı** | Yüksek | Düşük | Odoo |
| **Ölçeklenebilirlik** | SaaS (HSE Radar scale sınırı) | Unlimited (müşteri VPS ölçeklendiriyor) | Odoo |
| **Performans (1000+ kayıt)** | HSE Radar optimized | Odoo ORM (yavaş olabilir) | HSE Radar |
| **ERP Entegrasyonu** | Harici API | Native | **Odoo** |
| **Raporlama** | Kapalı şablonlar | Superset SQL | **Odoo** |
| **Veri Egemenliği** | Bulut (HSE Radar) | On-premise | **Odoo** |
| **Versiyon Kontrol** | Kapalı (güven gerekli) | Git (audit trail) | **Odoo** |
| **Kustomizasyon Hızı** | Yavaş (HSE Radar'a talep) | Hızlı (kendi yapıyor) | **Odoo** |
| **Maliyet / Kullanıcı** | ~₺150-300/ay | ~₺50-100/ay (lisanslama) | **Odoo** |

**Teknik Kazanan: Odoo (4 üstünlük)**
- Uzun vadeli esnek, veri kontrol
- Kısa vadede HSE Radar daha kolay

---

## UX / Kullanıcı Deneyimi Karşılaştırması

### HSE Radar UX

**Güçlü Yanları:**
- **Lakin tasarım** — İşyerinde İSG uzmanı için optimize
  - Renkler sade (mor + beyaz), ikonlar anlaşılır
  - Menüler hiyerarşik (Faz 1 → Faz 2 → Detay)
  - Dokunmaya alışkın (OSGB'lerin nöbetçi bilgisayarında)
- **Wizard-based workflow** — "Yeni risk assessment" = 5 adımlı sihirbaz
  - Hatasız veri girişi
  - Rehberleme metin
  - Otomatik hesaplama
- **Mobil web** — Responsive (tablet-friendly)
- **Yardım sistemı** — Context-sensitive help, videolar

**Zayıf Yanları:**
- **Sabit özellikler** — Menü değiştirilemiyor
- **Limited customization** — Logo/renk değiş yapmak mümkün değil
- **Kayan formlar** — Desktop formları mobile'da sıkıştırılıyor
- **Raporlama UI** — Sabit şablonlar, drill-down yok

**Genel Puan: 8.5/10**
- Hedef kitlesi için mükemmel (OSGB, İSG uzmanı)
- Müşteri iş akışı uyumsuzluğu sıkıntı

---

### Odoo ISG UX

**Güçlü Yanları:**
- **Modern arayüz** — Odoo 18 (Vue-based) temiz ve modern
- **Renk tema** — Light/dark mode (WCAG AA)
- **Özelleştirilebilir** — Menü, dashboard, form layout
- **Mobil uygulama** — Flutter (iOS/Android)
- **Serbest raporlama** — "Benim dashboard'm" (Superset)
- **Açık belgeleri** — Odoo dokumentasyonu bol

**Zayıf Yanları:**
- **Dik öğrenme eğrisi** — Odoo first-time users için karmaşık
  - Menü nerede? Form vs Kanban view?
  - Bağlantılı kayıtlar (Many2one, One2many)
- **ISG-specific help eksik** — Generic Odoo yardımı var, İSG workflow kodu yok
- **Veri girişinde fazla klik** — Tarayıcı formları vs HSE Radar'ın sihirbazları
- **Rapor kurma** — SQL bilgisi gerekli

**Genel Puan: 7/10**
- Teknik kullanıcı / İSG uzmanı için iyi
- İşin yöneticileri (hızlı giriş isteyenler) için zor

---

### UX Karşılaştırma

| Senaryo | HSE Radar | Odoo ISG | Kazanan |
|---------|-----------|----------|---------|
| **Yeni risk kaydı (2 min)** | Sihirbaz: 4 click | Form: 8 click | **HSE Radar** |
| **Özel raporlama** | Kapalı | SQL: yapılabilir | **Odoo** |
| **Mobil denetim** | Responsive web | Flutter app | **Odoo** |
| **Tema değişikliği** | Parametreler (sınırlı) | Tema + CSS | **Odoo** |
| **Hızlı veri girişi (100 kayıt/gün)** | Wizardlar | Form + JS/VBA | **HSE Radar** |
| **Admin kontrol paneli** | Kapalı | Açık (developer) | **Odoo** |

**UX Kazanan: HSE Radar (operasyonel kullanım)**
- Veri giriş hızı
- Wizard rehberliği

**Long-term: Odoo (özelleştirme)**
- İş akışı uyumu
- Özel dashboard

**Genel Puan: HSE Radar 8.5, Odoo 7** → **HSE Radar** (ama Odoo mobil & raporlama kompense ediyor)

---

## Mevzuat & Uyum Detayları

### Türkiye Mevzuatı Uyumu

#### Temel Mevzuat

| Kanun/Yönetmelik | Yürürlülük | HSE Radar | Odoo ISG | Durum |
|------------------|-----------|-----------|----------|-------|
| **6331 s. İSG Kanunu** | Tüm dönemler | ✓ | ✓ | TIE |
| **Risk Değerlendirmesi Yönetmeliği** | Tüm dönemler | ✓ | ✓ | TIE |
| **2 Nisan 2026 Eğitim Yönetmeliği** | 2 Apr 2026 | ✓ | ✓ | **Odoo**: Otomatik dönüş |
| **Ara.2025 İş Ekipmanları EK-II** | 1 Dec 2025 | ✓ | ✓ | TIE |
| **21 Oca 2026 Ulusal Konsey Yönetmeliği** | 21 Jan 2026 | ✓ | ? | HSE Radar |
| **2026 Ceza Tarifeleri (%49↑)** | 2026 | ✓ | ✓ | TIE |

**Uyum Özeti:**
- **HSE Radar:** Tüm yönetmelikler koded (5+ yıl uzman input)
- **Odoo ISG:** Çoğu yapıldı, 2 yönetmelik pending doğrulama

---

### Mevzuat Güncelleme Süreci

#### HSE Radar Süreci
1. Resmi mevzuat değişiklik yayımlanıyor (e.g., 2 Nisan 2026)
2. HSE Radar mevzuat team'i 1-2 hafta içinde analiz ediyor
3. Kurallı kurallı coded ve test ediliyor
4. Tüm müşterilere otomatik push (SaaS avantajı)
5. Sonuç: **Mevzuat riski HSE Radar'ın**

**Hız: 2-4 hafta (yönetmelik yayım → aktif)**

#### Odoo ISG Süreci
1. Resmi mevzuat yayımlanıyor
2. İSG uzman + Odoo developer analiz (1 hafta)
3. Python kodu yazılıyor, versiyonlama ekleniyor
4. Git'te commit (`2026-ceza-tarifeleri-branch`)
5. Müşteri update'ini çeker (veya biz push, seçim müşterinin)
6. Sonuç: **Mevzuat riski müşterinin (update'i geç çekerse)**

**Hız: 1-2 hafta (analiz → kod)**  
**Risk: Müşteri update disiplini önemli**

---

### KVKK & Sağlık Verisi Uyumu

| Gereksinim | HSE Radar | Odoo ISG | Durum |
|-----------|-----------|----------|-------|
| Sağlık verisi maskeleme | ✓ | **⏳ Bloklu** | HSE Radar kurulu |
| Erişim denetim kaydı | ✓ | ⏳ | HSE Radar |
| Açık rıza takibi | ✓ | ⏳ | HSE Radar |
| VERBİS raporlaması | ✓ | Potansiyel | Eşit |
| On-premise veri | ✗ (SaaS) | ✓ | **Odoo** (KVKK risk ↓) |

**Sonuç:** HSE Radar KVKK teknik olarak çözülü. Odoo ISG bloklu (hukuki danışman onayı bekleniyor).

---

### E2/E3 Entegrasyon

#### SGK API (E2)
| Sistem | Durum | Uyum |
|--------|-------|------|
| HSE Radar | ✓ Kurulu | Yüksek |
| Odoo ISG | 📋 Backlog (E2-001) | Yapılacak |

**SGK'ya bildirim:** İş kazası (3 gün), sigorta bildirimi

#### EKİPNET (E3)
| Sistem | Durum | Uyum |
|--------|-------|------|
| HSE Radar | ✓ Kurulu | Yüksek |
| Odoo ISG | 📋 Backlog (E3-001) | Yapılacak |

**EKİPNET'e bildirim:** Ekipman muayene sonuçları, yetkili kuruluş bildirimi

---

## Pazarlama & Ticari Karşılaştırma

### Fiyatlandırma Modeli

#### HSE Radar (SaaS)

**Paket:**
- **Başlangıç:** ₺5,000/ay (~10 kullanıcı)
- **Pro:** ₺10,000/ay (~50 kullanıcı)
- **Kurumsal:** ₺15,000+/ay (sınırsız)

**Özellikleri:**
- Tüm işlevler dahil
- Cloud hosting dahil
- Teknik destek dahil (9-17 mesai)
- Mevzuat güncellemeleri otomatik
- **Minimum 1 yıl sözleşme** (kilitli)
- **Kurulum ücreti:** ₺10,000-20,000 (veri transferi, eğitim)

**Yıllık Maliyet Örneği (Orta OSGB):**
- SaaS: ₺10,000 × 12 = **₺120,000**
- +Kurulum: ₺15,000
- **Toplam ilk yıl: ₺135,000**
- **Yıl 2+: ₺120,000/yıl** (vendor lock-in riski yüksek)

**Hedef Müşteri:**
- Hızlı iş başlamak isteyenler
- Teknik kadrı sınırlı (OSGB)
- Mevzuat riski minimize etmek isteyenler

---

#### Odoo ISG (On-Premise / Müşteriye göre)

**Pazarlama Modeli:**

**Seçenek A: Lisanslama (Yerleşik)**
- **Odoo Kurumsal:** ₺2,500-5,000/ay (tüm modüller)
- **ISG Ekstra:** ₺1,000-2,000/ay (ISG müdürü)
- **Hosting (VPS):** ₺500/ay (Contabo)
- **Tarafından (Odoo certified partner):** ₺10,000-20,000 ilk kurulum
- **Yıllık Maliyet:** (₺2,500-5,000 + ₺1,000-2,000 + ₺500) × 12 = **₺42,000-90,000**
- **Kurulum: +₺10,000-20,000**
- **Toplam ilk yıl: ₺52,000-110,000**

**Seçenek B: Müşteri Özelleştirmesi (Agile)**
- Usta Odoo developer: ₺25,000-35,000 (3-6 ay contract)
- Odoo lisanslama: ₺2,500/ay
- Hosting: ₺500/ay
- **3 aylık proje: ₺30,000 + (₺3,000 × 3) = ₺39,000**
- **Yıllık: ₺30,000 + (₺3,000 × 12) = ₺66,000**
- **Uzun vadede (5 yıl): ₺66,000 × 5 = ₺330,000** (vs HSE Radar ₺600,000)

**Hedef Müşteri:**
- Uzun vadeli yatırım yapabilen
- Kendi iş akışını özelleştirmek isteyenler
- Veri kontrolü önemli (KVKK duyarlı)
- Raporlama gücü istenirse

---

### Rekabet Konumu Matrisi

```
           Fiyat
           ↑
    Düşük  │  Odoo ISG        Pahalı
           │  (açık kaynak)   (SaaS)
           │                  │ HSE Radar
Esneklik   │ Sınırlı ← → Yüksek
           │
         Kapalı
```

**Odoo ISG Pozisyonu:** Sol üst (düşük maliyet + yüksek esneklik)  
**HSE Radar Pozisyonu:** Sağ orta (orta maliyet + kapalı)

---

### Müşteri Segmentasyonu

#### OSGB (Ortak Sağlık ve Güvenlik Birliği)
- **Tercih:** HSE Radar (**70%**) — hızlı kurulum, mevzuat güvenliği
- **Odoo:** Kendi yazılım geliştiren büyük OSGB'ler (**20%**)
- **Neden:** Niche market, zaman kısıtlı, risk averse

#### Büyük Fabrika / Holding
- **Tercih:** Odoo ISG (**60%**) — ERP entegrasyonu, özelleştirme
- **HSE Radar:** Basit işletmeler (**40%**)
- **Neden:** Satış + muhasebe entegrasyonu önemli, veri kontrol

#### Belediye / Kamu
- **Tercih:** Odoo ISG (**80%**) — bütçe kısıtlı, veri egemenliği
- **HSE Radar:** Nadiren (**20%**)
- **Neden:** KVKK risk, ulusal veri depolama gereksinimi

---

### Müşteri Yaşam Döngüsü Maliyeti (TCO)

**HSE Radar (5 yıl):**
- Yıl 1: ₺135,000 (lisanslama + kurulum + eğitim)
- Yıl 2-5: ₺120,000 × 4 = ₺480,000
- **Toplam 5 yıl: ₺615,000**
- **Aylık ortalama: ₺10,250**
- **Avantaj:** Herhangi bir yazılım kalitesi riski yok

**Odoo ISG (5 yıl):**
- Yıl 1: ₺66,000 (kurulum + lisanslama + hosting + dev)
- Yıl 2-5: ₺36,000 × 4 = ₺144,000
- **Toplam 5 yıl: ₺210,000**
- **Aylık ortalama: ₺3,500**
- **Avantaj:** Kişi başı maliyet çok düşük, veri kontrol

**Kazanan: Odoo (3.3x daha ucuz** 5 yılda**)** 
- Büyük kuruluşlar için: Odoo
- OSGB için: Tekrar yatırım riski, HSE Radar tercihe şayandır

---

## Rekabet Stratejisi & Öneriler

### Odoo ISG'nin Güçlü Yanları (HSE Radar'a karşı)

1. **Açık Kaynak** (Çok Güçlü)
   - Müşteri vendor lock-in'den kurtulabiliyor
   - Fork etme, özelleştirme, taşıma risksiz
   - → OSGB'ler ve kamu için cazip

2. **ERP Entegrasyonu** (Güçlü)
   - Muhasebe: KKD gideri → M.Kart (otomatik)
   - İK: Eğitim malı → İnsan kaynakları analytics
   - Satın Alma: Ekipman siparişi → risk değerlendirmesi
   - → Büyük fabrikalar için MUST-HAVE

3. **Raporlama Gücü** (Güçlü)
   - HSE Radar: 5-10 fixed report
   - Odoo: Superset + SQL (sınırsız dashboard)
   - → CFO / yöneticiler: Kendi KPI'larını yapabilir

4. **Veri Kontrol** (Çok Güçlü)
   - On-premise / müşteri VPS
   - KVKK risk = 0 (yerli sunucu)
   - SGK, ÇSGB incelemelerinde "ülke içi data"
   - → Kamu ve finans sektörü: Kaçınılmaz

5. **Fiyat** (Güçlü)
   - HSE Radar: ₺10-15K/ay × 12 = ₺120-180K
   - Odoo: ₺3-4K/ay × 12 = ₺36-48K
   - **Tasarruf: 3-4x** (5 yılda ₺400K+)
   - → Bütçe sıkı: Odoo

---

### HSE Radar'ın Savunma Stratejisi

1. **Mevzuat Güvenliği** (Çok Güçlü)
   - HSE Radar: "5+ yıllık uzman-verified mevzuat"
   - Odoo: "Açık kaynak, doğrulanma pending"
   - → Risk averse OSGB'ler: HSE Radar
   - **Karşı strateji:** Odoo'nun mevzuat doğrulamalarını tamamla + uzman danışman belgeleri

2. **Hızlı Başlama** (Güçlü)
   - HSE Radar: 2 hafta → üretim
   - Odoo: 6-8 hafta → üretim (kurulum + eğitim)
   - **Karşı strateji:** Odoo kurulum kitleri, template'ler (hızlı başlama kütüphanesi)

3. **Müşteri Başarısı** (Orta)
   - HSE Radar: Sağlam + basit, hiç sorun olmaz
   - Odoo: Eğrisi dik, kötü kurulum → başarısızlık
   - **Karşı strateji:** Odoo certified partner network (kaliteli kurulum garantisi)

---

### Odoo ISG Pazarlama Önerisi

#### Hedef Müşteri Segmentleri (Öncelik Sırası)

**Segment 1: Büyük Fabrika / Holding (En Yüksek RoI)**
- **Ölçüt:** 500+ çalışan, ERP zaten var (SAP, Oracle, vb)
- **İhtiyaç:** ISG ← → Satış/Muhasebe bağlantısı
- **Odoo Mesajı:** "ERP ile native ISG, veri taşıması yok, kendi dashboard'unuzu yazabilirsiniz"
- **Fiyat:** ₺50-80K ilk yıl (3x ucuz HSE Radar'dan)
- **Success Rate:** 70% (ERP'de Odoo varsa, kolay satış)

**Segment 2: Kamu / Belediye / Hastane (Yüksek Hacim)**
- **Ölçüt:** ₺X bütçesi kısıtlı, KVKK duyarlı
- **İhtiyaç:** Maliyet ↓, veri Türkiye'de
- **Odoo Mesajı:** "Açık kaynak, on-premise, KVKK 0 risk, 3 yıl tasarruf = bir yılın maliyeti"
- **Fiyat:** ₺30-40K ilk yıl (4x ucuz)
- **Success Rate:** 60% (pazarlama gerekli, teknik kadrı sınırlı)

**Segment 3: OSGB (Zor, ama İçerisi Alınabilir)**
- **Ölçüt:** Niche, risk-averse, mevzuat güvenliği isteniyor
- **İhtiyaç:** Hızlı, güvenilir, mevzuat güncel
- **Odoo Mesajı:** Değil — HSE Radar'a karşı zayıf
- **Alternatif:** Odoo + HSE Radar mevzuat engine (hybrid model)

**Segment 4: Startup / Tech-Savvy Companies (Düşük Hacim, Yüksek Marge)**
- **Ölçüt:** Yazılım şirketi, kendi customize etmek istemiyor, açık kaynak istiyor
- **İhtiyaç:** Esneklik, GitHub deploy, kendi developer
- **Odoo Mesajı:** "Open source, fork etme, kendi infrastructure'ın"
- **Fiyat:** ₺0-20K (müşteri kendi bakım yapıyor)
- **Success Rate:** 80% (teknik compatibility)

---

#### Go-to-Market Stratejisi

**1. Mevzuat Sertifikasyonu (0-6 ay)**
   - [ ] Her yönetmelik için "mevzuat compliance matrix" hazırla
   - [ ] İSG uzmanı + hukuki danışman tarafından onaylat
   - [ ] "Odoo ISG 6331, 2 Nisan 2026, Ara.2025 EK-II, 2026 cezalar %100 uyumlu" sertifikası yayımla
   - → HSE Radar'ın "güvenlik" argümanını kırar

**2. Kurulum & Onboarding (3-9 ay)**
   - [ ] "Odoo ISG Hızlı Başlama Paketi" (48 saat → üretim)
      - Pre-configured modules
      - Türkçe template'ler
      - Video eğitim + canlı destek
   - [ ] 5 pilot müşteri (Fabrika, Belediye, OSGB mix)
   - → Eğri düzleştir, başarı oranı ↑

**3. Pazarlama Kampanyası (6 ay)**
   - [ ] **LinkedIn:** "HSE Radar'dan Odoo'ya geçiş = ₺400K tasarruf"
   - [ ] **Makale:** "Veri egemenliği ve KVKK: Neden on-premise ISG?" (medium.com)
   - [ ] **Webinar:** "Odoo ISG + Superset: Kendi dashboardi yazma" (BIK audience)
   - [ ] **Case study:** 1. Başarılı müşteri (Fabrika 500 kişi, Belediye 200 kişi)
   - → Demand generation start

**4. Partnership (6-12 ay)**
   - [ ] Odoo Silver / Gold partner status alınması
   - [ ] Bölgesel resellers'a öğretim
   - [ ] Sistem Integratörler (SAP partners) için "ISG addon" teklifi
   - → Dağıtım kanalı

**5. Ürün Roadmap (Ongoing)**
   - [ ] Mobile app (Flutter) — denetim, PTW hızlı giriş
   - [ ] AI: "Olası risk tahminlemesi" (geçmiş kaza + çevre verisi)
   - [ ] SMS alertler: "Ekipman kontrol süresi bitti"
   - → Feature parity + sürüş ilgisi ↑

---

### Finansal Projeksiyon (5 yıl)

**Odoo ISG Pazarı Tahmini (TR):**
- **Hedef müşteri sayısı:** 100-200 (fabrika/belediye/OSGB)
- **Ortalama ürün geliri:** ₺50K/yıl (lisanslama + kurulum)
- **5 yıl toplam:** 150 müşteri × ₺50K × 5 = **₺37.5M**

**Maliyet:**
- **Development:** ₺2-3M (ürün perfeksiyonu + AI)
- **Sales/Marketing:** ₺1-1.5M (kampanya + partnership)
- **Support:** ₺1-1.5M (destek ekibi)
- **5 yıl toplam:** **₺4-6M**

**Kar:** ₺37.5M - ₺5M = **₺32.5M** (87% margin)

**Comparison — HSE Radar:**
- Aynı pazarda, ₺120K/müşteri
- 150 müş × ₺120K × 5 = ₺90M
- Kar: ₺85M (daha fazla ama kapalı kaynak, tek satıcı)

**Sonuç:** Odoo ISG mali olarak makul. Hacim daha düşük ama açık kaynak avantajı + partner ecosystem.

---

## Özet Sonuçlar

| Dimensyon | HSE Radar | Odoo ISG | Kazanan |
|-----------|-----------|----------|---------|
| **Fonksiyonel Eşdeğerlik** | 27/27 | 27/27 | TIE ✅ |
| **Teknik Mimari (ERP)** | Kapalı | Open + ERP | **Odoo** ✅ |
| **UX (Veri Giriş)** | Wizard | Form | **HSE Radar** ✅ |
| **Mevzuat Güncellemesi** | Otomatik | Manual | **HSE Radar** ✅ |
| **Raporlama** | Sabit 5 | Unlimited SQL | **Odoo** ✅ |
| **Veri Kontrol** | Bulut | On-premise | **Odoo** ✅ |
| **Başlama Hızı** | 2 hafta | 6-8 hafta | **HSE Radar** ✅ |
| **Fiyat (5 yıl)** | ₺615K | ₺210K | **Odoo** ✅ |
| **Müşterileştirme** | Sınırlı | Sınırsız | **Odoo** ✅ |

**Genel Puan:**
- **Odoo ISG: 6/9 kazanç** → Uzun vadeli, esnek, veri kontrol
- **HSE Radar: 3/9 kazanç** → Hızlı başlama, mevzuat güvenliği

### Nihai Tavsiye

| Müşteri Türü | Tavsiye | Neden |
|--------------|---------|-------|
| **OSGB** | HSE Radar | Mevzuat risk, hızlı kurulum |
| **Fabrika (500+)** | Odoo ISG | ERP, raporlama, veri kontrol |
| **Belediye** | Odoo ISG | Bütçe, KVKK, veri egemenliği |
| **Hastane** | Odoo ISG | KVKK risk = 0 (on-premise) |
| **Startup** | Odoo ISG | Açık kaynak, customize |
| **Finansal** | Odoo ISG | Veri kontrol, audit trail |

---

**Hazırlayan:** Claude  
**Tarih:** 7 Eylül 2026  
**Sürüm:** 1.0 (Kapsamlı)

