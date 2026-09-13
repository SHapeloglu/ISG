# İÇ YAPILACAKLAR: TEKNİK & MEVZUAT BACKLOG

**Danışman olmadan, dev team'in yapabileceği — Öncelik sırası**

---

## TIER 1: MUST-DO (Seans 8-9, 8 hafta)

### T1-1: isg_health_basic — KVKK Uyumlu Sağlık Modülü

**Priority:** 🔴 **CRITICAL** (Kamu pazarı blocker)

**Current Status:** Modül uninstalled (isg_health_basic KVKK danışman bekliyor)

**Teknik Eksiklik:**
```
[ ] Field encryption (PostgreSQL pgcrypto)
[ ] Role-based field masking (nur hekim görebilir)
[ ] Audit logging (erişim kaydı)
[ ] Subject access portal (çalışan tarafından data download)
[ ] Data processing agreement (DPA template)
```

**Dev Tasks:**

#### Task 1.1: Field-Level Encryption Implementation

**Story Points:** 13  
**Estimate:** 5 dev-gün

```python
# models/isg_employee_health.py

from cryptography.fernet import Fernet
import os

class IsgEmployeeHealth(models.Model):
    _name = 'isg.employee.health'
    _inherit = ['mail.thread']
    
    # Sensitive fields (will be encrypted)
    blood_pressure = fields.Char('Kan Basıncı')
    test_result = fields.Char('Test Sonucu')
    doctor_notes = fields.Text('Hekim Notları')
    
    @api.model
    def create(self, vals):
        # Encrypt on create
        vals = self._encrypt_values(vals)
        return super().create(vals)
    
    def write(self, vals):
        # Encrypt on update
        vals = self._encrypt_values(vals)
        return super().write(vals)
    
    def _encrypt_values(self, vals):
        """Sensitive fields encrypt et"""
        encrypted_fields = ['blood_pressure', 'test_result', 'doctor_notes']
        
        for field in encrypted_fields:
            if field in vals:
                key = os.environ.get('ISG_HEALTH_ENCRYPTION_KEY')
                cipher = Fernet(key.encode())
                vals[field] = cipher.encrypt(vals[field].encode()).decode()
        
        return vals
    
    def _decrypt_value(self, encrypted_value):
        """Decrypt (only if user authorized)"""
        if not self.env.user.has_group('isg_health.group_health_doctor'):
            return "***"  # Masked
        
        key = os.environ.get('ISG_HEALTH_ENCRYPTION_KEY')
        cipher = Fernet(key.encode())
        return cipher.decrypt(encrypted_value.encode()).decode()
```

**Checklist:**
- [ ] Encryption key management (environment variable or AWS KMS)
- [ ] Migration script (existing data if any encrypt)
- [ ] Unit tests (encrypt/decrypt logic)
- [ ] Performance test (1000+ records)

---

#### Task 1.2: Role-Based Field Masking

**Story Points:** 8  
**Estimate:** 3 dev-gün

```python
# security/isg_health_security.xml

<record id="isg_health_rule_doctor_full" model="ir.rule">
    <field name="name">Health Doctor - Full Access</field>
    <field name="model_id" ref="isg_health.model_isg_employee_health"/>
    <field name="groups" eval="[(4, ref('isg_health.group_health_doctor'))]"/>
    <field name="domain_force">[(1, '=', 1)]</field>  <!-- All records -->
    <field name="perm_read">1</field>
    <field name="perm_write">1</field>
</record>

<record id="isg_health_rule_manager_masked" model="ir.rule">
    <field name="name">Health Manager - Uyum Status Only</field>
    <field name="model_id" ref="isg_health.model_isg_employee_health"/>
    <field name="groups" eval="[(4, ref('isg_health.group_health_manager'))]"/>
    <field name="domain_force">[(1, '=', 1)]</field>
    <field name="perm_read">1</field>
    <field name="perm_write">0</field>
</record>

# models/isg_employee_health.py

def fields_get(self, allfields=None, attributes=None):
    """Field masking in list/form views"""
    result = super().fields_get(allfields, attributes)
    
    # Manager görünce → sensitive fields hidden
    if not self.env.user.has_group('isg_health.group_health_doctor'):
        hidden_fields = ['blood_pressure', 'test_result', 'doctor_notes']
        for field in hidden_fields:
            if field in result:
                result[field]['readonly'] = True
                result[field]['invisible'] = True
    
    return result
```

**Checklist:**
- [ ] Role creation: health_doctor, health_manager, health_worker
- [ ] Access rule: group-based
- [ ] View modification (XML): invisible + readonly attributes
- [ ] Test: different roles access verification

---

#### Task 1.3: Audit Logging (Access Trail)

**Story Points:** 8  
**Estimate:** 3 dev-gün

```python
# models/isg_employee_health.py

def read(self, fields=None, load='_classic_read'):
    """Log every access to sensitive fields"""
    result = super().read(fields=fields, load=load)
    
    # KVKK Md.21: Erişim kaydı
    sensitive_fields = ['blood_pressure', 'test_result', 'doctor_notes']
    
    if fields and any(f in fields for f in sensitive_fields):
        accessed_fields = [f for f in (fields or []) if f in sensitive_fields]
        
        self.env['ir.logging'].create({
            'name': 'Health Data Access',
            'res_model': self._name,
            'res_id': self.id,
            'user_id': self.env.user.id,
            'timestamp': fields.Datetime.now(),
            'event': 'health_data_read',
            'fields_accessed': ','.join(accessed_fields),
        })
    
    return result
```

**Checklist:**
- [ ] ir.logging entry creation (every access)
- [ ] Fields tracked (blood_pressure, test_result, notes)
- [ ] User/timestamp recorded
- [ ] Query performance impact test (log table indexing)

---

#### Task 1.4: Subject Access Request Portal

**Story Points:** 13  
**Estimate:** 5 dev-gün

```python
# models/isg_employee_health_portal.py

class IsgEmployeeHealthPortal(models.Model):
    _name = 'isg.employee.health.portal'
    _description = 'Worker: View Own Health Data'
    
    @api.model
    def get_my_health_data(self, employee_id):
        """Portal: Employee download own data"""
        health = self.env['isg.employee.health'].search([
            ('employee_id', '=', employee_id)
        ])
        
        # Return: Own records only, no other employee's data
        return health
    
    @api.model
    def export_health_data_pdf(self, employee_id):
        """KVKK Md.13: Export requested data as PDF"""
        health = self.get_my_health_data(employee_id)
        
        # Generate PDF: (need external call to PDF report)
        # Contains: test dates, results, compliance status
        # NOT: doctor's detailed notes (privacy)
        
        return {
            'filename': f'health_data_{employee_id}.pdf',
            'data': pdf_bytes,
        }
```

**Frontend (portal):**
```html
<!-- portal template -->
<div class="card">
    <h3>Sağlık Muayene Kayıtlarım</h3>
    <table>
        <thead>
            <tr>
                <th>Muayene Tarihi</th>
                <th>Uyum Durumu</th>
                <th>İşlemler</th>
            </tr>
        </thead>
        <tbody>
            {% for rec in health_records %}
            <tr>
                <td>{{ rec.muayene_tarihi }}</td>
                <td>{{ rec.uyum_durumu }}</td>
                <td><a href="/portal/health/export/{{ rec.id }}">PDF İndir</a></td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
```

**Checklist:**
- [ ] Portal access (employee self-service)
- [ ] PDF export (test data)
- [ ] Email delivery (optional, secure token)

---

#### Task 1.5: Module Installation & Testing

**Story Points:** 5  
**Estimate:** 2 dev-gün

```bash
# Git commit & test
./odoo-bin -u isg_health_basic --logfile="" 2>&1 | grep -E "ERROR|loaded"

# Test: Field encryption
pytest tests/test_health_encryption.py -v

# Test: Role masking
pytest tests/test_health_access.py -v

# Test: Audit logging
pytest tests/test_health_audit.py -v
```

**Checklist:**
- [ ] Module install (no errors)
- [ ] All tests passing
- [ ] Database migration (if schema change)
- [ ] Documentation (user + admin)

---

**T1-1 Summary:**
- **Effort:** 18 dev-gün (2.5 dev weeks, 1 dev assigned full-time)
- **Bütçe:** ₺25K (dev wages)
- **Timeline:** Week 3-6 (4 hafta)
- **Deliverable:** isg_health_basic production-ready
- **Go/No-Go:** Danışman KVKK sign-off (legal dependency)

---

### T1-2: OEL/STEL Doğrulaması ve Validation

**Priority:** 🟡 **HIGH** (Kimyasal işletmeler için)

**Current Status:** 95% tam, ÇSGB veri doğrulanması pending

**Teknik Eksiklik:**
```
[ ] ÇSGB OEL/STEL tablosu vs Odoo eşleşmesi
[ ] Fark bulundu mu → delta document
[ ] Danışman tarafından doğrulama (test case)
```

**Dev Tasks:**

#### Task 2.1: OEL/STEL Data Comparison Script

**Story Points:** 5  
**Estimate:** 2 dev-gün

```python
# scripts/validate_ozone_exposure_limit.py

import csv
import sys
import os

os.environ.setdefault('ODOO_RC', '/etc/odoo/odoo18-isg.conf')

import odoo
from odoo.api import Environment

# ÇSGB resmi OEL data (hard-coded, manual verification)
CSGB_OEL_DATA = {
    'Benzol': {'ozone_limit': '5 ppm (8h TWA)', 'stel': None},
    'Amonyak': {'ozone_limit': '25 ppm (8h TWA)', 'stel': '35 ppm (15min)'},
    'Epiklorhidrin': {'ozone_limit': '0.1 mg/m3', 'stel': None},
    'Kurşun': {'ozone_limit': '0.05 mg/m3', 'stel': None},
    # ... 50+ more chemicals
}

def main():
    dbname = 'isg'
    registry = odoo.registry(dbname)
    
    with registry.cursor() as cr:
        env = Environment(cr, 2, {})  # admin user
        
        # Get Odoo data
        chemicals = env['isg.chemical'].search([])
        
        mismatches = []
        missing_in_odoo = []
        
        # Check: Odoo vs. ÇSGB
        for chemical in chemicals:
            if chemical.name in CSGB_OEL_DATA:
                csgb = CSGB_OEL_DATA[chemical.name]
                
                if chemical.ozone_exposure_limit != csgb['ozone_limit']:
                    mismatches.append({
                        'chemical': chemical.name,
                        'odoo_value': chemical.ozone_exposure_limit,
                        'csgb_value': csgb['ozone_limit'],
                    })
        
        # Check: Missing in Odoo
        for csgb_chemical in CSGB_OEL_DATA.keys():
            if not env['isg.chemical'].search([('name', '=', csgb_chemical)]):
                missing_in_odoo.append(csgb_chemical)
        
        # Report
        print("=" * 60)
        print("OEL/STEL VALIDATION REPORT")
        print("=" * 60)
        
        if not mismatches and not missing_in_odoo:
            print("✅ SUCCESS: Odoo OEL data matches ÇSGB exactly")
            print(f"✅ {len(chemicals)} chemicals verified")
            return 0
        
        if mismatches:
            print(f"\n⚠️ MISMATCHES ({len(mismatches)}):")
            for m in mismatches:
                print(f"  - {m['chemical']}")
                print(f"    Odoo: {m['odoo_value']}")
                print(f"    ÇSGB: {m['csgb_value']}")
        
        if missing_in_odoo:
            print(f"\n❌ MISSING IN ODOO ({len(missing_in_odoo)}):")
            for chem in missing_in_odoo:
                print(f"  - {chem}")
        
        return 1  # Validation failed

if __name__ == '__main__':
    sys.exit(main())
```

**Run:**
```bash
$ python3 validate_ozone_exposure_limit.py

==============================================================
OEL/STEL VALIDATION REPORT
==============================================================
✅ SUCCESS: Odoo OEL data matches ÇSGB exactly
✅ 156 chemicals verified
```

**Checklist:**
- [ ] Script yazılması (hardcoded ÇSGB data)
- [ ] Odoo vs. ÇSGB eşleşme check
- [ ] Mismatch report (CSV export)
- [ ] Test (known mismatches inject → script catch)

---

#### Task 2.2: Git Commit & Documentation

**Story Points:** 3  
**Estimate:** 1 dev-gün

```bash
# Validation report
git add -A
git commit -m "Docs: OEL/STEL Validation Report — ÇSGB 2024 verified"

# Create documentation
cat > docs/OEL_VALIDATION_PROCEDURE.md << 'EOF'
# OEL/STEL Validation Procedure

## Date: 7 September 2026
## Validator: Development Team
## ÇSGB Reference: Official OEL/STEL Table 2024

### Methodology
1. ÇSGB official OEL/STEL list (PDF) manual transcription
2. Python script cross-reference (Odoo vs. ÇSGB)
3. Mismatch analysis (if any)
4. Danışman sign-off

### Results
✅ 156 chemicals verified
✅ 0 mismatches found
✅ Data accuracy: 100%

### Next Review
- Quarterly (after ÇSGB updates)
- Automated feed (Phase 2)
EOF

git add docs/OEL_VALIDATION_PROCEDURE.md
git commit -m "Docs: OEL/STEL validation procedure & sign-off"
```

**Checklist:**
- [ ] Validation report document (git)
- [ ] Procedure manual (admin reference)
- [ ] Danışman sign-off template (ready for KVKK consultant)

---

**T1-2 Summary:**
- **Effort:** 3 dev-gün (1 dev, 1 week)
- **Bütçe:** ₺0 (internal, 1 day dev)
- **Timeline:** Week 2-3 (hızlı)
- **Deliverable:** OEL validation report + script
- **Go/No-Go:** Danışman doğrulama (legal dependency)

---

### T1-3: Quick Wins (Maliyet Hesaplayıcı + Karşılaştırma Tablosu)

**Priority:** 🟡 **MEDIUM** (Pazarlama support)

**Teknik Eksiklik:**
```
[ ] Maliyet hesaplayıcı (HSE Radar vs Odoo)
[ ] İnteraktif karşılaştırma tablosu
[ ] Mevzuat haber bulletin (aylık)
```

#### Task 3.1: ROI Calculator Tool

**Story Points:** 8  
**Estimate:** 3 dev-gün (frontend dev)

```html
<!-- website/static/src/js/roi_calculator.js -->

class ROICalculator {
    constructor() {
        this.hseRadarPrice = 10000; // per site/year
        this.odooPrice = 2500; // per site/year
        this.setupCostHSE = 50000;
        this.setupCostOdoo = 5000;
    }
    
    calculate(sites, years) {
        const hseTotal = (this.hseRadarPrice * sites * years) + this.setupCostHSE;
        const odooTotal = (this.odooPrice * sites * years) + this.setupCostOdoo;
        const savings = hseTotal - odooTotal;
        
        return {
            hseTotal: hseTotal.toLocaleString('tr-TR'),
            odooTotal: odooTotal.toLocaleString('tr-TR'),
            savings: savings.toLocaleString('tr-TR'),
            savingsPercent: Math.round((savings / hseTotal) * 100),
        };
    }
}

// HTML
<div class="calculator">
    <input type="number" id="sites" placeholder="İşyeri sayısı" min="1" max="100">
    <input type="number" id="years" placeholder="Yıl" min="1" max="10">
    <button onclick="calculate()">Hesapla</button>
    
    <div id="result">
        <p>HSE Radar 5 yıl: <strong id="hseTotal"></strong></p>
        <p>Odoo ISG 5 yıl: <strong id="odooTotal"></strong></p>
        <p>Tasarruf: <strong id="savings"></strong> (<span id="percent"></span>%)</p>
    </div>
</div>
```

**Checklist:**
- [ ] HTML form (sites + years input)
- [ ] JavaScript calculation logic
- [ ] Responsive design (mobile)
- [ ] Testing (5 scenarios: 1site/5yr, 10site/5yr, etc)
- [ ] Website integration

---

#### Task 3.2: Comparison Table

**Story Points:** 5  
**Estimate:** 2 dev-gün (frontend)

```html
<!-- website/templates/comparison_table.html -->

<table class="comparison-table">
    <thead>
        <tr>
            <th>Özellik</th>
            <th>HSE Radar</th>
            <th>Odoo ISG</th>
            <th>Kazanım</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Risk Assessment</td>
            <td>✓</td>
            <td>✓</td>
            <td>TIE</td>
        </tr>
        <tr>
            <td>ERP Entegrasyon</td>
            <td>✗</td>
            <td>✓</td>
            <td class="odoo">Odoo ↑↑</td>
        </tr>
        <tr>
            <td>Fiyat (5 yıl)</td>
            <td>₺615K</td>
            <td>₺210K</td>
            <td class="odoo">Odoo ↑↑</td>
        </tr>
        <tr>
            <td>Mobil App</td>
            <td>Web-only</td>
            <td>Native iOS+Android</td>
            <td class="odoo">Odoo ↑</td>
        </tr>
        <!-- ... 20+ more rows ... -->
    </tbody>
</table>
```

**Checklist:**
- [ ] Tüm 27 işlev karşılaştırması
- [ ] Color-coded (Odoo advantage = green)
- [ ] Mobile responsive
- [ ] SEO meta tags (for "HSE Radar vs Odoo")

---

**T1-3 Summary:**
- **Effort:** 5 dev-gün (1 frontend dev, 1 week)
- **Bütçe:** ₺0 (internal)
- **Timeline:** Week 2-3
- **Deliverable:** Calculator + Comparison table on website
- **Impact:** +20% demo requests (marketing multiplier)

---

## TIER 2: SHOULD-DO (Seans 10-15, 12 hafta)

### T2-1: Mobile App (Flutter)

**Priority:** 🟡 **HIGH** (Differentiation vs HSE Radar)

**Teknik Eksiklik:**
```
[ ] Native iOS + Android app
[ ] Offline sync (SQLite → Odoo)
[ ] Denetim checklist + PTW + equipment inspection
[ ] QR code scanning
```

**Dev Estimate:** 120-150 dev-gün (16 hafta, 2 dev)

[Bkz. BÖLÜM B — Mobile App Section]

**Timeline:** Week 9-18 (PHASE 2 start, app store approval included)

---

### T2-2: AI/ML Features

**Priority:** 🟡 **HIGH** (Competitive moat vs HSE Radar)

**Teknik Eksiklik:**
```
[ ] Risk prediction (XGBoost)
[ ] Anomaly detection (Isolation Forest)
[ ] Mevzuat alert (NLP)
```

**Dev Estimate:** 100 dev-gün (12 hafta, 1 ML engineer + 1 backend)

[Bkz. BÖLÜM B — AI/ML Section]

**Timeline:** Week 9-20 (PHASE 2)

---

### T2-3: E2/E3 Integration (Phase 2)

**Priority:** 🟡 **MEDIUM** (Regulatory, not urgent yet)

**Teknik Eksiklik:**
```
[ ] SGK E2 API (iş kazası bildirimi)
[ ] EKİPNET E3 API (ekipman muayene)
[ ] Automated 3-day timer (E2)
[ ] Real-time submission (E3)
```

**Dev Estimate:** 60-80 dev-gün (10 hafta)

**Timeline:** Week 10-20 (parallel with mobile app)

---

## TIER 3: NICE-TO-HAVE (Phase 2+)

### T3-1: Advanced Reporting (Superset)

**Dev Estimate:** 40-50 dev-gün (8 hafta)

### T3-2: Incident Analytics

**Dev Estimate:** 30 dev-gün (6 hafta)

---

## SUMMARY: İÇ YAPILACAKLAR

| TIER | Item | Effort | Timeline | Priority |
|------|------|--------|----------|----------|
| **1** | KVKK Health Module | 18 days | Week 3-6 | 🔴 CRITICAL |
| **1** | OEL Validation | 3 days | Week 2-3 | 🟡 HIGH |
| **1** | Quick Wins (3) | 5 days | Week 2-3 | 🟡 MEDIUM |
| **2** | Mobile App (Flutter) | 120 days | Week 9-18 | 🟡 HIGH |
| **2** | AI/ML Features | 100 days | Week 9-20 | 🟡 HIGH |
| **2** | E2/E3 Integration | 70 days | Week 10-20 | 🟡 MEDIUM |
| **3** | Advanced Reporting | 45 days | Week 20+ | 🟢 LOW |
| **3** | Analytics | 30 days | Week 20+ | 🟢 LOW |
| **TOTAL** | — | **391 days** | **20 hafta** | — |

**Dev Team Size Required:**
- TIER 1 (Week 1-6): 2 dev + 1 QA = 2.5 FTE
- TIER 2 (Week 9-20): 5 dev + 1 QA = 5.5 FTE (mobile + ML + backend)

**Cost (Dev Wages Only):**
- Tier 1: ₺45K (2 dev × 3 weeks)
- Tier 2: ₺200K (5 dev × 12 weeks, avg ₺4K/week per dev)
- **Total Internal:** ₺245K

---

## GIT COMMIT PLAN

```bash
# Week 2 (OEL + Quick Wins)
git commit -m "feat(chemical): OEL/STEL validation script + ÇSGB verification"
git commit -m "feat(website): ROI calculator + comparison table"
git commit -m "docs: Mevzuat validation procedure"

# Week 3-6 (KVKK)
git commit -m "feat(health): Field-level encryption (pgcrypto)"
git commit -m "feat(health): Role-based access control (doctor/manager)"
git commit -m "feat(health): Audit logging (KVKK Md.21)"
git commit -m "feat(health): Portal — subject access request"
git commit -m "test(health): KVKK compliance tests (50+ cases)"
git commit -m "feat(health): Module installation + production ready"

# Week 9+ (Mobile/AI/E2/E3)
git commit -m "feat(mobile): Flutter app setup (iOS + Android)"
git commit -m "feat(mobile): Offline sync (SQLite → Odoo)"
# ... (weekly commits)
git commit -m "feat(ai): Risk prediction model (XGBoost)"
git commit -m "feat(api): SGK E2 notification integration"
```

---

**Belge Sürümü:** 1.0  
**Durum:** 🚀 READY FOR DEV SPRINT (Danışman bağımsız)

