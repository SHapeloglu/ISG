# CLAUDE.md — Yeni Chat Bağlamı (16 Ağustos 2026)

## Proje Özeti

Contabo VPS: Odoo 18 tabanlı Türkiye İSG platformu
- **Hedef:** HSE Radar %90+ eşdeğerlik
- **Durum:** 20/32 modül (%63) | FAZ 2 TAMAMLANDI
- **Domain:** isg.powerbi.com.tr

## Kurulu Modüller (20/32)

FAZ 0: 7/7 - isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

FAZ 1: 5/6 - isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence

FAZ 2: 9/9 TAMAMLANDI - isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw

## Dosya Yolları

- /opt/odoo/isg_addons/ - ISG modülleri
- /opt/odoo/venv18-isg/ - Python venv
- /etc/odoo/odoo18-isg.conf - Config
- .claude/ - Handoff dosyaları

## Terminal Kuralları

1. Komutları tek tek ver (art arda yazma)
2. Her komuta "--logfile=""" ekle (config'de logfile var)
3. Çıktısı: | tail -25
4. Permission denied: sudo chown -R odoo:odoo /path/

## Modül Yükleme

```bash
sudo systemctl stop odoo18-isg.service

sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" -d isg -i MODUL --stop-after-init 2>&1 | tail -25

sudo systemctl start odoo18-isg.service
```

## Modül Standartı

Her modül: __init__.py, __manifest__.py, models/, views/, security/, data/

Sequence: ISG-XXX-YYYY-NNNN
ACL: readonly (read), expert (r/w), manager (r/w/delete)
Record rules: company_id + workplace_id + site_id

## Bilinen Sorunlar

- recursive=True uyarısı (işlevsel değil)
- invisible parameter uyarıları
- Admin şifresi NULL (kalıcı şifre gerekli)
- isg_health_basic KVKK maskeleme (danışman onayı bekliyor)

## Son Tamamlananlar (16 Ağustos)

- isg_equipment (EK-II, periyodik kontrol)
- isg_ptw (İş izni, LOTO)
- FAZ 2 %100 bitti

## Sıradaki: FAZ 3

- isg_measurement_core + isg_measurement_hygiene
- isg_environment

## Git

cd /opt/odoo/isg_addons
git add -A
git commit -m "..."
git push origin main

Repo: https://github.com/SHapeloglu/ISG
