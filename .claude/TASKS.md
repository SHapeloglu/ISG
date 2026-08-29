# TASKS.md — Görev Listesi (29 Ağustos 2026 — isg_environment Tamamlandı)

## Tamamlanan Görevler ✅

### FAZ 3 — Ölçüm (3/3 %100) ✅ TAM BİTTİ
- [x] F3-001 isg_measurement_core
- [x] F3-002 isg_measurement_hygiene (gürültü)
- [x] **F3-003 isg_environment — Atık yönetimi, depolama, bertaraf (Commit 4eba10c)**

**Proje İlerleme: 31/32 Modül (%97)**

| Faz | Toplam | Tamamlanan | % |
|-----|--------|------------|---|
| FAZ 0 | 7 | 7 | %100 |
| FAZ 1 | 6 | 5 | %83 (isg_health_basic bloklu) |
| FAZ 2 | 9 | 9 | %100 |
| FAZ 3 | 3 | 3 | %100 ✅ |
| FAZ 4 | 4 | 4 | %100 |
| FAZ 5 | 3 | 1 | %33 (reporting yapıldı) |
| OSGB | 1 | 1 | %100 |
| **TOPLAM** | **32** | **31** | **%97** |

## Sıradaki Görevler

### B-Görevleri — Mevzuat Retrofit (5 gün)

- [x] B-1 isg.rate.table ✅
- [ ] **B-10 isg_training — 2 Nisan 2026 Tam Uyum (~2-3 gün)** ← BAŞLA BURADAN
  - İşe başlama eğitimi ayrı tür, yüz yüze zorunlu
  - Tehlike sınıfına göre tekrar periyotları (2 yıl / 1 yıl / 6 ay)
  - Dönüş eğitimi tetikleyicileri (6 ay uzak kaldı, kaza sonrası)
  - isg_incident entegrasyonu (state=resolved → training.record oluştur)
  - Özel gruplar (genç, yaşlı, engelli, gebe)

- [ ] **B-4 isg_board — Toplantı Sıklığı (~1 gün)**
  - Çok tehlikeli: 15 gün arası
  - Diğer: 1 ay arası

- [ ] **B-8 isg_penalty — Versiyonlama (~0.5-1 gün)**
  - valid_from alanı ekle
  - 2026 %49 artış

- [ ] **B-9 isg_core — danger_class.history (~0.5-1 gün)**
  - Tehlike sınıfı değişim geçmişi

### F5 Kontrol (~1 gün)

- [ ] **F5-002 QWeb PDF Şablonları** — durumu kontrol et
- [ ] **F5-003 HSE Radar Kabul Testi** — test protokolü

### Bloklu

- [ ] **F1-002 isg_health_basic** — KVKK danışman onayı bekleniyor

## Sıradaki Adımlar (Next Session)

1. B-10 başla (~2-3 gün)
2. B-4/B-8/B-9 (~2-3 gün)
3. F5 kontrol (~1 gün)
4. HSE Radar kabul testine hazır ol

**Toplam Kalan:** 5-7 gün
