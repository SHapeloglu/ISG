# ISG Platform — Backlog

Proje Durumu: 27/32 modül (%84)

## Tamamlanan Modüller (27)

FAZ 0-2 (16): isg_core, isg_security, isg_party, isg_location, isg_contractor,
  isg_board, isg_correspondence, isg_visitor, isg_capa, isg_risk, isg_incident,
  isg_audit, isg_emergency, isg_ppe, isg_chemical, isg_equipment, isg_ptw

FAZ 3 (2): isg_measurement_core, isg_measurement_hygiene

FAZ 4 (3): isg_legislation, isg_compliance, isg_penalty

FAZ 5 (1): isg_reporting

## Sıradaki Modüller (5)

1. F4-004 isg_simulator — Müfettiş Simülasyonu
   - Priority: Yüksek (HSE Radar parity %90 için)
   - Estimate: 1-2 hafta
   - Scope: Workplace profili → uygunluk özeti → ceza simülasyonu

2. OSGB Modülü — Ortak Sağlık Güvenlik Birimi
   - Priority: Yüksek
   - Estimate: 2-3 hafta
   - Scope: Uzman/hekim görevlendirme, sözleşme yönetimi

3. isg_health_basic — Sağlık Veri Yönetimi (F1-002)
   - Priority: Orta (KVKK onayı bekleme)
   - Estimate: 3-4 hafta (legal review sonrasında)
   - Scope: Sağlık taraması, periyodik muayene, KVKK maskeleme

4. EKİPNET Entegrasyonu
   - Priority: Düşük
   - Estimate: 4-6 hafta
   - Scope: Resmi iş ekipmanlı bilgi sistemi API

5. Entegrasyon Testleri (50-kayıt bulk test)
   - Priority: Yüksek (QA)
   - Estimate: 1-2 hafta
   - Scope: Modüller arası veri akışı, bug fix

## Deferred (Ertelenen)

- SSH GitHub Setup (erteleme nedeni: HTTPS çalışıyor)
- Advanced Raporlama (Superset BI entegrasyonu)
- Mobile App (later phase)

## Known Issues

- KVKK sağlık veri maskeleme: Dış hukuk danışmanı onayı bekleniyor
- EKİPNET API dokümantasyonu: Resmi kaynak yetersiz
- Tekrar ihlal çarpanı: Şu an basit (2.0), tarih-temelli kontrol gerekli

## HSE Radar Parity Hedefi

Mevcut: %84 (27/32 modül)
Hedef: %90+ (F4-004 isg_simulator + OSGB ile)

Feature Coverage:
- Risk: ✅
- Kaza: ✅
- Eğitim: ✅
- Ölçüm: ✅
- Mevzuat: ✅
- Ceza: ✅
- Simülasyon: ⏳ (sırada)
- Odoo Entegrasyonu: ✨ (avantaj)
