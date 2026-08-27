# BACKLOG.md — Gelecek Geliştirmeler ve İyileştirmeler

Son revizyon: 26 Ağustos 2026 — HSE Radar karşılaştırma + MEV retrofit sprint

⚡ Çok Kısa Vadeli (isg_osgb Öncesi)

1. isg.rate.table modeli (isg_core) — ✅ TAMAMLANDI
   - Uzman/hekim katsayıları versiyonlu tabloya taşındı
   - isg_osgb ön koşulu

🔧 MEV Borcu / Retrofit Görevleri (Tamamlanmış Modüllerde)

| # | Modül | Görev | Öncelik | Tahmini | Durum |
|---|---|---|---|---|---|
| B-1 | isg_hr | Katsayıları isg.rate.table'a taşı | 🔴 | 0.5 gün | ✅ Tamamlandı |
| B-2 | isg_contractor | Risk Bilgilendirmesi belge türü | ⚠️ | 0.5 gün | ✅ Tamamlandı |
| B-3 | isg_visitor | risk_briefing alanları | ⚠️ | 0.5 gün | ✅ Tamamlandı |
| B-4 | isg_board | Toplantı sıklığı retrofit | ⚠️ | 1 gün | Sırada |
| B-5 | isg_board | 21 Oca 2026 hukuki teyidi | ⚠️ | Harici | Bekliyor |
| B-6 | isg_document | e-imza metadata alanları | ⚠️ | 0.5 gün | ✅ Tamamlandı |
| B-7 | isg_risk | renewal_trigger alanı | ⚠️ | 0.5 gün | ✅ Tamamlandı |
| B-8 | isg_penalty | Tarife versiyonlama | ⚠️ | 0.5-1 gün | Sırada |
| B-9 | isg_core | danger_class.history modeli | 🔴 | 0.5-1 gün | Sırada |
| B-10 | isg_training | 2 Nisan 2026 tam uyum | 🔴 | 2-3 gün | Sırada (kritik) |

Kalan: B-4, B-5 (teyit), B-8, B-9, B-10

🆕 Yeni Modül Tasarım Notları

- isg_equipment (F2-008): Ara.2025 EK-II + EKİPNET + e-imza en baştan
- isg_incident (F2-003): SGK 3 iş günü + iki yönlü bağlantı (training, risk)

📋 Kısa Vadeli (Sonraki Oturumlar)

1. isg_osgb detaylı view'ları (capacity planning, ziyaret kaydı)
2. B-4/B-8/B-9 MEV retrofit (~1.5-2 gün)
3. isg_incident (F2-003) başlangıç (~3-4 gün)
4. Reporting temel dashboard'ları

🔄 Orta Vadeli — FAZ 2 Tamamlama (Revize Sıralama)

1. F2-003 isg_incident — en kritik
2. F2-008 isg_equipment — mevzuat kritik, veri katalog hazırlığı
3. F2-007 isg_chemical — uzman doğrulaması uzun, paralel başla
4. F2-004 isg_audit — compliance ile doğal bağlantı
5. F2-009 isg_ptw + isg_loto — karmaşık durum makinesi
6. F2-005 isg_ppe — nispeten basit
7. F2-006 isg_emergency — nispeten basit

FAZ 3 — Ölçüm ve Çevre
- F3-001 isg_measurement_core + isg_measurement_hygiene
- F3-002 isg_environment

F1-002 isg_health_basic (Bloklu)
- KVKK danışman onayı bekleniyor

Uzun Vadeli (Üretim Hazırlığı)

1. Superset entegrasyonu
2. E3 sistem entegrasyonu (SGK, EKİPNET, İSG-KATİP, e-imza)
3. Mobil uygulama (Flutter)
4. Dokümantasyon ve eğitim

Bilinen Sorunlar (Açık Konular)

Teknik Uyarılar:
- isg_site.hazard_type: unknown parameter 'invisible'
- html4css1.css: Permission denied
- isg_risk.assessment.renewal_trigger: unknown parameter 'tracking' (warning)

İleride Ele Alınacak:
- SSH key setup (HTTPS → SSH)
- Database backup automation
- Monitoring ve alerting

Performans Optimizasyonları:
- Compute field indexing
- Search view cache
- Report query optimization
