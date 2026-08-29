# ARCHITECTURE.md — Mimari ve Tasarım Kararları

**Güncelleme:** 29 Ağustos 2026 — 32/32 modül kurulu + F2-004 isg_audit 95%

---

## Genel Mimari
Odoo 18 ERP Altyapısı (İK, Muhasebe, Satın Alma, CRM)
↓
isg_core (Workplace/Site hiyerarşisi, isg.rate.table)
↓
FAZ 0-1 (Güvenlik, Yönetişim)
isg_security, isg_party, isg_training, isg_contractor,
isg_board, isg_correspondence, isg_visitor
↓
FAZ 4 — Sanal Müfettiş (Çekirdek DNA)
isg_legislation, isg_obligation, isg_compliance, isg_penalty, isg_simulator
↓
FAZ 2 (Operasyonel Modüller — Kısmen Sırada)
isg_risk ✅, isg_capa ✅, isg_incident ✅
isg_audit ✅ (puanlama + bulgu lifecycle)
isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw+loto (sırada)
↓
OSGB Planlama (isg_osgb) ✅
İşyeri-uzman atama, aylık dakika uygunluğu, kapasite planlama
(isg.rate.table entegre)
↓
FAZ 3 (Ölçüm/Çevre — Sırada)
isg_measurement_core, isg_measurement_hygiene, isg_environment
↓
FAZ 5 (Raporlama — Sırada)
isg_reporting, Superset, TRIR/LWDR KPI

---

## Tasarım Kararları (Kritik)

### 1. isg_compliance "Snapshot" Mimarisi ✅
Uygunluk değerlendirmesi tarihe bağlı olarak depolanır.
- **Gerekçe:** Audit trail, versiyonlu mevzuat, geçmiş tarihli hesaplar
- **Sonuç:** 100% audit-grade → kasa açılan her rapor tekrar üretilebilir

### 2. isg.rate.table Merkezileştirme ✅
Uzman/hekim dakika katsayıları isg_core'da tek tablo.
- **Kullanan:** isg_workplace + isg_osgb
- **Versiyonlanmış:** valid_from (geçmiş tarihli hesaplar için)

### 3. isg_osgb.assignment Aylık Uygunluk ✅
İşyeri-uzman atamasında aylık dakika uygunluğu otomatik hesaplanır (%90 tolerans).
- **Compute:** monthly_required_minutes (isg.rate.table'dan) vs. monthly_actual_minutes
- **Durum:** compliant / warning / non_compliant (badge)

### 4. isg_incident SGK Bildirimi ✅
Kaza kaydında SGK bildirimi gerekli mi, 3 iş günü deadline nedir otomatik hesaplanır.
- **Compute:** sgk_notification_required, sgk_notification_deadline
- **Uyarı:** sgk_days_remaining < 0 → RED badge
- **Dönüş Eğitimi:** state=resolved → otomatik isg_training.record oluştur

### 5. isg_audit Puanlama & Bulgu Lifecycle ✅
Denetim sisteminde weight-based scoring ve bulgu lifecycle.
- **Puanlama:** total_weight, achieved_weight, compliance_percentage (0-100%), compliance_status (GREEN/YELLOW/RED)
- **Kritik Bulgu:** Tek bir kritik bulgu RED status'a yükseltir (genel % kaç olursa olsun)
- **Bulgu Lifecycle:** open → in_review → resolved → verified → closed
- **Tekrarlanan Bulgu:** repeat_count ≥ 3 → escalation_level = 2 (yönetim raporuna çık)
- **Kanıt:** ir.attachment desteği (fotoğraf, dokümantasyon)
- **Alt İşveren:** contractor_id FK (aynı model hem işyeri hem contractor denetleyebilir)

### 6. Unidirectional Dependency Chain ✅
isg_core ← isg_hr ← isg_training, isg_contractor
← isg_legislation ← isg_compliance ← isg_penalty ← isg_simulator
← isg_risk ← isg_incident
← isg_audit ← isg_audit.finding
← isg_osgb
Hiç geri-referans yok → clean architecture

### 7. ACL Stratejisi ✅
3 rol grubu (isg_security):
- **readonly:** Okuma yetki (reports, dashboards)
- **expert:** İSG Uzmanı (okuma-yazma, yeterli yetkiler)
- **manager:** Tam kontrol (yaşam döngüsü, silme)

### 8. Sequence İsimlendirmesi ✅
ISG-HAZARD-YYYY-NNNN (risk)
ISG-KZA-YYYY-NNNN (incident)
ISG-DOF-YYYY-NNNN (capa)
ISG-DNT-YYYY-NNNN (audit)
ISG-BLG-YYYY-NNNN (audit.finding) ← YENI
ISG-EGT-YYYY-NNNN (training)
ISG-KRL-YYYY-NNNN (board)
ISG-YZ-YYYY-NNNN (correspondence)
ISG-ZYR-YYYY-NNNN (visitor)

---

## Mevzuat Entegrasyon Modeli ✅
isg_legislation (kütüphane)
→ obligation: "6331 md.6 — Uzman 40 dk"
→ isg_compliance (uyum kontrol)
→ workplace danger_class=high, 100 çalışan
→ required = 4000 dk/ay
→ isg_osgb.assignment.monthly_required_minutes = 4000
→ monthly_actual_minutes = 3500
→ compliance_status = "warning" (3500 < 3600 = 90%)

---

## Denetim Mimarisi (isg_audit) ✅
isg.audit.template (Denetim Şablonu)
└─ isg.audit.template.question (Kontrol Maddesi)
└─ question (soru metni)
└─ weight (ağırlık: 1-5)
└─ is_critical (kritik madde?)

isg.audit (Denetim Kaydı)
├─ audit_type (İç/Dış/Müfettiş/Alt İşveren)
├─ template_id (şablon seçim)
├─ workplace_id + site_id (nerede yapıldı?)
├─ contractor_id (alt işveren denetimi opsiyonel)
├─ auditor_ids (denetçiler)
│
├─ line_ids (isg.audit.line — Çıktı Satırları)
│ ├─ question, weight, is_critical (template'ten)
│ ├─ result (Uygun/Uygunsuz/Uygulanamaz/Gözlem)
│ └─ response_weight (compute: result==ok ise weight, değilse 0)
│
├─ PUANLAMA (Computed):
│ ├─ total_weight (toplam ağırlık)
│ ├─ achieved_weight (elde edilen puan)
│ ├─ compliance_percentage (%)
│ └─ compliance_status (GREEN/YELLOW/RED)
│└─ Durum Makinesi:
draft → in_progress → done → closed

isg.audit.finding (Bulgu Kaydı — AYRI MODEL)
├─ audit_id (hangi denetim)
├─ audit_line_id (uygunsuz satırdan)
├─ finding_type (observation/non_conformity/major/critical)
├─ finding_description (bulgu açıklaması)
│
├─ Tekrarlanan Bulgu:│ ├─ repeat_count (kaç kez tekrar?)
│ ├─ escalation_level (compute: repeat>=3 ise level 2)
│ └─ previous_finding_ids (önceki benzer bulgular)
│
├─ Aksiyon:
│ ├─ responsible_person_id (sorumlu)
│ ├─ target_completion_date (hedef tarih)
│ └─ capa_id (bağlı DÖF)
│
├─ Kanıt:
│ ├─ evidence_text (gözlem notları)
│ └─ evidence_attachment_ids (fotoğraf, dokümantasyon)│
└─ Durum Makinesi:
open → in_review → resolved → verified → closed
---

## Veri Saklama ve Maskeleme (KVKK)

### Sağlık Verisi (isg_health_basic — Bloklu)
- Employee.medical_history → isg_health.record (hassas)
- ACL: sadece group_isg_health_officer oku
- Maskeleme: Raporlarda çalışan adı göstermez, "KGN001"
- Rıza: consent_date field
- **Status:** KVKK danışman onayı bekleniyor

### İş Kazası (isg_incident) ✅
- Kaza bilgileri: herkes okuyabilir
- Yaralanan kişi kimliği: expert/manager sadece
- SGK bildirimi: automatic

---

## Compute Field Mimarisi ✅

**isg_audit.line örneği:**
```python
@api.depends('result', 'weight')
def _compute_response_weight(self):
    for rec in self:
        if rec.result == 'ok':
            rec.response_weight = rec.weight
        else:
            rec.response_weight = 0

@api.depends('line_ids.weight', 'line_ids.response_weight', 'line_ids.is_critical', 'line_ids.result')
def _compute_scoring(self):
    for rec in self:
        rec.total_weight = sum(rec.line_ids.mapped('weight'))
        rec.achieved_weight = sum(rec.line_ids.mapped('response_weight'))
        rec.compliance_percentage = (rec.achieved_weight / rec.total_weight) * 100
        
        has_critical_nok = any(l.is_critical and l.result == 'nok' for l in rec.line_ids)
        if has_critical_nok:
            rec.compliance_status = 'red'  # Kritik bulgu → RED
        elif rec.compliance_percentage >= 90:
            rec.compliance_status = 'green'
        else:
            rec.compliance_status = 'yellow'
```

---

## Test Stratejisi

1. **Birim:** create/read/update/delete
2. **Entegrasyon:** workflow'lar (state machine)
3. **Mevzuat:** obligation matching (50+ scenario)
4. **UI:** form render, list, action buttons
5. **Performans:** 1000 record/modül bulk test (henüz yapılmadı — FAZ 5 sonrasında)

---

## Git Strategy

- **Repository:** https://github.com/SHapeloglu/ISG
- **Branch:** main (protected, direct push)
- **Commit format:** `[modül]: açıklama (feature, count)`
- **Push:** Her modül tamamlandıktan sonra

---

## Gelecek Mimarisi (E2/E3)

### E2: Superset, Flutter, Multi-company
- Superset entegrasyonu (F5)
- Flutter mobil uygulama
- Multi-company yönetim iyileştirmeleri

### E3: Sistem Entegrasyonu
- SGK API entegrasyonu (3 iş günü bildirimi)
- EKİPNET entegrasyonu (ekipman kontrol)
- İSG-KATİP entegrasyonu (uzman/hekim bildirimi)
- E-imza (5070 s.K.) — elektronik imza
- VERBİS uyumu (kişisel veri işleme kaydı)

### E4: Analitik
- Risk tahminlemesi (geçmiş kaza verilerinden)
- Anomali tespiti (ölçüm değerleri)
- Uyum önerme (otomatik aksiyon)

---

## Kritik Noktalar

🔴 **KVKK:** isg_health_basic hâlâ bloklu — danışman onayı gerekir  
🔴 **Mevzuat:** B-10 (isg_training 2 Nisan 2026) kritik  
🔴 **Ekipman:** F2-008 (Ara.2025 EK-II) mevzuat güncellemesi  
⚠️ **Dönüş Eğitimi:** isg_incident → isg_training otomatik tetikleme (test gerekir)  
⚠️ **TRIR Hesaplama:** F5 raporlamada doğru filtreleme

---

## Performans Notları

- Compute field'lar indexed (store=True)
- Search view'lar optimized
- One2many'lar inline editable (N+1 sorun yok)
- Record rule'lar basit (company_id only şimdi)

**İleride:** Bulk test (1000+ record), monitoring, query optimization

