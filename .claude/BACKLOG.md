# BACKLOG.md — Gelecek Geliştirmeler

**Son güncelleme:** 29 Ağustos 2026 — Doğrulama Oturumu

## 🎯 Hemen Başlanacak (1-2 hafta, ~7-9 gün)

### 1. isg_environment (F3-003) — ~2-3 gün ⏳
**Status:** Yazılmamış, git'te commit yok — UNUTULMUŞ GÖREV

Bileşenler:
- `isg.waste.code` — Atık kodu kataloğu (TR atık kodları)
- `isg.waste.storage` — Atık depolama alanı kaydı
- `isg.waste.disposal` — Atık bertaraf kaydı (tarih, miktar, maliyeti)
- Çevre etki değerlendirmesi (opsiyonel)

Views: Liste, form, kanban (depo durumu), search (atık tipi, lokasyon)

Mevzuat: Çevre kanunları, tehlikeli atık kaydı, depolama koşulları

---

### 2. B-4: isg_board — Toplantı Sıklığı — ~1 gün ⏳

**Sorun:** Mevzuat danger_class'a göre farklı toplantı periyodu gerektirir
- Çok tehlikeli: 15 gün arası
- Diğer: 1 ay arası

**Çözüm:**
- `isg_board_meeting.next_meeting_date_expected` compute'a danger_class ekle
- Kurul oluşturmasında danger_class'a göre başlangıç aralığı belirle
- Test: çok tehlikeli 15 gün, normal 30 gün

**Dosyalar:** isg_board/models/isg_board_meeting.py

---

### 3. B-8: isg_penalty — Versiyonlama + 2026 %49 Artış — ~0.5-1 gün ⏳

**Sorun:** Ceza tutarları yılda güncelleniyor. Sistem geçmiş tarihli denetim için eski tarifeler bilmeli.

**Çözüm:**
- `isg.penalty.tariff` modeline `valid_from` (date) alanı ekle
- Ceza hesaplamasında `valid_from` dikkate alınsın
- Geçmiş tarihli simülasyonda (F4-004), o tarihte geçerli tarifeler kullanılsın
- Veri seti: her yıl 1 Ocak'ta yeni sürüm (data xml)

**Dosyalar:** isg_penalty/models/isg_penalty_tariff.py, isg_simulator/models/isg_simulator.py

---

### 4. B-9: isg_core — danger_class.history — ~0.5-1 gün ⏳

**Sorun:** İşyerinin tehlike sınıfı değişebiliyor. Sistem hangi dönemde hangi sınıf olduğunu bilmeli.

**Çözüm:**
- `isg.workplace.danger_class.history` ayrı modeli oluştur
  - workplace_id, danger_class_old → danger_class_new, change_date, reason, modified_by
- `isg_workplace.danger_class` onchange'e history kaydı oluştur
- Geçmiş uyunluk kontrolü, o tarihte geçerli danger_class'ı kullansın

**Dosyalar:** isg_core/models/isg_core_danger_class_history.py (yeni)

---

### 5. B-10: isg_training — 2 Nisan 2026 Tam Uyum — ~2-3 gün ⏳

**Sorunlar:**

1. **İşe başlama eğitimi ayrı tür**
   - Yüz yüze zorunlu, uzaktan kabul edilmez
   - Minimum 2 saat, işe başlama günü
   - `isg.training.type.induction_flag` (boolean) ekle

2. **Tehlike sınıfına göre tekrar periyotları**
   - Az tehlikeli: 2 yıl
   - Tehlikeli: 1 yıl
   - Çok tehlikeli: 6 ay
   - `isg.training.type.repeat_months` (int)
   - next_training_date otomatik hesaplansın

3. **Dönüş eğitimi tetikleyicileri**
   - 6 ay uzak kaldı → dönüş eğitimi
   - Kaza geçirdi → dönüş eğitimi
   - F2-003 isg_incident'ten: state=resolved → otomatik isg_training.record oluştur

4. **Özel gruplar**
   - Genç (18-25), yaşlı (55+), engelli, gebe/emziren
   - `hr.employee.special_group` (multi-select)
   - Eğitim planında özel grup bazlı ayarlamalar

**Dosyalar:** isg_training/models/*.py, hr_employee _inherit (special_group, last_attendance_date)

**Entegrasyon:** isg_incident (state=resolved → training.record), hr_attendance (son tarih)

---

### 6. F5-002 & F5-003 Kontrol — ~1 gün ⏳

**F5-002: QWeb PDF Şablonları**
- isg_reporting modülü kurulu ama PDF şablonları var mı kontrol et
- TRIR/LWDR raporları PDF çıktısı alabilir mi?

**F5-003: HSE Radar Kabul Testi**
- Test protokolü yazılmış mı?
- 27 HSE Radar işlev × 5 test = 135 senaryo
- Acceptance criteria belirle

---

## 📋 Uzun Vadeli (Sonrası)

### E3 Sistem Entegrasyon (2-3 hafta)

- **SGK API:** 3 günü kaza bildirimi otomasyonu
- **EKİPNET:** Periyodik kontrol sonuçlarını gönder
- **İSG-KATİP:** Uzman/hekim bildirimleri
- **E-imza (5070 s.K.):** Dokümanlara elektronik imza
- **VERBİS:** Kişisel veri işleme kaydı (KVKK md.7)

### E2 Altyapı (Paralel)

- **Superset:** TRIR/LWDR dashboard'ları
- **Flutter:** Mobil uygulama (denetim, PTW, ölçüm, kaza — offline mode)
- **Multi-company:** Record rule'lar daha esnek

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

### Mevzuat Borcu (MEV)

| # | Modül | İssue | Öncelik | Status |
|---|---|---|---|---|
| MEV-001 | isg_training | 2 Nisan 2026 | 🔴 Kritik | B-10 sırada |
| MEV-004 | isg_penalty | 2026 %49 artış | ⚠️ Yüksek | B-8 sırada |
| MEV-005 | isg_core | danger_class.history | ⚠️ Yüksek | B-9 sırada |
| MEV-008 | isg_board | Toplantı sıklığı | ⚠️ Orta | B-4 sırada |

---

## 🎯 Başlangıç Sırası (Tavsiye)

**Kısa Vadeli (7-9 gün):**
1. isg_environment (~2-3 gün)
2. B-4, B-8, B-9, B-10 (~4-5 gün, paralel yapılabilir)
3. F5-002/F5-003 Kontrol (~1 gün)

**Ardından:**
4. Superset + raporlama (~1-2 hafta)
5. E3 Entegrasyon (~2-3 hafta)
6. Flutter mobil (~2-3 hafta)

**Son:**
7. HSE Radar kabul testi (full regression)
8. isg_health_basic (KVKK onayı sonrası)
