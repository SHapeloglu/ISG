# isg_incident — Modül Durumu

## Durum: TAMAMLANDI ✅ (12 Ağustos 2026)

## Dosyalar
- models/isg_incident.py — tek model, tüm alanlar
- views/isg_incident_views.xml — list, form, search, action
- views/isg_incident_menus.xml — "Kaza ve Ramak Kala" (sequence=40)
- security/isg_incident_security.xml — şirket bazlı record rule
- security/ir.model.access.csv — readonly/expert/manager ACL
- data/isg_incident_sequence.xml — ISG-KZ-YYYY-NNNN (noupdate=1)

## Düzeltilen Bug
- action_create_capa'da isg.capa'da olmayan responsible_id alanı silindi

## Test Edildi
- ISG-KZ-2026-0001 sequence doğru
- SGK bildirim tarihi olay_tarihi+3 gün otomatik hesaplanıyor
- DÖF Kaydı Oluştur butonu görünüyor
- Durum makinesi: draft→investigation→sgk_pending→closed
