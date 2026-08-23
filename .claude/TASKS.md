# İSG Platform — Proje Görevleri (Tasks)

**Proje Durumu: 27/32 modül (%84) — FAZ 4 Devam**

## Tamamlanan Görevler ✅

### FAZ 0–2: Temel İSG (100%)
- ✅ isg_core, isg_security, isg_party, isg_location, isg_contractor
- ✅ isg_board, isg_correspondence, isg_visitor
- ✅ isg_capa, isg_risk, isg_incident, isg_audit, isg_emergency
- ✅ isg_ppe, isg_chemical, isg_equipment, isg_ptw

### FAZ 3: Ölçüm (100%)
- ✅ isg_measurement_core, isg_measurement_hygiene

### FAZ 5: Raporlama (100%)
- ✅ isg_reporting (TRIR/LWDR KPIs)

### FAZ 4: Mevzuat/Uygunluk (75%)
- ✅ F4-001 isg_legislation — Mevzuat kataloğu
- ✅ F4-002 isg_compliance — Uygunluk değerlendirme motoru
- ✅ F4-003 isg_penalty — Ceza hesaplama motoru (ÇSGB 2026)
- ⏳ F4-004 isg_simulator — Müfettiş simülasyonu (sırada)

## Sıradaki Görevler (Backlog)

### Kısa Vadeli (1–2 haftaya)
1. **F4-004 isg_simulator** — Simülasyon motoru
   - Workplace profili → uygunluk özeti → ceza tahmini
   - Rapor: muhtemel ceza, risk alanları, iyileştirme önerileri
   - Deadline: Bu hafta

2. **OSGB Modülü** — Son FAZ modülü
   - Ortak Sağlık Güvenlik Birimi yönetimi
   - Sözleşme, hizmet kapsamı, uzman/hekim atama
   - Deadline: 2–3 hafta

### Orta Vadeli (1 ay)
3. **Entegrasyon Testleri** — 50-kayıt bulk test
   - Her modül için 50 örnek veri
   - Modüller arası veri akışı doğrulama
   - Bug fix ve optimizasyon

4. **SSH GitHub Setup** — VCS güvenliği
   - Contabo VPS'ten SSH key oluşturma
   - GitHub'da deploy key tanımı
   - HTTP → SSH geçişi

### Uzun Vadeli (2 ay+)
5. **KVKK Sağlık Veri Maskeleme** — Yasal uygunluk
   - Dış hukuk danışmanı onayı (beklemede)
   - isg_health_basic modülü (F1-002)
   - Veri şifreleme ve erişim kontrolleri

6. **EKİPNET Entegrasyonu** — Dış sistem bağlantısı
   - Resmi iş ekipmanlı bilgi sistemi API
   - isg_equipment'dan veri export
   - Real-time senkronizasyon

7. **HSE Radar Gap Analizi** — Final parity check
   - Feature-by-feature karşılaştırma
   - Eksik alanlar ve iyileştirmeler
   - Deployment readiness raporu

## Not: Tamamlanan Modüller
- 27/32: isg_core, isg_security, isg_party, isg_location, isg_contractor, isg_board,
  isg_correspondence, isg_visitor, isg_capa, isg_risk, isg_incident, isg_audit,
  isg_emergency, isg_ppe, isg_chemical, isg_equipment, isg_ptw,
  isg_measurement_core, isg_measurement_hygiene, isg_reporting,
  isg_legislation, isg_compliance, isg_penalty

- 5 eksik (sırada): isg_simulator, isg_osgb (OSGB), isg_health_basic (sağlık — KVKK bekleme),
  + 2 ek modül (EKİPNET, advanced raporlama)
