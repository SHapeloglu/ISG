# SESSION.md — Oturum Özeti ve Devam Noktası

## Son Oturum: 14 Ağustos 2026

### Tamamlanan İşler

#### FAZ 0 — Temel Mimari (TAMAMLANDI ✅)
- 7 modül (isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base)

#### FAZ 1 — Kurumsal Yönetişim (TAMAMLANDI ✅)
- isg_contractor (F1-001) ✅
- isg_training (F1-003) ✅
- isg_visitor (F1-004) ✅
- isg_board (F1-005) ✅
- isg_correspondence (F1-006) ✅
- **F1-002 isg_health_basic: KVKK danışman onayı bekliyor — EN SONA BIRAK**

#### FAZ 2 — Çekirdek İSG Operasyonları (6/9 TAMAMLANDI ✅)
- [x] **F2-001** `isg_capa` — DÖF/CAPA, kök neden analizi ✅
- [x] **F2-002** `isg_risk` — Risk değerlendirmesi ✅
- [x] **F2-003** `isg_incident` — İş kazası / ramak kala ✅
- [x] **F2-004** `isg_audit` — Denetim ve kontrol listeleri ✅
- [x] **F2-005** `isg_ppe` — KKD yönetimi ✅
- [x] **F2-006** `isg_emergency` — Acil durum planı ✅
- [ ] **F2-007** `isg_chemical` — Kimyasal envanter (SİRADA)
- [ ] **F2-008** `isg_equipment` — Ekipman ve periyodik kontrol (EKİPNET)
- [ ] **F2-009** `isg_ptw` + `isg_loto` — İş izni ve LOTO

### Proje İstatistiği

| Faz | Toplam | Tamamlanan | % |
|-----|--------|------------|---|
| FAZ 0 | 7 | 7 | %100 |
| FAZ 1 | 6 | 5 | %83 |
| FAZ 2 | 9 | 6 | %67 |
| **TOPLAM FAZ 0-2** | **22** | **18** | **%82** |

**Kurulu modüller**: 46 (Odoo native 27 + ISG 19)
**Adam-gün harcanmış**: ~%50
**Kalandan**: FAZ 3-5 (Ölçüm, Sanal Müfettiş, Raporlama) + OSGB

### Devam Noktası

**Yeni chat'te ilk yapılacak iş:**
→ **F2-007 `isg_chemical`** — Kimyasal envanter ve SDS/GBF

### Bilinen Açık Konular

1. `isg_contractor` contractor_level — recursive=True eklenmeli
2. `isg_location` hazard_type — unknown parameter 'invisible' WARNING (işlevsel değil)
3. `isg_visitor` ppe_notes — model seviyesinde invisible parametresi (işlevsel değil)
4. `isg_risk` site_id — NOT NULL constraint warning (işlevsel, şimdilik yoksay)
5. `isg_health_basic` — KVKK danışman onayı bekliyor

### Servis Komutları

```bash
# Durum kontrol
sudo systemctl status odoo18-isg.service

# Modül güncelle
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" \
  -d isg -u MODUL_ADI --stop-after-init 2>&1 | tail -15
sudo systemctl start odoo18-isg.service
```

### Kurulu Modüller (46 toplam, 19 ISG)

**FAZ 0-2 (19):**
- isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base
- isg_contractor, isg_training, isg_visitor, isg_board, isg_correspondence
- isg_capa, isg_risk, isg_incident, isg_audit, isg_ppe, isg_emergency

**Hazır ama kurulmamış:**
- isg_chemical, isg_equipment (FAZ 2)
- isg_health_basic (FAZ 1, KVKK bekleniyor)
- FAZ 3-5 ve OSGB modülleri

### Geliştirici Notu

Junior Odoo developer ile adım adım çalışıyoruz. Session başlangıç kuralı: Her chat'te VPS dosya durumunu `ls` ve `cat` ile doğrulayıp devam et.
