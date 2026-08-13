# SESSION.md — Oturum Özeti ve Devam Noktası

## Son Oturum: 12 Ağustos 2026

### Tamamlanan İşler

#### FAZ 0 — Temel Mimari (TAMAMLANDI ✅)
#### FAZ 1 — Kurumsal Yönetişim (TAMAMLANDI ✅, F1-002 hariç)
#### FAZ 2 — Çekirdek İSG Operasyonları (Devam Ediyor)

**`isg_capa` (F2-001):** ✅ (önceki oturum)

**`isg_risk` (F2-002):** ✅ TAMAMLANDI
- Modül kuruldu, tarayıcıda test edildi, tüm alanlar çalışıyor
- `models/isg_risk_assessment.py`: 6 durumlu state machine (draft→in_progress→done→approved→renewal→archived), yenileme tarihi compute (tehlike sınıfına göre +2/4/6 yıl), revizyon zinciri (action_new_revision), onaylayan takibi (approver_id, approval_date), toplam/yüksek risk/açık DÖF sayaçları (store=True)
- `models/isg_risk_line.py`: L Matrisi (5x5) + Fine-Kinney (Kinney-Wiruth standart skalası), kalıntı risk, DÖF entegrasyonu (action_create_capa → isg.capa kaydı açar)
- `models/isg_capa_ext.py`: isg.capa'ya source='risk_assessment' seçeneği + risk_line_id alanı eklendi
- `views/isg_risk_assessment_views.xml`: list, form, search, action
- `views/isg_risk_line_views.xml`: list, form, search, action
- `views/isg_risk_menus.xml`: Risk Değerlendirmesi ana menüsü (sequence=30)
- `security/isg_risk_security.xml`: şirket bazlı record rule
- `security/ir.model.access.csv`: readonly/expert/manager ACL (assessment + line)
- `data/isg_risk_sequence.xml`: ISG-RD-YYYY-NNNN (noupdate=1)

**Önemli Ders (Bu Oturumda Öğrenildi):**
- SESSION.md "başlatıldı" gibi belirsiz notlar bırakmaz — her dosyayı ls/cat ile doğrula
- VPS'te önceki oturumdan kalma yarım/hatalı taslak dosyalar olabilir, her yeni oturumda kontrol et
- store=True olmayan compute alanlar search domain'de kullanılamaz (Unsearchable field hatası)
- selection_add ile eklenen seçenekte ondelete='set default' geçersiz (default yoksa) → 'cascade' kullan

### Devam Noktası

**Sıradaki: F2-003 `isg_incident`** — İş kazası / ramak kala modülü
- Kaza kaydı (6331 md.14 bildirimi)
- SGK 3 iş günü bildirim takibi
- Ramak kala kaydı
- DÖF bağlantısı (isg_capa)

### Bilinen Açık Konular

1. `isg_contractor` contractor_level — recursive=True eklenmeli
2. `isg_location` hazard_type — unknown parameter 'invisible' WARNING (işlevsel değil)
3. `isg_visitor` ppe_notes — invisible parametresi (işlevsel değil)
4. Admin şifresi — PostgreSQL NULL yapıldı, kalıcı şifre belirlenmeli
5. `isg_health_basic` — KVKK danışman onayı bekliyor
6. `isg_risk_line` record rule eksik — satır kayıtları şirket bazlı izole değil (ilerleyen fazda düzeltilecek)

### Kurulu Modüller (44 toplam, 15 ISG)

isg_core, isg_security, isg_party, isg_location, isg_document,
isg_hr, isg_base, isg_training, isg_contractor, isg_board,
isg_correspondence, isg_visitor, isg_capa, isg_risk, hr_skills
### Servis Komutları

```bash
# Modül güncelle
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" \
  -d isg -u MODUL_ADI --stop-after-init 2>&1 | grep -E "ERROR|loaded" | tail -10
sudo systemctl start odoo18-isg.service

# Yeni modül kur
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" \
  -d isg -i MODUL_ADI --stop-after-init 2>&1 | grep -E "ERROR|loaded" | tail -10
sudo systemctl start odoo18-isg.service
```
