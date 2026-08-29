# BACKLOG.md — Gelecek Geliştirmeler ve İyileştirmeler

**Son güncelleme:** 29 Ağustos 2026 — F2-004 isg_audit tamamlandı

---

## 🎯 Kısa Vadeli (Sonraki 1-2 hafta)

### FAZ 2 — Operasyonel Modüller (5 modül sırada)

Yazılacak sıralama (önem ve zaman):

1. **F2-005 isg_ppe** (~2 gün) — KKD yönetimi
   - `isg.ppe.type`: KKD türü (eldiven, gözlük, ayakkabı vb.)
   - `isg.ppe.inventory`: Stok yönetimi
   - `isg.ppe.allocation`: Çalışana zimmet kaydı
   - Yenileme takibi ve uyarı sistemi
   - isg_hr KKD beden ölçüleri entegrasyonu

2. **F2-006 isg_emergency** (~1.5 gün) — Acil durum planı
   - `isg.emergency.plan`: Acil durum planı
   - `isg.emergency.drill`: Tatbikat kaydı
   - `isg.emergency.evacuation`: Tahliye planı
   - isg_location toplanma noktaları entegrasyonu

3. **F2-007 isg_chemical** (~3-4 gün) — OEL/STEL limitleri
   - `isg.chemical`: Kimyasal envanter
   - `isg.chemical.exposure`: Maruziyet kaydı
   - OEL/STEL limit tablosu (Türkiye ÇSGB)
   - Depolama uyumluluk matrisi
   - Veri seti: OEL/STEL değerleri uzman doğrulaması
   - KKDIK/REACH yükümlülüğü (bildirim takvimi)

4. **F2-008 isg_equipment** (~2-3 gün) — 🔴 KRİTİK mevzuat
   - Ara.2025 EK-II ekipman kataloğu
   - Periyodik kontrol takvimi
   - EKİPNET hazırlık raporu (e-imza compat)
   - Yetkili muayene kuruluşu kaydı
   - Veri seti: EK-II ekipman listesi doğrulama (uzman onayı gerekir)

5. **F2-009 isg_ptw + isg_loto** (~3-4 gün) — En karmaşık
   - `isg.ptw`: İş İzni (sıcak iş, kapalı alan, elektrik, yüksekte, radyasyon, genel)
   - `isg.ptw.precondition`: Ön koşul kontrol listesi (inline)
   - `isg.loto`: LOTO izolasyon (enerji kaynağı kilitleme/etiketleme)
   - Çok aşamalı onay zinciri (talep → bölüm → uzman → kaptan)
   - Durum makinesi: requested → approved → active → closed
   - Kontrol noktaları ve kilitler (ortak kilit prosedürü)

### B-Görevleri — MEV Retrofit (~1.5-2 gün)

| # | Modül | Görev | Tahmini |
|---|---|---|---|
| B-4 | isg_board | Toplantı sıklığı (çok tehlikeli 15 gün, diğer 1 ay) | 1 gün |
| B-8 | isg_penalty | Tarife versiyonlama + 2026 %49 artış | 0.5-1 gün |
| B-9 | isg_core | danger_class.history modeli (değişim geçmişi) | 0.5-1 gün |
| B-10 | isg_training | 2 Nisan 2026 tam uyum | 2-3 gün |

---

## 🔄 Orta Vadeli (2-4 hafta)

### FAZ 3 — Ölçüm ve Çevre (~7-10 gün)

- **F3-001 isg_measurement_core + isg_measurement_hygiene** (~5-7 gün)
  - `isg.measurement.campaign` (yıllık ölçüm planı)
  - `isg.measurement.result` (ham sonuç)
  - Limit profili (sürümlü OEL/STEL)
  - Uygunluk değerlendirmesi (AŞIM → otomatik DÖF)
  - Yetkili laboratuvar akışı

- **F3-002 isg_environment** (~2-3 gün)
  - Atık kodu kataloğu
  - Atık depolama ve bertaraf
  - Çevre etki değerlendirmesi (düşük öncelik)

### FAZ 5 — Raporlama (~7-12 gün)

- **F5-001 isg_reporting** (~5-10 gün)
  - Superset entegrasyonu
  - Dashboard'lar (KPI: TRIR, LWDR, kaza sıklığı, uygunluk oranları)
  - Aylık/yıllık raporlar
  - ÇSGB rapor formatları
  - Sertifikalı veri kümeleri

- **F5-002 QWeb PDF şablonları** (~2-3 gün)
- **F5-003 HSE Radar Kabul Testi** (~2-3 gün)

### Bloklu

- **F1-002 isg_health_basic** — KVKK danışman onayı bekleniyor

---

## 📋 Uzun Vadeli (Üretim Hazırlığı)

### E2 Altyapı (Superset, Flutter, Multi-company)
- Superset entegrasyonu (F5 ile paralel)
- Flutter mobil uygulama
- Multi-company yönetim iyileştirmeleri

### E3 Sistem Entegrasyonu (SGK, EKİPNET, İSG-KATİP, E-imza)
- SGK API entegrasyonu (3 iş günü bildirimi)
- EKİPNET entegrasyonu (ekipman periyodik kontrol)
- İSG-KATİP entegrasyonu (uzman/hekim bildirimi)
- E-imza (5070 s.K.) — elektronik imza desteği
- VERBİS uyumu (kişisel veri işleme kaydı)

### E4 Analitik ve Yapay Zeka
- Risk tahminlemesi (geçmiş kaza verilerinden)
- Anomali tespiti (normal dışı ölçüm değerleri)
- Uyum önerme (otomatik aksiyon önerileri)

---

## 🐛 Teknik Borç ve Uyarılar

### Açık Konular
- [ ] isg_site.hazard_type — unknown parameter 'invisible' (view uyarısı)
- [ ] html4css1.css — Permission denied (CSS rendering)
- [ ] Admin şifresi — PostgreSQL NULL (kalıcı şifre gerekir)

### İyileştirmeler
- [ ] Compute field indexing (performans)
- [ ] Search view cache (hızlandırma)
- [ ] Report query optimization
- [ ] SSH key setup (HTTPS → SSH git)
- [ ] Database backup automation
- [ ] Monitoring ve alerting (Datadog veya Prometheus)

### Mevzuat Borcu (MEV) — F2-004 isg_audit Sonrası

| # | Modül | İssue | Öncelik | Status |
|---|---|---|---|---|
| MEV-001 | isg_training | 2 Nisan 2026 tam uyum | 🔴 Kritik | B-10 sırada |
| MEV-002 | isg_equipment | Ara.2025 EK-II + EKİPNET | 🔴 Kritik | F2-008 sırada |
| MEV-003 | isg_incident | SGK 3 iş günü + dönüş eğitimi | 🔴 Kritik | ✅ Tamamlandı |
| MEV-004 | isg_penalty | 2026 %49 artış + yıllık güncelleme | ⚠️ Yüksek | B-8 sırada |
| MEV-005 | isg_core | danger_class.history (değişim geçmişi) | ⚠️ Yüksek | B-9 sırada |
| MEV-006 | isg_contractor | Risk Bilgilendirmesi kaydı | ⚠️ Orta | ✅ Tamamlandı |
| MEV-007 | isg_visitor | risk_briefing alanları | ⚠️ Orta | ✅ Tamamlandı |
| MEV-008 | isg_board | 21 Oca 2026 Ulusal Konsey | ⚠️ Orta | B-4/B-5 sırada |
| MEV-009 | isg_risk | renewal_trigger (otomatik yenileme) | ⚠️ Orta | Tasarımda |
| MEV-010 | isg_document | e-imza (5070 s.K.) metadata | ⚠️ Orta | ✅ Tamamlandı |

---

## 📊 Proje İstatistikleri

| Metrik | Değer |
|---|---|
| Toplam Modül | 32 (42 B-görevleri dahil) |
| Kurulu Modül | 59 (Odoo native + ISG) |
| Toplam Model | 100+ |
| Kod Satırı | 18,000+ (Python + XML) |
| Commit Sayısı | 32+ |
| Proje Süresi | 30+ gün |
| HSE Radar Eşdeğerlik | %95+ (32 modül) |

---

## 🎯 Sonraki Adımlar

1. **Hemen başla:** FAZ 2 (F2-005 isg_ppe, F2-006, F2-007, F2-008, F2-009)
2. **Paralel:** B-4/B-8/B-9/B-10 MEV retrofit görevleri
3. **Son:** FAZ 3, FAZ 5, HSE Radar kabul testi
4. **Üretim:** E3 entegrasyonu (SGK, EKİPNET, İSG-KATİP, e-imza)

---

## 🏆 İçerik: isg_audit (F2-004) Tamamlanma Özeti

**Yapılan:**
- Puanlama/Skorlama sistemi (weight-based compliance %)
- Tekrarlanan bulgu takibi (repeat_count, escalation_level)
- Bulgu lifecycle (5 durum: open → resolved → closed)
- DÖF bağlantısı (otomatik + manual action)
- Kanıt dosyaları (ir.attachment support)
- Kanban view (durum bazlı kartlar)
- Alt işveren denetimi (contractor_id)
- Sequence (ISG-DNT + ISG-BLG)

**Sonuç:** HSE Radar'ın denetim modülünü tam eşdeğerlik + ek özelliklerle karşıladık.

