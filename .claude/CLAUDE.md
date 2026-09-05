# CLAUDE.md — Seans 5 Bağlamı (05 Eylül 2026 — Seans 4 BİTTİ)

## 🎉 SEANS 4 TAMAMLANDI

✅ **F5-002: 5 QWeb PDF Rapor Şablonu KURULU**
- Risk Değerlendirmesi (isg_risk)
- Kaza/Ramak Kala (isg_incident)
- Denetim (isg_audit)
- Ekipman Periyodik Kontrol (isg_equipment)
- İş Hijyeni Ölçüm (isg_measurement_hygiene)
- Tüm template'ler ir.actions.report'a kayıtlı

✅ **VPS Durumu Doğrulandı**
- 30/30 ISG modülü kurulu (%100)
- HSE Radar Eşdeğerliği: ~90%
- Log: ERROR 0, Servis: running

❌ **Test Framework (isg_tests)**
- 7 modül için test yazıldı (CRUD, workflow, relations)
- Alan validasyon sorunları → sonraya bırakıldı
- Strateji: Seans 5'te temiz version

## 🚀 Seans 5 Başlangıcı

**Kaldığın Yer:**
- Commit: f5f8c3e (F5-002 PDF şablonları)
- Modül: 30/30 kurulu (%100)
- HSE Radar Eşdeğerliği: ~90%
- Log: Temiz, ERROR 0

**Sıradaki İş (Sıra TBD):**

### Seçenek 1: F5-003 (HSE Radar Kabul Testi) — 1-2 gün
- 27 işlev × 5 senaryo = 135 test case
- Normal akış, olumsuz akış, yetkisiz akış
- Çok şirket/işyeri/site testleri
- PDF raporlarının doğru render edilip edilmediği

### Seçenek 2: isg_tests (Test Framework Cleanup) — 1-2 gün
- Tüm 7 modülün alanlarını düzelt
- TransactionCase testlerini valid kıl
- CI/CD hazırlığı

### Seçenek 3: E2/E3 Entegrasyon (İsteğe Bağlı) — 2-4 hafta
- SGK API bildirimi
- EKİPNET dosya yükleme
- KVKK maskeleme

## VPS Info
- Config: /etc/odoo/odoo18-isg.conf
- Addons: /opt/odoo/isg_addons/
- Database: isg (30/30 ISG modülü)
- Service: odoo18-isg.service (running)

## Kural Hatırlatma
- Terminal: 1 komut, çıktı bekle, devam et
- Log: `--logfile=""`
- Odoo 18: `<list>` not `<tree>`, `invisible=` not `states=`
- Git: Sık commit, her milestone'dan sonra .claude dosyalarını güncelle

**Seans 5'e Hazır: Hangi işi yapmak istiyorsun? (F5-003, isg_tests, E2/E3?)**
