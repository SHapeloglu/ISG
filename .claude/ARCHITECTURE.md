# ARCHITECTURE.md — Mimari ve Tasarım Kararları (31 Ağustos 2026 — B-10 Tamamlandı)

**Güncelleme:** 31 Ağustos 2026 — 31/32 modül kurulu, isg_training_scheduler eklendi

## Genel Mimari
Odoo 18 ERP (base, mail, hr, account, stock, 30+)
↓
isg_core (Workplace/Site, isg.rate.table)
↓
FAZ 0: Güvenlik + Yönetişim (7/7 ✅)
↓
FAZ 1: Kurumsal (5/6 ✅ isg_health_basic bloklu)
│ ✅ isg_training — B-10 tamamlandı (2 Nisan 2026 uyum)
│
FAZ 2: Operasyonel (9/9 ✅ TAM)
capa, risk, incident, audit, ppe, emergency, chemical, equipment, ptw
↓
OSGB: İşyeri-uzman planlama (1/1 ✅)
↓
FAZ 3: Ölçüm (3/3 ✅ TAM)
measurement_core, measurement_hygiene, environment
↓
FAZ 4: Sanal Müfettiş (4/4 ✅ TAM)
legislation, compliance, penalty, simulator
↓
FAZ 5: Raporlama (1/3 ✅)
reporting (TRIR/LWDR KPI, PDF pending)

## Tasarım Kararları (Kritik)

### 1. Snapshot Mimarisi (isg_compliance) ✅

Uyunluk değerlendirmesi tarihe bağlı freezelanmış:
- evaluation_date: Ne zaman değerlendirildi?
- obligation_version: Hangi mevzuat sürümü?
- status: O tarihte uyumlu mu?

**Faydası:** 100% audit trail — 2 ay sonra rapor tekrar üretilebilir, aynı sonuç gelir

### 2. isg.rate.table Merkezileştirmesi ✅

Tüm uzman/hekim dakika katsayıları tek tabloda:
- danger_class → minutes_per_employee_per_month
- role (uzman/hekim)
- fulltime_threshold (kaç çalışanda tam zamanlı?)
- valid_from (sürüm geçmişi — B-8'de eklenecek)

**Kullanan:** isg_workplace, isg_osgb, isg_hr

### 3. isg_osgb.assignment Aylık Uygunluk ✅

OSGB'nin atadığı uzmanın aylık dakika yeterliliği:
- monthly_required_minutes (isg.rate.table'dan otomatik)
- monthly_actual_minutes (uzmanın ziyaret süresi)
- compliance_status: GREEN (≥90%), YELLOW (75-89%), RED (<75%)

**Faydası:** OSGB hangi müşterilerine tam hizmet veriyor, kapasite takibi

### 4. isg_incident SGK Bildirimi ✅

Kaza kaydında SGK bildirimi otomatik:
- sgk_notification_required (injury_type != none)
- sgk_notification_deadline (3 iş günü, weekendler hariç)
- sgk_status: RED (geçti), YELLOW (<1 gün), GREEN (ok)

**Tetikleyici:** state=resolved → otomatik dönüş eğitimi (B-10 ✅ tamamlandı)

### 5. isg_audit Puanlama ✅

Weight-based scoring:
- total_weight: Tüm kontrol maddelerinin toplam ağırlığı
- achieved_weight: Uygun bulunduğunun toplam ağırlığı
- compliance_percentage: (achieved / total) * 100
- compliance_status: GREEN (≥90%), YELLOW (70-89%), RED (<70% veya kritik bulgu varsa)

**Kritik Bulgu Kuralı:** Tek bir kritik madde UYGUNSUZ ise, genel % kaç olursa olsun RED

### 6. isg_audit.finding Tekrarlanan Bulgu ✅

Bulgu lifecycle:
- repeat_count: Kaç kez tekrar?
- escalation_level: repeat ≥ 3 ise level 2 (yönetim raporunda çıkarsın)
- finding_type: observation, non_conformity, major, critical
- state: open → in_review → resolved → verified → closed
- capa_id: DÖF bağlantısı
- evidence_attachment_ids: Kanıt dosyaları

### 7. isg_training Scheduler (B-10 ✅ TAM)

**Dönüş Eğitimi Tetikleyicisi:** 6 ay işten uzak kalma → otomatik eğitim kaydı

- `isg.training.scheduler` modeli (singleton, cron runner)
- `ir.cron` kaydı — her gece 2'de çalışır
- `action_process_return_training()` — 6 ay öncesi `last_working_date` olan çalışanları bulup eğitim kaydı oluştur
- `isg_training.type.return` — seed data (min 8 saat, RG 33212 Md 7)
- Bug fix: `isg_incident.action_create_return_training()` — alan uyuşmazlığı düzeltildi

**Mevzuat:** RG 33212 Md 7 — 6 aydan fazla işten uzak kalanlara dönüş eğitimi zorunlu

### 8. Unidirectional Dependency Chain ✅

Hiçbir modül arkaya dönerek diğerini import etmez. Sadece yukarıya bağımlılık:
isg_core ← isg_hr ← isg_training, isg_contractor
isg_legislation ← isg_compliance ← isg_penalty ← isg_simulator
isg_incident → isg_capa (DÖF oluşturma) → isg_training (dönüş eğitimi)
isg_audit → isg_audit.finding → isg_capa

**Faydası:** Deployment sırası net, circular import yok

### 9. ACL Stratejisi ✅

3 rol grubu (isg_security):
- readonly: Raporlar, dashboard (okuma)
- expert: İSG Uzmanı (okuma-yazma, yeterli yetkiler)
- physician: İşyeri Hekimi (sağlık verisi — bloklu)
- manager: Tam kontrol (yaşam döngüsü, onay, silme)
- superadmin: Sistem yönetimi

### 10. Sequence İsimlendirmesi ✅

| Model | Prefix | Örnek |
|---|---|---|
| isg_risk | ISG-HZR- | ISG-HZR-2026-0001 |
| isg_incident | ISG-KZA- | ISG-KZA-2026-0042 |
| isg_capa | ISG-DOF- | ISG-DOF-2026-0015 |
| isg_audit | ISG-DNT- | ISG-DNT-2026-0008 |
| isg_audit.finding | ISG-BLG- | ISG-BLG-2026-0089 |
| isg_training | ISG-EGT- | ISG-EGT-2026-0123 |

---

## Modül Bağımlılıkları (Güncellenmiş)
isg_core (temel)
├─ isg_security (rol + ACL)
├─ isg_party, isg_location, isg_document
├─ isg_hr (employee _inherit)
├─ isg_base (uuid.mixin, outbox)
│
├─ F1 Serisi (training ✅, contractor, visitor, board, correspondence)
│ └─ isg_capa (DÖF)
│ ├─ isg_risk
│ ├─ isg_incident → isg_training (dönüş eğitimi ✅)
│ ├─ isg_audit
│ ├─ isg_ppe, isg_emergency, isg_chemical
│ ├─ isg_equipment, isg_ptw
│
├─ isg_osgb (rate.table kullanır)
│
├─ isg_legislation → isg_compliance → isg_penalty → isg_simulator
│
├─ isg_measurement_core + isg_measurement_hygiene
│ └─ isg_environment
│
└─ isg_reporting (TRIR/LWDR KPI)

---

## Veri Saklama

### Sağlık Verisi (isg_health_basic — Bloklu, KVKK)

⚠️ Özel nitelikli kişisel veri — KVKK danışman onayı bekliyor

Alanlar:
- medical_history, diagnosis, medications — `groups='isg_security.group_isg_physician'`
- restrictions — herkes görsün (yapılabilir/yapılamaz)
- consent_date (KVKK rıza)
- consent_revoked_date (rıza çekilirse veri silinir)

### İş Kazası (isg_incident) — Açık

- workplace_id, incident_type, incident_description — herkes görür
- injured_employee_id — sadece expert/manager (record rule)
- sgk_notification_deadline — otomatik hesap

### Eğitim Kaydı (isg_training.record) — B-10 ✅

- Tüm eğitim kayıtları erişilebilir (iç kontrol için)
- Dönüş eğitimi: `state='draft'` (onaylanmayı bekler)
- Attendee'ler otomatik bağlanır (bug fix ile)
- Periyot `next_training_date` otomatik hesaplanır

---

## Test Stratejisi

1. **Birim:** create/read/update/delete her modülde
2. **Entegrasyon:** workflow'lar (state machine)
3. **Mevzuat:** obligation matching (50+ senaryo)
4. **UI:** form render, list, action buttons
5. **Performans:** 1000 record bulk test (FAZ 5 sonrası)
6. **Cron:** Scheduler tetikleyicileri (dönüş eğitimi, penalty versiyonlama vb.)

---

## Git Strategy

- **Repository:** https://github.com/SHapeloglu/ISG
- **Branch:** main (protected)
- **Commit format:** `[görev]: açıklama`
- **Örnek:** `[B-10] isg_training 2 Nisan 2026 uyum: özel gruplar, dönüş eğitimi bug fix`

---

## Kritik Noktalar

🟢 **Tamamlanan (B-10):**
- ✅ isg_training (2 Nisan 2026 mevzuat uyumu)
- ✅ Dönüş eğitimi tetikleyicisi (6 ay kuralı)
- ✅ isg_incident bug fix (alan uyuşmazlığı)

🔴 **KVKK:** isg_health_basic hâlâ bloklu — danışman onayı gerekir

🟡 **Mevzuat Retrofit:** B-4/B-8/B-9 (~2-3 gün)

⚠️ **Raporlama:** F5-002/F5-003 doğrulama pending

---

## Gelecek Mimari (E2/E3)

**E2:** Superset entegrasyon, Flutter mobil, multi-company optimization

**E3:** SGK API, EKİPNET, İSG-KATİP, e-imza (5070 s.K.), VERBİS uyumu

**E4:** Risk tahminlemesi (ML), anomali tespiti, uyum önerme

---

## Sonraki Seans

**Competitive Gap Analysis** — HSE Radar ile kapsamlı karşılaştırma
- Mevzuat kapsam (hangi yönetmelikleri kaçırıyor?)
- UI/UX deneyimi (form layout, workflow, navigation)
- Entegrasyon (ERP, SGK, KVKK, e-imza)
- Raporlama (HSE Radar'ın en zayıf yanı — burada geçebiliriz)
- Performans (hacim, load testing)
- **Çıkış:** Önceliklendirilmiş düzeltme listesi
