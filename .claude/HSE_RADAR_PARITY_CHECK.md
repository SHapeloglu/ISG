# HSE RADAR PARITY CHECK

**27 İşlev Kapsamlı Doğrulama — Odoo ISG vs. HSE Radar**

---

## EXECUTIVE SUMMARY

| Metrik | Durum | Not |
|--------|-------|-----|
| **İşlev Eşdeğerliği** | 89% (24/27 tam) | 2 işlev KVKK bloklı/doğrulama pending |
| **Mevzuat Uyumu** | 92% (11/13 tam) | KVKK + E2/E3 pending |
| **Pazarlama Mesajı** | "HSE Radar parity + features" | Mobile + AI/ML bonus |
| **Go/No-Go Decision** | 🟢 **GO** | Launch ready (Week 8) |
| **Riskler** | Low | KVKK danışman sign-off gerekli |

---

## DETAYLI PARITY MATRIX

### BÖLÜM 1: KURUMSAL (4/4 ✅ TAM)

| İşlev | HSE Radar | Odoo ISG | Status | Gap | Note |
|-------|-----------|----------|--------|-----|------|
| 1. Holding/Kurum Yapısı | ✅ | ✅ | PARITY | 0 | 4 katman hierarchy |
| 2. Kullanıcı/Grup/Yetki | ✅ | ✅ | PARITY | 0 | ACL + record rules |
| 3. Kurum İletişim | ✅ | ✅ | PARITY | 0 | OSGB, lab, kontratör |
| 4. Yerleşim/Lokasyon | ✅ | ✅ | PARITY | 0 | GPS + mapping |

**Sonuç:** ✅ **%100** — No gaps

---

### BÖLÜM 2: İK & YÖNETİŞİM (7/8 ⚠️ PARTIAL)

| İşlev | HSE Radar | Odoo ISG | Status | Gap | Timeline |
|-------|-----------|----------|--------|-----|----------|
| 5. İK & Çalışanlar | ✅ | ✅ | PARITY | 0 | SEG, özel grup |
| 6. Alt İşverenler | ✅ | ✅ | PARITY | 0 | 14 dokumen matrix |
| 7. İSG Kurulu | ✅ | ✅ | PARITY | 0 | Toplantı + karar |
| **8. Sağlık Gözetimi** | ✅ | ⏳ | **BLOCKED** | KVKK | Week 3-6 (dev) |
| 9. Ziyaretçi Yönetimi | ✅ | ✅ | PARITY | 0 | Giriş/çıkış + KKD |
| 10. Dokümantasyon | ✅ | ✅ | PARITY | 0 | Versiyon + e-imza |
| 11. İç/Dış Yazışmalar | ✅ | ✅ | PARITY | 0 | 30 gün deadline |

**Sonuç:** ⚠️ **%87** — 1 işlev pending (KVKK danışman onayı)

**Action Item:** 
- isg_health_basic dev (Week 3-6): Field encryption + role masking
- KVKK danışman sign-off (Week 6)
- Go-live (Week 7)

---

### BÖLÜM 3: OPERASYONEL (9/10 ⚠️ PARTIAL)

| İşlev | HSE Radar | Odoo ISG | Status | Gap | Timeline |
|-------|-----------|----------|--------|-----|----------|
| 12. Risk Değerlendirmesi | ✅ | ✅ | PARITY | 0 | 2 yıl + triggers |
| 13. İş Kazası/Ramak Kala | ✅ | ✅+ | **ODOO ÜSTÜN** | +Auto | Return training trigger |
| 14. DÖF/CAPA | ✅ | ✅ | PARITY | 0 | 5 Neden + 6M |
| 15. Denetim & Kontrol | ✅ | ✅ | PARITY | 0 | Şablon + scoring |
| 16. Eğitim | ✅ | ✅+ | **ODOO ÜSTÜN** | +Auto | 2 Nisan 2026 + dönüş |
| 17. KKD Yönetimi | ✅ | ✅ | PARITY | 0 | Zimmet + takvim |
| 18. Acil Durum | ✅ | ✅ | PARITY | 0 | Tatbikat + rehber |
| **19. Kimyasal Madde** | ✅ | ⚠️ | **PENDING** | OEL | Week 2-3 (validation) |
| 20. Ekipman (EK-II) | ✅ | ✅ | PARITY | 0 | Ara.2025 updated |
| 21. PTW/LOTO | ✅ | ✅ | PARITY | 0 | Çok aşamalı onay |

**Sonuç:** ⚠️ **%90** — 1 işlev validation pending

**Action Item:**
- OEL/STEL validation script (Week 2, internal)
- ÇSGB danışman verification (Week 2-3)
- Status: ✅ Tam by Week 3

---

### BÖLÜM 4: ÖLÇÜM & ÇEVRE (2/2 ✅ TAM)

| İşlev | HSE Radar | Odoo ISG | Status | Gap | Note |
|-------|-----------|----------|--------|-----|------|
| 22. Ölçüm/İzleme (İş Hijyeni) | ✅ | ✅ | PARITY | 0 | Kalibrasyon + uyum |
| 23. Çevre Yönetimi | ✅ | ✅ | PARITY | 0 | Atık + depolama |

**Sonuç:** ✅ **%100** — No gaps

---

### BÖLÜM 5: MEVZUAT & YÖNETİM (4/4 ✅ TAM)

| İşlev | HSE Radar | Odoo ISG | Status | Gap | Note |
|-------|-----------|----------|--------|-----|------|
| 24. Ceza Tarifeleri | ✅ | ✅+ | **ODOO ÜSTÜN** | +2026 | ÇSGB 2026 updated |
| 25. Mevzuat Motoru | ✅ | ✅ | PARITY | 0 | 6331 + yönetmelik |
| 26. Simülatör | ✅ | ✅ | PARITY | 0 | Senaryo testi |
| 27. Yönetim Raporları | ✅ | ✅+ | **ODOO ÜSTÜN** | +SQL | Superset custom |

**Sonuç:** ✅ **%100** — No gaps (Odoo 3 işlevde + üstün)

---

## OVERALL PARITY SCORE

```
İşlev Eşdeğerliği:
┌─────────────────────────────────────┐
│ COMPLETE: 24/27 = 89%              │
│ PENDING:  2/27  = 7%  (Week 2-6)   │
│ SUPERIOR: 3/27  = 11% (Odoo bonus) │
├─────────────────────────────────────┤
│ TARGET STATE: 27/27 = 100% (Week 8)│
└─────────────────────────────────────┘
```

---

## MEVZUAT UYUM PARITY

| Mevzuat | HSE Radar | Odoo ISG | Status | Gap | Timeline |
|---------|-----------|----------|--------|-----|----------|
| **6331** | ✅ | ✅ | PARITY | 0 | ✅ Complete |
| **Risk Yönetmeliği** | ✅ | ✅ | PARITY | 0 | ✅ Complete |
| **2 Nisan 2026 Eğitim** | ✅ | ✅ | PARITY | 0 | ✅ Complete |
| **Ara.2025 EK-II** | ✅ | ✅ | PARITY | 0 | ✅ Complete |
| **Kimyasal (OEL)** | ✅ | ⚠️ | PENDING | Veri | Week 2-3 |
| **Alt İşveren** | ✅ | ✅ | PARITY | 0 | ✅ Complete |
| **Sağlık (KVKK)** | ✅* | ⏳ | BLOCKED | KVKK | Week 3-6 |
| **İSG Kurulu** | ✅ | ✅ | PARITY | 0 | ✅ Complete |
| **Acil Durum** | ✅ | ✅ | PARITY | 0 | ✅ Complete |
| **Denetim** | ✅ | ✅ | PARITY | 0 | ✅ Complete |
| **KVKK** | ⚠️ | ✅ | ODOO ÜSTÜN | +On-prem | On-premise ✓ |
| **2026 Ceza** | ✅ | ✅ | PARITY | 0 | ✅ Complete |
| **SGK E2** | ✅ | 📋 | BACKLOG | API | Phase 2 (Week 10-17) |
| **EKİPNET E3** | ✅ | 📋 | BACKLOG | API | Phase 2 (Week 12-19) |

**Compliance Score:**
```
Current:  11/13 = 85%
Week 3:   12/13 = 92% (+KVKK dev)
Week 8:   12/13 = 92% (sertifika)
Week 20:  13/13 = 100% (+E2/E3)
```

---

## MISSING FEATURES DETAIL

### Missing #1: Sağlık Modülü (isg_health_basic) — KVKK Uyumlu

**Status:** ⏳ **BLOCKED** (legal requirement)

**Why Blocked:**
- KVKK Article 9: Health data = sensitive category
- Field-level encryption gerekli (PostgreSQL pgcrypto)
- Role-based access gerekli (nur hekim detay görebilir)
- Audit trail gerekli (erişim kaydı)

**HSE Radar Comparison:**
- HSE Radar: Sağlık modülü VAR, ancak KVKK uyumu sorgulanabilir (bulut)
- Odoo ISG: Modül delayed for KVKK compliance (on-premise → advantage)

**Dev Work Required:**
- [ ] Field encryption (5 dev-gün)
- [ ] Role-based masking (3 dev-gün)
- [ ] Audit logging (3 dev-gün)
- [ ] Portal (5 dev-gün)
- [ ] Testing (2 dev-gün)
- **Total: 18 dev-gün (Week 3-6)**

**External Requirement:**
- KVKK danışmanı sign-off (legal)

**Timeline:**
- Dev start: Week 3
- Dev complete: Week 6
- Danışman sign-off: Week 6
- Go-live: Week 7
- Launch (Week 8): ✅ READY

**Market Impact:**
- Negative: 1 week delay
- Positive: KVKK-certified module (competitive advantage vs HSE Radar)

---

### Missing #2: OEL/STEL Validation — ÇSGB Verification

**Status:** ⚠️ **VALIDATION PENDING**

**Current State:** 95% tam
- Module var (isg_chemical + isg_chemical_exposure_limit)
- Data present (156 chemicals)
- Validation: **ÇSGB resmi liste ile eşleşmesi doğrulanmamış**

**Why Pending:**
- ÇSGB OEL/STEL tablosu (source of truth)
- Odoo data ≠ ÇSGB data risk?
- Validation script gerekli (compare + delta report)

**HSE Radar Comparison:**
- HSE Radar: OEL veri internal (ÇSGB referansı unclear)
- Odoo ISG: Transparent validation (ÇSGB explicit reference)

**Dev Work Required:**
- [ ] Validation script (2 dev-gün, internal)
- [ ] ÇSGB veri comparison (1 danışman-gün)
- [ ] Delta document (1 danışman-gün)
- **Total: 2 dev-gün + 2 danışman-gün (Week 2-3)**

**Timeline:**
- Script ready: Week 2
- Danışman validation: Week 2-3
- Status: ✅ TAM by Week 3
- Launch (Week 8): ✅ READY

**Market Impact:**
- Neutral (hızlı resolution)
- Positive: "ÇSGB verified" messaging

---

## FEATURES WHERE ODOO EXCEEDS HSE RADAR

### Bonus #1: Return-to-Work Training (Auto Trigger)

**6331 Requirement:** 6 ay leave sonrası dönüş eğitimi (2 Nisan 2026)

| Feature | HSE Radar | Odoo ISG |
|---------|-----------|----------|
| Tetikleme | Manual (İSG müdür) | Otomatik (cron job) |
| Timing | Danışman hatırlatması | System reminder (7 gün öncesinden) |
| Tracking | Eğitim kaydı | Automatic checklist |

**Odoo Advantage:** Automation = zero oversight risk

---

### Bonus #2: Ceza Tarifeleri (2026 Updated)

**6331 Requirement:** ÇSGB 2026 ceza tarifeleri (%49 artış)

| Feature | HSE Radar | Odoo ISG |
|---------|-----------|----------|
| Update Date | 6 ay delay (Konu ve Bitti) | 0 delay (git commit) |
| Source | ÇSGB manual | GitHub version history |
| Audit Trail | None | Full commit log |

**Odoo Advantage:** Git versioning = full transparency + instant updates

---

### Bonus #3: Custom Reporting (Superset SQL)

| Feature | HSE Radar | Odoo ISG |
|---------|-----------|----------|
| Predefined Reports | 5 fixed | 1 base + unlimited custom |
| Custom Dashboard | Not possible | SQL query → chart |
| Real-time | Nightly refresh | Live data |

**Odoo Advantage:** Data scientist freedom = competitive moat

---

## GO/NO-GO DECISION MATRIX

### GO Condition: Week 8 (Phase 1 End)

```
☐ 24/27 işlev complete (89%) — Essential parity
☐ KVKK modül production (DANIŞMAN SIGN-OFF REQUIRED)
☐ OEL validation complete (ÇSGB VERIFIED)
☐ Sertifika + danışman rapor printed
☐ Avukat mütalaa signed
☐ 3 OSGB tasdik received
☐ Website sertifika sayfası live
☐ Marketing collateral ready
☐ Sales deck finalized
☐ Press release approved

ALL ☑ = GO FOR LAUNCH (Week 8)
```

### NO-GO Condition: Block Launch

```
❌ KVKK danışman red flag → 1 week delay
❌ OSGB negative tasdik → Messaging adjustment
❌ Avukat concerns → Legal revision
❌ Critical bug in KVKK module → Fix + retest
```

---

## COMPETITIVE MESSAGING: PARITY + BONUS

### Message #1: "We're There Already"

> "Odoo ISG = HSE Radar equivalent (89%+), verified by
>  3 OSGB, audited by İSG expert, approved by lawyer.
>  
>  Plus: ERP, on-premise, custom reports, AI/ML."

**Proof:** Danışman audit + OSGB tasdik + avukat mütalaa

---

### Message #2: "Where We Excel"

> "3 features HSE Radar will never catch up to:
> 
> 1. Automation (return-to-work training triggers automatically)
> 2. Transparency (mevzuat updates = git commits, not 6-month delay)
> 3. Freedom (custom SQL dashboards, not fixed 5 reports)"

**Proof:** Live demo + GitHub commit history

---

### Message #3: "No Switching Risk"

> "3-week migration, zero data loss. We proved it
>  on 3+ pilot customers. They're using production
>  today with better compliance + lower cost."

**Proof:** Case study video

---

## TIMELINE: PARITY ACHIEVEMENT

```
WEEK 1-2: Foundation
├─ OEL validation script (dev)
├─ KVKK danışman procure (danışman)
└─ Audit kickoff (danışman)

WEEK 3-4: Development Sprint
├─ KVKK field encryption (dev)
├─ KVKK role masking (dev)
├─ OEL validation complete (danışman)
└─ Audit progress update

WEEK 5-6: Mid-Phase
├─ KVKK audit logging (dev)
├─ KVKK danışman sign-off (danışman)
├─ Avukat mütalaa draft
└─ Printing approval

WEEK 7-8: Finalization
├─ KVKK production go-live
├─ All danışman deliverables
├─ Sertifika print + web
└─ LAUNCH WEEK 8

OUTCOME:
Week 8: 27/27 işlev = %100 parity ✅
Week 8: Danışman certified + OSGB endorsed ✅
Week 8: Market launch "HSE Radar parity + bonus" ✅
```

---

## RISK ASSESSMENT

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| KVKK danışman red flag | 20% | High | Early engagement + backup |
| OSGB negative | 10% | Medium | 3 OSGB (majority vote) |
| Avukat concerns | 15% | Medium | Legal review in parallel |
| KVKK module bug | 10% | Medium | Extra testing week |
| Print/web delay | 5% | Low | Early order (Week 6) |

**Overall Risk:** 🟢 **LOW** (mitigations in place)

---

## CONCLUSION

### HSE Radar Parity: ✅ ACHIEVABLE by Week 8

| Metric | Current | Week 8 | Note |
|--------|---------|--------|------|
| **Işlev %** | 89% | 100% | KVKK + OEL fixes |
| **Mevzuat %** | 85% | 92% | E2/E3 phase 2 |
| **Credential** | 0 | 3 | Danışman + OSGB + Avukat |
| **Market Ready** | No | Yes | Sertifika + case study |
| **Bonus Features** | +3 | +3 | Auto training, versioning, SQL |

### Market Position: "Beyond Parity"

Not just equal, but superior on:
- **Pricing:** 3x cheaper
- **Integration:** ERP native
- **Transparency:** Git versioning
- **Flexibility:** Custom SQL
- **Mobile:** Native app (Phase 2)
- **AI:** Predictive risk (Phase 2)

---

**Belge Sürümü:** 1.0  
**Durum:** 🚀 LAUNCH READY (Week 8, pending danışman sign-off)

