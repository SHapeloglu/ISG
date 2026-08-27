# ARCHITECTURE.md — Mimari ve Tasarım Kararları

Genel Mimari: Odoo 18 İSG Platform

Odoo 18 ERP Altyapısı (İK, Muhasebe, Satın Alma, CRM)
↓
isg_core (Workplace/Site hiyerarşisi, isg.rate.table)
↓
FAZ 0-1 (Güvenlik, Yönetişim)
isg_security, isg_party, isg_training, isg_contractor, isg_board
↓
FAZ 4 — Sanal Müfettiş (Çekirdek DNA)
1. isg_legislation — mevzuat kütüphanesi (7 obligation)
2. isg_compliance — uygunluk motoru (snapshot mimarisi)
3. isg_penalty — ceza hesabı (2026 tarife)
4. isg_simulator — bulgular modeli
↓
FAZ 2 (Operasyonel Modüller)
isg_risk, isg_capa, isg_incident (✅ sırada)
isg_audit, isg_ppe, isg_emergency, isg_chemical, isg_equipment, isg_ptw+loto
↓
OSGB Planlama (isg_osgb)
İşyeri-uzman atama, aylık dakika uygunluğu, kapasite planlama
(isg.rate.table entegre)
↓
FAZ 3 (Ölçüm/Çevre)
isg_measurement_core, isg_measurement_hygiene, isg_environment
↓
FAZ 5 (Raporlama)
isg_reporting, Superset, TRIR/LWDR KPI

Tasarım Kararları (Kritik):

1. isg_compliance "Snapshot" Mimarisi
Uygunluk değerlendirmesi tarihe bağlı olarak depolanır.
Gerekçe: Audit trail, versiyonlu mevzuat, geçmiş tarihli hesaplar.
Sonuç: 100% audit-grade → kasa açılan her rapor tekrar üretilebilir.

2. isg.rate.table Merkezileştirme
Uzman/hekim dakika katsayıları isg_core'da tek tablo.
Kullanan: isg_workplace + isg_osgb
Versiyonlanmış: valid_from (geçmiş tarihli hesaplar için)
Gerekçe: Ortak kaynak → veri bütünlüğü

3. isg_osgb.assignment "Compliance Status"
İşyeri-uzman atamasında aylık dakika uygunluğu otomatik hesaplanır (%90 tolerans).
Manager dashboard: red-yellow-green renkler

4. Unidirectional Dependency Chain
isg_core ← isg_hr ← isg_training, isg_contractor
         ← isg_legislation ← isg_compliance ← isg_penalty ← isg_simulator
         ← isg_risk ← isg_incident
         ← isg_osgb

Hiç geri-referans yok.

5. ACL Stratejisi
3 rol grubu (isg_security):
- group_isg_readonly (okuma)
- group_isg_expert (uzman, okuma-yazma)
- group_isg_manager (tüm yaşam döngüsü)

6. Sequence İsimlendirmesi
ISG-HAZARD-YYYY-NNNN, ISG-RISK-YYYY-NNNN, ISG-INCIDENT-YYYY-NNNN
ISG-CAPA-YYYY-NNNN, ISG-AUDIT-YYYY-NNNN, ISG-CEZA-YYYY-NNNN

Mevzuat Entegrasyon Modeli:

isg_legislation (kütüphane)
→ obligation: "6331 md.6 — Uzman 40 dk"
→ isg_compliance (uyum kontrol)
→ workplace danger_class=high, 100 çalışan
→ required = 4000 dk/ay
→ isg_osgb.assignment.monthly_required_minutes = 4000
→ monthly_actual_minutes = 3500
→ compliance_status = "warning" (3500 < 3600 = 90%)

Veri Saklama ve Maskeleme (KVKK):

Sağlık Verisi (isg_health_basic):
- Employee.medical_history → isg_health.record (hassas)
- ACL: sadece group_isg_health_officer oku
- Maskeleme: Raporlarda çalışan adı göstermez, "KGN001"
- Rıza: consent_date field

Test Stratejisi:
1. Birim: create/read/update/delete
2. Entegrasyon: workflow'lar
3. Mevzuat: obligation matching (50+ scenario)
4. UI: form render, list, action buttons
5. Performans: 1000 record/modül bulk test

Git: main branch, direct push

Gelecek (E2/E3):
E2: Superset, Flutter, multi-company
E3: SGK/EKİPNET/İSG-KATİP, e-imza
