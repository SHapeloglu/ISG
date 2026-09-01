# ARCHITECTURE.md — Mimari ve Tasarım Kararları (01 Eylül 2026 — B-9 Tamamlandı)

**Güncelleme:** 01 Eylül 2026 — 31/32 modül kurulu, B-4/B-8/B-9 tamamlandı, MEV-002 başlanacak

[önceki içeriği koruyoruz, sadece sonunda kısım güncelleyelim]

...

## Son Yapılanlar (Bu Oturum — B-9)

✅ **B-4: isg_board toplantı sıklığı**
- danger_class string bug fix ('very_dangerous' → 'high')
- Çok tehlikeli: 15 gün, diğer: 1 ay

✅ **B-8: isg_penalty versiyonlama**
- valid_from alanı (tarifesi sürüm geçmişi)
- Geçmiş tarihli simülasyonda doğru tarifeler
- 2026 %49 ceza artışı versiyonlanabilir

✅ **B-9: isg_core danger_class.history**
- isg.workplace.danger_class.history modeli oluşturuldu
- @onchange('danger_class') ile otomatik history kaydı
- Geçmiş uyunluk kontrolü desteği

---

## Sonraki Seans

**MEV-002: isg_equipment — Ara.2025 EK-II Güncellemesi**
- Ekipman kataloğu (kompresör, vinç, asansör, forklift, platform...)
- e-imza desteği (5070 s.K.)
- EKİPNET bildirim hazırlık alanları
- Periyodik kontrol raporu form

Tahmini süre: 3-5 gün
