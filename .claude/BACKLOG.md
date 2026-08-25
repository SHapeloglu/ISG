# BACKLOG.md — Gelecek Geliştirmeler ve Iyileştirmeler

Kısa Vadeli (Sonraki Oturum)

1. isg_osgb Modülü Başlat
   - OSGB profili ve uzman/hekim kadrosu
   - İşyeri-Uzman atama
   - Süre uygunluk kontrolü (6331 md.6)
   - Kapasite planlama
   - İSG-KATİP hazırlık

2. F5-001 isg_reporting
   - QWeb PDF şablonları
   - Superset entegrasyonu
   - Compliance/Risk/Penalty dashboards
   - HSE Radar kabul testi

3. Entegrasyon Testi
   - 50-record/modül bulk test
   - Compliance chain: legislation → compliance → penalty → simulator
   - Risk chain: hazard → assessment → control → CAPA

Orta Vadeli (Gelecek Faseler)

FAZ 2 Tamamlama
- F2-003 isg_incident (İş kazası bildirimi)
- F2-004 isg_audit (Denetim ve kontrol listeleri)
- F2-005 isg_ppe (KKD yönetimi)
- F2-006 isg_emergency (Acil durum planı)
- F2-007 isg_chemical (Kimyasal envanter)
- F2-008 isg_equipment (Ekipman ve periyodik kontrol)
- F2-009 isg_ptw + isg_loto (İş izni ve LOTO)

FAZ 3 — Ölçüm ve Çevre
- F3-001 isg_measurement_core + isg_measurement_hygiene
- F3-002 isg_environment

F1-002 isg_health_basic (Bloklu)
- KVKK danışman onayı bekleniyor
- Sağlık verisi maskeleme mimarisi
- Rıza yönetimi

Uzun Vadeli (Üretim Hazırlığı)

1. Superset Entegrasyonu
   - Raporlama dashboards kurulumu
   - Real-time data pipeline
   - Mobile dashboards

2. E3 Sistem Entegrasyonu
   - SGK bildirimleri (TTKB)
   - EKİPNET entegrasyonu
   - İSG-KATİP entegrasyonu

3. Mobil Uygulama
   - Flutter uygulaması
   - Field risk assessment
   - Incident reporting

4. Kullanıcı Dokümantasyonu
   - Kullanım kılavuzları
   - Video eğitim serileri
   - Eğitim materyalleri

5. Üretim Dağıtımı
   - Docker containerization
   - Cloud deployment (AWS/Azure)
   - High availability setup
   - Backup strategy

Bilinen Sorunlar (Açık Konular)

Teknik Uyarılar
- isg_site.hazard_type: unknown parameter 'invisible' (işlevsel değil)
- html4css1.css: Permission denied (CSS rendering uyarısı)
- isg_risk.line: Model declared but cannot be loaded (FAZ 2 kalıntısı)

Ileride Ele Alınacak
- SSH key setup (HTTPS -> SSH git authentication)
- Database backup automation
- Monitoring ve alerting sistemi

Performans Optimizasyonları
- Compute field indexing
- Search view cache
- Report query optimization
