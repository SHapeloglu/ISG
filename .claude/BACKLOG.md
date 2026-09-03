# BACKLOG.md — Gelecek Geliştirmeler (03 Eylül 2026 — Seans 3 Devam)

## 🎯 Hemen Başlanacak (3-5 gün)

### MEV-002: isg_equipment — Ara.2025 EK-II Güncellemesi — BAŞLANACAK ← START
**Mevzuat:** İş Ekipmanları Yönetmeliği (Aralık 2025)

**Gereksinim:**
- Ara.2025 EK-II ekipman kataloğu (kompresör, vinç, asansör, baskı kapı, forklift, platform, kaldırma cihazları)
- Periyodik kontrol periyodu (6 ay / 1 yıl / vb.) ve yöntem
- e-imza desteği (5070 s.K.)
- EKİPNET sözleşme onayı + bildirim hazırlık
- Kontrol sonucu rapor ve uyarı sistemi (kontrol tarihi yaklaşınca)

**Tahmini Adam-Gün:** 3-5 gün

---

## 📋 Sonraki Sırada (1-2 hafta)

### isg_ptw + isg_loto — İş izni + LOTO (4-6 gün)
- İzin türleri (sıcak iş, kapalı alan, elektrik, yüksekte)
- Ön koşul kontrol listeleri
- Çok aşamalı onay zinciri
- LOTO izolasyon nokta yönetimi

### isg_emergency — Acil durum (2-3 gün)
- Acil durum planı, tatbikat, tahliye
- isg_location entegrasyonu

---

## 📊 Medium Priority (2-3 hafta)

### MEV-008: Risk bilgilendirmesi (0.5 gün)
- isg_visitor, isg_contractor risk briefing alanları

### F5-002/F5-003: PDF şablonları + test (1-2 gün)
- QWeb şablonları inceleme
- Test case'ler hazırlama

---

## ✅ Tamamlanan B-Görevleri (Seans 2-3)

- [x] **B-4 isg_board** — danger_class string bug
- [x] **B-8 isg_penalty** — valid_from versiyonlama
- [x] **B-9 isg_core** — danger_class.history modeli
- [x] **B-10 isg_training** — 6 ay uzak kalma dönüş eğitimi

---

## 📈 Gap Analysis Sonuçları (30 Ağustos)

Kapsamlı rapor hazırlandı (ISG_Gap_Analysis_20260901.md):
- **Mevzuat Boşlukları:** MEV-002 (EK-II) en kritik, 0.5-5 gün
- **İşlevsel Eksikler:** F2 serisi 7 modül (22-33 gün) — TAMAMLANDI ✅
- **Top 10 Düzeltme:** Sıralanmış, adam-gün tahminli
- **Full Eşdeğerlik:** 11-20 gün daha

---

## 🎯 Başlangıç Sırası (Tavsiye)

**Bu Hafta:**
1. MEV-002 isg_equipment (3-5 gün) ← **START**
2. isg_ptw + isg_loto (4-6 gün)

**Sonraki Hafta:**
3. isg_emergency (2-3 gün)
4. MEV-008 + F5 (küçük fixler + doğrulama)

---

## Bloklu (KVKK Danışman)

- isg_health_basic (F1-002) — KVKK danışman onayı bekleniyor
