# ARCHITECTURE.md — Mimari ve Tasarım Kararları (03 Eylül 2026 — Seans 3 Devam)

**Güncelleme:** 03 Eylül 2026 — 33/33 modül kurulu, %100 tamamlandı, MEV-002 başlanacak

## Son Yapılanlar (Seans 3)

✅ **isg_audit scoring FIX (NA hariç)**
- applicable_lines = rec.line_ids.filtered(lambda l: l.result != 'na')
- total_weight = sum(applicable_lines.mapped('weight'))
- compliance_percentage doğru hesaplanıyor

✅ **isg_audit_finding repeat_count AUTO**
- Bulgu oluşturulurken benzer bulgular query (kategori + açıklama prefix)
- repeat_count otomatik set
- escalation_level: >= 3 ise level 2

✅ **isg_incident SGK notification + dönüş eğitimi**
- sgk_notification_deadline: incident_date + 4 takvim günü (3 iş günü)
- return_to_work_training_id: Dönüş eğitimi tetikleyicisi
- action_create_return_training(): otomatik

✅ **isg_ppe KKD envanter**
- IsgPpeType: 9 kategori
- IsgPpeStock: stok + min_quantity uyarısı
- IsgPpeIssue: zimmet, expiry_date compute (lifespan_months)

✅ **isg_chemical OEL/STEL + uyumsuzluk**
- IsgChemicalOel: Türkiye ÇSGB TWA (8h) + STEL (15min)
- IsgChemicalIncompatibility: depolama matrisi (kritik/yüksek/orta)
- Ters kayıt kontrolü (A-B ve B-A)

---

## Sonraki Seans

**MEV-002: isg_equipment — Ara.2025 EK-II Güncellemesi**
- Ekipman kataloğu (kompresör, vinç, asansör, forklift, platform...)
- e-imza desteği (5070 s.K.)
- EKİPNET bildirim hazırlık alanları
- Periyodik kontrol raporu form

Tahmini süre: 3-5 gün
