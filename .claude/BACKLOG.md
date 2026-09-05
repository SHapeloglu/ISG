# BACKLOG.md — Seans 5 (05 Eylül 2026)

## 🎯 ÖNCELİKLİ (Seans 5+)

### F5-003 — HSE Radar Kabul Testi (1-2 gün)
**Status:** 🔄 Sırada  
**Neden:** HSE Radar eşdeğerliğinin %100'e ulaşması için son parça

**Test Planı:**
- [ ] 27 işlev × 5 senaryo = 135 test case
- [ ] Normal akış testleri
- [ ] Olumsuz akış testleri (error handling)
- [ ] Yetkisiz erişim testleri (ACL)
- [ ] Çok şirket/işyeri/site testleri
- [ ] PDF raporlarının render edilmesi
- [ ] Log kontrolü (ERROR 0)

### isg_tests — Test Framework Cleanup (1-2 gün)
**Status:** ⏳ Bekleme  
**Neden:** TransactionCase testleri alan validation sorunlarında takıldı

**Yapılacak:**
- [ ] Tüm 7 modülün alanlarını doğrula
- [ ] test_isg_core, test_isg_incident, test_isg_audit vb. fix et
- [ ] Tüm testleri `--test-enable` ile çalıştır
- [ ] CI/CD hazırlığı (GitHub Actions)

---

## 📋 SONRASI (2-4 hafta)

### E2/E3 Entegrasyon (İsteğe Bağlı)
- [ ] SGK bildirimi API
- [ ] EKİPNET dosya yükleme
- [ ] KVKK maskeleme (isg_health_basic)
- [ ] E-imza (5070 s.K., MEV-006)

---

## ✅ BLOKLU

- isg_health_basic (KVKK danışman onayı)

---

## İlerleme

| Faz | Tamamlanan | % |
|-----|-----------|---|
| FAZ 0-4 | 26/30 | 87 |
| FAZ 5 | 2/3 | 67 |
| **TOPLAM** | **28/33** | **85** |

**Adam-Gün:** ~65/80 tamamlandı (%81)

**Tarih:** 05 Eylül 2026, 19:38 UTC
