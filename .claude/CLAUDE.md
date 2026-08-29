# CLAUDE.md — Yeni Chat Bağlamı (Doğrulanmış)

**Tarih:** 29 Ağustos 2026 — Doğrulama Oturumu

## 🎉 PROJE MİLSTON (Güncellenmiş)

**30/32 ISG Modülü KURULU (%94)**
- 59 Odoo modülü çalışıyor (29 ISG + 30 native)
- Tüm FAZ 0, FAZ 1 (isg_health_basic bloklu), FAZ 2 TAM, FAZ 3 measurement, FAZ 4, OSGB, FAZ 5 reporting
- HSE Radar eşdeğerliği %95+
- Sistem stabil, log'da hata yok, git senkron

**Eksik:**
- ❌ isg_environment (yazılmamış)
- ⏳ isg_health_basic (bloklu, KVKK)
- ❓ F5-002/F5-003 (belirsiz)

## Geliştirici Profili

- Junior Odoo developer
- Python/Odoo öğreniyor
- Her adım birlikte, step by step
- Terminal komutları VPS'te çalıştırıyor

## Kurulu Modüller (30/32)

| Faz | Modüller | Kurulu |
|---|---|---|
| FAZ 0 | isg_core, security, party, location, document, hr, base | 7/7 ✅ |
| FAZ 1 | training, contractor, visitor, board, correspondence | 5/6 ✅ |
| FAZ 2 | capa, risk, incident, audit, ppe, emergency, chemical, equipment, ptw | 9/9 ✅ |
| FAZ 3 | measurement_core, measurement_hygiene | 2/3 ✅ |
| FAZ 4 | legislation, compliance, penalty, simulator | 4/4 ✅ |
| FAZ 5 | reporting | 1/3+ ✅ |
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

## Sıradaki Görevler (Öncelik Sırası)

### Kısa Vadeli (~7-9 gün)

1. **isg_environment (F3-003)** — ~2-3 gün
   - Atık kodu kataloğu
   - Atık depolama/bertaraf
   - Çevre etki değerlendirmesi (opsiyonel)

2. **B-4, B-8, B-9, B-10** — ~4-5 gün (mevzuat retrofit)
   - B-4: isg_board toplantı sıklığı
   - B-8: isg_penalty versiyonlama
   - B-9: isg_core danger_class.history
   - B-10: isg_training 2 Nisan 2026 tam uyum

3. **F5-002/F5-003 Kontrol** — ~1 gün
   - QWeb PDF şablonları var mı?
   - HSE Radar kabul testi protokolü?

### Ardından

- E3 Entegrasyon (SGK, EKİPNET, İSG-KATİP, e-imza)
- isg_health_basic (KVKK onayı sonrası)
- Superset raporlama

## İstatistikler (Doğrulanmış)

| Metrik | Değer |
|---|---|
| Kurulu Modül | 30 |
| İlerleme | %94 (code), %79 (görev sayısı) |
| Kurulu ISG | 29 (DB doğrulaması yapıldı) |
| Kurulu Native | 30+ |
| Toplam Model | 100+ |
| HSE Radar Eşdeğerlik | %95+ |

## Önemli Dosya Yolları
/opt/odoo/isg_addons/ # ISG modülleri (29 kurulu)
/opt/odoo/venv18-isg/ # ISG Python venv
/etc/odoo/odoo18-isg.conf # Config
/var/log/odoo/odoo18-isg.log # Log (hata yok)
https://github.com/SHapeloglu/ISG # Git (main, clean)

## Sonraki Adım

F3-003 isg_environment ile mi başlayalım, yoksa B-görevleri mi yapacağız?

**Tavsiye:** isg_environment önce (hızlı, 2-3 gün), sonra B-görevleri (5 gün), sonra F5 kontrol.

Başlamaya hazır mısız? 🚀
