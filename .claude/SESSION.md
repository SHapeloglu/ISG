# SESSION.md — Oturum Özeti

## Son Oturum: 14 Ağustos 2026 (Uzun Oturum — 5 Modül)

### Tamamlanan Modüller

**F2-002 `isg_risk`** ✅
- Risk değerlendirmesi (6 durum: draft→in_progress→done→approved→renewal→archived)
- L Matrisi (5x5) + Fine-Kinney (Kinney-Wiruth standart)
- Kalıntı risk takibi, otomatik yenileme tarihi (tehlike sınıfına göre +2/4/6 yıl)
- DÖF entegrasyonu (yüksek risk satırında otomatik isg.capa açılır)
- Sequence: ISG-RD-YYYY-NNNN

**F2-003 `isg_incident`** ✅
- İş kazası / ramak kala / meslek hastalığı kaydı
- 6331 md.14 SGK 3 iş günü bildirim takibi (otomatik hesaplanan deadline)
- DÖF bağlantısı
- Sequence: ISG-KZ-YYYY-NNNN

**F2-004 `isg_audit`** ✅
- Denetim şablonu (isg.audit.template + question) — sorular kategorize edilmiş
- Denetim kaydı (isg.audit + line) — ok/nok/na/obs sonuçları
- Şablon → denetim satırı yükleme fonksiyonu
- Kritik madde uygunsuzsa otomatik DÖF açılır
- Sequence: ISG-DNT-YYYY-NNNN

**F2-006 `isg_emergency`** ✅
- Acil durum planı (isg.emergency.plan) — toplanma noktaları, acil durum türleri, ekip
- Tatbikat kaydı (isg.emergency.drill) — tatbikat türü, tahliye süresi, sonuç
- Durum makinesi: planned → done → cancelled
- Sequence: ISG-ADP-YYYY-NNNN (plan), ISG-TAT-YYYY-NNNN (tatbikat)

**F2-005 `isg_ppe`** ✅
- KKD türü (isg.ppe.type) — 18 standart KKD türü verisi: baret, eldiven, gözlük, ayakkabı, tulum vb.
- KKD stok (isg.ppe.stock) — işyeri bazlı stok, minimum seviye, kritik stok uyarısı
- Zimmet kaydı (isg.ppe.issue) — çalışana KKD zimmet, otomatik yenileme tarihi (ömrü × ay), iş_hr beden ölçüleri otomatik önerisi
- Durum makinesi: issued → returned / expired / lost
- Sequence: ISG-KKD-YYYY-NNNN
- **Önemli:** isg_hr ile entegrasyon — çalışanın `ppe_clothing_size` (Selection), `ppe_shoe_size` (Char), `ppe_glove_size` (Selection) alanları zimmet formunda gösterilir

### Kurulu Modüller (47 toplam)

**ISG Modülleri (20):**
isg_core, isg_security, isg_party, isg_location, isg_document,
isg_hr, isg_base, isg_training, isg_contractor, isg_board,
isg_correspondence, isg_visitor, isg_capa,
isg_risk, isg_incident, isg_audit, isg_emergency, isg_ppe,
hr_skills, (+ 2 diğer)

### Bilinen Teknik Konular

1. **isg_contractor contractor_level** — recursive=True eklenmeli (SESSION'da not: recursive=True bug)
2. **isg_location hazard_type** — unknown parameter 'invisible' WARNING (işlevsel değil, view yükselmesi gerekiyor)
3. **isg_ppe.type.size_type** — unknown parameter 'invisible' WARNING (işlevsel değil, view yükselmesi gerekiyor)
4. **isg_health_basic** — KVKK danışman onayı bekliyor
5. **isg_risk_line record rule eksik** — çapraz-şirket izolasyonu yok
6. **GitHub SSH setup** — password authentication başarısız, SSH key gerekli
7. **Admin şifresi** — PostgreSQL NULL yapıldı, kalıcı şifre belirlenmeli

### Kaldığımız Yer

- Bugün 5 modül tamamlandı (**Hızlı İlerleme**)
- Sıradaki: **F2-007 `isg_chemical`** — Kimyasal envanter (OEL/STEL tablosu, depolama matrisi)
- GitHub push başarısız (SSH key needed)
- Lokal commit'ler başarılı, sonraki oturumda SSH setup + push

### Seçilmiş Tasarım Kararları

- **Fine-Kinney:** Standart Kinney-Wiruth skalası (0.2–10 prob, 0.5–10 freq, 1–100 sev) — HSE Radar paritesi için
- **Risk Seviyeleri:** L Matrix (acceptable/low/medium/high/intolerable), FK (aynı 5 seviye, farklı eşikler)
- **Otomatik Computeler:** renewal_date, expiry_date, effective_danger_class, line_stats — tümü store=True
- **KKD Verisi:** 18 standart CE uyumlu türü (baret, eldiven, gözlük, ayakkabı, tulum vb., ömürleri spec'lenmiş)
- **DÖF Entegrasyonu:** risk_assessment + audit + incident → isg.capa source seçeneği genişletildi

### Hata Düzeltme Süreci Bu Oturumda

1. isg_risk — önceki taslak hatalı (`source='risk'` geçersiz, `UserError` import yok, seçenek belgesiz) → sıfırdan yazıldı
2. isg_capa_ext — ondelete='set default' hatasında cascade'e değiştirildi (base field'ın default'u yoktu)
3. isg_ppe_issue — related alanlar Selection tanımlanırken Char'ı Selection'a çevirildi (isg_hr tip uyuşmazlığı)

### Proje Durumu

- **Tamamlanan:** FAZ 1 (governance) +  FAZ 2 ilk 5 modülü (risk, incident, audit, emergency, ppe)
- **İlerleme:** ~60% FAZ 2 (32 modülün 5'i = 16%, F2 başında 32 modül planı vardı)
- **VPS Durumu:** 47 modül kurulu, 20 ISG modülü aktif, servis stabil
- **Sıradaki (Öncelik):** F2-007 chemical (karmaşık), F2-008 equipment, F2-009 ptw+loto

### Session Özeti

Bu oturum dikkat çekici hızlı ilerleme kaydetti: 5 modülü başarıyla tamamladı ve GitHub'a commit etti (push SSH setup bekliyor). Sistemdeki en sık hata modeli: önceki taslakların yanlış tanımlanmış field'ları (type mismatch, eksik import, geçersiz parameter). Her modülde VPS'te `ls`/`cat` ile doğrulama yapıldı, SESSION.md'ye bilinen sorunlar eklendi.

