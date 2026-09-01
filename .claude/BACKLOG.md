# BACKLOG.md — Gelecek Geliştirmeler (01 Eylül 2026 — B-9 Tamamlandı)

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

### isg_incident — SGK Bildirimi + Dönüş Eğitimi
- Kaza kaydı (state machine)
- SGK 3 iş günü bildirimi uyarısı
- Otomatik dönüş eğitimi tetikleyicisi (isg_training ile link)
- **Tahmini:** 3-5 gün

### isg_audit — Denetim Motoru
- Bulgu kaydı (finding model)
- Weight-based compliance scoring
- Tekrarlanan bulgu escalation (3+)
- **Tahmini:** 4-6 gün

---

## 📊 Medium Priority (2-3 hafta)

- isg_ppe (KKD envanter, zimmet) — 3-4 gün
- isg_chemical (kimyasal, OEL/STEL limit) — 3-4 gün
- isg_ptw + isg_loto (iş izni, LOTO) — 4-6 gün
- (Paralel yapılabilir)

---

## 🐛 Teknik Borç

- [ ] isg_site.hazard_type — 'invisible' warning (operasyonel değil)
- [ ] html4css1.css — Permission denied warning (operasyonel değil)
- [ ] Admin şifresi — PostgreSQL NULL (kalıcı şifre belirlenmeli)

---

## ✅ Tamamlanan B-Görevleri (01 Eylül 2026)

- [x] **B-4 isg_board** (f511508) — danger_class string bug
- [x] **B-8 isg_penalty** (2aa4983) — valid_from versiyonlama
- [x] **B-9 isg_core** (d037d71) — danger_class.history modeli

---

## 📈 Gap Analysis Sonuçları

Kapsamlı rapor hazırlandı (ISG_Gap_Analysis_20260901.md):
- **Mevzuat Boşlukları:** MEV-002 (EK-II) en kritik, 0.5-5 gün
- **İşlevsel Eksikler:** F2 serisi 7 modül (22-33 gün)
- **Top 10 Düzeltme:** Sıralanmış, adam-gün tahminli
- **Full Eşdeğerlik:** 25-35 gün daha

---

## 🎯 Başlangıç Sırası (Tavsiye)

**Bu Hafta:**
1. MEV-002 isg_equipment (3-5 gün) ← START
2. isg_incident (3-5 gün)

**Sonraki Hafta:**
3. isg_audit (4-6 gün)
4. isg_ppe, isg_chemical, isg_ptw (paralel, 2-3 hafta)
5. Küçük fixler + doğrulama (F5-002/F5-003)
