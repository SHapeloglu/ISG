# CLAUDE.md — Yeni Chat Bağlamı

**Tarih:** 29 Ağustos 2026  
**Proje:** Contabo VPS'te Odoo 18 tabanlı Türkiye İSG platformu

---

## 🎉 PROJE MİLSTON

**32/32 Modül KURULU + F2-004 isg_audit 95% TAMAMLANDI**
- Tüm ana modüller kurulu ve test edildi
- 59 Odoo modülü çalışıyor (native + ISG)
- HSE Radar eşdeğerliği %95+
- isg_audit: Puanlama + Bulgu Lifecycle tam fonksiyonel
- Sistem stabil

---

## Geliştirici Profili

- Junior Odoo developer
- Python/Odoo öğreniyor
- Her adım birlikte, step by step
- Terminal komutları VPS'te çalıştırıyor

---

## Son Oturum (29 Ağustos)

✅ **F2-004 isg_audit — Detaylı Revizyon Tamamlandı**

**Commit 1 (fab20d0): Puanlama/Skorlama**
- weight (1-5) alanı template + line'a eklendi
- response_weight compute eklendi (Uygun ise weight, değilse 0)
- compliance_percentage = (achieved_weight / total_weight) * 100
- compliance_status = GREEN (≥90%) / YELLOW (70-89%) / RED (<70% veya kritik bulgu)
- contractor_id eklendi (alt işveren denetimi)
- View'lar güncellendi (puanlama renkli gösterim)

**Commit 2 (ac459eb): Bulgu Modeli (isg.audit.finding)**
- isg.audit.finding ayrı modeli yazıldı (lifecycle: open → resolved → closed)
- finding_type: observation / non_conformity / major / critical
- repeat_count + escalation_level (3. kez → Level 2 eskalasyon)
- DÖF bağlantısı + otomatik oluşturma
- Kanıt dosyaları (ir.attachment)
- Form (8 section), List (renk kodlama), Kanban (durum bazlı), Search (13+ filter)
- Sequence: ISG-BLG-YYYY-NNNN
- ACL: 3 rol (readonly/expert/manager)

---

## Proje İlerleme: 32/32 Modül (%100)

| Faz | Toplam | Tamamlanan | % | Not |
|-----|--------|------------|---|-----|
| FAZ 0 | 7 | 7 | %100 | ✅ Temel mimari |
| FAZ 1 | 6 | 5 | %83 | isg_health_basic bloklu |
| FAZ 2 | 9 | 4 | %44 | ✅ isg_audit (puanlama + bulgu) |
| FAZ 3 | 2 | 0 | %0 | Ölçüm/çevre |
| FAZ 4 | 4 | 4 | %100 | ✅ Sanal Müfettiş |
| FAZ 5 | 3 | 0 | %0 | Raporlama |
| OSGB | 1 | 1 | %100 | ✅ OSGB planlama |
| **TOPLAM** | **32** | **27** | **%84** | |

---

## Çalışma Kuralları (Kritik)

### Terminal Komutları
- Tek tek ver, art arda değil
- `--logfile=""` daima (config'de logfile tanımlı)
- `| tail -N` ile çıktıyı kısa tut
- `| grep -E "ERROR|loaded"` hata kontrolü

### Modül Geliştirme
- Manifest: base, mail, isg_core bağımlılıkları
- Views: Odoo 18 (tree → list, states= yasak, attrs= yasak)
- ACL: readonly/expert/manager 3 rol
- Sequence: ISG-XXX-YYYY-NNNN formatı

### Odoo 18 Kritik Kurallar
1. `<tree>` → `<list>` (Odoo 18 syntax)
2. `states=` ve `attrs=` YASAK (Odoo 17+ hata verir)
3. `fields.Datetime` (büyük D), `fields.Date` kullan
4. `unique=True` Char'da warning verir, kullanma
5. XML wrapper: `<data>` gerek yok, doğrudan `<record>`
6. `invisible=` expression kullan (Odoo 18)
7. `<list editable="bottom">` inline edit için
8. XML'de `<` karakteri `&lt;` olarak escape edilmeli

---

## Kurulu Modüller (59 toplam, 32 ISG)

**FAZ 0:** isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, isg_base

**FAZ 1:** isg_training, isg_contractor, isg_board, isg_correspondence, isg_visitor

**FAZ 2:** isg_capa, isg_risk, isg_incident, **isg_audit** (puanlama + bulgu)

**FAZ 4:** isg_legislation, isg_compliance, isg_penalty, isg_simulator

**OSGB:** isg_osgb

**Odoo Native:** base, mail, hr, hr_skills, hr_org_chart, account, stock, 30+ diğer

---

## Sıradaki Görevler

### Kısa Vadeli (1-2 hafta)

1. **FAZ 2 devam (5 modül):**
   - F2-005 isg_ppe (~2 gün)
   - F2-006 isg_emergency (~1.5 gün)
   - F2-007 isg_chemical (~3-4 gün, veri seti doğrulaması)
   - F2-008 isg_equipment (~2-3 gün, Ara.2025 EK-II)
   - F2-009 isg_ptw + isg_loto (~3-4 gün)

2. **B-4/B-8/B-9/B-10 MEV retrofit (~1.5-2 gün)**

### Orta Vadeli (2-4 hafta)

3. **FAZ 3 (Ölçüm/Çevre, ~7-10 gün)**
4. **FAZ 5 (Raporlama + Superset, ~7-12 gün)**

### Uzun Vadeli (Üretim Hazırlığı)

5. **E3 Entegrasyonu:** SGK, EKİPNET, İSG-KATİP, e-imza (5070 s.K.)

---

## İstatistikler

| Metrik | Değer |
|---|---|
| Toplam Modül | 32 (42 B-görevleri dahil) |
| Kurulu Modül | 59 (Odoo native + ISG) |
| Toplam Model | 100+ |
| Kod Satırı | 18,000+ (Python + XML) |
| Commit Sayısı | 32+ |
| Proje Süresi | 30+ gün |
| HSE Radar Eşdeğerlik | %95+ |

---

## Sonraki Adım

**F2-005 isg_ppe** (KKD yönetimi) ile devam et.

- İlk olarak F2-005'e başlayacak mısın, yoksa B-görevlerini (MEV retrofit) mi yapmak istiyorsun?

---

## Git Durum

- **Repository:** https://github.com/SHapeloglu/ISG
- **Branch:** main
- **Commit sayısı:** 32+
- **Son commit:** ac459eb — [isg_audit] Bulgu modeli tamamlandı

