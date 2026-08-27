# CLAUDE.md — Yeni Chat Bağlamı

Tarih: 26 Ağustos 2026

Proje Özeti:
Contabo VPS üzerinde Odoo 18 tabanlı Türkiye İSG platformu.
Hedef: HSE Radar ile %95+ eşdeğerlik + Odoo ERP entegrasyonu.

Geliştirici Profili:
- Junior Odoo developer
- Python/Odoo öğreniyor
- Her adım birlikte, step by step
- Terminal komutları sunucuda çalıştırıyor

Son Oturum (26 Ağustos):
✅ B-1: isg.rate.table
✅ B-2/B-3/B-6/B-7: MEV retrofit
✅ isg_osgb başlandı

Proje İlerleme: 30/32 modül (%93.75)
Sistem: Stabil, 58 modül çalışıyor

Çalışma Kuralları:
- Komutları tek tek ver
- Terminal çıktısını bekle
- `--logfile=""` daima
- Manifest: base, mail
- Views: Odoo 18 (list editable="bottom")
- ACL: readonly/expert/manager
- Sequence: ISG-XXX-YYYY-NNNN

Odoo 18 Uyumluluğu (KRİTİK):
1. <tree> → <list>
2. states= ve attrs= YASAK
3. fields.Datetime (büyük D)
4. unique=True Char'da WARNING
5. XML: <data> wrapper gerek yok
6. <list editable="bottom">
7. tracking=True Selection'da desteklenmiyor

Kurulu Modüller (58 toplam, 30 ISG):
isg_core, isg_security, isg_party, isg_location, isg_document, isg_hr, 
isg_base, isg_training, isg_contractor, isg_board, isg_correspondence, 
isg_visitor, isg_legislation, isg_compliance, isg_penalty, isg_simulator,
isg_capa, isg_risk, isg_osgb

Sıradaki:
1. isg_osgb view'ları
2. B-4/8/9 MEV retrofit
3. F2-003 isg_incident

Proje Durum: %71 (adam-gün %75)
