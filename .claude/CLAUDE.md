# CLAUDE.md — Yeni Chat Bağlamı (22 Ağustos 2026 — Session 4)

## Proje Özeti

Contabo VPS: Odoo 18 tabanlı Türkiye İSG platformu
- **Hedef:** HSE Radar %90+ eşdeğerlik
- **Durum:** 25/32 modül (%78) | FAZ 4-001 ✅ TAMAMLANDI
- **Domain:** isg.powerbi.com.tr

## Kurulu Modüller (25/32)

FAZ 0: 7/7 ✅ - isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base
FAZ 1: 5/6 - isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence (F1-002 KVKK bekliyor)
FAZ 2: 9/9 ✅ - isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw
FAZ 3: 2/2 ✅ - isg_measurement_core, isg_measurement_hygiene
FAZ 4: 1/4 - isg_legislation ✅ (NEW!)
FAZ 5: 1/3 - isg_reporting

## Dosya Yolları

- /opt/odoo/isg_addons/ - ISG modülleri
- /opt/odoo/venv18-isg/ - Python venv
- /etc/odoo/odoo18-isg.conf - Config
- .claude/ - Handoff dosyaları (SESSION.md, TASKS.md, CLAUDE.md, ARCHITECTURE.md, BACKLOG.md)

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
Encoding: # -*- coding: utf-8 -*-

## Odoo 18 Kritik Uyarılar

- `<tree>` → `<list>` (views'de)
- Embedded tree'ler → `<list editable="bottom">`
- `attrs=` / `states=` → `invisible=`
- `ir.model.access.csv` dosya adında nokta olmalı (ir_model_access değil!)
- Manifest'te `base` bağımlılığı gerekebilir (CSV import zamanı)
- `unique=True` → WARNING
- `fields.DateTime` yoktur → `fields.Datetime`

## Bilinen Sorunlar

- recursive=True uyarısı (işlevsel değil, BACKLOG.md'de)
- invisible parameter uyarıları (işlevsel değil)
- Admin şifresi NULL (kalıcı şifre gerekli)
- isg_health_basic KVKK maskeleme (danışman onayı bekliyor)

## Son Tamamlananlar (22 Ağustos 2026 — Session 4)

✅ **F4-001 isg_legislation** — Mevzuat ve Yükümlülük Motoru
  - 3 model: isg.legislation, isg.obligation, isg.obligation.applicability
  - 7 mevzuat kaydı (6331, YÖN'ler, vs)
  - 7 yükümlülük tanımı (Risk, Eğitim, Uzman/Hekim, İSG Kurulu, Acil Durum, vs)
  - Uygulanabilirlik kuralları: danger_class, min/max_employee, sector_type, NACE_kodu
  - List, Form, Search views
  - ACL: readonly/expert/manager
  - Record rules: global read-only (mevzuat merkezi veri seti)

## Sıradaki: FAZ 4-002 (KRITIK)

⭐ **F4-002 `isg_compliance`** — Uygunluk Değerlendirmesi Motoru

İşyeri profili verilince:
1. Hangi yükümlülükler geçerli? (uygulanabilirlik kurallarına göre)
2. Her yükümlülük için kanıt bulunuyor mu? (ir.attachment, isg.document)
3. Kanıt geçerli mi? (saklama süresi, imza, vs)
4. Sonuç: COMPLIANT / NON_COMPLIANT / PENDING / EXPIRED
5. Eksik/vadesi geçmiş kanıt → DÖF otomatik oluştur

**Bu modül HSE Radar'ın çekirdek özelliği — "sanal müfettiş" fonksiyonunun alt yapısı**

## Git

cd /opt/odoo/isg_addons
git add -A
git commit -m "Message"
git push origin main

Repo: https://github.com/SHapeloglu/ISG
