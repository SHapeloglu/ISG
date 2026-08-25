# BACKLOG.md — Gelecek Geliştirmeler ve İyileştirmeler

_Son revizyon: 25 Ağustos 2026 — HSE Radar karşılaştırma raporu sonrası_

---

## ⚡ Çok Kısa Vadeli (isg_osgb Öncesi — Ön Koşul)

Bu madde isg_osgb'nin doğrudan bağımlı olduğu, önce bitmesi gereken tek kalem:

1. **isg.rate.table modeli (isg_core içinde)** — ✅ ONAYLANDI
   - Uzman/hekim süre katsayılarını (tehlike_sinifi × rol → dakika) isg_hr'den ayrı, versiyonlu (`valid_from` alanlı) ortak bir tabloya çıkar
   - Gerekçe: isg_osgb aynı katsayıları tekrar kullanacak; versiyonsuz olursa geçmiş tarihli hesaplama (2024'te kaç dk gerekiyordu) imkansız — isg_compliance'daki snapshot mimarisiyle aynı prensip
   - isg_hr'nin mevcut compute metodu bu tablodan okuyacak şekilde güncellenir
   - Tahmini: ~0.5 gün
   - **isg_osgb'den önce yapılmalı**

---

## 🔧 MEV Borcu / Retrofit Görevleri (Tamamlanmış Modüllerde)

HSE Radar karşılaştırma raporu §2-3'ten. "✅ tamamlandı" işaretli modüllerde 2025-2026 mevzuat değişikliklerinden kaynaklanan eksikler. Sistemi çalışmaz hale getirmiyor ama F5-003 (HSE Radar kabul testi) öncesi kapatılmalı.

| # | Modül | Görev | Öncelik | Tahmini | Bağımlılık | Durum |
|---|---|---|---|---|---|---|
| B-1 | isg_hr | Katsayıları isg.rate.table'a taşı (MEV-005) | 🔴 | 0.5 gün | — | ✅ Onaylandı, ilk sırada |
| B-2 | isg_contractor | "İşyerine Özgü Risk Bilgilendirmesi" belge türü ekle (MEV-007) | ⚠️ | 0.5 gün | — | Öneri sunuldu |
| B-3 | isg_visitor | `risk_briefing_ack` + `risk_briefing_date` + tutanak alanı (MEV-008) | ⚠️ | 0.5 gün | — | Öneri sunuldu |
| B-4 | isg_board | Toplantı sıklığı kuralını isg_legislation obligation kaydına bağla (retrofit) | ⚠️ | 1 gün | isg_legislation (hazır) | Öneri sunuldu |
| B-5 | isg_board | 21 Oca 2026 Ulusal Konsey Yönetmeliği hukuki teyidi (MEV-010) | ⚠️ | Harici (hukuki) | — | Bekliyor |
| B-6 | isg_document | e-imza metadata alanları (`signature_type`, `signer_name`, `cert_serial`, `sign_date`) — gerçek entegrasyon E3'e ertelendi (MEV-011) | ⚠️ | 0.5 gün | — | Öneri sunuldu |
| B-7 | isg_risk | `renewal_trigger` alanı ekle (Periyodik/Kaza/Ekipman/Taşınma/Yeni Teknoloji) — otomasyon isg_incident'ı bekler (MEV-009) | ⚠️ | 0.5 gün (alan) | isg_incident (otomasyon için) | Öneri sunuldu |
| B-8 | isg_penalty | Tarife tablosunda `valid_from`/`valid_to` versiyon kontrolü — 2026 %49 zam yeni kayıt olarak girilmeli, üzerine yazılmamalı (MEV-004) | ⚠️ | 0.5-1 gün | — | Öneri sunuldu |
| B-9 | isg_core | `isg.workplace.danger.class.history` modeli — tehlike sınıfı değişim geçmişi (MEV-006). **Not:** Bu sadece mevzuat borcu değil, isg_compliance'ın snapshot mimarisiyle mimari tutarlılık sorunu da taşıyor — geçmiş tarihli değerlendirme o tarihteki sınıfı bilmeli | 🔴 | 0.5-1 gün | — | Öneri sunuldu, öncelik yükseltildi |
| B-10 | isg_training | 🔴 KRİTİK, 2 Nisan 2026 tam uyumu (MEV-001) — bkz. aşağıda ayrı ele alınmış | 🔴 | ~2-3 gün | isg_incident (kısmen) | Öneri sunuldu |

### B-10 Detay — isg_training MEV-001

**(A) Şimdi yapılabilir:**
- `isg.training.type`'a `is_onboarding` ayrımı + constraint (`min_duration_hours=2`, `delivery_method` zorunlu yüz yüze)
- Tehlike sınıfı bazlı tekrar takvimi kontrolü (mevcut `regulation_compliant` compute'unu genişlet)
- Özel grup (genç/yaşlı/engelli/gebe) planı — ⚠️ **KVKK dikkat:** gebelik hassas veri, isg_health_basic'teki ACL mantığıyla aynı şekilde korunmalı

**(B) isg_incident'ı bekliyor:**
- "Kaza geçirdi → dönüş eğitimi" otomatik tetikleyicisi
- "6 ay işten uzak kaldı" tetikleyicisi — isg_hr'daki izin/rapor verisine bağımlı, ayrıca kontrol edilmeli

---

## 🆕 Yeni Modül Tasarım Notları (Henüz Yazılmamış)

Bunlar zaten roadmap'te ama HSE Radar analizinde çıkan tasarım uyarıları:

- **isg_equipment (F2-008):** Ara.2025 EK-II güncel listesi + EKİPNET + e-imza alanları **en baştan** dahil edilmeli, sonradan MEV görevi açılmasın (MEV-002)
- **isg_incident (F2-003):** SGK 3 iş günü bildirim uyarısı + **iki yönlü bağlantı en baştan tasarlanmalı**: (1) kaza kapanınca → isg_training'de otomatik ihtiyaç kaydı, (2) kaza kapanınca → isg_risk'te `renewal_trigger=kaza` işareti. Basit Many2one + action yeterli, event-bus gerekmez (MEV-003)

---

## 📋 Kısa Vadeli (Sonraki Oturumlar)

1. **B-1: isg.rate.table** (isg_osgb ön koşulu — bkz. yukarı)

2. **isg_osgb Modülü**
   - OSGB profili ve uzman/hekim kadrosu
   - İşyeri-Uzman atama
   - Süre uygunluk kontrolü (6331 md.6) — isg.rate.table'dan okur
   - Kapasite planlama
   - İSG-KATİP hazırlık

3. **isg_incident (F2-003)** — MEV-003 tasarım notlarıyla birlikte, öncelik yükseltildi (bkz. §6 sıralama revizyonu)

4. **F5-001 isg_reporting** — temel dashboard'larla başla (compliance/risk/penalty zaten hazır), F2 modülleri bitikçe genişlet
   - QWeb PDF şablonları
   - Superset entegrasyonu
   - Compliance/Risk/Penalty dashboards (erken versiyon)
   - HSE Radar kabul testi (F5-003) — MEV borcu kapatıldıktan sonra

5. **Entegrasyon Testi**
   - 50-record/modül bulk test
   - Compliance chain: legislation → compliance → penalty → simulator
   - Risk chain: hazard → assessment → control → CAPA

---

## 🔄 Orta Vadeli — FAZ 2 Tamamlama (Revize Sıralama)

HSE Radar raporu §6 önerisine göre yeniden sıralandı (mevzuat kritikliği + bağımlılıklar + karmaşıklık):

1. **F2-003 isg_incident** — en kritik, isg_training ve isg_risk'in eksik parçaları buna bağımlı
2. **F2-008 isg_equipment** — mevzuat kritik (Ara.2025 EK-II), veri kataloğu hazırlığı zaman alır, erken başlanmalı
3. **F2-007 isg_chemical** — OEL/STEL veri seti uzman doğrulaması uzun sürebilir, paralel ilerlesin diye erken başlatılmalı
4. **F2-004 isg_audit** — Sanal Müfettiş (compliance) motoruyla doğal bağlantısı var, görece kolay
5. **F2-009 isg_ptw + isg_loto** — en karmaşık durum makinesi, orta-geç sırada
6. **F2-005 isg_ppe** — nispeten basit (stock.move bağlantılı)
7. **F2-006 isg_emergency** — nispeten basit (location bağlantılı)

## FAZ 3 — Ölçüm ve Çevre
- F3-001 isg_measurement_core + isg_measurement_hygiene
- F3-002 isg_environment

## F1-002 isg_health_basic (Bloklu)
- KVKK danışman onayı bekleniyor
- Sağlık verisi maskeleme mimarisi
- Rıza yönetimi

---

## Uzun Vadeli (Üretim Hazırlığı)

1. **Superset Entegrasyonu**
   - Raporlama dashboards kurulumu
   - Real-time data pipeline
   - Mobile dashboards

2. **E3 Sistem Entegrasyonu**
   - SGK bildirimleri (TTKB)
   - EKİPNET entegrasyonu
   - İSG-KATİP entegrasyonu
   - Gerçek e-imza (TÜRKKEP/e-Güven) — B-6'nın metadata hazırlığı üzerine

3. **Mobil Uygulama**
   - Flutter uygulaması
   - Field risk assessment
   - Incident reporting

4. **Kullanıcı Dokümantasyonu**
   - Kullanım kılavuzları
   - Video eğitim serileri
   - Eğitim materyalleri

5. **Üretim Dağıtımı**
   - Docker containerization
   - Cloud deployment (AWS/Azure)
   - High availability setup
   - Backup strategy

---

## Bilinen Sorunlar (Açık Konular)

### Teknik Uyarılar
- isg_site.hazard_type: unknown parameter 'invisible' (işlevsel değil)
- html4css1.css: Permission denied (CSS rendering uyarısı)
- isg_risk.line: Model declared but cannot be loaded (FAZ 2 kalıntısı)

### İleride Ele Alınacak
- SSH key setup (HTTPS → SSH git authentication)
- Database backup automation
- Monitoring ve alerting sistemi

### Performans Optimizasyonları
- Compute field indexing
- Search view cache
- Report query optimization
