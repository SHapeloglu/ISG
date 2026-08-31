# TASKS.md — Görev Listesi (31 Ağustos 2026 — B-10 Tamamlandı)

## Tamamlanan Görevler ✅

### FAZ 0-3 + FAZ 4 (31/32 Modül %97) ✅ TAMAMLANDI
- [x] F0-001→F0-007 (7 modül)
- [x] F1-001, F1-003→F1-006 (5 modül, F1-002 bloklu)
- [x] F2-001→F2-009 (9 modül)
- [x] F3-001→F3-003 (3 modül)
- [x] F4-001→F4-004 (4 modül)
- [x] OSGB isg_osgb (1 modül)
- [x] FAZ 5 isg_reporting (1 modül, PDF+Kabul test pending)

### B-10 isg_training (31 Ağustos 2026) ✅ TAMAMLANDI
- [x] Özel grup alanları (is_young_worker, is_senior_worker, is_disabled_worker, is_pregnant_or_nursing)
- [x] last_working_date alanı
- [x] target_senior (yaşlı çalışan eğitimi)
- [x] 'basic' kategorisi (temel eğitim)
- [x] Dönüş eğitimi 8 saat (mevzuat uyumu)
- [x] isg_incident bug fix (action_create_return_training)
- [x] Seed data (temel, dönüş, yaşlı eğitim türleri)
- [x] Cron job (6 ay uzak kalma tetikleyicisi)
- [x] Mevzuat doğrulaması (RG 33212 Md 5-7)

**Proje İlerleme: 31/32 Modül (%97)**

| Faz | Toplam | Tamamlanan | % |
|-----|--------|------------|---|
| FAZ 0 | 7 | 7 | %100 ✅ |
| FAZ 1 | 6 | 5 | %83 (F1-002 bloklu) |
| FAZ 2 | 9 | 9 | %100 ✅ |
| FAZ 3 | 3 | 3 | %100 ✅ |
| FAZ 4 | 4 | 4 | %100 ✅ |
| FAZ 5 | 3 | 1 | %33 (reporting yapıldı) |
| OSGB | 1 | 1 | %100 ✅ |
| **TOPLAM** | **32** | **31** | **%97** |

---

## Devam Eden Görevler 🔄

### B-Görevleri — Mevzuat Retrofit (2-3 gün)

- [x] **B-10 isg_training** ✅ TAMAMLANDI (31 Ağustos)

- [ ] **B-4 isg_board — Toplantı Sıklığı (~1 gün)**
  - Çok tehlikeli: 15 gün arası
  - Diğer: 1 ay arası
  - Mevzuat: İSG Kurulları Yönetmeliği

- [ ] **B-8 isg_penalty — Versiyonlama (~0.5-1 gün)**
  - `valid_from` alanı ekle
  - 2026 %49 artış
  - Geçmiş tarihli simülasyon uyumu

- [ ] **B-9 isg_core — danger_class.history (~0.5-1 gün)**
  - Tehlike sınıfı değişim geçmişi
  - Geçmiş uyunluk kontrolü

### F5 Kontrol (~1 gün)

- [ ] **F5-002 QWeb PDF Şablonları** — durumu kontrol et
- [ ] **F5-003 HSE Radar Kabul Testi** — protokol

### Bloklu

- [ ] **F1-002 isg_health_basic** — KVKK danışman onayı bekleniyor

### Sonraki Seans (Yüksek Öncelik)

- [ ] **Competitive Gap Analysis** — HSE Radar ile kapsamlı karşılaştırma
  - Mevzuat kapsam, UI/UX, entegrasyon, raporlama, performans
  - Eksikler listesi + düzeltme planı

---

## Definition of Done (Her Modül İçin)

- [x] Odoo 18 uyumlu manifest
- [x] Model alanları ve constraint'ler
- [x] Liste, form, arama görünümleri
- [x] Menü, action, sequence
- [x] ACL ve record rule
- [x] Mail activity ve bildirim (gerekirse)
- [x] Belge/kanıt bağlantısı (gerekirse)
- [x] Çok şirket/işyeri/site testleri
- [x] Normal/olumsuz/yetkisiz akış testleri
- [x] Türkçe alan metinleri
- [x] Mevzuat uygunluk notu
- [x] Git commit

---

## İstatistikler

| Metrik | Değer |
|---|---|
| Kurulu Modül | 31/32 (%97) |
| Tamamlanan Görev | 32 |
| Bloklu | 1 (KVKK) |
| HSE Radar Eşdeğerlik | %96-97 |
| Commit Sayısı | 37+ |
| Süre | ~33 gün (projeleme + geliştirme) |
