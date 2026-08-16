# CLAUDE.md — Yeni Chat Bağlamı (16 Ağustos 2026)

## Proje Özeti

Contabo VPS üzerinde Odoo 18 tabanlı Türkiye İSG platformu.

**Hedef:** HSE Radar ile %90+ eşdeğerlik  
**Durum:** 20/32 modül (%63) | FAZ 2 TAMAMLANDI ✅

## Kurulu Modüller (20/32)

**FAZ 0:** 7/7 ✅  
isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

**FAZ 1:** 5/6 ✅  
isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence

**FAZ 2:** 9/9 ✅ TAMAMLANDI  
isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw

## Terminal Komutları

```bash
# Modülü yükle
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" -d isg -i MODUL --stop-after-init 2>&1 | tail -25
sudo systemctl start odoo18-isg.service
```

## Dosya Yolları

- /opt/odoo/isg_addons/ — Modüller
- /etc/odoo/odoo18-isg.conf — Config
- .claude/ — Handoff dosyaları

## Son Tamamlananlar (16 Ağustos)

- isg_equipment (EK-II, periyodik kontrol)
- isg_ptw (İş izni, LOTO)
- FAZ 2 %100 ✅

## Sıradaki: FAZ 3

- F3-001: isg_measurement_core + isg_measurement_hygiene
- F3-002: isg_environment
