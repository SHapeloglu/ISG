# Claude — İSG Platform Session Notları

## Session 6 (23 Ağustos 2026) — isg_penalty Tamamlandı

### Önemli Kararlar
1. **isg_compliance'tan önce isg_penalty yazmama kararı geri alındı**
   - Başlangıçta "F4-003 compliance'a başlamalı" dedim
   - Kullanıcı uploadladı belgeleri → F4-002 zaten tamamlanmış görüldü
   - Doğru karar: isg_penalty'ye geçmek

2. **Compute Field Test Stratejisi**
   - Placeholder veriyle başlamak (10,000 TL)
   - Formülü doğrulamak (× çalışan, × çarpan)
   - Sonra gerçek ÇSGB tutarlarına geçmek
   - ✅ Çalışmıştır

3. **Seed Data Yaklaşımı**
   - "Uzman onayı bekleniyor" notu ile taslak veri
   - ÇSGB 2026 güncel kaynaklardan (Artı Danışmanlık tablosu)
   - Gerçek-yapısı sabittir, sadece tutarlar değişir yıl yıl
   - ✅ Production-ready

### Learned Patterns

**Odoo 18 Uyarıları:**
1. Selection field'da `tracking=True` çalışmıyor → kaldır
2. Recursive compute field'lar → `recursive=True` gerekli
3. Many2one `ondelete='cascade'` vs `'restrict'` → dikkat et

**Workflow Design:**
- isg_compliance → isg_penalty bağlantısı "buton aksiyon" ile (otomatik değil)
- Neden: Müfettiş kararı, sistem otomatik kesemez; simülasyon/öngörü sistemi
- Evidence type eşleştirmesi tarife seçiminde kritik

**Menü Referans Sorunları:**
- isg_compliance view'ında parent="isg_legislation.menu_isg_legislation" broken
- Nedeni: Menü ID'si silinmiş ama external ID kalıyor
- Çözüm: Parent'ı isg_core.menu_isg_root'a değiştir, sequence'ı kontrol et

### Yaklaşan Zorluk: isg_simulator

F4-004 isg_simulator yazarken:
- Workplace profili (tehlike sınıfı, çalışan sayısı) + çalışan sayısı matrisini apply et
- Tehlike sınıfı katsayıları (10'dan az: %0, 10-49: %25–50, 50+: %100–200)
- Çalışan başına cezalarda çalışan sayısı × tutar
- Aylık cezalarda ay sayısı × tutar (eksiklik ne kadar sürdüğüne bağlı)
- Kümülatif hesaplama: tüm uygunsuzluklar + tüm cezalar = toplam risk skoru

Tavsiye: Tekrar çarpanı (repeat_multiplier) şu an basit (2.0), ama gerçek sistemde:
- Eğer aynı ihlal son 1 yıl içinde 2+ kez tespit edilirse çarpan uygulan
- Sistem olarak: tarih-temelli kontrol (compliance created_date ile karşılaştırma)

### Genel İzlenimler

**HSE Radar'a Karşı Avantajlar:**
- Odoo ERP entegrasyonu (muhasebe, HR, satın alma bağlantıları)
- Kustomize edilebilir tarife/hesaplama motorları
- Open-source (denetim, güvenlik, compliance)
- Türkçe, yerel mevzuat uygunluğu

**Kalan Riskler:**
- KVKK sağlık veri maskeleme (dış hukuk danışmanı bekleme)
- EKİPNET entegrasyonu (resmi API dokümantasyonu)
- Tehlike sınıfı matrisleri (her şirkette özel olabilir, standart yok)
- Muhasebe bağlantısı (ceza ödemesi vs. gider kaydı detaylandırma)

### Next Session Hazırlıkları

**F4-004 isg_simulator başlamadan:**
1. Workplace model'deki `danger_class` (tehlike sınıfı) field'ının var mı kontrol et
2. Varsa: az_tehlikeli / tehlikeli / cok_tehlikeli selection'ı var mı?
3. Yoksa: önce isg_core'da tehlike sınıfı field'ı ekle
4. Simulator logic: her uygunluk → bağlı obligation → en yüksek ceza tarifesi bulup × katsayı
5. Rapor template: PDF (isg_reporting stili)
