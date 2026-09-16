# BACKLOG.md — Seans 12 Sonrası Roadmap & Open Issues

## 📅 Immediate Horizon (Seans 13-14)

### Seans 13: isg_training B-10 (Planned Next)
**Goal:** April 2, 2026 Regulation Compliance + Incident→Return Training Trigger

**Scope:**
- Training module scaffold (model, views, ACL)
- Training types: Orientation, Refresher, Specialized, Return-to-work
- Attendance tracking, certificate management
- Incident trigger: When incident.status='closed', auto-create training records for affected workers
- Regulation applicability: RG 33212 article mapping
- Integration: isg_incident, isg_location (by tehlike_sınıfı)

**Estimate:** 2-3 days  
**Blockers:** None (independent)  
**Risk:** Incident model interface (if changed last sync)

### Seans 14 (Optional): isg_health_basic Enhancements
**Scope:**
- Encryption key rotation (generate new key, re-encrypt all physician_notes)
- Audit log retention policy (30/90/365 day tiers)
- Batch audit log cleanup script (via ir.cron)
- Audit log read tracking (optional, adds noise)

**Estimate:** 1-1.5 days  
**Blockers:** None  
**Dependencies:** S12 encryption working

## 🎯 Medium Term (Seans 15-17, ~1 month)

### B-4: isg_legislation Retrofit (KVKK-Compliant)
- Mevzuat records: Add KVKK compliance tag / data classification
- Obligation applicability: Privacy-aware display
- Integration: isg_health_basic sensitive field references

**Estimate:** 1-2 days  
**Status:** Scoped, not started

### B-8, B-9: Other Mevzuat Tasks
- (Details in IC_YAPILACAKLAR_DEV_BACKLOG.md)
- Combined: ~1-2 days

### F5-002, F5-003: PDF Reports
- isg_legislation compliance report template (RG 33212 checklist)
- isg_occupational_disease risk assessment report
- HSE Radar feature parity check

**Estimate:** 1 day  
**Dependencies:** reportlab or built-in Odoo PDF

## 🔒 Blocked Issues (Cannot Proceed Without)

### ₺300K Faz 1 Bütçe Onayı (CRITICAL)
- **Status:** Awaiting decision (as of Sept 16, 2026)
- **Impact:** If YES → Proceed to consultant RFP. If NO → Pause Phase 1.
- **Timeline:** Expected end of September 2026
- **Action:** Decision-maker to confirm by Sept 30

### Danışmanlık RFP (Dependent on Budget)
- **Target Firms:** 5 IT consulting companies (₺139-164K total Phase 1)
- **RFP Document:** A_DANISMANLIK_VE_ONAYLA_R_PAKETI.md (ready)
- **Scope:** KVKK audit, HSE Radar feature gap analysis, regulatory certification support
- **Action:** Send RFP if budget approved

### res.users.workplace_ids Attribute Definition
- **Purpose:** Record rule domains need to filter by user's assigned workplaces
- **Scope:** Extends hr.employee with workplace_id (Many2many?) relationship
- **Status:** TODO, would unblock workplace-based access control
- **Estimate:** 4-6 hours

## 🚨 Known Limitations & TODOs

### isg_health_basic
- [x] Encryption implemented (Fernet)
- [x] Audit log implemented
- [ ] Encryption key rotation script (scheduled)
- [ ] Audit log read tracking (optional)
- [ ] Audit log archival (1yr+ retention)
- [ ] Record rules for workplace access control (pending res.users.workplace_ids)

### isg_training (B-10)
- [ ] Model scaffold
- [ ] Incident trigger logic
- [ ] Certificate generation (optional PDF)
- [ ] Attendance/completion tracking

### isg_incident
- [ ] Verify model interface hasn't changed (last sync: S11)
- [ ] Status field: Ensure 'closed' state exists
- [ ] Worker assignment: One2many linking to incidents

### General
- [ ] Contabo VPS egress whitelist for github.com:443 (admin task, reduces push friction)
- [ ] Permanent encryption key strategy (currently fallback to generated)
- [ ] Multi-database testing (currently dev-only, 1 DB)

## 📊 Open Decisions

1. **Audit Log Retention Policy**
   - Option A: Keep indefinitely (audit compliance, storage cost)
   - Option B: Archive after 1 year to separate table
   - Option C: Delete after 365 days
   - Recommendation: B (compliance + manageable size)

2. **Encryption Key Management**
   - Option A: Environment variable only (ISG_ENCRYPTION_KEY)
   - Option B: File-based fallback + env var (current)
   - Option C: Vault integration (HashiCorp, AWS KMS)
   - Recommendation: Current (B) for MVP; upgrade to C if enterprise

3. **Record Rule Strategy**
   - Option A: User.workplace_ids attribute (current plan)
   - Option B: User.department_id (HR standard)
   - Option C: Custom assignment table (overkill)
   - Recommendation: A (org structure aligned)

## 📈 Estimated Phase 1 Timeline (If Budget OK)
Sept 16-30: RFP sent, consultant procurement (2 weeks)
Oct 1-15: Consultant starts (KVKK audit, HSE feature gap, etc.) (2 weeks)
Oct 16-31: Dev completes B-10, B-4/8/9, F5-002/003 (3 weeks)
Nov 1-15: Consultant sign-off, certification prep (2 weeks)
Nov 16-30: Final testing, HSE Radar pilot comparison (2 weeks)
Total: ~8-9 weeks, 26 developer-days + consultant days
Cost: ₺300K Phase 1 (dev time + consultant)

If budget NOT approved: Continue with lower-priority backlog (Seans 13+ self-funded).

## 🎓 Learning Outcomes (Seans 11-12)

- Odoo 18 field parameter rules (invisible, tracking limits)
- Fernet symmetric encryption patterns
- Compute + inverse field pattern (transparent field masking)
- Create/write/unlink hooks for audit logging
- XML record ordering & ref path resolution

## 🔗 Related Docs
- `SESSION.md` — This seans work summary
- `TASKS.md` — Active task list
- `CLAUDE.md` — Dev guidelines
- `ARCHITECTURE.md` — Module dependencies
- `IC_YAPILACAKLAR_DEV_BACKLOG.md` — Detailed dev sprint tasks
- `HSE_RADAR_PARITY_CHECK.md` — Feature comparison matrix
- `A_DANISMANLIK_VE_ONAYLA_R_PAKETI.md` — RFP document

