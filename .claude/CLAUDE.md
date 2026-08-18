# CLAUDE.md — Yeni Chat Bağlamı

## Proje Özeti

Contabo VPS üzerinde Odoo 18 tabanlı Türkiye ISG platformu geliştiriyoruz. Hedef: HSE Radar ile %90 işlevsel eşdeğerlik + Odoo ERP entegrasyonu.

## Mevcut Durum (18 Ağustos 2026)

- 22/32 modül kurulu | %69 tamamlama
- FAZ 0-2 tamamlandı
- FAZ 3-001 tamamlandı (isg_measurement_core)
- FAZ 5-001 tamamlandı (isg_reporting TRIR/LWDR KPI)
- Sıradaki: FAZ 3-002 isg_measurement_hygiene

## Geliştirici Profili

- Junior seviye Odoo geliştirici
- Step-by-step öğrenme
- Terminal komutları tek tek

## Modül Kurulum Prozesi

1. sudo systemctl stop odoo18-isg.service
2. sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin -c /etc/odoo/odoo18-isg.conf --logfile="" -d isg -i MODUL_ADI --stop-after-init
3. sudo systemctl start odoo18-isg.service
4. sudo systemctl status odoo18-isg.service

## En Son Modül: F3-001 isg_measurement_core

Snapshot Mimarisi:
- Ölçüm kaydedildiğinde cihaz kalibrasyon bilgileri dondurulur
- Limit değerleri versiyonlu (2024 vs 2026 mevzuatı)
- Ham sonuç asla değişmez
- Uygunluk hesaplaması snapshot limit'e göre
- Limit aşımında otomatik DÖF oluşur

5 Model:
- isg_measurement_campaign
- isg_measurement_device
- isg_measurement_sample
- isg_measurement_result (SNAPSHOT)
- isg_measurement_limit (versiyonlu)

Security: 15 rule

## Kurulu Modüller (22 toplam)

FAZ 0 (7): isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base
FAZ 1 (5): isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
FAZ 2 (9): isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw
FAZ 3 (1): isg_measurement_core
FAZ 5 (1): isg_reporting

## Odoo 18 Notları

- tree yerine list view
- states attribute kaldırıldı
- attrs yerine invisible
- XML'de ampersand &amp; yapılmalı
- Compute field @api.depends() ile

---

Soru olursa terminal çıktısı paylaş, adım adım ilerleriz.
