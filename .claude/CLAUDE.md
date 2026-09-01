# CLAUDE.md — Yeni Chat Bağlamı (01 Eylül 2026 — B-9 Tamamlandı, MEV-002 Başlangıç)

**Tarih:** 01 Eylül 2026 — B-4/B-8/B-9 tamamlandı, gap analysis hazırlandı, MEV-002 başlanacak

## 🎉 PROJE MİLSTON (Güncellenmiş)

**31/32 ISG Modülü KURULU (%97)**
- 58 Odoo modülü çalışıyor (31 ISG + 27 native)
- Tüm FAZ 0, FAZ 1 (isg_health_basic bloklu), FAZ 2 TAM, FAZ 3, FAZ 4, OSGB, FAZ 5 (reporting)
- **HSE Radar eşdeğerliği %96-97** (full eşdeğerlik için 25-35 gün)
- Sistem stabil, log'da hata yok, git senkron

**3 B-Görev Tamamlandı:**
- ✅ B-4: isg_board danger_class bug fix
- ✅ B-8: isg_penalty valid_from versiyonlama
- ✅ B-9: isg_core danger_class.history modeli

**Gap Analysis Raporu Hazırlandı:**
- 4 bölüm operasyonel format
- MEV- boşlukları detaylandırılmış
- Top 10 Düzeltme Listesi (sıralanmış, adam-gün tahminli)

## Geliştirici Profili

- Junior Odoo developer
- Python/Odoo öğreniyor
- Her adım birlikte, step by step
- Terminal komutları VPS'te çalıştırıyor

## Kurulu Modüller (31/32)

| Faz | Modüller | Kurulu |
|---|---|---|
| FAZ 0 | isg_core, security, party, location, document, hr, base | 7/7 ✅ |
| FAZ 1 | training (**✅ B-10**), contractor, visitor, board, correspondence | 5/6 ✅ |
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

### HEMEN BAŞLANACAK (~3-5 gün)

**MEV-002: isg_equipment — Ara.2025 EK-II Güncellemesi**
- Ekipman kataloğu: kompresör, vinç, asansör, baskı kapı, forklift, platform, kaldırma cihazları
- Periyodik kontrol periyodu (6 ay / 1 yıl / vb.) ve yöntem
- e-imza desteği (5070 s.K.)
- EKİPNET sözleşme onayı + bildirim hazırlık
- Kontrol sonucu rapor ve uyarı sistemi
- Mevzuat: İş Ekipmanları Yönetmeliği (Ara.2025 güncellendi)

### İkinci Hafta (~3-5 gün)

**isg_incident — SGK Bildirimi + Dönüş Eğitimi**
- Kaza kaydı (state machine)
- SGK 3 iş günü bildirimi uyarısı
- Otomatik dönüş eğitimi tetikleyicisi (isg_training ile link)

**isg_audit — Denetim Motoru**
- Bulgu kaydı (finding model)
- Weight-based compliance scoring
- Tekrarlanan bulgu escalation (3+ tekrar)

### Üçüncü Hafta (~2-4 hafta)

- isg_ppe, isg_chemical, isg_ptw (paralel yapılabilir)
- MEV-008 (risk bilgilendirmesi) + isg_emergency (küçük fixler)
- F5-002/F5-003 (doğrulama)

### Bloklu

- **isg_health_basic** — KVKK danışman onayı bekleniyor (F1-002)

## İstatistikler (Doğrulanmış)

| Metrik | Değer |
|---|---|
| Kurulu Modül | 31/32 (%97) |
| İlerleme | %97 (modül), %96-97 (HSE Radar eşdeğerlik) |
| Kurulu ISG | 31 |
| Kurulu Native | 28 |
| Toplam Model | 105+ |
| HSE Radar Eşdeğerlik | %96-97 |
| Full Eşdeğerlik İçin | 25-35 gün |
| Commit Sayısı | 40+ |

## Önemli Dosya Yolları
/opt/odoo/isg_addons/ # ISG modülleri (31 kurulu)
/opt/odoo/venv18-isg/ # ISG Python venv
/etc/odoo/odoo18-isg.conf # Config
/var/log/odoo/odoo18-isg.log # Log (hata yok)
https://github.com/SHapeloglu/ISG # Git (main, clean)

## Son Yapılanlar (Bu Oturum — B-9 Tamamlandı)

✅ **B-4: isg_board danger_class bug fix**
- String hatası: 'very_dangerous' → 'high'
- Toplantı sıklığı: çok tehlikeli 15 gün, diğer 1 ay

✅ **B-8: isg_penalty versiyonlama**
- valid_from alanı (tarifesi sürüm geçmişi)
- Geçmiş tarihli simülasyonda doğru tarifeler

✅ **B-9: isg_core danger_class.history**
- isg.workplace.danger_class.history modeli
- Otomatik history kaydı (@onchange)
- Geçmiş uyunluk kontrolü desteği

✅ **Gap Analysis Raporu**
- 4 bölüm, operasyonel format
- MEV-002 (EK-II) en kritik
- Top 10 Düzeltme Listesi hazırlandı

## Sonraki Adım

**MEV-002: isg_equipment — Ara.2025 EK-II Güncellemesi**
- Skeleton var, implementasyon yapılacak
- Ekipman kataloğu + periyodik kontrol form
- e-imza + EKİPNET alanları
- Tahmini: 3-5 gün

Başlamaya hazır! 🚀
