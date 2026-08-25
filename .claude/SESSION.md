# SESSION.md — Oturum Özeti ve Devam Noktası

## Son Oturum: 25 Ağustos 2026

### Tamamlanan İşler (Bu Oturum)

**B-1 `isg.rate.table` Modeli (isg_core içinde):** ✅ TAMAMLANDI
- İSG Uzman/Hekim süre katsayılarını (danger_class × role → dakika) versiyonlu, ortak tabloya taşındı
- Model: `isg.rate.table` (danger_class, role, minutes_per_employee, valid_from, active)
- get_rate() metodu: verilen tarihte geçerli katsayıyı döndürür
- Seed data (XML): 6 kayıt (2025-01-01 geçerlilik tarihi ile)
  - Uzman: 10/20/40 dk (az/medium/high)
  - Hekim: 4/6/15 dk (az/medium/high)
- isg_workplace.py güncellenmiş: compute metodları tablodan katsayı okuyor
- ACL: isg_rate_table user/manager kayıtları eklendi
- Commit: B-1 (25 Ağustos 2026)

### Proje İlerleme

**29/32 Modül (%90.6) — İlaveten B-1 tamamlandı**

### Kurulu Modüller (57 toplam, 29 ISG)

Mevcut + B-1 tarafından etkilenen:
- isg_core (isg_rate_table eklendi)

### Sıradaki Görevler

1. **B-2: isg_contractor** — İşyerine Özgü Risk Bilgilendirmesi belge türü (~0.5 gün)
2. **B-3: isg_visitor** — risk_briefing alanları (~0.5 gün)
3. **isg_osgb** — OSGB Planlama/Görevlendirme (isg_rate_table'dan okuyacak)

Alternatif: Öncelik karşılaştırması için BACKLOG.md'e bakın.

### Belgeleri Güncelle ve Push Et

```bash
git add -A
git commit -m "B-1: isg.rate.table modeli tamamlandı (uzman/hekim süre katsayıları)"
git push origin master
```

### Geliştirici Notu

B-1, isg_osgb'nin ön koşulu — isg_osgb başlamadan önce yapılması gerekiyordu. Tamamlandı.
