# CLAUDE.md — Seans 4 Bağlamı (03 Eylül 2026 — Seans 3 BİTTİ)

**Tarih:** 03 Eylül 2026, 07:53 UTC — isg_equipment kurulu, 33/33 %100, Seans 3 TAMAMLANDI

## 🎉 SON DURUM

✅ **33/33 ISG Modülü KURULU (%100)**
- 58 Odoo modülü toplam
- Servis stabil, log temiz
- Git senkron

✅ **Bu Seansda (Seans 3) Kurulu:**
1. isg_audit (scoring FIX + repeat_count AUTO)
2. isg_incident (SGK notification + dönüş eğitimi)
3. isg_ppe (KKD envanter)
4. isg_chemical (OEL/STEL + uyumsuzluk)
5. isg_equipment (EK-II + periyodik kontrol) ✅ SON

**HSE Radar Eşdeğerliği:** %75-80
**Full Eşdeğerlik İçin:** 11-20 gün daha

---

## 🚀 Seans 4 Başlangıç Bilgisi

**Kaldığın Yer:** 
- isg_equipment kurulu ve çalışıyor
- 33/33 modül ✅
- Commit: 301e7c0 (.claude: Seans 3 tamamlandı)

**Sıradaki İş:**
1. **isg_ptw + isg_loto** (4-6 gün) ← BAŞLA BURADAN
   - İş izni (Sıcak iş, kapalı alan, elektrik, yüksekte)
   - LOTO (Lockout/Tagout) izolasyon yönetimi
   - Ön koşul kontrol listeleri
   - Çok aşamalı onay zinciri

2. **isg_emergency** (2-3 gün)
3. MEV-008 + F5 (ufak fixler, doğrulama)

**VPS Durumu:**
- Servis: running (sudo systemctl status odoo18-isg.service)
- Database: isg, 33 modül kurulu
- Config: /etc/odoo/odoo18-isg.conf
- Addons: /opt/odoo/isg_addons/
- Git: main branch, senkron

---

## Bir Önceki Seanslar (Özet)

| Seans | Tarih | Modüller | Tamamlanan |
|---|---|---|---|
| 1 | 27-31 Ağustos | F0-5 + OSGB | 27/32 |
| 2 | 01-02 Eylül | B-4/8/9 + gap analysis | 30/33 |
| 3 | 02-03 Eylül | audit/incident/ppe/chemical/equipment | **33/33 (%100)** |
| 4 | BAŞLANACAK | ptw+loto + emergency + fixes | → %100 HSE |

---

## Kritik Hatırlatmalar

- VPS'te tek komut (art arda değil)
- `--logfile=""` daima
- `| tail -N` ile kısa tut
- Odoo 18: `<list>` (not `<tree>`), `invisible=` (not `states=`)
- Sequence: ISG-XXX-YYYY-NNNN
- Tracking: Many2one'larda WARNING (uyar)
- Git: Hep senkron, commit: sık

**Başlamaya Hazır: SİZİN HARITANIZ HAZIR! 🗺️**
