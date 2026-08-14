# ARCHITECTURE.md — İSG Platform Mimari Belgesi

## Genel Bakış

İSG (İş Sağlığı ve Güvenliği) Platform, Odoo 18 üzerine kurulu, Türkiye'nin 6331 Kanunu ve ilgili yönetmeliklere uyumlu, kurumsal İSG yönetim sistemidir. HSE Radar ile fonksiyonel eşdeğerlik hedefiyle geliştirilmekte, ek olarak Odoo'nun yerleşik ERP entegrasyonunu sunar.

**Platform:** Odoo 18.0  
**Database:** PostgreSQL  
**VPS:** Contabo (vmi3389964), isg.powerbi.com.tr  
**Dil:** Python 3.12, XML, JavaScript  
**Version Control:** GitHub (SHapeloglu/ISG)

---

## Mimari Katmanlar
┌─────────────────────────────────────────────────────┐
│ PRESENTATION LAYER (Web UI) │
│ - Odoo Web Interface (list/form/search views) │
│ - Tree/Kanban views (özel gösterimler) │
│ - Mobile (Claude for iOS/Android) │
└─────────────────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────┐
│ BUSINESS LOGIC LAYER (Models) │
│ - FAZ 1: Governance (13 modül — isg_core vb.) │
│ - FAZ 2: Operations (20+ modül — risk, audit vb.) │
│ - Compute fields, state machines, validations │
│ - DÖF orchestration (isg_capa hub) │
└─────────────────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────┐
│ DATA ACCESS LAYER (ORM) │
│ - Odoo ORM (models.Model, fields.*) │
│ - PostgreSQL backend │
│ - Record rules, ACL security │
│ - Tracking & audit (mail.thread) │
└─────────────────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────┐
│ DATABASE │
│ - PostgreSQL 13+ │
│ - 47 modül × ~5-10 tablo = ~200+ tablo │
└─────────────────────────────────────────────────────┘
---

## Modül Hiyerarşisi & Bağımlılıklar

### FAZ 0 — Foundation
- **isg_core** — İşyeri, site, personel tabanı
- **isg_security** — Güvenlik grupları (readonly/expert/manager)

### FAZ 1 — Governance (İyi Yönetişim, 13 modül)
Depends: isg_core, isg_security, hr
├── isg_party ——————┐
├── isg_location ———┤
├── isg_document ───┤
├── isg_hr —————────┤
├── isg_base ───────┤
├── isg_training ───┤
├── isg_contractor──┤
├── isg_board ──────┤ (tümü hr_employee'ye bağlı)
├── isg_correspondence
├── isg_visitor
├── isg_health_basic
└── (HR Skills)
### FAZ 2 — Core Operations (32 modül planlı, 20 kurus)
All depend: isg_core, isg_security, isg_hr, isg_capa

TAMAMLANDI:
├── isg_capa ────────────── DÖF merkezi (corrective/preventive)
├── isg_risk ────────────── Risk Değerlendirmesi (L Matrisi + FK)
│ └→ creates isg_capa (high/intolerable risk)
├── isg_incident ────────── İş Kazası (SGK 3 gün takibi)
│ └→ creates isg_capa
├── isg_audit ───────────── Denetim (template + bulgu)
│ └→ creates isg_capa (critical finding)
├── isg_emergency ──────── Acil Durum (plan + tatbikat)
└── isg_ppe ────────────── KKD (zimmet + envanter)

DEVAM EDIYOR / PLANLANYOR:
├── isg_chemical ───────── Kimyasal (OEL/STEL + MSDS)
├── isg_equipment ──────── Ekipman Kontrol
├── isg_ptw ────────────── İş İzni
├── isg_loto ───────────── LOTO
├── isg_confined_space ─── Kapalı Alan
├── isg_hot_work ──────── Sıcak İşler
├── isg_excavation ────── Kazı
├── isg_scaffold ──────── İskele
├── isg_electrical ────── Elektrik
├── isg_noise ────────── Gürültü Ölçümü
├── isg_vibration ────── Titreşim Ölçümü
├── isg_lighting ────── Aydınlatma Ölçümü
├── isg_air_quality ──── Hava Kalitesi
├── isg_ergonomics ───── Ergonomi
├── isg_psychosocial ─── Psikososyal Risk
├── isg_biological ───── Biyolojik Tehlike
├── isg_fire_safety ──── Yangın Güvenliği
├── isg_hazmat ──────── Tehlikeli Madde
├── isg_vehicle ────── Araç Güvenliği
├── isg_contractor_supervision — Alt İşveren Ziyareti
├── isg_accident_investigation — Kaza Soruşturması
├── isg_near_miss_tracking ── Ramak Kala
├── isg_medical_removal ──── Tıbbi Çıkarma
├── isg_occupational_disease — Meslek Hastalığı
├── isg_statistics ────────── Raporlama (TRIR/LWDR)
└── isg_audit_action_plan ─── Denetim Sonrası Izleme
---

## Veri Modeli — Temel Kavramlar

### Merkez: isg_capa (Düzeltici/Önleyici Faaliyet)
isg.capa (DÖF Kaydı)
├── name: ISG-DÖF-2026-0001 (sequence)
├── source: incident / audit / risk_assessment / ... (selection_add)
├── workplace_id: isg.workplace (required)
├── severity: low / medium / high / critical (required)
├── capa_type: corrective / preventive (required)
├── state: open / analysis / action / verification / closed / cancelled
├── open_date, target_date, completion_date
├── responsible_id: hr.employee
└── description, notes
**Neden merkez?** Risk, incident, audit, vb. tüm modüller yüksek risk/bulgu/kaza durumunda DÖF açar. isg_capa tüm İSG akışının hub'ı.

### Risk: isg_risk.assessment + isg_risk.line
isg.risk.assessment
├── name: ISG-RD-2026-0001
├── workplace_id, site_id
├── method: l_matrix / fine_kinney (seçilir)
├── assessment_date, next_review_date (otomatik: danger_class'a göre +2/4/6 yıl)
├── state: draft → in_progress → done → approved → renewal → archived
├── team_ids: hr.employee (many2many)
└── risk_line_ids: one2many

isg.risk.line
├── hazard_description, category (fiziksel/kimyasal/bio/ergo/etc.)
├── L Matrisi: probability_l (1-5) × severity_l (1-5) → score (1-25)
├── Fine-Kinney: prob (0.2-10) × freq (0.5-10) × sev (1-100) → score (0-?)
├── risk_level: acceptable / low / medium / high / intolerable (compute)
├── residual (after control): residual_score, residual_level
├── control_measures, responsible_id, deadline
└── capa_id: isg.capa (create otomatik if high/intolerable)
**Puan Eşlemeleri:**
- **L Matrisi:** 1-4 acceptable, 5-9 low, 10-16 medium, 17-25 high/intolerable
- **Fine-Kinney:** <20 acceptable, 20-70 low, 70-200 medium, 200-400 high, >400 intolerable

### Incident: isg_incident
isg.incident
├── name: ISG-KZ-2026-0001
├── incident_type: accident / near_miss / occupational_disease
├── incident_date, occurrence_time
├── workplace_id, site_id, location_detail
├── injured_employee_id, involved_party_ids
├── injury_type: none / minor / major / fatal
├── state: draft → investigation → sgk_pending → closed
├── sgk_notification_deadline: auto (incident_date + 3 days)
├── sgk_notification_date, sgk_ref_number
├── witness_ids, investigator_id
├── root_cause, corrective_actions
└── capa_id: isg.capa (create otomatik if serious)
### Audit: isg_audit.plan + isg_audit.line
isg.audit
├── name: ISG-DNT-2026-0001
├── audit_type: internal / external / inspection / supplier
├── template_id: isg.audit.template (optional, şablon yükle buton)
├── workplace_id, site_id
├── auditor_ids: many2many hr.employee
├── state: draft → in_progress → done → closed
├── audit_line_ids: one2many

isg.audit.line
├── question, category, legal_reference, is_critical
├── result: ok / nok / na / obs
├── finding, evidence
├── capa_id: isg.capa (create otomatik if nok + critical)
└── control_status: planned / in_progress / done
### Emergency: isg_emergency.plan + isg_emergency.drill
isg.emergency.plan
├── name: ISG-ADP-2026-0001
├── title, workplace_id, site_id
├── emergency_types: many2many (yangın, deprem, kimyasal vb.)
├── team_ids: many2many hr.employee (acil durum ekibi)
├── assembly_point_ids: many2many isg.assembly.point
├── state: draft → active → review → archived

isg.emergency.drill
├── name: ISG-TAT-2026-0001
├── plan_id: isg.emergency.plan (required)
├── drill_type: evacuation / fire / earthquake / chemical / medical / full
├── drill_date, duration, participant_count
├── evacuation_time_minutes
├── result: successful / partial / failed
├── findings, improvements
└── next_drill_date
### PPE: isg_ppe.type + isg_ppe.stock + isg_ppe.issue
isg.ppe.type (Standart 18 Tür)
├── name: "Emniyet Miğferi", "Nitril Eldiven" vb.
├── category: head / eye / hearing / respiratory / hand / foot / body / fall / other
├── standard: EN 397, EN 388 vb.
├── lifespan_months: 24, 12, 60 vb.
├── requires_size: bool
└── size_type: clothing / shoe / glove

isg.ppe.stock
├── ppe_type_id, workplace_id
├── quantity, min_quantity
├── is_low_stock: computed (quantity ≤ min_quantity)
└── location: Depo konumu

isg.ppe.issue (Zimmet)
├── name: ISG-KKD-2026-0001
├── employee_id, ppe_type_id, quantity
├── issue_date, expiry_date (otomatik: lifespan_months)
├── return_date
├── employee_clothing_size, employee_shoe_size, employee_glove_size (related isg_hr'dan)
├── state: issued / returned / expired / lost
└── Durum makinesi + action_return(), action_lost(), action_reissue()
---

## Veri Akışları (Kritik Örnekler)

### Akış 1: Risk Değerlendirmesi → DÖF
Kullanıcı Risk Değerlendirmesi kaydı açar (draft)
Satırları ekler, olasılık × şiddet puanlar
Sistem otomatik risk_level hesaplar (compute)
risk_level = 'high' veya 'intolerable' ise:
→ action_create_capa() otomatik çalışır (F2-005 isg_ppe'de benzer)
→ isg.capa kaydı oluşur (source='risk_assessment')
DÖF kaydında kontrol tedbirleri planlanır
Tamamlanınca risk satırında residual_risk hesaplanır
### Akış 2: İş Kazası → DÖF + SGK Bildirimi
Kaza kaydı açılır (incident_type='accident')
Sistem sgk_notification_deadline otomatik hesaplar
(incident_date + 3 days, 6331 md.14)
Durum: draft → investigation (soruşturma)
Ciddi kaza ise action_create_capa() otomatik çalışır
Durum: sgk_pending (SGK bildirimi bekleniyor)
İnsan: SGK ref numarası girse
Durum: closed
### Akış 3: Denetim Bulgusu → DÖF
Denetim kaydı oluştur, şablondan soruları yükle
Her soru için ok/nok sonucu gir
nok + is_critical=True ise:
→ action_create_capa() otomatik çalışır
→ capa severity='critical' olur (diğer source'lardan daha ciddi)
DÖF'ün bitişinde audit_line.capa_id otomatik referanslanır
---

## Security & Access Control

### Gruplar (isg_security.group_isg_*)
group_isg_readonly (tümü okuma, yazma yok)
group_isg_expert (read + write + create, unlink yok)
group_isg_manager (full access, unlink dahil)
group_isg_admin (ileride: system genişlemeleri)
### Record Rules (ir.rule)
Kural: [('company_id', 'in', company_ids)]
└─ Her modüle applied → şirket bazlı veri izolasyonu
(Multi-tenant uyumluluğu için)

NOT: Bazı modüllerde satır kuralı eksik (backlog):

isg_risk_line (satırlar yüksek risk içerebilir, filtresiz?)
isg_audit_line (benzer)
### Tracking & Audit
Tüm modüller mail.thread inherit eder
├── Değişiklik geçmişi (chatter)
├── Zamanlı aktiviteler
├── field tracking (tracking=True)
└── State değişiklikleri logged

6331 md.10 (Dokümantasyon) uyumluluğu sağlanır
---

## Sequence Tasarımı
ISG-XX-YYYY-NNNN

XX = Modül Kodu
RD (Risk Değerlendirmesi)
KZ (Kaza)
DNT (Denetim)
ADP (Acil Durum Planı)
TAT (Tatbikat)
KKD (KKD Zimmet)
vb.

YYYY = Takvim Yılı (self-incrementing)
NNNN = 4 haneli numara (001 → 9999)

Avantajları:

    İnsan okunaklı, baskı dostu
    Tarihçe takibi kolay (yıl bazında)
    Multi-şirket uyumlu (company_id=False)


---

## Compute Field Pattern

```python
# Store=False: Sadece display
@api.depends('field_a', 'field_b')
def _compute_display(self):
    for rec in self:
        rec.display = f"{rec.field_a} - {rec.field_b}"

# Store=True: Search/filter kullanılacaksa ZORUNLU
@api.depends('risk_line_ids.risk_level')
def _compute_high_risk_count(self):
    for rec in self:
        rec.high_risk_count = len(rec.risk_line_ids.filtered(
            lambda l: l.risk_level in ('high', 'intolerable')
        ))
```

**Kural:** Search domain'de bir field kullanılıyorsa → store=True

---

## API Entegrasyon Noktaları

### 1. İSG Yazılımı → ERP (Gelecek)

Kaza → Muhasebe (hasar masrafları)
DÖF → İş Emri (KKD yenileme, ekipman bakım)
Eğitim → HR (çalışan eğitim saati takibi)


### 2. Harici Sistem → İSG

SGK veri → İş kazası sorgulama
OEL/STEL tablosu → Kimyasal modul (veri tabanı lookup)
MSDS dökümanı → İSG Document storage


### 3. Raporlama Çıktısı

    PDF rapor (Risk Değerlendirmesi, Denetim Bulgusu)
    Excel export (kaza istatistikleri)
    Dashboard (TRIR, LWDR, frequency rate)


---

## Teknoloji Stack

| Layer | Technology |
|-------|-----------|
| Web Server | Odoo 18 (built-in) |
| Database | PostgreSQL 13+ |
| Backend | Python 3.12, Odoo ORM |
| Frontend | HTML/CSS/JavaScript (Odoo Web) |
| Mobile | Claude iOS/Android (gelecek) |
| VPS | Contabo (2 vCPU, 4 GB RAM, Ubuntu 24) |
| Version Control | Git (GitHub SHapeloglu/ISG) |
| CI/CD | Manual (test → commit → push) |

---

## Deployment & Maintenance

### Sunucu Yapısı

/opt/odoo/
├── odoo18/ (Odoo binary)
├── venv18-isg/ (Python virtualenv)
├── isg_addons/ (Tüm ISG modülleri)
│ ├── isg_core/
│ ├── isg_risk/
│ ├── isg_incident/
│ ├── ... (17+ modül)
│ └── .git/ → GitHub
└── /etc/odoo/
└── odoo18-isg.conf

PostgreSQL:
Database: isg
Tables: ~200+ (47 modül)
Users: odoo (app user)


### Servis Yönetimi
```bash
sudo systemctl status odoo18-isg.service
sudo systemctl restart odoo18-isg.service
sudo systemctl stop odoo18-isg.service

Logfile: /var/log/odoo/odoo18-isg.log
```

### Backup Stratejisi

Database: PostgreSQL pg_dump (daily)
Dosyalar: /opt/odoo/isg_addons (git managed)
Attachments: filestore (if configured)


---

## Bilinen Limitasyonlar & TODOs

### Teknik Borç
1. isg_contractor.contractor_level — recursive=True bug
2. isg_location.hazard_type — view parameter uyumsuzluğu
3. Record rule eksiklikleri (cross-company isolation)
4. Email/SMS bildirimleri (otomatik uyarı)
5. Mobil uygulama (Claude for iOS/Android)

### Feature Borcu (HSE Radar'ın Ötesi)
1. İstatistik paneli (TRIR, LWDR, frequency rate)
2. Muhasebe entegrasyonu (kaza masrafları)
3. Excel/PDF rapor şablonları (custom report)
4. Workflow otomasyonu (email triggers, SMS alerts)

---

## Sözlük & Kavramlar

| Terim | Açıklama | Örnek |
|-------|----------|-------|
| DÖF | Düzeltici/Önleyici Faaliyet | Yüksek risk'e karşı kontrol tedbiresi |
| OSGB | Özel Sağlık ve Güvenlik Birim | İşyerinin İSG danışmanı |
| SEG | Çalışan Sağlığı Grubu | Hekimlik muayene hizmeti |
| PTW | İş İzni (Permit-to-Work) | Tehlikeli işler için yazılı izin |
| LOTO | Kilitleme (Lockout Tagout) | Enerji kaynağı kontrol |
| OEL/STEL | Maruziyet Limiti | Hava kalitesi standartları |
| Ramak Kala | Near-miss | Kazaya dönüşebilecek potansiyel olay |
| İSG-KATİP | İSG Sistemi Yönetim Sorumlusu | Kurumsal İSG koordinatörü |
| TRIR | Total Recordable Incident Rate | Kaza sıklığı metriği |
| LWDR | Lost Workday Rate | İş günü kaybı metriği |

---

## Referanslar

- **Mevzuat:** 6331 Kanunu, ilgili Yönetmelikler (2025-2026)
- **Standart:** ISO 31010 (Risk Assessment)
- **Benchmarks:** HSE Radar (ticari ürün), Riskmatik
- **Version Control:** https://github.com/SHapeloglu/ISG

---

**Son Güncelleme:** 14 Ağustos 2026  
**Mimari Sürüm:** 2.0 (FAZ 2, 5 modül tamamlandı)

