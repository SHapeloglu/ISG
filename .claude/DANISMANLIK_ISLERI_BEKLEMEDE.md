# DANIŞMANLIK İŞLERİ — BEKLEMEDE (Bütçe Onayı Gerekli)

**Durum:** Tüm maddeler ₺300K Faz 1 bütçe onayına bağlı. Onay gelene kadar bu listeye AKTİF olarak dokunulmuyor, sadece referans olarak tutuluyor.
**Son güncelleme:** 17 Eylül 2026

---

## 🔴 KRİTİK (Bütçe onaylanır onaylanmaz ilk sırada)

### D1. KVKK Danışmanı — isg_health_basic Hukuki Onayı
- **Durum:** Teknik iş TAMAMLANDI (Seans 12: encryption + audit log). Sadece hukuki sign-off bekliyor.
- **Kapsam:** Field encryption + role-based access + audit logging'in KVKK uyumluluğu incelemesi, DPA template onayı, hukuki tasdik belgesi
- **Bütçe:** ₺10-15K
- **Süre:** 2-3 hafta
- **Not:** Teknik hazırlık bitti, bu bir formalite değil — hukuki risk gerçek, atlanamaz

### D2. İSG Uzman Danışmanlığı — Mevzuat Audit
- **Kapsam:** 6331 + tüm yönetmelikler uyum incelemesi, 27 işlev karşılaştırma tablosu, mevzuat uyum matrisi (100+ satır)
- **Bütçe:** ₺50-60K
- **Süre:** 6 hafta

### D3. Avukat Mütalaa (Hukuki Tasdik)
- **Kapsam:** 6331 uyumluluğunun hukuki tasdiki, 10-15 sayfa mütalaa
- **Bütçe:** ₺40-50K
- **Süre:** 5 hafta

---

## 🟡 YÜKSEK ÖNCELİK (Faz 1 içinde, kritikten sonra)

### D4. 3 OSGB Tasdik Konsorsiyumu
- **Kapsam:** İstanbul/Ankara/İzmir OSGB'lerden 30 gün demo + yazılı tasdik belgesi
- **Bütçe:** ₺8K
- **Süre:** 8 hafta

### D5. OEL/STEL ÇSGB Resmi Doğrulama (İmza)
- **Not:** Karşılaştırma script'i biz hazırlıyoruz (bkz. BACKLOG.md #6), burada sadece resmi imza/danışman onayı kalıyor
- **Bütçe:** ₺5K
- **Süre:** 2 hafta

### D6. Sertifikasyon Raporu + Mevzuat Matrix (Web)
- **Kapsam:** Danışman + OSGB + Avukat bulgularının sentezi, basılı + web sertifika
- **Bütçe:** ₺17K (sertifika + matrix + web)
- **Süre:** 2-3 hafta (diğerleri bitince)

---

## 🟢 ORTA/DÜŞÜK ÖNCELİK (Faz 2, daha sonra)

### D7. MEV-010: 21 Ocak 2026 Ulusal Konsey Yönetmeliği Etkisi
- **Kapsam:** isg_board'a etkisinin hukuki teyidi
- **Süre:** 0.5 gün tasarım + hukuki görüş

### D8. SGK E2 Entegrasyonu (İş Kazası Bildirimi API)
- **Kapsam:** SGK API credentials, 3 gün otomatik bildirim, retry logic
- **Bütçe:** ₺25-30K
- **Süre:** 8 hafta
- **Bağımlılık:** Müşteriden SGK API credentials gerekli

### D9. EKİPNET E3 Entegrasyonu (Ekipman Muayene API)
- **Kapsam:** Real-time ekipman muayene bildirimi
- **Bütçe:** ₺20-25K
- **Süre:** 8 hafta

### D10. E-imza Implementasyonu (5070 s.K.)
- **Kapsam:** isg_document'te gerçek OpenPGP/X.509 e-imza (şu an sadece framework var)
- **Bütçe:** ₺30-40K (kompleks, sertifika yönetimi)
- **Süre:** 5-7 gün

---

## 💰 Bütçe Özeti (Scenario B — Önerilen)

| Kalem | Bütçe |
|---|---|
| İSG Uzman Danışmanlığı | ₺60K |
| OSGB Konsorsiyum (3) | ₺8K |
| Hukuki Danışmanlık | ₺45K |
| Sertifikasyon + Matrix | ₺17K |
| Yönetim & Koordinasyon | ₺20K |
| **TOPLAM (Faz 1 danışmanlık)** | **~₺150K** |

E2/E3 entegrasyonu ve e-imza (D8-D10) bu tutara dahil değil, Faz 2 için ayrı değerlendirilecek (~₺75-95K ek).

## 📌 Ne Zaman Aktif Hale Gelir?
Bütçe onayı geldiğinde:
1. D1 (KVKK sign-off) ilk sırada — teknik iş zaten hazır, sadece bekliyor
2. D2 + D3 paralel başlatılabilir
3. D4 (OSGB) paralel, düşük bütçe/uzun süre
4. D5-D6 diğerleri bitince
5. D7-D10 Faz 2'de ayrıca değerlendirilir

## 🔗 Kaynak Dosyalar (proje geçmişinden, referans)
- `A_DANISMANLIK_VE_ONAYLA_R_PAKETI.md` — detaylı paket dökümü
- `DANISMANLIK_IS_LISTESI.md` — danışman iletişim/procurement detayları
- `EXECUTION_MASTER_PLAN.md` — tam faz planı (₺591K, 20 hafta, daha geniş kapsam)
