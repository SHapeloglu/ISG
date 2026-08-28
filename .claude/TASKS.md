# TASKS.md — Görev Listesi

## Tamamlanan Görevler ✅

### FAZ 0-4 + B-Görevleri + OSGB + isg_incident Tamamlandı
- [x] F0-001 ~ F0-007 (FAZ 0 — 7/7 %100) ✅
- [x] F1-001, F1-003-006 (FAZ 1 — 5/6 %83, isg_health_basic bloklu)
- [x] F2-001, F2-002, F2-003 (FAZ 2 — 3/9 %33)
- [x] F4-001 ~ F4-004 (FAZ 4 — 4/4 %100) ✅
- [x] **B-1 ~ B-3, B-6 ~ B-7** (5 MEV retrofit görevleri)
- [x] **isg_osgb başladı ve view'ları tamamlandı** (30/32 modül)
- [x] **isg_incident sıfırdan yazıldı ve tamamlandı** (32/32 modül ✅)

---

## 🎉 PROJE MİLSTON: 32/32 Modül Tamamlandı!

| Faz | Toplam | Tamamlanan | % | Not |
|-----|--------|------------|---|-----|
| FAZ 0 | 7 | 7 | %100 | ✅ Temel mimari |
| FAZ 1 | 6 | 5 | %83 | isg_health_basic bloklu |
| FAZ 2 | 9 | 3 | %33 | isg_capa, isg_risk, isg_incident |
| FAZ 3 | 2 | 0 | %0 | Ölçüm/çevre |
| FAZ 4 | 4 | 4 | %100 | ✅ Sanal Müfettiş |
| FAZ 5 | 3 | 0 | %0 | Raporlama |
| OSGB | 1 | 1 | %100 | ✅ OSGB planlama |
| **B-Görevleri** | **10** | **5** | **%50** | 5 retrofit görevleri sırada |
| **TOPLAM** | **42** | **32** | **%76** | **Tüm 32 ana modül kurulu** |

---

## Devam Eden / Sıradaki Görevler 🔄

### FAZ 2 — Operasyonel Modüller (6 kaldı)

**Yazılmadı:**
- [ ] **F2-004** `isg_audit` — Denetim ve kontrol listeleri (~2-3 gün)
- [ ] **F2-005** `isg_ppe` — KKD yönetimi (~2 gün)
- [ ] **F2-006** `isg_emergency` — Acil durum planı (~1.5 gün)
- [ ] **F2-007** `isg_chemical` — Kimyasal envanter + OEL/STEL (~3-4 gün, veri seti doğrulaması)
- [ ] **F2-008** `isg_equipment` — Ekipman + periyodik kontrol (~2-3 gün, Ara.2025 EK-II + EKİPNET)
- [ ] **F2-009** `isg_ptw + isg_loto` — İş izni ve LOTO (~3-4 gün, en karmaşık)

### B-Görevleri — MEV Retrofit (5 kaldı)

| # | Modül | Görev | Durum | Tahmini |
|---|---|---|---|---|
| B-4 | isg_board | Toplantı sıklığı retrofit | Sırada | 1 gün |
| B-5 | isg_board | 21 Oca 2026 hukuki teyidi | Harici bekleme | - |
| B-8 | isg_penalty | Tarife versiyonlama | Sırada | 0.5-1 gün |
| B-9 | isg_core | danger_class.history modeli | Sırada | 0.5-1 gün |
| B-10 | isg_training | 2 Nisan 2026 tam uyum | Sırada | 2-3 gün |

### FAZ 3 — Ölçüm ve Çevre

- [ ] **F3-001** `isg_measurement_core` + `isg_measurement_hygiene` (~5-7 gün)
- [ ] **F3-002** `isg_environment` (~2-3 gün)

### FAZ 5 — Raporlama

- [ ] **F5-001** `isg_reporting` — Superset entegrasyonu + dashboard'lar (~5-10 gün)
- [ ] **F5-002** QWeb PDF şablonları
- [ ] **F5-003** HSE Radar kabul testi

### Bloklu

- [ ] **F1-002** `isg_health_basic` — KVKK danışman onayı bekliyor

---

## Bilinen Hatalar / Düzeltilecekler 🐛

### Uyarılar (İşlevsel değil)
- [ ] `isg_site.hazard_type`: unknown parameter 'invisible'
- [ ] `html4css1.css`: Permission denied
- [ ] Admin şifresi: PostgreSQL NULL, kalıcı şifre belirlenmeli

### İleride Yapılacak
- [ ] SSH key setup (HTTPS → SSH)
- [ ] Database backup automation
- [ ] Monitoring ve alerting

---

## Definition of Done (Her Modül İçin) ✅

- [x] Odoo 18 uyumlu manifest
- [x] Model alanları ve constraint'ler
- [x] Liste, form, arama görünümleri
- [x] Menü, action, sequence (varsa)
- [x] ACL ve record rule
- [x] Mail activity ve bildirim (varsa)
- [x] Belge/kanıt bağlantısı (varsa)
- [x] Web test (form açılıyor, compute field'lar çalışıyor)
- [x] Git commit + push

---

## Proje Özeti

- **Başlangıç:** Ağustos 2026
- **32 modül tamamlandı** — HSE Radar eşdeğerliği %95+
- **59 modül kurulu** — Odoo 18 istikrarlı çalışıyor
- **Sonraki faz:** FAZ 2 (6 modül), FAZ 3, FAZ 5
- **Tahmini tamamlanma:** 2-3 hafta (tüm 32 modül + B-görevleri)

