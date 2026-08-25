# CLAUDE.md — Yeni Chat Bağlamı

Proje Özeti
Contabo VPS üzerinde Odoo 18 tabanlı Türkiye İSG (İş Sağlığı ve Güvenliği) platformu geliştiriyoruz. Hedef: HSE Radar ile %90+ işlevsel eşdeğerlik + Odoo ERP avantajı.

Geliştirici Profili
- Odoo'da 3+ modül deneyimi, junior seviye
- Python/Odoo öğreniyor
- Her adımı birlikte, step by step
- Anlamadığı yerlerde soruyor
- Sunucuya SSH ile bağlanıp terminal komutları çalıştırıyor

Çalışma Kuralları

Terminal Komutları
- Komutları tek tek ver, art arda değil
- Her komutun çıktısını bekle
- `| tail -N` ile kısa tut
- Log için her zaman `--logfile=""`
- Permission denied → `sudo chown -R odoo:odoo /opt/odoo/isg_addons/MODUL/`

Modül Geliştirme Standardı
- Her modül: __manifest__.py, __init__.py, models/, views/, security/, data/
- `sudo -u odoo tee ... << 'EOF'` ile dosya yaz
- Her modülü systemctl stop/start arasında kur
- Sequence prefix: ISG-XXX-YYYY-NNNN formatı

Odoo 18 Uyumluluk Kuralları (KRİTİK)
1. ACL dosyası: ir.model.access.csv (nokta, alt çizgi değil)
2. Views: <list> (eski <tree> değil)
3. Embedded lists: <list editable="bottom">
4. states= ve attrs= YASAK → invisible= kullan
5. fields.DateTime (T büyük), tracking=True selection'da yok
6. unique=True Char'da WARNING → kaldır
7. One2many: inverse_name doğru olmalı
8. Menu: action tanımı kullan/referans et

Proje Stratejisi

Geliştirme Yaklaşımı (3 Hat)
1. OCA/hazır → kur
2. Başka dilden → port et
3. Sıfırdan Türkiye'ye özgü → yazarız

Sıfırdan Yazılacak Kritik Alanlar
1. Mevzuat/yükümlülük motoru (F4-001 ✅)
2. OSGB planlama (sırada)
3. KVKK/sağlık gizliliği (F1-002 bloklu)
4. Çok katmanlı güvenlik sınırı (✅)
5. Simülatör (F4-004 ✅)

Mevzuat Kritik Notlar

Değişiklik | Tarih | Etkilenen Modül
2 Nisan 2026 Eğitim Yönetmeliği | 2026-04-02 | isg_training ✅
İş Ekipmanları Yönetmeliği EK-II | 2025-12 | F2-008 isg_equipment
İdari para cezaları %49 artış | 2026 | isg_penalty ✅
Risk Değerlendirmesi periyodu | 2 yıl | isg_risk ✅
Uz/hekim süre güncellemesi | 2025 | isg_osgb (sırada)

Dosya Yolları

/opt/odoo/isg_addons/          # ISG modülleri
/opt/odoo/venv18-isg/          # ISG Python venv
/etc/odoo/odoo18-isg.conf      # ISG config
/opt/odoo/isg_addons/.claude/  # Dokümantasyon
/var/log/odoo/odoo18-isg.log   # ISG log

Proje İlerleme: 29/32 (%90.6)

FAZ 0: 7/7 (100%) - Temel Mimari
FAZ 1: 5/6 (83%) - Kurumsal Yönetişim (isg_health_basic bloklu)
FAZ 2: 2/9 (22%) - Çekirdek İSG (isg_capa, isg_risk)
FAZ 3: 0/2 (0%) - Ölçüm
FAZ 4: 4/4 (100%) - Sanal Müfettiş (isg_legislation → simulator)
FAZ 5: 0/3 (0%) - Raporlama
OSGB: 0/1 (0%)

Kurulu Modüller: 57 toplam (29 ISG)

Sıradaki 3 Modül

1. isg_osgb - OSGB Planlama/Görevlendirme (Tavsiye)
2. F5-001 - Raporlama & Dashboards
3. F1-002 - Health Module (KVKK danışman onayı bekliyor)
