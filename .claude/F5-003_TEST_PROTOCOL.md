# F5-003 HSE Radar Kabul Testi — Test Protokolü

**Tarih:** 05 Eylül 2026  
**Amaç:** 27 HSE Radar işlevinin Odoo uygulamasında %90+ eşdeğerlik doğrulama  
**Yöntem:** CRUD + Kritik Workflow + Raporlama + Validasyon

---

## Test Alanları (27 İşlev)

### FAZ 0 — Temel Yapı (7 işlev)
1. ✅ Holding/Kurum/İşletme (isg_core) — CRUD + multi-company
2. ✅ Kullanıcı/Grup/Yetkilendirme (isg_security) — ACL test
3. ✅ Kurumsal/İletişim (isg_party) — Many2one relations
4. ✅ Yerleşim Birimleri (isg_location) — Lokasyon ağacı
5. ✅ İK ve Çalışanlar (isg_hr) — SEG, danger_class
6. ✅ Dokümantasyon (isg_document) — Sürüm, hash, kilit
7. ✅ Kurumsal Yazışma (isg_correspondence) — Deadline takibi

### FAZ 1 — Yönetişim (5 işlev)
8. ✅ İSG Kurulu (isg_board) — Toplantı, karar, yeter sayı
9. ✅ Alt İşverenler (isg_contractor) — Zincir, belge matrisi
10. ✅ Ziyaretçi Yönetimi (isg_visitor) — Giriş/çıkış, risk briefing
11. ✅ Eğitim (isg_training) — 2 Nisan 2026 yönetmelik, dönüş eğitimi
12. ⏳ Sağlık Gözetimi (isg_health_basic) — KVKK bloklu

### FAZ 2 — Operasyon (10 işlev)
13. ✅ Risk Değerlendirmesi (isg_risk) — Hazard, probability × severity
14. ✅ İş Kazası (isg_incident) — SGK 3 gün bildirimi, dönüş eğitimi tetikleyicisi
15. ✅ DÖF/CAPA (isg_capa) — State machine, kök neden, aksiyon
16. ✅ Denetim (isg_audit) — Bulgu, puanlama, tekrar sayısı
17. ✅ KKD Yönetimi (isg_ppe) — Envanter, zimmet, yenileme
18. ✅ Acil Durum (isg_emergency) — Plan, tatbikat, tahliye
19. ✅ Kimyasal (isg_chemical) — OEL/STEL, depolama uyumluluğu
20. ✅ Ekipman (isg_equipment) — EK-II, periyodik kontrol, EKİPNET
21. ✅ İş İzni (isg_ptw) — PTW, LOTO, ön koşul, çok aşamalı onay
22. ✅ Ölçüm (isg_measurement_hygiene) — Ham sonuç, limit sürüm

### FAZ 3 — Çevre (1 işlev)
23. ✅ Çevre Yönetimi (isg_environment) — Atık, depolama

### FAZ 4 — Mevzuat (3 işlev)
24. ✅ İdari Cezalar (isg_penalty) — 2026 tarife, valid_from
25. ✅ Sanal Müfettiş (isg_legislation + isg_compliance) — Yükümlülük, uygunluk
26. ✅ Simülatör (isg_simulator) — Workplace profili → ceza simülasyonu

### FAZ 5 — Raporlama (2 işlev)
27. ✅ Raporlar (isg_reporting) — PDF şablonları (F5-002), KPI

---

## Test Senaryoları (Her İşlev İçin)

### Senaryo 1: CRUD Temel
- **Create:** Record oluştur, alanları doldur
- **Read:** Kaydı oku, verify
- **Update:** Alan değiştir, kaydı güncelle
- **Delete:** Kaydı sil (uygunsa)

### Senaryo 2: Workflow/State Machine
- Örn. incident: draft → investigation → closed
- Örn. ptw: draft → active → closed
- State geçişi validation'ları

### Senaryo 3: Relations + Multi-level
- Many2one: employee → workplace, incident → employee
- One2many: audit → findings, ptw → precondition_checks
- Many2many: training → attendees
- Related fields (danger_class via workplace)

### Senaryo 4: Critical Business Logic
- Uzman/hekim süre hesaplaması (isg_hr)
- SGK 3 gün deadline (isg_incident)
- Risk puanı hesaplaması (isg_risk)
- Uygunluk yüzdesi (isg_audit)
- Dönüş eğitimi tetikleyicisi (isg_training)

### Senaryo 5: Raporlama + Validation
- PDF generate edilir mi?
- Doğru alanlar render mi?
- ERROR yok mu log'da?

---

## Test Çalışması Planı

### Gün 1: Sample Data + CRUD
- [ ] Her 27 işlev için min sample data oluştur (Python script)
- [ ] CRUD testleri çalıştır (gözlemsel)

### Gün 2: Workflow + Logic
- [ ] Critical workflow testleri (incident SGK bildir, ptw onay, etc.)
- [ ] Business logic validasyonları (süre calc, risk score, compliance %)

### Gün 3: Raporlama + Final
- [ ] 5 PDF raporu generate et + manual inspection
- [ ] Error log final taraması
- [ ] Acceptance test checklist

---

## Başarı Kriterleri

✅ **PASS** kriteri:
- 27 işlevin tümü CRUD yapabiliyor
- Kritik workflow'lar errorless çalışıyor
- 5 PDF raporu generate oluyor
- Log: ERROR = 0
- HSE Radar işlev eşdeğerliği ≥ 90%

---

**Başlangıç:** 05 Eylül 2026, 19:31 UTC
