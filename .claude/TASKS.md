# TASKS.md — Seans 12 Sonrası Aktif Backlog

## 🎯 Kısa Vadeli (Bu Hafta)

### Seans 13 Başlangıcı
- [ ] VPS verify: git log, modül count (psql), .claude/ files
- [ ] isg_training B-10 başla (April 2, 2026 regulation)

## 📋 Orta Vadeli Backlog (Sıraya Göre)

### B-10: isg_training (Seans 13+)
- Scope: Full training module + incident→return trigger
- Estimate: 2-3 days
- Dependency: None (isg_health_basic done)
- Status: Planning

### isg_health_basic Enhancements (Optional Seans 14)
- Field-level encryption key rotation
- Audit log retention policy (30/90/365 day archive)
- Batch audit log cleanup script
- Estimate: 1-1.5 days

### B-4/B-8/B-9: Mevzuat Retrofit
- Scope: 3 modül, regulation update synch
- Estimate: 2-3 days
- Status: Backlog

### F5-002/F5-003: PDF Report Templates
- Scope: isg_legislation / isg_occupational_disease reports
- HSE Radar parity check
- Estimate: 1 day
- Status: Backlog

## 🔒 Blokalı Konular

### ₺300K Faz 1 Bütçe Onayı
- Etkisi: Developer days, consultant RFP
- Tahmini yanıt: End of September 2026

### Danışmanlık RFP (₺139-164K)
- 5 firma listesi hazır
- RFP dokümanter: A_DANISMANLIK_VE_ONAYLA_R_PAKETI.md
- Action: Bütçe onayı sonrası gönder

### res.users.workplace_ids Attribute
- Gerekçe: Record rule domains için
- Scope: isg_hr modülü extension
- Status: TODO (Seans 13 plans)

## 🚀 Tamamlanan (Seans 12)
- [x] Encryption helper class
- [x] Field-level encryption (physician_notes)
- [x] Audit log model + views + ACL
- [x] Create/write/unlink hooks
- [x] DB table creation + verification

## 📊 Genel Proje Durumu
- **31/32 modül** kurulu (%97)
  - Kalan: isg_health_basic legal review (blokalı)
- **Git:** main branch, 39a27e4 HEAD
- **VPS:** vmi3389964, isg.powerbi.com.tr
