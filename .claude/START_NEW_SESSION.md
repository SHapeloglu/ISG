# START_NEW_SESSION.md — Yeni Seans Onboarding (5 Adım)

**Bu dosyayı her seans başında oku (Seans 1, 2, 3, ... sonsuza kadar)**

---

## ✅ ADIM 1: VPS Bağlantısı Doğrula (1 min)

```bash
cd /opt/odoo/isg_addons
pwd
ls -la .claude/
```

**Beklenen:** `/opt/odoo/isg_addons` ve `.claude/` klasörü var

---

## ✅ ADIM 2: Git & Modül Durumu Kontrol Et (2 min)

```bash
git log --oneline -5
git status
sudo -u postgres psql -d isg -c "SELECT COUNT(*) FROM ir_module_module WHERE state='installed';"
```

**Beklenen:**
- HEAD: latest commit (bakalım hangi seans?)
- Working tree: clean
- Module count: 31 (Seans 12), 32 (final)

---

## ✅ ADIM 3: Odoo Service Check (1 min)

```bash
sudo systemctl status odoo18-isg.service | head -10
tail -50 /var/log/odoo/odoo18-isg.log | grep -E "ERROR|WARNING" | tail -5
```

**Beklenen:** Active (running), no ERROR lines

---

## ✅ ADIM 4: Context Dosyalarını Oku (3 min)

**Sırada:**
1. `.claude/SESSION.md` — Son seans neler yaptı?
2. `.claude/TASKS.md` — Sonraki task ne?
3. `.claude/CLAUDE.md` — Kuralları hatırla
4. `.claude/BACKLOG.md` — Blokajlar var mı?
5. `.claude/CONTEXT_FOR_CLAUDE.md` — Hızlı snapshot

**Tavsiye:** Claude'un aşağıda sorduğu soruyu yanıtlamak için dosyaları kapat ve kendi başında özetle.

---

## ✅ ADIM 5: Claude'a Seans Başlatma Mesajı Gönder

**Yapı:**
Seans [N]: [İş Başlığı]

Durum: [X]/32 modül kurulu, HEAD: [commit hash]
VPS: vmi3389964, isg.powerbi.com.tr
Son seans (Seans N-1): [Ne yaptı? Tamamlanan vs. Açık konular]

Devam etmek için:

[Doğrulanacak ilk şey]
[Yazılacak ilk dosya]
[Açılacak ilk modül]


**Örnek (Seans 13):**
Seans 13: isg_training B-10 — April 2, 2026 Regulation Training Module

Durum: 31/32 modül kurulu, HEAD: 39a27e4
VPS: vmi3389964, isg.powerbi.com.tr
Son seans (Seans 12): Encryption + audit log sistem eklendi (isg_health_basic)

Devam etmek için:

VPS'i doğrula (git log, modül sayısı)
isg_training scaffold başla (model, views, ACL)
April 2, 2026 regulation RG 33212 maddelerini mapla

---

## 🚨 Hata Durumunda

### Git status dirty
```bash
git diff                  # Ne değişti?
git checkout -- .        # Revert (DIKKAT: unsaved work kaybolur)
# veya
git add -A && git commit -m "WIP: ..." && git push
```

### Module count wrong
```bash
sudo -u postgres psql -d isg -c "SELECT name, state FROM ir_module_module WHERE state != 'installed' LIMIT 10;"
```

### Service down
```bash
sudo systemctl restart odoo18-isg.service
sleep 5
sudo systemctl status odoo18-isg.service
```

### Log'da ERROR
```bash
tail -200 /var/log/odoo/odoo18-isg.log | grep -A30 "ERROR"
# Ya da
sudo systemctl stop odoo18-isg.service
# Upgrade et, bak hata mesajına
```

---

## 📝 Seans Sonunda

**Zorunlu:**
1. `.claude/SESSION.md` güncelle (ne yaptın?)
2. `.claude/TASKS.md` güncelle (sonraki ne?)
3. `.claude/CONTEXT_FOR_CLAUDE.md` güncelle (snapshot)
4. Git add/commit:
```bash
   git add .claude/
   git commit -m "SEANS [N]: [İşin Özeti]"
   git push origin main
```

**Başarısız olursan:**
- Push başarısız (egress)? Bekle veya `-f` ile retry
- Commit başarısız? `git status` bak
- Dosya yazma başarısız? sudo kontrol et, permission kontrol et

---

## 🎓 Sık Hatalar (Kaçınılması Gereken)

| Hata | Çözüm |
|------|-------|
| "VPS bağlantısı yok" | ssh credentials kontrol et |
| "git push rejected" | `git pull --rebase`, sonra `git push` |
| "Modül upgrade başarısız" | Log'ı oku, dependency/syntax hatası ara |
| ".claude/ dosyaları bayat" | Her seans sonunda update et |
| "Python script hata" | Venv path kontrol et: `/opt/odoo/venv18-isg/bin/python3` |
| "Config dosyası bulunamadı" | `/etc/odoo/odoo18-isg.conf` path kontrol et |

---

## 🎯 Seans Zamanlaması

- **Orta:** 2-3 saat (feature, model scaffold, test)
- **Uzun:** 4-6 saat (complex feature, debugging, refactor)
- **Kısa:** 30-60 dakika (bug fix, patch, doc update)

Tahmin et ve başla!

