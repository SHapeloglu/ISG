# CLAUDE.md — Geliştirme Rehberi ve Kararlar

## Kültür & İlkeler

### 1. HSE Radar Referanslı Geliştirme
- **Hedef:** HSE Radar ile fonksiyonel eşdeğerlik
- **Kural:** HSE Radar'da olmayan özellikler ayrı backlog'a (TASKS.md Feature Borcu)
- **Neden:** Müşteri beklentisi ve pazar paritesi

### 2. Oturum Başı Doğrulama (KRİTİK)
- Her oturumun başında VPS'te gerçek dosya durumunu `ls`/`cat` ile kontrol et
- SESSION.md **sadece doğrulanmış durumu** yansıt
- **Ders:** Önceki oturumlarda "başlatıldı" gibi belirsiz notlar → çakışan taslak dosyalar → sürpriz hatalar

### 3. Komut Disiplini
- Terminal komutları **tek tek** çalıştır — pasting çok komuta sebep olur
- Çıktı sonrası Claude tanıdır ve bir sonraki adımı verir
- Hatalı komutu görmek önemli (gerçek hatanın kaynağı)

### 4. Test-Sonra-Geliştir
- Model → manifest → security → data → view → kurulum
- Her modülün tarayıcı testini yapmadan GitHub push etme

### 5. Kalite Gatekeeping
- `store=True` olmayan compute alanlar search domain'de kullanılamaz
- Related alanlar parent'taki tipi miras alır, selection parametresi gereksiz
- `ondelete='set default'` geçersiz (base field'ın default'u yoksa) → 'cascade' kullan
- Selection_add eklenen seçenek için doğru ondelete seç

## Teknik Desenler

### A. Alan Adlandırması

İngilizce fieldler: _id, _date, _count (Odoo standart)
Türkçe string'ler: "Çalışan", "Denetim" vb. (label olarak)
Sequence alanları: _sequence, default=10 (editable=True embedded list'te)
### B. Durum Makinesi Dekoratörü
```python
state = fields.Selection([
    ('draft', 'Taslak'),
    ('in_progress', 'Devam Ediyor'),
    ('done', 'Tamamlandı'),
], default='draft', tracking=True, copy=False)

# Action metodları
def action_start(self): self.write({'state': 'in_progress'})
def action_done(self): self.write({'state': 'done'})

# View header'da statusbar_visible
<field name="state" widget="statusbar" statusbar_visible="draft,in_progress,done"/>
```

### C. Many2one Domain Filtre
```python
# Form'da linked field kısıtlama
site_id = fields.Many2one('isg.site', 
    domain="[('workplace_id', '=', workplace_id)]")

# **Uyarı:** Nested ilişki (assessment_id.workplace_id) alan-seviyesi domain'de çalışmaz
# Düzelt: View'da context ile veya computed filter
```

### D. Compute Alanı — Store Gereksinimi
```python
# Search/filter kullanacaksa MUTLAKA store=True
field_count = fields.Integer(compute='_compute_count', store=True)

# Sadece display için readonly olabilir
display_name = fields.Char(compute='_compute_display', store=False)
```

### E. DÖF Entegrasyonu Şablonu
```python
def action_create_capa(self):
    self.ensure_one()
    if self.capa_id:
        raise UserError('Zaten DÖF var: %s' % self.capa_id.name)
    
    capa = self.env['isg.capa'].create({
        'workplace_id': self.workplace_id.id,
        'source': 'risk_assessment',  # veya 'audit' vb.
        'severity': 'critical' if self.is_critical else 'medium',
        'description': 'Açıklama — %s' % self.name,
    })
    self.capa_id = capa.id
    return {...}  # action dialog
```

## Dosya Yapısı (Standart)modül_adı/
├── manifest.py # name, depends, data (sıra önemli)
├── init.py # from . import models
├── models/
│ ├── init.py # from . import model_adı
│ └── model_adı.py # Model sınıfları
├── views/
│ ├── model_views.xml # list, form, search, action
│ └── menus.xml # menuitem
├── security/
│ ├── model_security.xml # record rule (ir.rule)
│ └── ir.model.access.csv # ACL (readonly/expert/manager)
└── data/
├── sequence.xml # ir.sequence (prefix ISG-XX-YYYY-NNNN)
└── lookups.xml # Standart veri (KKD türleri vb.)## Manifest Kontrol Listesi

```python
{
    'name': 'Türkçe Adı',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/ISG',
    'summary': 'Kısa açıklama',
    'author': 'ISG Platform',
    
    # Bağımlılıklar (minimum: isg_core, isg_security)
    'depends': [
        'isg_core', 'isg_security', 'isg_hr', ...
    ],
    
    # Veri dosyaları (order matters!)
    'data': [
        'security/ir_model_access.csv',
        'security/model_security.xml',
        'data/sequences.xml',
        'data/lookups.xml',
        'views/model_views.xml',
        'views/menus.xml',
    ],
    
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
```

## Ortak Hatalar & Çözümler

| Hata | Sebep | Çözüm |
|------|-------|-------|
| `TypeError: Type of related field inconsistent` | Related alanın tipi parent'ta farklı | grep parent field, select. tipini eşle |
| `Unsearchable field in domain` | Compute alanında store=True yok | store=True ekle |
| `selection attribute ignored (related field)` | Related'da selection param. gereksiz | Parametreyi sil (tip otomatik gelir) |
| `ondelete='set default' invalid` | Base field'da default yok | ondelete='cascade' yap |
| `unknown parameter 'invisible'` | Model seviyesinde invisible (view parametresi) | Parametreyi sil, view'a taşı |
| `Failed to load registry` | Manifest veya import hatası | tail -50 kurulum çıktısı, grep ERROR |
| Module kurulmuyor (`--logfile=""` gerekli) | Config file'da logfile path tanımlı, stderr'e gitmez | `--logfile=""` flag'i zorunlu |

## Git İş Akışı

```bash
# Her oturumun sonunda
git add -A
git commit -m "F2-XXX modül_adı tamamlandı — açıklama"
git push origin main  # SSH key setup gerekli (ileri)

# GitHub SSH (gelecekteki oturum)
ssh-keygen -t ed25519 -C "email@example.com"
cat ~/.ssh/id_ed25519.pub  # GitHub Settings → SSH Keys'e kopyala
git remote set-url origin git@github.com:SHapeloglu/ISG.git
```

## Önemli VPS Komutları

```bash
# Modül kurulumu
sudo systemctl stop odoo18-isg.service
sudo -u odoo /opt/odoo/venv18-isg/bin/python3 /opt/odoo/odoo18/odoo-bin \
  -c /etc/odoo/odoo18-isg.conf --logfile="" -d isg \
  -i modül_adı --stop-after-init 2>&1 | tail -50
sudo systemctl start odoo18-isg.service

# Hata tanısı
sudo grep -A 30 "Failed to load registry" /var/log/odoo/odoo18-isg.log

# Dosya kontrol
sudo cat /opt/odoo/isg_addons/modül_adı/models/__init__.py
sudo ls -la /opt/odoo/isg_addons/modül_adı/

# Sahiplik düzelt
sudo chown -R odoo:odoo /opt/odoo/isg_addons/modül_adı/
```

## Tasarım Kararları Bu Projede

### Risk Puanlama
- **Fine-Kinney:** Standart Kinney-Wiruth (0.2–10 × 0.5–10 × 1–100)
- **L Matrisi:** 5×5, max 25 puan
- **Threshold:** Fine-Kinney <20 acceptable, 20–400 aralığında basaçak
- **Neden:** Standart endüstri, HSE Radar uyumluluğu, denetçi beklentisi

### KKD Verisi
- **18 Standart Türü:** Baret, eldiven, gözlük, ayakkabı, tulum vb.
- **CE Standartları:** EN 397, EN 388, EN ISO 20345 vb. (belirtilmiş)
- **Ömürler:** Teknisyen spec'i (eldiven 12 ay, tulum 24 ay vb.)
- **Beden Entegrasyonu:** isg_hr'daki clothing/shoe/glove size'ları zimmet'te göster

### Sequence Formatı
- **Tüm Modüller:** `ISG-XX-YYYY-NNNN` (XX = modül kodu, YYYY = yıl, NNNN = 4 haneli numara)
- **Örnekler:** ISG-RD-2026-0001 (risk), ISG-KZ-2026-0001 (incident), ISG-KKD-2026-0001 (ppe)

### DÖF Entegrasyonu
- **Yüksek Risk:** risk_line.risk_level in ('high', 'intolerable') → otomatik DÖF aç
- **Audit Bulgusu:** audit_line.result == 'nok' + is_critical=True → otomatik DÖF
- **Source Seçeneği:** isg.capa'ya 'risk_assessment', 'audit', vb. eklendi (selection_add)

## Sonraki Oturum Kontrol Listesi[ ] SESSION.md / TASKS.md / CLAUDE.md gz dosyasını yükle
[ ] VPS'te ls ile gerçek dosya durumunu doğrula
[ ] GitHub SSH setup (şifreyle push başarısız)
[ ] F2-007 isg_chemical başla:
- OEL/STEL tablosu
- MSDS linkage
- Depolama matrisi
- İkinci el risk assessment
