# BACKLOG.md — Detaylı Proje Referans (16 Ağustos 2026)

## HSE Radar Paritesi Hedefi

Hedefimiz HSE Radar'ın Türkiye ISG fonksiyonlarının %90+ kaplicağını yapmak.

**Şu anki kapsama: ~65%** (20/32 modül)

## Tamamlanan HSE Radar Fonksiyonları ✅
- Risk Değerlendirmesi (L Matrisi + Fine-Kinney)
- İş Kazası / Ramak Kala Takibi
- Denetim & Bulgu Kaydı
- KKD Yönetimi (Zimmet, Envanter)
- Acil Durum Planı (Tatbikat)
- Kurumsal Yönetişim (Kurul, Eğitim, Yazışma)
- Kimyasal Envanter + SDS
- Ekipman Periyodik Kontrol (EKİPNET)
- İş İzni (PTW) + LOTO

## Planlanmış Fonksiyonlar (FAZ 3-5)
- Ölçüm Orkestrasyonu (Gürültü, Toz, Titreşim, Işık)
- Mevzuat Motoru (Yükümlülük, Uygunluk Değerlendirmesi)
- OSGB Planlama (Uzman/Hekim Görevlendirmesi)
- Raporlama (TRIR, LWDR, Histogram)

---

## Modül Detayları (20/32)

### FAZ 0 — Temel Mimari (7/7 ✅)
- isg_core (İşyeri, site, uzman/hekim süre hesaplama)
- isg_security (5 rol: readonly, expert, physician, manager, superadmin)
- isg_party (OSGB/Lab/Muayene/Altİşveren rolleri)
- isg_location (GPS, kapasite, toplanma noktası)
- isg_document (SHA-256, sürüm/kilit/e-imza)
- isg_hr (SEG, çalışan İSG profili)
- isg_base (UUID mixin, outbox altyapısı)

### FAZ 1 — Kurumsal Yönetişim (5/6 ✅)
- isg_contractor (Alt işveren zinciri, belge matrisi)
- isg_training (Eğitim planı, 2 Nisan 2026 yönetmelik)
- isg_visitor (Ziyaretçi kaydı, KKD bildirimi)
- isg_board (İSG kurulu, toplantı, karar takibi)
- isg_correspondence (Gelen/giden yazışma, yasal süre)
- **Bekleyen:** isg_health_basic (KVKK maskeleme) — EN SONA

### FAZ 2 — Çekirdek ISG Operasyonları (9/9 ✅ TAMAMLANDI)
- isg_capa (DÖF/CAPA, kök neden analizi)
- isg_risk (Risk matrisi, kontrol önlemleri, yenileme koşulları)
- isg_incident (İş kazası, SGK bildirimi, ramak kala)
- isg_audit (Denetim planı, kontrol listeleri, bulgu kaydı)
- isg_ppe (KKD envanter, zimmet, yenileme takibi)
- isg_emergency (Acil durum planı, tatbikat, tahliye)
- isg_chemical (Kimyasal envanter, SDS, GHS, depolama uyumluluğu)
- isg_equipment (EK-II kataloğu, periyodik kontrol, EKİPNET)
- isg_ptw (İş izni, ön koşullar, çok aşamalı onay, LOTO)

### FAZ 3 — Ölçüm & Çevre (0/2 — Sırada)
- isg_measurement_core + isg_measurement_hygiene
  - Gürültü (OEL/STEL)
  - Toz, kimyasal buhar, titreşim, işık
  - Yetkili laboratuvar onay akışı

- isg_environment (Çevre etkisi analizi)

### FAZ 4 — Sanal Müfettiş (0/4)
- isg_legislation + isg_obligation (Mevzuat/yükümlülük motoru)
- isg_compliance (Uygunluk değerlendirmesi, kanıt yönetimi)
- isg_penalty (2026 ceza tutarları)
- isg_simulator (Sanal müfettiş)

### FAZ 5 — Raporlama (0/3)
- isg_reporting + Superset (TRIR, LWDR, trend analizi)
- QWeb PDF şablonları
- HSE Radar test & acceptance

### Özel Modül (0/1)
- isg_osgb (OSGB planlama, uzman/hekim görevlendirmesi)

---

## Bilinen Hatalar 🐛

### Uyarılar (Işlevsel değil, sadece log)
- [ ] `isg_contractor.contractor_level` — recursive=True eksik (warning)
- [ ] `isg_location.hazard_type` — unknown parameter 'invisible' (view upgrade gerekli)
- [ ] `isg_site.hazard_type` — unknown parameter 'invisible'
- [ ] `isg_ppe.type.size_type` — unknown parameter 'invisible'
- [ ] `html4css1.css` — Permission denied (işlevsel değil)
- [ ] `isg_core` — no group ACL warning (geçici çözüm)

### Düzeltilmesi Gerekli
- [ ] Admin şifresi — PostgreSQL üzerinden NULL yapıldı, kalıcı şifre belirlenmeli
- [ ] Record rules — isg_risk_line, isg_audit_line, isg_ppe_issue için workplace/site filtering
- [ ] isg_chemical_inventory — workplace filtering eksik

### KVKK / Sağlık Verisi (F1-002 ile birlikte)
- [ ] isg_health_basic — ACL maskeleme (hekim grubu dışında göremez)
- [ ] Erişim log kaydı — sağlık verisine erişim denetimi
- [ ] Açık rıza tracking — KVKK rıza yönetimi

---

## Geliştirme Stratejisi

1. **OCA varsa kur** — tekerleği yeniden icat etme
2. **Port edilebilirse port et** — özellikle MIT lisanslı kod
3. **Türkiye'ye özgüyse sıfırdan yaz** — mevzuat, KVKK, OSGB
4. **Her faz tamamlanmadan sonrakine geçme**
5. **Küçük adımlar, sık test**

---

## Sürüm Tarihleri

- **1 Ağustos 2026:** İlk VPS kurulumu
- **8 Ağustos 2026:** FAZ 0-1 tamamlandı (12 modül)
- **14 Ağustos 2026:** FAZ 2 başlandı, isg_chemical hazırlığı
- **15 Ağustos 2026:** isg_chemical kuruldu (19 modül)
- **16 Ağustos 2026:** isg_equipment + isg_ptw kuruldu (20 modül) — FAZ 2 TAMAMLANDI ✅
