# F2-002 isg_risk — TAMAMLANDI ✅ (10 Ağustos 2026)

## Oluşturulan Dosyalar
- models/isg_risk_assessment.py — Ana değerlendirme modeli
- models/isg_risk_line.py — Tehlike/risk satır modeli  
- models/isg_capa_ext.py — isg.capa modeline risk_assessment_id eklendi
- views/isg_risk_assessment_views.xml
- views/isg_risk_line_views.xml
- views/isg_risk_menus.xml
- security/isg_risk_security.xml
- security/ir.model.access.csv
- data/isg_risk_sequence.xml

## Öğrenilen Dersler
- Odoo 18 list view: widget="badge" üzerinde decoration-* kullanılamaz
- Embedded list'te parent field'a erişim: parent.method (method değil)
- isg.capa genişletmesi isg_risk içinde _inherit ile yapıldı

## Modeller
- isg.risk.assessment — Sequence: ISG-RD-YYYY-NNNN
- isg.risk.line
- isg.capa (_inherit, risk_assessment_id eklendi)

## Sıradaki
F2-003 isg_incident — İş Kazası / Ramak Kala
