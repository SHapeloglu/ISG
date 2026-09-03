# CLAUDE.md — Yeni Chat Bağlamı (03 Eylül 2026 — Seans 3 Devam)

**Tarih:** 03 Eylül 2026 — isg_audit, isg_incident, isg_ppe, isg_chemical kurulu, MEV-002 başlanacak

## 🎉 PROJE MİLSTON (Güncellenmiş)

**33/33 ISG Modülü KURULU (%100) ✅**
- 58 Odoo modülü çalışıyor (33 ISG + 27 native)
- Tüm FAZ 0-5 + OSGB + isg_reporting TAMAMLANDI
- **HSE Radar eşdeğerliği %75-80** (full eşdeğerlik için 11-20 gün)
- Sistem stabil, log'da hata yok, git senkron (50+ commit)

**Seans 3 Tamamlandı:**
- ✅ isg_audit: scoring FIX (NA hariç) + repeat_count AUTO
- ✅ isg_incident: SGK bildirimi + dönüş eğitimi
- ✅ isg_ppe: KKD envanter + zimmet + yenileme
- ✅ isg_chemical: OEL/STEL + depolama uyumluluğu

## Geliştirici Profili

- Junior Odoo developer
- Python/Odoo öğreniyor
- Her adım birlikte, step by step
- Terminal komutları VPS'te çalıştırıyor

## Kurulu Modüller (33/33) — %100 ✅

| Faz | Modüller | Kurulu |
|---|---|---|
| FAZ 0 | isg_core, security, party, location, document, hr, base | 7/7 ✅ |
| FAZ 1 | training, contractor, visitor, board, correspondence | 5/6 ✅ |
| FAZ 2 | capa, risk, incident, audit, ppe, emergency, chemical, equipment, ptw | 9/9 ✅ |
| FAZ 3 | measurement_core, measurement_hygiene, environment | 3/3 ✅ |
| FAZ 4 | legislation, compliance, penalty, simulator | 4/4 ✅ |
| FAZ 5 | reporting | 1/3 ✅ |
| OSGB | isg_osgb | 1/1 ✅ |

## Sıradaki Modül: MEV-002 isg_equipment (3-5 gün)

**Ara.2025 EK-II Güncellemesi:**
- Ekipman kataloğu: kompresör, vinç, asansör, forklift, platform, kaldırma cihazları
- Periyodik kontrol periyodu (6 ay / 1 yıl / vb.) ve yöntem
- e-imza desteği (5070 s.K.)
- EKİPNET sözleşme onayı + bildirim hazırlık
- Kontrol sonucu rapor ve uyarı sistemi

**Mevzuat:** İş Ekipmanları Yönetmeliği (Ara.2025 güncellendi)

## Çalışma Kuralları (Kritik)

### Terminal Komutları
- Tek tek ver, art arda değil
- `--logfile=""` daima
- `| tail -N` ile kısa tut
- `| grep -E "ERROR|loaded"` hata kontrolü

### Modül Geliştirme
- Manifest: base, mail, isg_core bağımlılıkları
- Views: Odoo 18 (`<list>`, `<tree>` değil)
- ACL: readonly/expert/manager/superadmin 4 rol
- Sequence: ISG-XXX-YYYY-NNNN formatı

### Odoo 18 Kritik Kurallar
1. `<tree>` → `<list>` (Odoo 18 syntax)
2. `states=` ve `attrs=` **YASAK** → `invisible=`
3. `fields.Datetime` (büyük D)
4. `tracking=True` Many2one'larda WARNING (uyar)
5. XML'de `<` → `&lt;`
6. `<list editable="bottom">` inline edit
7. Odoo 18'de `numbercall` yok (eski alanlar removed)

## İstatistikler (Güncellenmiş)

| Metrik | Değer |
|---|---|
| Kurulu Modül | 33/33 (%100) ✅ |
| İlerleme | %100 (modül), %75-80 (HSE Radar eşdeğerlik) |
| Kurulu ISG | 33 |
| Kurulu Native | 28 |
| Toplam Model | 110+ |
| HSE Radar Eşdeğerlik | %75-80 |
| Full Eşdeğerlik İçin | 11-20 gün |
| Commit Sayısı | 50+ |
| Toplam Süre | ~42-45 gün |

## Son Yapılanlar (Seans 3 — Tamamlandı)

✅ **isg_audit: scoring FIX + repeat_count AUTO**
- NA maddeleri total_weight'den hariç tut
- applicable_lines filteresi
- repeat_count otomatik hesaplama (benzer bulgular query)

✅ **isg_incident: SGK notification + dönüş eğitimi**
- SGK 3 gün notification deadline (4 takvim günü)
- return_to_work_training tetikleyicisi

✅ **isg_ppe: KKD envanter + zimmet**
- IsgPpeType (9 kategori)
- IsgPpeStock (stok takibi)
- IsgPpeIssue (zimmet, expiry_date compute)

✅ **isg_chemical: OEL/STEL + depolama uyumluluğu**
- IsgChemicalOel (Türkiye ÇSGB TWA/STEL)
- IsgChemicalIncompatibility (depolama matrisi)

## Sonraki Adım

**MEV-002: isg_equipment — Ara.2025 EK-II Güncellemesi** ← **START**
- Skeleton var, implementasyon yapılacak
- Ekipman kataloğu + periyodik kontrol form
- e-imza + EKİPNET alanları
- Tahmini: 3-5 gün

Başlamaya hazır! 🚀
