# CLAUDE.md — Yeni Chat Bağlamı (14 Ağustos 2026)

## Proje Özeti

Contabo VPS üzerinde Odoo 18 tabanlı Türkiye ISG platformu geliştiriyoruz.
Hedef: HSE Radar ile 90%+ işlevsel eşdeğerlik + Odoo ERP entegrasyonu.

## Mevcut Durum

Kurulu Modüller: 46 (Odoo native 27 + ISG 19)

FAZ Ilerleme:
- FAZ 0 Temel Mimari: 100%
- FAZ 1 Kurumsal Yönetişim: 83%
- FAZ 2 Çekirdek ISG Ops: 67%
- GENEL: 56% (18/32 modül)

FAZ 2 Tamamlanan (6/9):
- isg_capa (F2-001)
- isg_risk (F2-002)
- isg_incident (F2-003)
- isg_audit (F2-004)
- isg_ppe (F2-005)
- isg_emergency (F2-006)

Sırada (FAZ 2): isg_chemical, isg_equipment, isg_ptw+isg_loto

## Geliştirici Profili

Junior Odoo developer, terminal komutlarını çalıştırıp çıktı paylaşıyor.
SSH bağlantısı var, VPS'e direkt erişim.

## Çalışma Kuralları

Terminal Komutları:
- Tek tek ver, art arda değil
- Her komutun çıktısını bekle
- MUTLAK: --logfile="" (config'de logfile tanımlı)
- Hata yoksa çıktı yok → normal, devam et

Session Başlangıç (KRİTİK!):
- Her chat'te ls -la /opt/odoo/isg_addons/
- cat ile dosyaları doğrula
- Varsayım yapma — gerçek durumu kontrol et

Modül Geliştirme:
- Dosya: sudo -u odoo tee ... > /dev/null << 'EOF'
- Sequence: ISG-XXX-YYYY-NNNN
- Test: kurulum sonrası hata kontrolü

## Mevzuat Kritik Notlar

- Eğitim Yönetmeliği (2 Nisan 2026): isg_training
- İş Ekipmanları EK-II (Aralık 2025): isg_equipment
- Cezalar %49 artış (2026): isg_penalty
- Uzman/hekim süreleri (2025): isg_hr, isg_osgb

## Sıradaki Modül: F2-007 isg_chemical

Kimyasal Envanter ve SDS/GBF Yönetimi
- isg.chemical: Kimyasal envanter
- isg.chemical.inventory: Stok
- Mevzuat: Kimyasal Maddeler Yönetmeliği
- GHS sınıflama kategorileri

Temel alanlar:
- name, sku, ghs_class
- Hazırlık tarihi, depo konumu, min/max stok
- SDS dosyası (ir.attachment)
- company_id, workplace_id, site_id
