# 🚀 YENİ SESSION BAŞLATMA — Adım Adım

**Bu dosya her yeni session'da ilk yapılacak şeydir.**

---

## ADIM 1: Bu Dosyayı Oku (1 dakika)
```bash
cat .claude/START_NEW_SESSION.md
```

---

## ADIM 2: Proje Durumuyla Tanış (2 dakika)

### Projenin Amacı
Odoo 18 tabanlı **Türkiye İSG Platformu** (HSE Radar eşdeğerliği).

### Son Durum
- **HSE Radar Eşdeğerliği:** ✅ %100 TAMAMLANDI
- **Seans:** 6 tamamlandı, Seans 7'den başlıyorsun
- **Modül:** 30/31 kurulu (isg_health_basic bloklu)
- **Test Data:** 11 record oluşturuldu

### Şu Anda Ne Gerekli?
- F5-003 Final Validation (PDF raporları + checklist)
- HSE Radar sertifikasyon
- Ürün release'e hazırlanma

---

## ADIM 3: Gerçek Durumu Doğrula (3 dakika)

### 🔍 Kontrol Komutları (Hepsini Çalıştır)

**1️⃣ Git Durumu:**
```bash
git log --oneline -1 && echo "---" && git status
```
**Beklenen:** 
- HEAD: 13ec546 (F5-003 commit)
- Status: clean veya .claude/ modified

---

**2️⃣ Modül Sayısı:**
```bash
sudo -u postgres psql -d isg -c "select count(*) from ir_module_module where name like 'isg_%' and state='installed';"
```
**Beklenen:** 30 (veya 31 eğer isg_health_basic kuruldu)

---

**3️⃣ Servis Durumu:**
```bash
sudo systemctl status odoo18-isg.service | grep active
```
**Beklenen:** `active (running)`

---

**4️⃣ Log Temizliği (Güncel Errorlar):**
```bash
grep "ERROR" /var/log/odoo/odoo18-isg.log | grep -v "2026-09-06 05:" | tail -3 || echo "✅ Güncel error yok"
```
**Beklenen:** Sadece eski hatalar (05:28) veya hiçbir şey

---

## ADIM 4: Test Data ID'lerini Hatırla

Seans 6'da oluşturulan records:
Workplace: 39
Site: 10
Employee: 33
Authorized Body: 76
Risk Assessment: 11
Incident: 6
Audit: 14
Equipment: 5
Equipment Inspect: 3
PTW: 4
LOTO: 2

Bu ID'leri PDF raporlama ve checklist'te kullanacaksın.

---

## ADIM 5: .claude/ Dosya Yapısı

```bash
ls -la .claude/
```

**Şunları oku (sırasıyla):**
1. `SESSION.md` — Son seans özeti
2. `TASKS.md` — Yapılacaklar
3. `CLAUDE.md` — Proje felsefesi
4. `F5-003_TEST_PROTOCOL.md` — Test protokolü (27 işlev)
5. `ARCHITECTURE.md` — Teknik mimari
6. `BACKLOG.md` — Gelecek görevler

---

## ADIM 6: Bugünün Seçimi

**Şu 4 seçenekten birini seç:**

### A️⃣ **Web UI Test** (15-20 min) ⭐ ÖNERİLİ
- Admin panel login
- Modülleri gez (navigasyon)
- Test data records'ü açtır (ID: 11, 6, 14)
- UI tam çalışıyor mu?
- **Sonuç:** Web interface validation ✅

### B️⃣ **PDF Raporlama** (20-30 min)
- 5 PDF şablonunu test
- Record ID'leri kullanarak PDF generate
- Raporlar düzgün render mi?
- **Sonuç:** PDF validation ✅

### C️⃣ **Acceptance Checklist** (45-60 min)
- F5-003_TEST_PROTOCOL.md oku
- 27 işlev tamamlandı mı doğrula
- HSE Radar %100 sertifikasyon
- **Sonuç:** Official acceptance test ✅

### D️⃣ **isg_health_basic Kurma** (2-3 gün)
- KVKK mimarisini kur
- Sağlık verisi maskeleme
- Alan bazlı ACL
- **Sonuç:** Bloklu modül aktif
- **Not:** KVKK danışman onayı gerekli

---

## ADIM 7: Claude'a Bağlam Ver

Kontrol komutlarının çıktısını + seçimi kopyala-yapıştır:
Kontrol Komutları Sonuçları:
[git durumu çıktısı]
[modül sayısı]
[servis durumu]
[log sonucu]

Seçim: A (veya B/C/D)

Bunu ver, Claude başlayacak.

---

## 📝 ÖZET ÇIZELGE

| Adım | İşlem | Süre |
|------|-------|------|
| 1 | Bu dosyayı oku | 1 min |
| 2 | Proje durumuyla tanış | 2 min |
| 3 | 4 kontrol komutu çalıştır | 3 min |
| 4 | Test data ID'lerini hatırla | 1 min |
| 5 | .claude/ dosyalarını oku | 5 min |
| 6 | Seçim yap (A/B/C/D) | 2 min |
| 7 | Claude'a context ver | - |
| **TOPLAM** | **Hazır!** | **15 min** |

---

## 🎯 CLAUDE'A VERİLECEK EXACT PROMPT

Yukarıdaki 7 adımı yaptıktan sonra, bu prompt'u kopyala-yapıştır:
Seans 7 başlatılıyor. Şu kontroller tamamlandı:

✓ Git: [git status output]
✓ Modül: [psql output]
✓ Servis: [systemctl output]
✓ Log: [log check result]

Seçim: [A/B/C/D]

Lütfen başla.

---

## ⚠️ SORUN ÇÖZÜM

**Eğer kontrol komutlarında hata varsa:**
- Git status dirty? → `git restore .claude/`
- Servis down? → `sudo systemctl restart odoo18-isg.service`
- Log ERROR'lar güncel? → Haber ver
- Modül sayısı ≠ 30? → Haber ver

---

**🚀 Artık yeni session'a hazırsın!**

Şu metodu her seferinde kullan:
1. Bu dosyayı oku
2. 4 kontrol komutu çalıştır
3. Seçim yap
4. Claude'a context ver
5. Başla

**Hiçbir bilgi kaybı olmaz.**

