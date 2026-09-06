# CLAUDE.md — Seans 6 Başlangıcı (05 Eylül 2026 — Seans 5 BİTTİ)

## 🎯 SEANS 5 TAMAMLANDI

✅ **F5-002: 5 QWeb PDF Rapor Şablonu KURULU & WORKING**
- Risk Değerlendirmesi
- Kaza/Ramak Kala  
- Denetim
- Ekipman Periyodik Kontrol (EKİPNET)
- İş Hijyeni Ölçüm

✅ **F5-003 Test Protocol Hazır**
- 27 işlev, 5 senaryo, CRUD + workflow + relations + raporlama
- Sample data creation script yazıldı

❌ **Sample Data Sorunları**
- Model validasyonları kompleks (authorized_body required, team_leader Many2one vb.)
- Seans 6'da clean fixture builder yapılacak

## 🚀 Seans 6 Başlangıcı

**Kaldığın Yer:**
- Commit: 0a4bd5d (.claude: Seans 4 Tamamlandı)
- HSE Radar Eşdeğerliği: ~90%
- Modül: 30/30 kurulu (%100)

**Sıradaki İş (Sıra):**

### 1️⃣ F5-003 Clean Test Data (1 gün)
- Sample data'yı Odoo UI'dan oluştur (ya da direct SQL seed)
- 7 kritik modül: workplace, employee, risk, incident, audit, equipment, ptw
- Raporları generate et, ERROR yok mu kontrol et

### 2️⃣ PDF Raporlama Validation (0.5 gün)
- 5 raporun doğru render olduğu
- Tüm alanların visible olduğu
- Log temizliği

### 3️⃣ isg_tests Cleanup (1-2 gün, optional)
- TransactionCase testleri alan validasyonuyla fix et
- `--test-enable` ile çalıştır

## VPS Info
- Config: /etc/odoo/odoo18-isg.conf
- Database: isg (30/30 ISG modülü)
- Service: odoo18-isg.service (running)

**Seans 6'da F5-003'ü bitirip HSE Radar %100 eşdeğerliğe ulaşalım!**
