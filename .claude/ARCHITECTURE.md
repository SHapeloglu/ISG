# ARCHITECTURE.md — ISG Platform Modül Mimarisi (Doğrulanmış: 17 Eylül 2026)

**Kaynak:** VPS `git log` + `ls isg_addons/` + `psql ir_module_module` çıktısı (17 Eylül 2026)
**Durum:** 31/31 üretim modülü kurulu (%100). `isg_tests` ayrı, uninstalled, sayıma dahil değil.

## FAZ 0 — Temel Mimari
- **isg_core**: isg.workplace, isg.site — İSG işyeri, NACE, tehlike sınıfı, SGK sicil no
- **isg_security**: 5 rol grubu (readonly/expert/physician/manager/superadmin), category
- **isg_party**: res.partner _inherit — OSGB/Lab/Muayene/AltİşverenTedarikçi rolleri
- **isg_location**: isg.site genişletme — GPS, kapasite, tehlikeli alan, toplanma noktası
- **isg_document**: ir.attachment _inherit — SHA-256 hash, sürüm/kilit/e-imza
- **isg_hr**: hr.employee _inherit — isg_workplace_id, danger_class, KKD ölçüleri, isg.seg
- **isg_base**: isg.uuid.mixin, isg.outbox (E3 entegrasyon kuyruğu)

## FAZ 1 — Kurumsal Yönetişim
- **isg_contractor**: Alt işveren zinciri, 14 belge matrisi
- **isg_training**: Eğitim türleri, 2 Nisan 2026 yönetmelik periyotları, dönüş eğitimi cron
- **isg_board**: İSG kurulu, toplantı, karar takibi
- **isg_correspondence**: Gelen/giden yazışma, 30 gün süre takibi
- **isg_visitor**: Ziyaretçi giriş/çıkış, KKD bildirimi
- **isg_health_basic**: KVKK uyumlu sağlık gözetimi — Fernet encryption, audit log (Seans 12)

## FAZ 2 — Çekirdek İSG Operasyonları
- **isg_capa**: DÖF/CAPA, 5 Neden + 6M kök neden analizi
- **isg_risk**: Risk değerlendirmesi, olasılık×şiddet matrisi
- **isg_incident**: İş kazası/ramak kala, SGK 3 gün bildirim hazırlığı
- **isg_audit**: Denetim planı, kontrol listesi, bulgu puanlama
- **isg_ppe**: KKD envanter, zimmet, yenileme takvimi
- **isg_emergency**: Acil durum planı, tatbikat, tahliye
- **isg_chemical**: Kimyasal envanter, OEL/STEL, GHS sınıflama
- **isg_equipment**: EK-II ekipman kataloğu, periyodik kontrol, EKİPNET hazırlık
- **isg_ptw**: İş izni + LOTO, çok aşamalı onay

## FAZ 3 — Ölçüm ve Çevre
- **isg_measurement_core** + **isg_measurement_hygiene**: Ölçüm kampanyası, kalibrasyon snapshot
- **isg_environment**: Atık kodu, depolama, bertaraf

## FAZ 4 — Sanal Müfettiş
- **isg_legislation**: Mevzuat kaydı, yükümlülük tanımlama
- **isg_compliance**: Uygulanabilirlik motoru, uygunluk değerlendirme
- **isg_penalty**: 2026 ceza tarifeleri (%49 artış), valid_from versiyonlama
- **isg_simulator**: Senaryo testi, geçmiş tarihli değerlendirme

## FAZ 5 — Raporlama
- **isg_reporting**: TRIR/LWDR KPI, Superset hazırlık

## Özel
- **isg_osgb**: OSGB planlama/görevlendirme motoru, uzman/hekim süre hesaplama

## 🔐 Security Model (isg_security)
group_isg_readonly (15) — Salt okuma
group_isg_expert (16) — İSG Uzmanı
group_isg_physician (17) — İşyeri Hekimi
group_isg_manager (18) — İSG Yöneticisi
group_isg_superadmin (19) — İSG Süper Yönetici
category (91)

## ⚠️ TODO: res.users.workplace_ids
Henüz tanımlanmadı. Holding→şirket→işyeri→site record rule zinciri bu attribute'a bağımlı; tanımlanana kadar workplace bazlı erişim kontrolü placeholder durumda.

## Encryption Pattern (isg_health_basic, Seans 12)
```python
# Storage (hidden)
physician_notes_encrypted = fields.Char(readonly=True)
# Display (compute + inverse, role-based masking)
physician_notes = fields.Text(compute='_compute_physician_notes', inverse='_inverse_physician_notes')
```
Audit: `isg.employee.health.audit` modeli — create/write/unlink hook'larla otomatik loglama.
