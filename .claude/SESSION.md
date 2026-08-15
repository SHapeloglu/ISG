# SESSION.md — Oturum Özeti (15 Ağustos 2026)

## Mevcut Durum

**18/32 modül kurulu** | **FAZ 2: 7/9 (%78) tamamlandı**

### FAZ 0 — Temel Mimari (7/7 ✅)
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

### FAZ 1 — Kurumsal Yönetişim (5/6 ✅)
- isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- **Bekleyen:** F1-002 isg_health_basic (KVKK danışman onayı) — EN SONA

### FAZ 2 — Çekirdek ISG Operasyonları (7/9 — %78)
**Tamamlanan:**
- F2-001 isg_capa (DÖF/CAPA) ✅
- F2-002 isg_risk (Risk değerlendirmesi) ✅
- F2-003 isg_incident (İş kazası) ✅
- F2-004 isg_audit (Denetim) ✅
- F2-005 isg_ppe (KKD yönetimi) ✅
- F2-006 isg_emergency (Acil durum) ✅
- F2-007 isg_chemical (Kimyasal envanter) ✅ YENİ

**Sırada:**
- [ ] F2-008 isg_equipment (EKİPNET / Periyodik kontrol)
- [ ] F2-009 isg_ptw + isg_loto (İş izni + LOTO)

### Kurulu Modüller (18 toplam)
isg_audit, isg_base, isg_board, isg_capa, isg_chemical,
isg_contractor, isg_core, isg_correspondence, isg_document,
isg_emergency, isg_hr, isg_incident, isg_location, isg_party,
isg_ppe, isg_risk, isg_security, isg_training, isg_visitor

## Devam Noktası

**Sıradaki görev:** F2-008 `isg_equipment` modülü

## Servis Komutları

```bash
# Durum
sudo systemctl status odoo18-isg.service

# Modül güncelle
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" \
  -d isg -u MODUL --stop-after-init 2>&1 | grep -E "ERROR|loaded" | tail -10
sudo systemctl start odoo18-isg.service

# Yeni modül kur
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" \
  -d isg -i MODUL --stop-after-init 2>&1 | grep -E "ERROR|loaded" | tail -10
sudo systemctl start odoo18-isg.service
```
