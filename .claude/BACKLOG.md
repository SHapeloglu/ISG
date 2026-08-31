# BACKLOG.md — Gelecek Geliştirmeler (31 Ağustos 2026)

## 🎯 Hemen Başlanacak (2-3 gün, ~5-7 gün)

### 1. B-4: isg_board — Toplantı Sıklığı — ~1 gün ⏳
**Mevzuat:** İSG Kurulları Yönetmeliği

**Sorun:** Danger_class'a göre farklı toplantı periyodu gerektirir
- Çok tehlikeli: 15 gün arası
- Diğer (az/tehlikeli): 1 ay arası

**Çözüm:**
- `isg_board_meeting.next_meeting_date_expected` compute'a danger_class ekle
- Test: çok tehlikeli 15 gün, normal 30 gün

---

### 2. B-8: isg_penalty — Versiyonlama + 2026 %49 Artış — ~0.5-1 gün ⏳
**Mevzuat:** 2026 ÇSGB ceza tutarları (yılda güncellenir)

**Sorun:** Ceza tutarları yılda güncelleniyor. Sistem geçmiş tarihli denetim için eski tarifeler bilmeli.

**Çözüm:**
- `isg.penalty.tariff` modeline `valid_from` (date) alanı ekle
- Ceza hesaplamasında `valid_from` dikkate alınsın
- Geçmiş tarihli simülasyonda (F4-004), o tarihte geçerli tarifeler kullanılsın
- Veri seti: her yıl 1 Ocak'ta yeni sürüm

---

### 3. B-9: isg_core — danger_class.history — ~0.5-1 gün ⏳
**Mevzuat:** İşyeri tehlike sınıfı değişiklikleri takibi

**Sorun:** İşyerinin tehlike sınıfı değişebiliyor. Sistem hangi dönemde hangi sınıf olduğunu bilmeli.

**Çözüm:**
- `isg.workplace.danger_class.history` ayrı modeli oluştur
  - workplace_id, danger_class_old → danger_class_new, change_date, reason, modified_by
- `isg_workplace.danger_class` onchange'e history kaydı oluştur
- Geçmiş uyunluk kontrolü, o tarihte geçerli danger_class'ı kullansın

---

### 4. F5-002 & F5-003 Kontrol — ~1 gün ⏳

**F5-002: QWeb PDF Şablonları**
- isg_reporting modülü kurulu ama PDF şablonları var mı kontrol et
- TRIR/LWDR raporları PDF çıktısı alabilir mi?

**F5-003: HSE Radar Kabul Testi**
- Test protokolü yazılmış mı?
- 27 HSE Radar işlev × 5 test = 135 senaryo
- Acceptance criteria belirle

---

## 📋 Uzun Vadeli (Sonrası)

### Competitive Gap Analysis (Sonraki Seans — Yüksek Öncelik)

Kapsamlı HSE Radar karşılaştırması:
- Mevzuat kapsam (hangi yönetmelikleri kaçırıyor?)
- UI/UX (kullanıcı deneyimi farkları)
- Entegrasyon (ERP, SGK, KVKK vb.)
- Raporlama (HSE Radar'ın en zayıf yanı)
- Performans (hacim, load testing)
- Fiyatlandırma/lisans modeli

---

### E3 Sistem Entegrasyon (2-3 hafta)

- **SGK API:** 3 günü kaza bildirimi otomasyonu
- **EKİPNET:** Periyodik kontrol sonuçlarını gönder
- **İSG-KATİP:** Uzman/hekim bildirimleri
- **E-imza (5070 s.K.):** Dokümanlara elektronik imza
- **VERBİS:** Kişisel veri işleme kaydı (KVKK md.7)

---

### E2 Altyapı (Paralel)

- **Superset:** TRIR/LWDR dashboard'ları
- **Flutter:** Mobil uygulama (denetim, PTW, ölçüm, kaza — offline mode)
- **Multi-company:** Record rule'lar daha esnek

---

### E4 Analitik (İleri)

- **Risk tahminlemesi:** Geçmiş kaza verilerinden ML modeli
- **Anomali tespiti:** Ölçüm outliers, compliance düşüşü
- **Uyum önerme:** Benzer işyerleri karşılaştırması

---

## 🐛 Teknik Borç

### Açık Konular
- [ ] isg_site.hazard_type — 'invisible' warning
- [ ] html4css1.css — Permission denied warning
- [ ] Admin şifresi — PostgreSQL NULL

### İyileştirmeler
- [ ] Compute field indexing (performans)
- [ ] Search view cache
- [ ] SSH key setup (HTTPS → SSH git)
- [ ] Database backup automation
- [ ] Monitoring (Datadog/Prometheus)

### Mevzuat Doğrulaması (Tamamlanan ✅)

| # | Modül | İssue | Öncelik | Status |
|---|---|---|---|---|
| MEV-001 | isg_training | 2 Nisan 2026 | 🔴 Kritik | ✅ B-10 TAMAMLANDI |
| MEV-004 | isg_penalty | 2026 %49 artış | ⚠️ Yüksek | B-8 sırada |
| MEV-005 | isg_core | danger_class.history | ⚠️ Yüksek | B-9 sırada |
| MEV-008 | isg_board | Toplantı sıklığı | ⚠️ Orta | B-4 sırada |

---

## ✅ Düzeltilen Hata

**BACKLOG.md Periyot Hatası:**
- **Eski (YANLIŞ):** B-10'da "periyot değerleri 24/12/6 ayda bir" yazılmıştı
- **Doğru:** RG 33212 Md 14 gereği: Az tehlikeli 36 ay (3 yıl), Tehlikeli 24 ay (2 yıl), Çok tehlikeli 12 ay (1 yıl)
- **Kod:** Mevcut isg_training_type.py zaten DOĞRU (period_low=36, period_medium=24, period_high=12)
- **Doğrulama:** Web araştırması yapılıp multiple bağımsız kaynaktan teyit edildi

---

## 🎯 Başlangıç Sırası (Tavsiye)

**Kısa Vadeli (2-3 gün):**
1. B-4, B-8, B-9 (~2-3 gün, paralel yapılabilir)
2. F5-002/F5-003 Kontrol (~1 gün)

**Sonraki Seans:**
3. **Competitive Gap Analysis** (~1-2 gün, rapor hazırlık)
4. Gap'leri kapatma (~1-2 hafta, prioritize)

**Ardından:**
5. E3 Entegrasyon (~2-3 hafta)
6. E2 Altyapı (~2-3 hafta)
7. HSE Radar Kabul Testi (full regression)
8. isg_health_basic (KVKK onayı sonrası)
