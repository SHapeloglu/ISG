# BACKLOG.md — Detaylı Proje Referans ve Planı

## HSE Radar Paritesi Hedefi

Hedefimiz HSE Radar'ın Türkiye ISG fonksiyonlarının %90+ kaplicağını yapmak + Odoo ERP entegrasyonu.

**Şu anki kapsama: ~60%**

### Tamamlanan HSE Radar Fonksiyonları ✅
- Risk Değerlendirmesi (L Matrisi + Fine-Kinney)
- İş Kazası / Ramak Kala Takibi
- Denetim & Bulgu Kaydı
- KKD Yönetimi (Zimmet, Envanter)
- Acil Durum Planı (Tatbikat)
- Kurumsal Yönetişim (Kurul, Eğitim, Yazışma)

### Planlanmış HSE Radar Fonksiyonları (Devam Ediyor)
- Kimyasal Envanter + OEL/STEL (F2-007) — BAŞLANDI
- Ekipman Periyodik Kontrol (F2-008) — SIRA
- İş İzni (PTW) Sistemi (F2-009) — SIRA

### Henüz Yapılmamış (FAZ 3-5)
- Ölçüm Orkestrasyonu (Gürültü, Toz, Titreşim, Işık)
- Mevzuat Motoru (Yükümlülük, Uygunluk Değerlendirmesi)
- OSGB Planlama (Uzman/Hekim Görevlendirmesi)
- Raporlama (TRIR, LWDR, Histogram)

---

## Detaylı Modül Planı (32 modül)

### FAZ 0 — Temel Mimari (7 TAMAMLANDI)
Veri modeli, security, base templates

### FAZ 1 — Kurumsal Yönetişim (6, 5 TAMAMLANDI)
Kurul, Eğitim, Alt işveren, Çalışan, Yazışma, Ziyaretçi
**Bekleyen:** F1-002 isg_health_basic (KVKK danışman onayı)

### FAZ 2 — Çekirdek ISG Operasyonları (9, 7 TAMAMLANDI)
**Tamamlanan:**
- F2-001: isg_capa (DÖF/CAPA)
- F2-002: isg_risk (Risk değerlendirmesi)
- F2-003: isg_incident (İş kazası)
- F2-004: isg_audit (Denetim)
- F2-005: isg_ppe (KKD)
- F2-006: isg_emergency (Acil durum)
- F2-007: isg_chemical (Kimyasal — YENİ)

**Sırada:**
- F2-008: isg_equipment (Ekipman kontrol)
- F2-009: isg_ptw + isg_loto (İş izni)

### FAZ 3 — Ölçüm & Çevre (2, 0 TAMAMLANDI)
- F3-001: isg_measurement_core + isg_measurement_hygiene
  - Gürültü (OEL/STEL)
  - Toz (İnhalasyon, depo)
  - Kimyasal (Buhar, maruziyet)
  - Titreşim
  - Işık (Lux)
  - Isıl konfor (PMV/PPD)
  
- F3-002: isg_environment (Çevre etkisi analizi)

### FAZ 4 — Sanal Müfettiş (4, 0 TAMAMLANDI)
- F4-001: isg_legislation + isg_obligation
  - Mevzuat kaydı ve sürüm takibi
  - Yükümlülük motoru (kural tabanlı)
  
- F4-002: isg_compliance (Uygunluk değerlendirmesi)
  - Kanıt yönetimi
  - Snapshot (tarihi dondurma)
  
- F4-003: isg_penalty (Ceza ve yaptırımlar)
  - 2026 idari ceza tutarları
  
- F4-004: isg_simulator (Sanal müfettiş)
  - İşyeri profili → otomatik kontrol listesi

### FAZ 5 — Raporlama & İş Zekası (3, 0 TAMAMLANDI)
- F5-001: isg_reporting + Superset
  - TRIR, LWDR, Frequency Rate
  - Trend analizi, histogram
  
- F5-002: QWeb PDF şablonları
  - Risk matrisi raporu
  - Denetim bulgusu
  - Kaza raporu
  
- F5-003: HSE Radar test & acceptance
  - Feature parity doğrulama
  - Performance vs. HSE Radar

### Özel Modüller (OSGB)
- isg_osgb: OSGB planlama ve görevlendirme
  - Uzman/hekim süre hesaplama (6331 md.6)
  - Kapasite planlama
  - İSG-KATİP bildirimi

---

## Bilinen Technical Debt

### Açık Hatalar
1. `isg_contractor.contractor_level` — recursive=True eksik
2. `isg_location.hazard_type` — unknown parameter 'invisible' (view upgrade)
3. `isg_ppe.type.size_type` — unknown parameter 'invisible' (view upgrade)
4. `isg_risk.site_id` — NOT NULL constraint warning (işlevsel, operasyonel)
5. Admin şifresi — kalıcı şifre belirlenmeli

### Eksik Record Rules
- isg_risk_line, isg_audit_line, isg_ppe_issue — çok işyeri/site izolasyonu
- isg_chemical_inventory — workplace filtering

### KVKK / Sağlık Verisi
- isg_health_basic → ACL maskeleme (hekim grubu dışında göremez)
- Erişim log kaydı eksik
- Açık rıza tracking eksik

---

## Gelecek İcra Planı

### Sonraki 2-3 Hafta (FAZ 2 Tamamlama)
- F2-008 isg_equipment (EKİPNET entegrasyonu)
- F2-009 isg_ptw + isg_loto (çok aşamalı onay)

### Sonraki 1 Ay (FAZ 3 Başlangıç)
- Ölçüm orkestrasyonu iskeletleri
- OEL/STEL veri seti hazırlığı

### 2+ Ay (FAZ 4-5)
- Mevzuat/yükümlülük motoru
- Raporlama & BI

---

## Not: Sürüm Geçmişi

- **8 Ağustos 2026**: FAZ 1 tamamlandı (5 modül)
- **14 Ağustos 2026**: FAZ 2 başlandı (isg_chemical hazırlığı)
- **15 Ağustos 2026**: F2-007 isg_chemical kurulu, FAZ 2 7/9 = %78
