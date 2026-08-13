# SESSION.md — Oturum Özeti

## Son Oturum: 13 Ağustos 2026

### Tamamlanan Modüller Bu Oturumda

**F2-002 `isg_risk`** ✅
- 6 durumlu state machine, Fine-Kinney + L Matrisi, kalıntı risk, DÖF entegrasyonu
- ISG-RD-YYYY-NNNN sequence

**F2-003 `isg_incident`** ✅
- İş kazası / ramak kala / meslek hastalığı
- SGK 3 iş günü bildirim takibi (6331 md.14)
- DÖF bağlantısı
- ISG-KZ-YYYY-NNNN sequence

**F2-004 `isg_audit`** ✅
- Denetim şablonu (isg.audit.template + question)
- Denetim kaydı (isg.audit + line)
- Şablon → denetim satırı yükleme
- Kritik madde uygunsuzsa otomatik DÖF
- ISG-DNT-YYYY-NNNN sequence

### Sıradaki: F2-005 `isg_ppe` — KKD Yönetimi

### Kurulu Modüller (46 toplam, 17 ISG)
isg_core, isg_security, isg_party, isg_location, isg_document,
isg_hr, isg_base, isg_training, isg_contractor, isg_board,
isg_correspondence, isg_visitor, isg_capa, isg_risk,
isg_incident, isg_audit, hr_skills

### Bilinen Açık Konular
1. isg_contractor contractor_level — recursive=True eklenmeli
2. isg_location hazard_type — unknown parameter 'invisible' WARNING
3. isg_health_basic — KVKK danışman onayı bekliyor
4. isg_risk_line record rule eksik — şirket bazlı izolasyon yok
