# Session 6: F4-003 isg_penalty (23 Ağustos 2026)

## Başlangıç Durumu
- 26/32 modül yüklü (%81)
- F4-001 isg_legislation, F4-002 isg_compliance tamamlandı
- Sırada: F4-003 isg_penalty (İdari Para Cezaları — ÇSGB 2026)

## Tamamlanan İşler

### 1. isg_penalty Modülü Yazılması
- **2 Model:**
  - `isg.penalty.tariff` — Ceza tarife kataloğu (madde, tutar, çarpan, evidence_type)
  - `isg.penalty` — Fiili/olası ceza kaydı (compliance bağlantılı, otomatik tutar compute)
- **Otomatik Hesaplama:**
  - Formula: tarife tutarı × (çalışan başına uygulanırsa çalışan_sayısı) × tekrar_çarpanı
  - Compute field: `_compute_calculated_amount`
- **Workflow:**
  - `isg.compliance` formuna "Ceza Hesapla" butonu eklendi
  - Button action: `action_create_penalty()` metodu
  - Evidence type'tan otomatik tarife eşleştirmesi
  - Yeni penalty kaydı oluşturma, compliance'tan form açma

### 2. UI/UX
- List view: Badge statusbar (taslak/bildirildi/kesinleşti/ödendi)
- Form view: Genel ve ceza hesaplama alanları, statusbar
- Search view: Filtreleme (taslak, kesinleşti), grouping (işyeri, durum)
- Menü: "İdari Cezalar" → "Ceza Kayıtları" + "Ceza Tarifesi"

### 3. Seed Data (ÇSGB 2026)
6 tarife kaydı (temel tutarlar, %25.49 artışla):
1. Test Ceza (placeholder) — 10,000 TL
2. İSG Uzmanı Görevlendirmemesi (26/1-b) — 333,789 TL/ay
3. İşyeri Hekimi Görevlendirmemesi (26/1-b) — 333,789 TL/ay
4. Sağlık Gözetimi Eksikliği (26/1-f) — 22,194 TL/çalışan
5. Risk Değerlendirmesi Eksikliği (26/1-ç) — 133,329 TL
6. İSG Eğitimi Eksikliği (26/1-ğ) — 8,980 TL/çalışan

**Not:** Taslak veri, ÇSGB resmi kaynağından derlenmiş (Artı Danışmanlık 2026 tablosu).
Tehlike sınıfı katsayıları ve çalışan sayısı matrisinin modele eklenmesi ayrı bir adım (F4-003b).
Uzman onayı bekleniyor.

### 4. Sorun Çözümleri
- `isg_contractor` modülündeki `contractor_level` field'ına `recursive=True` eklendi (Odoo 18 uyarısı)
- `isg_penalty.status` field'ından `tracking=True` kaldırıldı (Selection field unsupported)
- `isg_compliance` view'daki parent menü referansları güncellendi (broken menu 230 referansı)

## Test Sonuçları
✅ Model yükleme
✅ Tarife kaydı oluşturma (form render, compute field test)
✅ Penalty kaydı oluşturma (compliance'tan buton tıkla, otomatik tutar hesaplama)
✅ Compute field doğrulama: 10,000 TL → 20,000 TL (tekrar çarpanı ile)
✅ Seed data yükleme

## Git Commit
- Commit: `bdd1f9f`
- Message: "F4-003: isg_penalty modülü (İdari Para Cezaları) — ÇSGB 2026"
- Files: 10 (models, views, security, data, manifest)

## Proje Durumu
**27/32 modül (%84)**
- FAZ 4 (Mevzuat/Uygunluk): 3/4 tamamlandı (F4-001, F4-002, F4-003)
  - Sırada: F4-004 isg_simulator (müfettiş simülasyonu)

## Sıradaki: F4-004 isg_simulator
**Amaç:** İşyeri profiline göre "müfettiş gelirse ne olur" simülasyonu.
- Input: workplace profil (tehlike sınıfı, çalışan sayısı, ölçüm sonuçları, eğitim kayıtları)
- Process: Tüm uygunluk değerlendirmeleri ve cezaları kümülatif hesaplama
- Output: Rapor (muhtemel ceza toplamı, risk alanları, iyileştirme önerileri)

## Notlar
- Oturum süresi: ~4 saat (model yazma, workflow kurma, UI test, Git)
- Odoo 18 karmaşıklık: Orta (3 sorun çözüldü — recursive field, tracking param, menü ref)
- Müfettiş workflow tamamlandı (legislation → compliance → penalty zinciri)
