# CONTEXT_FOR_CLAUDE.md — Hızlı Seans Başlangıç Snapshot (Doğrulanmış: 17 Eylül 2026)

**Geçerlilik:** 17 Eylül 2026
**HEAD:** f74a5e7
**Modüller:** 31/31 kurulu (%100) — isg_tests ayrı/uninstalled, sayıma dahil değil

## 🏁 Hızlı Başlangıç (Yeni Seans)

### 1. VPS Doğrulama (her seans başında ZORUNLU)
```bash
cd /opt/odoo/isg_addons
git log --oneline -5
ls -la | grep isg_
sudo -u postgres psql -d isg -c "SELECT name, state FROM ir_module_module WHERE name LIKE 'isg_%' ORDER BY name;"
sudo systemctl status odoo18-isg.service | head -5
```

**Neden zorunlu:** 17 Eylül 2026'da `.claude/` dosyalarının bir kısmı (eski oturumlardan) gerçek VPS durumuyla çelişen bilgi içeriyordu (yanlış modül mimarisi, "isg_training henüz başlamadı" gibi). VPS çıktısı her zaman tek gerçek kaynak.

### 2. Dosyaları Oku
```bash
cat .claude/SESSION.md
cat .claude/TASKS.md
cat .claude/CLAUDE.md
cat .claude/BACKLOG.md
```

### 3. Danışmanlık İşlerine Dokunma
`.claude/DANISMANLIK_ISLERI_BEKLEMEDE.md` — bütçe onayı gelene kadar bu liste pasif, sadece referans için var.

---

## 📦 Gerçek Proje Durumu (17 Eylül 2026, VPS doğrulanmış)

### Modüller (32 klasör, 31 installed)
isg_audit, isg_base, isg_board, isg_capa, isg_chemical, isg_compliance,
isg_contractor, isg_core, isg_correspondence, isg_document, isg_emergency,
isg_environment, isg_equipment, isg_health_basic, isg_hr, isg_incident,
isg_legislation, isg_location, isg_measurement_core, isg_measurement_hygiene,
isg_osgb, isg_party, isg_penalty, isg_ppe, isg_ptw, isg_reporting, isg_risk,
isg_security, isg_simulator, isg_training, isg_visitor
+ isg_tests (uninstalled)

### Git History (son 10)
f74a5e7 (HEAD -> main, origin/main) SEANS 12 — İç Dokümantasyon Güncelleme
39a27e4 fix(isg_health_basic): Field parameter ve XML reference düzeltmeleri
35fdc77 feat(isg_health_basic): Encryption ve audit log sistemi eklendi
3cce1f6 SEANS 12 PLAN
ea535ac SEANS 11: scaffold tamamlandı (31/31 modül)
4235cc4 Merge branch 'main'
5880e1c feat(isg_health_basic): KVKK uyumlu scaffold
c2b772d fix(isg_location): hazard_type invisible parametresi kaldırıldı
6dc741b Add files via upload
3fb1b90 SEANS 7: F5-003 Final Validation — HSE Radar %100 doğrulandı

### Son Tamamlanan İş: isg_health_basic (Seans 12)
- Fernet encryption (`encryption_helper.py`)
- `physician_notes_encrypted` + `physician_notes` (compute/inverse, role-based masking)
- `isg.employee.health.audit` modeli (create/write/unlink hooks)
- ACL: manager/expert/readonly

---

## 🎯 Sıradaki İş (bizim yapabileceklerimiz, danışman gerekmiyor)

1. ✅ Dokümantasyon düzeltmesi (tamamlanıyor)
2. → **res.users.workplace_ids + record rule'lar** (öncelik #1)
3. Bilinen bug temizliği (contractor_level, hazard_type, ppe_notes, isg_group_ids)
4. F5-002/F5-003 doğrulama
5. MEV-008 risk bilgilendirmesi
6. isg_health_basic iyileştirmeleri (key rotation, retention) — opsiyonel
7. OEL/STEL script hazırlığı

## ⚠️ Bilinen Sorunlar
- `res.users.workplace_ids` tanımlanmamış → record rule'lar placeholder
- Contabo VPS github.com:443 egress bazen git push'u engelliyor
- Encryption key rotation / audit retention script'i yok

## 🔒 Danışmanlık İşleri (AYRI TUTULUYOR, dokunma)
→ `.claude/DANISMANLIK_ISLERI_BEKLEMEDE.md`

---

## 🚀 Kontrol Listesi (Seans Başında)
- [ ] VPS bağlantısı OK
- [ ] git log HEAD kontrol edildi
- [ ] psql module count: 31 installed
- [ ] systemctl status: running
- [ ] .claude/ dosyalar bu snapshot ile tutarlı mı kontrol edildi
- [ ] Danışmanlık listesine yanlışlıkla dokunulmadı
