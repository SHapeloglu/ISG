# CLAUDE.md — Yeni Chat Bağlamı (31 Ağustos 2026 — B-10 Tamamlandı)

**Tarih:** 31 Ağustos 2026 — B-10 tamamlandı, gap analysis hazırlığında

## 🎉 PROJE MİLSTON (Güncellenmiş)

**31/32 ISG Modülü KURULU (%97)**
- 59 Odoo modülü çalışıyor (31 ISG + 28 native)
- Tüm FAZ 0, FAZ 1 (isg_health_basic bloklu), FAZ 2 TAM, FAZ 3, FAZ 4, OSGB, FAZ 5 (reporting)
- **HSE Radar eşdeğerliği %96-97** (mevzuat düzeltmeleri pending)
- Sistem stabil, log'da hata yok, git senkron

**Eksik:**
- ❌ isg_health_basic (bloklu, KVKK danışman onayı bekleniyor)
- ⏳ F5-002/F5-003 (doğrulama pending)
- ⏳ B-4/B-8/B-9 (mevzuat düzeltmeleri, ~2-3 gün)

## Geliştirici Profili

- Junior Odoo developer
- Python/Odoo öğreniyor
- Her adım birlikte, step by step
- Terminal komutları VPS'te çalıştırıyor

## Kurulu Modüller (31/32)

| Faz | Modüller | Kurulu |
|---|---|---|
| FAZ 0 | isg_core, security, party, location, document, hr, base | 7/7 ✅ |
| FAZ 1 | training (**✅ B-10 tamamlandı**), contractor, visitor, board, correspondence | 5/6 ✅ |
| FAZ 2 | capa, risk, incident, audit, ppe, emergency, chemical, equipment, ptw | 9/9 ✅ |
| FAZ 3 | measurement_core, measurement_hygiene, environment | 3/3 ✅ |
| FAZ 4 | legislation, compliance, penalty, simulator | 4/4 ✅ |
| FAZ 5 | reporting | 1/3 ✅ |
| OSGB | isg_osgb | 1/1 ✅ |

## Çalışma Kuralları (Kritik)

### Terminal Komutları
- Tek tek ver, art arda değil
- `--logfile=""` daima
- `| tail -N` ile kısa tut
- `| grep -E "ERROR|loaded"` hata kontrolü

### Modül Geliştirme
- Manifest: base, mail, isg_core bağımlılıkları
- Views: Odoo 18 (`<tree>` → `<list>`, `states=` yasak, `attrs=` yasak)
- ACL: readonly/expert/manager 3 rol
- Sequence: ISG-XXX-YYYY-NNNN formatı

### Odoo 18 Kritik Kurallar
1. `<tree>` → `<list>` (Odoo 18 syntax)
2. `states=` ve `attrs=` **YASAK** (Odoo 17+ hata)
3. `fields.Datetime` (büyük D), `fields.Date` kullan
4. `unique=True` Char'da warning
5. XML'de `<` → `&lt;`, `&` → `&amp;`
6. `invisible=` expression kullan
7. `<list editable="bottom">` inline edit için
8. `ir.cron`: Odoo 18'de `numbercall` yok (eski alanlar kaldırıldı)

## Sıradaki Görevler (Öncelik Sırası)

### Kısa Vadeli (~2-3 gün)

1. **B-4, B-8, B-9** — ~2-3 gün (mevzuat retrofit)
   - B-4: isg_board toplantı sıklığı (15 gün vs 1 ay)
   - B-8: isg_penalty versiyonlama (valid_from)
   - B-9: isg_core danger_class.history

2. **F5-002/F5-003 Kontrol** — ~1 gün
   - QWeb PDF şablonları var mı?
   - HSE Radar kabul testi protokolü?

### Sonraki Seans (YÜKSEKÖ ÖNCELİK)

3. **Competitive Gap Analysis** — HSE Radar ile kapsamlı karşılaştırma
   - Mevzuat kapsam (hangi yönetmelikleri kaçırıyor?)
   - UI/UX (kullanıcı deneyimi farkları)
   - Entegrasyon (ERP, SGK, KVKK)
   - Raporlama (HSE Radar'ın en zayıf yanı)
   - Performans (hacim, load testing)
   - **Sonuç:** Eksi puanlar listesi + düzeltme planı

### Ardından

- E3 Entegrasyon (SGK, EKİPNET, İSG-KATİP, e-imza)
- isg_health_basic (KVKK onayı sonrası)
- Superset raporlama + Flutter mobil

## İstatistikler (Doğrulanmış)

| Metrik | Değer |
|---|---|
| Kurulu Modül | 31/32 (%97) |
| İlerleme | %97 (modül), %96-97 (HSE Radar eşdeğerlik) |
| Kurulu ISG | 31 |
| Kurulu Native | 28 |
| Toplam Model | 105+ |
| HSE Radar Eşdeğerlik | %96-97 |
| Commit Sayısı | 37+ |

## Önemli Dosya Yolları
/opt/odoo/isg_addons/ # ISG modülleri (31 kurulu)
/opt/odoo/venv18-isg/ # ISG Python venv
/etc/odoo/odoo18-isg.conf # Config
/var/log/odoo/odoo18-isg.log # Log (hata yok)
https://github.com/SHapeloglu/ISG # Git (main, clean)

## Son Yapılanlar (Bu Oturum — B-10)

✅ **isg_training 2 Nisan 2026 Tam Uyum**
- Özel grup alanları (4 boolean)
- `last_working_date` (6 ay tetikleyicisi)
- `target_senior` (yaşlı 55+)
- 'basic' kategorisi (temel eğitim)
- Dönüş eğitimi 8 saat
- Bug fix: `action_create_return_training()` alan uyuşmazlığı
- Cron job: 6 ay uzak kalma → otomatik dönüş eğitimi

✅ **Mevzuat Doğrulaması**
- RG 33212 Md 5-7 (eğitim yönetmeliği) ✅
- Tekrar periyotu (36/24/12 ay) ✅
- BACKLOG.md hata düzeltildi (periyotlar doğruydu, BACKLOG yanlıştı)

## Sonraki Adım

**Competitive Gap Analysis** — HSE Radar ile kapsamlı karşılaştırma
- Kod/tasarım eklemek yerine **eksikleri listelemek** hedefi
- Mevzuat, UI/UX, entegrasyon, raporlama, performans boyutlarında
- **Çıkış:** Önceliklendirilmiş düzeltme listesi

Başlamaya hazır! 🚀
