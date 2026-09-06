# SEANS 6 BAŞLANGICI — Ready-to-Start Checklist

## ✅ PRE-SESSION VERIFICATION (Seans 6 başında çalıştır)

### 1. VPS Durumu Kontrol Et
```bash
# Terminal: git status, log kontrol
git log --oneline -5
git status

# Servis running mı?
sudo systemctl status odoo18-isg.service | grep -E "active|failed"

# Log temiz mi?
grep "ERROR" /var/log/odoo/odoo18-isg.log | tail -5 || echo "No errors found"
```

### 2. Modül Listesi Doğrula
```bash
# 30/30 modül kurulu mu?
psql -d isg -c "select count(*) from ir_module_module where name like 'isg_%' and state='installed';"
# Beklenen: 30
```

### 3. .claude Dosyaları Oku
- SESSION.md — Kaldığın yer
- TASKS.md — Yapılacak işler
- F5-003_TEST_PROTOCOL.md — Test planı
- BACKLOG.md — Sonraki öncelikler

### 4. Seans 6 Plan
**Gün 1 (F5-003 Implementation)**
- Odoo UI'dan test data oluştur (7 kritik modül)
- 5 PDF raporunu generate et
- ERROR log kontrol

**Gün 2 (Validation)**
- PDF raporları manual inspect
- HSE Radar 27 işlev compliance check
- Final git commit

---

## 📋 SEANS 6 AKIŞI

### Adım 1: Test Data Oluştur (Odoo UI)
Workplace: Test Facility
Site: Main
Employee: Test Worker
Risk Assessment
Incident (SGK flow)
Audit + Findings
Equipment Inspection
PTW + LOTO

### Adım 2: PDF Raporları Generate Et
- Risk raporu: http://localhost:8069/.../report/pdf/
- Incident raporu
- Audit raporu
- Equipment raporu
- Measurement raporu

### Adım 3: Validation
- ERROR yok mu log'da?
- Tüm alanlar render mi?
- HSE Radar 27 işlev OK mi?

### Adım 4: Commit & Close
git commit -m "F5-003: Test Data + PDF Validation Completed — HSE Radar 100%"
.claude update
git push

---

## 📞 PROBLEM ÇÖZÜMÜ (Seans 6'da karşılaşırsan)

**Data creation field error:**
- Model alan adlarını grep'le: `grep "fields\." isg_MODULE/models/*.py`
- SQL'de manuel insert et: `INSERT INTO table ... VALUES ...`

**PDF render error:**
- Template XPath syntax kontrol et: `</t>` not `</t-if>`
- Model field exists: `SELECT * FROM ir_model_fields WHERE model='model.name'`

**Log ERROR:**
- Full traceback: `tail -80 /var/log/odoo/odoo18-isg.log`
- Module reload: `sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin -c /etc/odoo/odoo18-isg.conf --logfile="" -d isg -u MODULE --stop-after-init`

---

## 🎯 BAŞARI KRITERI (Seans 6 sonu)
- ✅ 7 modülün test datası oluşturuldu
- ✅ 5 PDF raporu generate edildi
- ✅ Log: ERROR = 0
- ✅ HSE Radar eşdeğerliği = %100
- ✅ Git commit + .claude update

---

**SEANS 6 BAŞLAMAYA HAZIR!** 🚀

Last commit: cb4db3b (.claude: Seans 5 FINAL)
Date: 05 September 2026, 20:25 UTC
