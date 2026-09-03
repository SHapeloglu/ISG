# ARCHITECTURE.md — Mimarı ve Tasarım (Seans 3 TAMAMLANDI)

**Güncelleme:** 03 Eylül 2026, 07:53 UTC — isg_equipment kurulu, 33/33 %100

## Seans 3'te Tamamlanan

✅ **isg_audit scoring FIX (NA hariç)**
- applicable_lines = rec.line_ids.filtered(lambda l: l.result != 'na')
- total_weight sadece uygulanabilir maddeler
- compliance_percentage doğru

✅ **isg_audit_finding repeat_count AUTO**
- Kategori + açıklama prefix match
- escalation_level >= 3 ise level 2

✅ **isg_incident SGK notification + dönüş eğitimi**
- Deadline: incident_date + 4 takvim günü (3 iş günü)
- return_to_work_training otomatik

✅ **isg_ppe KKD envanter**
- IsgPpeType (9 kategori)
- IsgPpeStock (min_quantity uyarısı)
- IsgPpeIssue (zimmet, expiry_date)

✅ **isg_chemical OEL/STEL + uyumsuzluk**
- IsgChemicalOel (Türkiye ÇSGB TWA/STEL)
- IsgChemicalIncompatibility (depolama)
- Ters kayıt kontrolü

✅ **isg_equipment EK-II ekipman kataloğu**
- IsgEquipment (15+ ekipman türü)
- IsgEquipmentType (EK-II kategori)
- IsgEquipmentInspection (periyodik kontrol + EKİPNET)
- Ara.2025 EK-II seed data

---

## Seans 4 Başlangıç

**Sıradaki:** isg_ptw + isg_loto
- İş izni (sıcak, kapalı, elektrik, yüksekte)
- LOTO izolasyon yönetimi
- Ön koşul checklists
- Multi-step approval chain
