# CLAUDE.md — Yeni Chat Bağlamı (23 Ağustos 2026 — Session 5)

## Proje Özeti

Contabo VPS: Odoo 18 tabanlı Türkiye İSG platformu
- **Hedef:** HSE Radar %90+ eşdeğerlik
- **Durum:** 26/32 modül (%81) | FAZ 4-002 ✅ TAMAMLANDI
- **Domain:** isg.powerbi.com.tr

## Kurulu Modüller (26/32)

FAZ 0: 7/7 ✅ - isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base
FAZ 1: 5/6 - isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence (F1-002 KVKK bekliyor)
FAZ 2: 9/9 ✅ - isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw
FAZ 3: 2/2 ✅ - isg_measurement_core, isg_measurement_hygiene
FAZ 4: 2/4 - isg_legislation ✅, isg_compliance ✅ (NEW!)
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
- CSV dosyaları heredoc içinde çok satırlı olmaz — tee komutu karışabilir

## Kritik Mimariler

### Snapshot Mimarisi (F3-001)
- Ölçüm kaydedildiginde cihaz kalibrasyon, limit değerleri DONDURULUR
- Ham sonuc asla degismez
- Uygunluk hesaplamasi snapshot limite göre yapilir

### Mevzuat Altyapısı (F4-001)
- isg.legislation: Kanun/yönetmelik metadata
- isg.obligation: Yükümlülük tanımı + kanıt türü + saklama süresi
- isg.obligation.applicability: Uygulanabilirlik kuralları (danger_class, min_employee, sector_type, NACE)

### Uygunluk Değerlendirmesi Motoru (F4-002) — YENI!
İşyeri profili → Otomatik yükümlülük hesaplama → Kanıt kontrolü → Uygunluk snapshot

1. İşyeri profili girilir (NACE, danger_class, employee_count)
2. isg.obligation.applicability kurallarına göre geçerli yükümlülükler otomatik hesaplanır
3. Her yükümlülük için kanıt taraması yapılır
4. Uygunluk snapshot: COMPLIANT / NON_COMPLIANT / PENDING / EXPIRED
5. Kanıt eksik → DÖF otomatik oluştur

**Bu HSE Radar'ın ruh: "Müfettiş gelirse ne bulacak?"**

## Bilinen Sorunlar

- recursive=True uyarısı (işlevsel değil, BACKLOG.md'de)
- invisible parameter uyarıları (işlevsel değil)
- Admin şifresi NULL (kalıcı şifre gerekli)
- isg_health_basic KVKK maskeleme (danışman onayı bekliyor)

## Son Tamamlananlar (23 Ağustos 2026 — Session 5)

✅ **F4-002 isg_compliance** — Uygunluk Değerlendirmesi Motoru
  - 2 model: isg.compliance, isg.compliance.evidence
  - _compute_applicable_obligations: İşyeri profiline göre otomatik yükümlülük hesaplama
  - action_evaluate_compliance: Değerlendirme yapıp otomatik DÖF üretimi
  - 4 durum: uygun/eksik/beklemede/vadesi_geçmiş
  - ACL: readonly/expert/manager
  - Record rules: company_id bazında
  - Views: list (badge widget), form, search (durum filtreleri)

## Sıradaki: FAZ 4-003 (KURMAŞ)

⭐ **F4-003 `isg_penalty`** — İdari Para Cezaları

ÇSGB 2026 ceza tarifesi:
- Model: isg.penalty (yükümlülük → ceza miktarı)
- Otomatik ceza hesaplama (uyumsuzluk × tutar)
- Views: penalty tarifleri, uyumsuzluk → ceza matrisi

## Git

cd /opt/odoo/isg_addons
git add -A
git commit -m "Message"
git push origin main

Repo: https://github.com/SHapeloglu/ISG
