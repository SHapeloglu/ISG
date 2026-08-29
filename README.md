# İSG Platform — Odoo 18 Türkiye İş Sağlığı ve Güvenliği Platformu

[![License: LGPL-3.0](https://img.shields.io/badge/License-LGPL%203.0-blue.svg)](https://opensource.org/licenses/LGPL-3.0)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-green)](https://www.python.org/)
[![Odoo: 18.0](https://img.shields.io/badge/Odoo-18.0-red)](https://www.odoo.com/)
[![Status: Active Development](https://img.shields.io/badge/Status-Active-brightgreen)]()

---

## 📋 Proje Özeti

**İSG Platform**, Türkiye'de işletmelerin 6331 sayılı İş Sağlığı ve Güvenliği Kanunu ve bağlı mevzuata uyum sağlamasını kolaylaştıran, **Odoo 18** tabanlı, açık kaynaklı bir İşyeri Sağlık ve Güvenliği (İSG) yönetim platformudur.

**Hedef:** HSE Radar (ticari yazılım) ile %95+ işlevsel eşdeğerlik + Odoo ERP'nin native entegrasyonu (muhasebe, İK, satın alma, CRM).

---

## ✨ Temel Özellikler

### 🏗️ **Temel Mimari (FAZ 0)**
- ✅ Holding → Şirket → İşyeri → Fiziksel Site hiyerarşisi
- ✅ Kullanıcı/grup/yetkilendirme sistemi (3 rol: Readonly/Expert/Manager)
- ✅ Dokümantasyon ve arşiv (SHA-256, e-imza compat, sürüm yönetimi)
- ✅ Çalışan İSG profili (SEG, KKD beden ölçüleri, uzman/hekim dakika formülü)

### 🏢 **Kurumsal Yönetişim (FAZ 1)**
- ✅ Alt işveren yönetimi (zincir yapısı, belge matrisi)
- ✅ Eğitim planlama (2 Nisan 2026 Yönetmeliği uyumlu)
- ✅ İSG Kurulu yönetimi (toplantı, karar takibi)
- ✅ Gelen/giden yazışma (yasal süre takibi)
- ✅ Ziyaretçi yönetimi (KKD bildirimi, risk briefing)

### ⚠️ **Operasyonel İSG (FAZ 2 — Kısmen Tamamlandı)**
- ✅ Risk Değerlendirmesi (lokasyon bazlı, yenileme tetikleyicileri)
- ✅ DÖF/CAPA (kök neden analizi, 5 Neden, aksiyon takibi)
- ✅ **İş Kazası / Ramak Kala / Meslek Hastalığı** (SGK 3 iş günü bildirimi, TRIR eligibility)
- 🔄 Denetim ve Kontrol Listeleri (sırada)
- 🔄 KKD Yönetimi (sırada)
- 🔄 Acil Durum Planı (sırada)
- 🔄 Kimyasal Envanter + OEL/STEL (sırada)
- 🔄 Ekipman + Periyodik Kontrol (Ara.2025 EK-II, sırada)
- 🔄 İş İzni + LOTO (sırada)

### 📊 **Ölçüm ve Çevre (FAZ 3 — Sırada)**
- 🔄 Gürültü / Toz / Kimyasal Buhar / Titreşim Ölçümleri
- 🔄 Limit Profili (sürümlü OEL/STEL)
- 🔄 Çevre Yönetimi

### 🤖 **Sanal Müfettiş (FAZ 4 — TAMAMLANDI)**
- ✅ **Mevzuat Kütüphanesi** (7+ temel obligation)
- ✅ **Uygunluk Motoru** (snapshot mimarisi, audit-grade)
- ✅ **Ceza Hesabı** (2026 %49 artış, yıllık otomatik güncelleme)
- ✅ **Simülatör** (bulgular modeli, istatistikler)

### 📈 **Raporlama (FAZ 5 — Sırada)**
- 🔄 Superset Entegrasyonu
- 🔄 Dashboard'lar (KPI: TRIR, LWDR, kaza sıklığı, uygunluk oranları)
- 🔄 Aylık/Yıllık Raporlar
- 🔄 ÇSGB Rapor Formatları

### 🏛️ **OSGB Planlama (Özel Modül — TAMAMLANDI)**
- ✅ OSGB Profili ve Uzman/Hekim Kadrosu
- ✅ İşyeri-Uzman Atama
- ✅ Aylık Süre Uygunluğu (%90 tolerans)
- ✅ Kapasite Planlama
- ✅ İSG-KATİP Hazırlık

---

## 🚀 Kurulum

### Sistem Gereksinimleri

- **İşletim Sistemi:** Ubuntu 20.04+ veya Debian 11+
- **Python:** 3.10+
- **PostgreSQL:** 12+
- **Odoo:** 18.0 Community Edition
- **RAM:** 4GB (geliştirme), 8GB+ (üretim)
- **Disk:** 20GB+ (veritabanı + loglar)

### Hızlı Kurulum (VPS'te)

```bash
# 1. ISG Repo'sunu klonla
cd /opt/odoo
git clone https://github.com/SHapeloglu/ISG.git isg_addons

# 2. Bağımlılıkları yükle (Odoo venv içinde)
source /opt/odoo/venv/bin/activate
pip install -r isg_addons/requirements.txt  # (varsa)

# 3. Modülleri Odoo'ya ekle (config'de addons_path'e koy)
# /etc/odoo/odoo.conf:
# addons_path = /opt/odoo/addons,/opt/odoo/isg_addons

# 4. Servisi restart et ve modülleri kur
sudo systemctl restart odoo
# Web arayüzü: Settings → Apps → Search: "isg" → Install

# 5. Database'i update et (CLI)
sudo -u odoo /opt/odoo/venv/bin/python3 /opt/odoo/odoo-bin \
  -c /etc/odoo/odoo.conf -d isg_db -i isg_core,isg_security,isg_party,... --stop-after-init
```

### Docker (Opsiyonel)

```dockerfile
FROM odoo:18.0
RUN git clone https://github.com/SHapeloglu/ISG.git /mnt/extra-addons/isg_addons
```

---

## 📦 Modüller (32 Ana Modül)

### FAZ 0 — Temel Mimari (7/7 — %100)

| Modül | Açıklama | Status |
|-------|----------|--------|
| `isg_core` | İşyeri, Site, tehlike sınıfı, uzman/hekim dakika | ✅ |
| `isg_security` | Rol grupları (Readonly/Expert/Manager) | ✅ |
| `isg_party` | OSGB/Lab/Muayene rolleri | ✅ |
| `isg_location` | Fiziksel lokasyon, GPS, toplanma noktaları | ✅ |
| `isg_document` | Dokümantasyon, sürüm, e-imza, SHA-256 | ✅ |
| `isg_hr` | Çalışan İSG profili, SEG, KKD beden ölçüleri | ✅ |
| `isg_base` | UUID mixin, outbox (entegrasyon) | ✅ |

### FAZ 1 — Kurumsal Yönetişim (5/6 — %83)

| Modül | Açıklama | Status |
|-------|----------|--------|
| `isg_contractor` | Alt işveren, zincir, belge matrisi | ✅ |
| `isg_training` | Eğitim planı, katılım (2 Nisan 2026 uyumlu) | ✅ |
| `isg_visitor` | Ziyaretçi, giriş/çıkış, KKD bildirimi | ✅ |
| `isg_board` | İSG Kurulu, toplantı, karar | ✅ |
| `isg_correspondence` | Gelen/giden yazışma, yasal süre | ✅ |
| `isg_health_basic` | Sağlık gözetimi, KVKK maskeleme | ⏳ (KVKK danışman onayı) |

### FAZ 2 — Operasyonel İSG (3/9 — %33)

| Modül | Açıklama | Status |
|-------|----------|--------|
| `isg_risk` | Risk değerlendirmesi, lokasyon bazlı | ✅ |
| `isg_capa` | DÖF/CAPA, kök neden, aksiyon takibi | ✅ |
| `isg_incident` | Kaza/ramak kala/meslek hastalığı, SGK bildirimi, TRIR | ✅ |
| `isg_audit` | Denetim, kontrol listeleri, bulgu → DÖF | 🔄 |
| `isg_ppe` | KKD envanter, zimmet, yenileme | 🔄 |
| `isg_emergency` | Acil durum planı, tatbikat, tahliye | 🔄 |
| `isg_chemical` | Kimyasal envanter, OEL/STEL, depolama uyumluluğu | 🔄 |
| `isg_equipment` | Ekipman, periyodik kontrol (Ara.2025 EK-II), EKİPNET | 🔄 |
| `isg_ptw` / `isg_loto` | İş İzni, LOTO, çok aşamalı onay | 🔄 |

### FAZ 3 — Ölçüm ve Çevre (0/2 — %0)

| Modül | Açıklama | Status |
|-------|----------|--------|
| `isg_measurement_core` + `hygiene` | Gürültü/toz/kimyasal ölçümleri, limit profili | 🔄 |
| `isg_environment` | Çevre yönetimi, atık kodları | 🔄 |

### FAZ 4 — Sanal Müfettiş (4/4 — %100)

| Modül | Açıklama | Status |
|-------|----------|--------|
| `isg_legislation` | Mevzuat kütüphanesi (7+ obligation) | ✅ |
| `isg_compliance` | Uygunluk motoru (snapshot) | ✅ |
| `isg_penalty` | Ceza hesabı (2026 %49 artış) | ✅ |
| `isg_simulator` | Simülatör, bulgular modeli | ✅ |

### FAZ 5 — Raporlama (0/3 — %0)

| Modül | Açıklama | Status |
|-------|----------|--------|
| `isg_reporting` | Dashboard'lar (TRIR, LWDR, KPI) + Superset | 🔄 |
| — | QWeb PDF şablonları | 🔄 |
| — | HSE Radar kabul testi | 🔄 |

### OSGB (1/1 — %100)

| Modül | Açıklama | Status |
|-------|----------|--------|
| `isg_osgb` | OSGB planlama, uzman/hekim atama, kapasite | ✅ |

---

## 🏗️ Mimari

```
Odoo 18 ERP Altyapısı (İK, Muhasebe, Satın Alma, CRM)
        ↓
    isg_core (Workplace/Site, danger_class, rate_table)
        ↓
    FAZ 0-1 (Güvenlik, Yönetişim)
    ↓ isg_security, isg_party, isg_training, isg_contractor, ...
        ↓
    FAZ 4 — Sanal Müfettiş (Mevzuat Motor) ✅
    ↓ isg_legislation, isg_compliance, isg_penalty, isg_simulator
        ↓
    FAZ 2 (Operasyonel) — Kısmen Tamamlandı
    ↓ isg_risk, isg_capa, isg_incident, isg_audit, ...
        ↓
    OSGB Planlama (isg_osgb) ✅
        ↓
    FAZ 3 (Ölçüm/Çevre) — Sırada
    ↓ isg_measurement, isg_environment
        ↓
    FAZ 5 (Raporlama) — Sırada
    ↓ isg_reporting, Superset, PDF şablonları
```

---

## 🔑 Temel Özellikler

### Uygunluk Motoru (Snapshot Mimarisi)
```python
# Tarih bağlı uygunluk değerlendirmesi
rec.compliance_status = 'compliant'  # Geçmiş tarihte tekrar hesaplanabilir
rec.snapshot_date = fields.Date.today()
```

### Compute Field'lar
```python
# isg_incident örneği: SGK Bildirimi
@api.depends('incident_type', 'severity')
def _compute_sgk_notification_required(self):
    for rec in self:
        rec.sgk_notification_required = (
            rec.incident_type in ['accident', 'occupational_disease']
            and rec.severity in ['serious', 'fatal']
        )
```

### OSGB Kapasite Planlama
```python
# İşyeri-Uzman aylık dakika uygunluğu
rec.monthly_required_minutes = (
    rec.workplace_id.employee_count * 
    rate_table.get_rate(rec.workplace_id.danger_class, rec.role)
)
rec.compliance_status = 'compliant' if rec.monthly_actual_minutes >= rec.monthly_required_minutes * 0.9
```

---

## 📋 Kullanım

### 1. OSGB Yönetimi
```
OSGB Yönetimi → OSGB Kuruluşları
  ├─ Temel Bilgiler: OSGB adı, yetki belgesi, iletişim
  ├─ İSG Uzmanları: Sınıf A/B/C uzman kadrosu
  ├─ İşyeri Hekimleri: Hekim kaydı
  └─ İşyeri Atamaları: İşyeri-uzman atama + aylık dakika uygunluğu
```

### 2. Risk Değerlendirmesi
```
İSG Operasyonları → Risk Değerlendirmesi
  ├─ Tehlike Tanımlama (lokasyon bazlı)
  ├─ Risk Puanlama (olasılık × şiddet)
  ├─ Kontrol Önlemleri (elimination → PPE hiyerarşisi)
  └─ Yenileme Tetikleyicileri (kaza, taşınma, yeni ekipman)
```

### 3. İş Kazası Kaydı
```
İSG Kazası Yönetimi → İş Kazası
  ├─ Kaza Bilgileri: Türü (Accident/Near Miss/Disease), Şiddeti
  ├─ Yaralanma Detayları: Yaralanma türü, beden bölümü, kayıp gün
  ├─ SGK Bildirimi: Otomatik deadline (3 iş günü)
  ├─ Soruşturma: Bulgu kaydı
  ├─ Koku Analizi: CAPA bağlantısı
  └─ Dönüş Eğitimi: Otomatik isg_training.record oluştur
```

---

## 🔐 Güvenlik

### ACL (Erişim Kontrolü)
- **isg_security.group_isg_readonly:** Okuma yetki (reports, dashboards)
- **isg_security.group_isg_expert:** İSG Uzmanı (okuma-yazma, moderate yetkiler)
- **isg_security.group_isg_manager:** Tam kontrol (yaşam döngüsü, silme)

### KVKK (Kişisel Verileri Koruma Kanunu)
- Sağlık verisi ayrı ACL grubu (isg_health_officer)
- Maskeleme: Raporlarda "KGN001" (çalışan adı gösterilmez)
- Rıza takibi: consent_date field
- Erişim denetim kaydı: Loglanmış tüm erişimler

---

## 🛠️ Geliştirme

### Bağımlılıklar
```bash
# Python 3.10+
# PostgreSQL 12+
# Odoo 18.0 Community

# Python paketleri
pip install odoo==18.0
pip install python-dateutil
```

### Modül Yapısı
```
isg_module/
├── __manifest__.py
├── __init__.py
├── models/
│   ├── __init__.py
│   └── model_name.py
├── views/
│   └── views.xml
├── security/
│   └── ir.model.access.csv
├── data/
│   └── data.xml
└── README.md
```

### Naming Conventions
- **Sequence:** `ISG-XXX-YYYY-NNNN` (ör: ISG-KZA-2026-0001)
- **Model:** `isg.module.name` (ör: `isg.incident`)
- **Field:** `snake_case` (ör: `sgk_notification_date`)

---

## 📊 İstatistikler

| Metrik | Değer |
|--------|-------|
| Toplam Modül | 32 ana + 10 retrofit |
| Kurulu Odoo Modülü | 59 |
| Model Sayısı | 100+ |
| Kod Satırı (Python + XML) | 15,000+ |
| Commit Sayısı | 30+ |
| Proje Süresi | 30+ gün |
| HSE Radar Eşdeğerlik | %95+ |

---

## 📚 Dokümantasyon

- **SESSION.md** — Oturum özeti ve devam noktası
- **TASKS.md** — Görev listesi ve ilerleme
- **BACKLOG.md** — Gelecek geliştirmeler
- **CLAUDE.md** — Geliştirici bağlamı
- **ARCHITECTURE.md** — Sistem mimarisi

Detaylı belgeler `.claude/` dizininde.

---

## 🤝 Katkı Etme

1. Repo'yu fork et
2. Feature branch oluştur (`git checkout -b feature/isg-audit`)
3. Commit et (`git commit -am 'Add isg_audit module'`)
4. Push et (`git push origin feature/isg-audit`)
5. Pull Request aç

### Kod Standardları
- Python: PEP 8
- XML: Odoo 18 standards
- Commit mesajı: `[module]: açıklama (feature/fix)`

---

## 📝 Lisans

LGPL 3.0 — Bkz. [LICENSE](LICENSE)

---

## 👥 İletişim

- **GitHub Issues:** Hata raporları ve öneriler
- **Email:** info@kelvinaydinlatma.com.tr
- **Proje Sahibi:** [SHapeloglu](https://github.com/SHapeloglu)

---

## 🙏 Teşekkürler

- Odoo Community Edition
- OCA (Odoo Community Association)
- Türkiye İSG Mevzuatı Uzmanları
- [Riskmatik](https://www.riskmatik.com.tr/) — Referans benchmark

---

## 📌 Roadmap

- **Ağustos 2026:** FAZ 0-4 + OSGB + isg_incident tamamlandı ✅
- **Eylül 2026:** FAZ 2 (6 modül), FAZ 3, FAZ 5 hedefleniyor
- **Ekim 2026:** E3 Entegrasyonu (SGK, EKİPNET, İSG-KATİP, e-imza)
- **Q4 2026:** HSE Radar Kabul Testi, Üretim Hazırlığı

---

**Son Güncelleme:** 28 Ağustos 2026  
**Status:** Active Development — 32/32 Ana Modül Kurulu
