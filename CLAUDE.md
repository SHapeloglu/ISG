# CLAUDE.md — Yeni Chat Bağlamı (22 Ağustos 2026)

## Proje Özeti
Contabo VPS: Odoo 18 tabanlı Türkiye İSG platformu
- **Hedef:** HSE Radar %90+ eşdeğerlik
- **Durum:** 24/32 modül (%75) | FAZ 3 TAMAMLANDI | FAZ 4 BAŞLANDI
- **Domain:** isg.powerbi.com.tr

## Kurulu Modüller (24/32)

**FAZ 0:** 7/7 ✅ — isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

**FAZ 1:** 5/6 (%83) — isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- Bekleyen: F1-002 isg_health_basic (KVKK danışman onayı)

**FAZ 2:** 9/9 ✅ — isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw

**FAZ 3:** 2/2 ✅ TAMAMLANDI
- F3-001 isg_measurement_core (kampanya, cihaz, numune, sonuç, limit — snapshot mimarisi)
- F3-002 isg_measurement_hygiene (gürültü: LAeq, LCeq, Lpeak, inherit + invisible pattern)

**FAZ 4:** 1/4 (%25)
- F4-001 isg_legislation ✅ (kanun, yükümlülük, uygulanabilirlik kuralları)
- Planlanan: F4-002 compliance, F4-003 penalty, F4-004 simulator

**FAZ 5:** 1/3 — isg_reporting (TRIR/LWDR KPI)

## Dosya Yolları

- `/opt/odoo/isg_addons/` — ISG modülleri
- `/opt/odoo/venv18-isg/` — Python venv
- `/etc/odoo/odoo18-isg.conf` — Config
- `/opt/odoo/isg_addons/.claude/` — Handoff dosyaları

## Terminal Kuralları

1. Komutları tek tek ver (art arda yazma)
2. Her komuta `--logfile=""` ekle (config'de logfile var)
3. Çıktısı: `| grep -E "ERROR|loaded" | tail -10` veya `| tail -100`
4. Permission denied: `sudo chown -R odoo:odoo /path/`

## Modül Yükleme

```bash
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" -d isg -i MODUL --stop-after-init 2>&1 | grep -E "ERROR|loaded" | tail -10
sudo systemctl start odoo18-isg.service
```

## Modül Standartı

- Klasör: `__init__.py`, `__manifest__.py`, `models/`, `views/`, `security/`, `data/`
- Sequence: `ISG-XXX-YYYY-NNNN`
- ACL: readonly (read), expert (r/w), manager (r/w/delete)
- Record rules: company_id + workplace_id + site_id

## Kritik Mimariler

### 1. Snapshot Mimarisi (F3-001)
Ölçüm kaydedildiginde cihaz kalibrasyon + limit değerleri DONDURULUR. Sonradan limit degisse bile eski ölçüm kaydı korunur.

### 2. Parametre Dispatch Mimarisi (F3-002)
Ölçüm sonucu modeline inherit ile parametre-özel alanları eklenir. measurement_type seçim → invisible="measurement_type != 'TYPE'" ile view kontrol.

### 3. Mevzuat Motoru Mimarisi (F4-001+)
İşyeri profili → Uygulanabilir Yükümlülükler → Uygunluk Değerlendirmesi
- isg.legislation: Kanun/yönetmelik
- isg.obligation: Yükümlülük tanımı + kanıt türü
- isg.obligation.applicability: "Bu yükümlülük kime uygulanır?" kuralları
- (F4-002) isg.compliance: Uygunluk kontrol motoru

## Bilinen Sorunlar

- `recursive=True` uyarısı (isg_contractor.contractor_level)
- `invisible` parameter uyarıları (isg_location.hazard_type, isg_visitor.ppe_notes)
- Admin şifresi NULL (kalıcı şifre gerekli)
- isg_health_basic KVKK maskeleme (danışman onayı bekliyor) — EN SONA BIRAK

## Son Tamamlananlar (22 Ağustos)

✅ **F3-002 isg_measurement_hygiene**
- Gürültü parametreleri: LAeq, LCeq, Lpeak, Lpeak Referans (140 dB ÇSGB)
- Inherit + invisible pattern, özel DÖF açıklaması
- FAZ 3 %100 tamamlandı

✅ **F4-001 isg_legislation**
- 3 model (legislation, obligation, applicability)
- Mevzuat-odaklı domain kuralları (danger_class, min_employee, sektor, NACE)
- 3-level ACL, menu structure
- FAZ 4 başladı

## Sıradaki: F4-002 (Uygunluk Değerlendirmesi)

⭐ HSE Radar'ın **gerçek DNA'sı** — sistem "danışman" olmaya başlayacak
- İşyeri profili → otomatik uygulanabilir yükümlülükler hesaplama
- Her yükümlülük için kanıt kontrolü
- Uygunluk snapshot (COMPLIANT / NON_COMPLIANT / PENDING)
- İşyerinin uyum yüzdesi raporu

## Git

```bash
cd /opt/odoo/isg_addons
git add -A
git commit -m "Message"
git push origin main
```

Repo: https://github.com/SHapeloglu/ISG
