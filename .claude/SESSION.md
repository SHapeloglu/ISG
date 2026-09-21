# SESSION.md — Oturum Özeti ve Devam Noktası (Doğrulanmış: 21 Eylül 2026)

## Son Doğrulanmış Durum: 21 Eylül 2026

31/31 üretim modülü kurulu (%100). Bu seansta işyeri/şirket bazlı record rule (güvenlik) çalışması yapıldı.

## Bu Seansta Yapılanlar (commit sırasıyla)

1. `c76b855` — isg_health_basic: workplace_id compute alanına store=True + readonly/expert/manager record rule (isg.employee.health + isg.employee.health.audit). Audit kayıtları write/unlink kapalı (KVKK Md.21).
2. `412de4a` — isg_audit/isg_incident/isg_risk: daha önce çalışma dizininde yazılmış ama commit edilmemiş kalan record rule düzeltmeleri bulunup commit edildi.
3. `507d1ca` — isg_compliance/isg_emergency/isg_environment/isg_ppe: eski/gevşek desenden yeni desene (user.isg_workplace_ids + company fallback) taşındı. isg_compliance ve isg_environment manifest'lerine eksik isg_security bağımlılığı eklendi.

## ÖNEMLİ GOTCHA (bu seansta öğrenildi)

`noupdate="1"` olan security XML dosyalarında bir `ir.rule` kaydının XML id'sini değiştirirsen, Odoo eski kaydı SİLMEZ — yanına yenisini ekler. ir.rule'lar aynı grup için OR ile birleştiği için eski gevşek kural sessizce kazanır, düzeltme etkisiz kalır. Böyle durumda eski kayıtları Odoo shell'den elle silmek gerekir:
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin shell -c /etc/odoo/odoo18-isg.conf -d isg --no-http << 'PYEOF'
rules = env['ir.rule'].browse([ID_LISTESI])
rules.unlink()
env.cr.commit()
PYEOF
(commit() şart, shell'de otomatik commit yok). `noupdate="0"` (varsayılan) dosyalarda bu sorun yok, Odoo eski kaydı otomatik değiştiriyor.

## Devam Noktası — Kalan İş (Aşama 3)

Şu 16 modülde HİÇ workplace/company record rule yok (sadece grup bazlı ACL var — expert/manager her şirketin/işyerinin verisini görebiliyor):

isg_board, isg_capa, isg_contractor, isg_correspondence, isg_document, isg_hr,
isg_location, isg_osgb, isg_party, isg_penalty, isg_reporting, isg_simulator,
isg_training, isg_visitor, isg_core, isg_base

Bunlar "Aşama 1/2"deki gibi desen taşıma değil, sıfırdan yazma gerektiriyor. Öncelik önerisi: isg_hr (çalışan kişisel verisi) ve isg_contractor (ticari veri) önce, diğerleri sonra.

Her modül için sıra:
1. Modelin workplace_id/company_id alanı var mı, compute ise store=True var mı kontrol et
2. security/ altında yeni dosya yaz (readonly/expert/manager, isg_workplace_ids + fallback deseni — önceki commit'lerdeki dosyalar örnek alınabilir)
3. Manifest'te isg_security bağımlılığı var mı kontrol et, yoksa ekle
4. `-u MODUL_ADI --stop-after-init` ile test et, ERROR var mı bak
5. Eski kural kalıntısı var mı `SELECT name FROM ir_rule WHERE ...` ile kontrol et (özellikle noupdate="1" dosyalarda)
6. Servisi başlat, commit + push

### Bilinen Açık Konular (değişmedi)
- isg_contractor.contractor_level → recursive=True eklenmeli
- isg_location.hazard_type, isg_visitor.ppe_notes → invisible parametresi WARNING (işlevsel değil)
- Contabo VPS github.com:443 egress kısıtlaması — bazen git push'u engelliyor (bu seansta sorun çıkarmadı)
- F5-002/F5-003, MEV-008, OEL/STEL script — hâlâ bekliyor (TASKS.md'de #4/#5/#7)

### Servis Komutları
```bash
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" \
  -d isg -u MODUL_ADI --stop-after-init 2>&1 | tail -40
sudo systemctl start odoo18-isg.service
```
