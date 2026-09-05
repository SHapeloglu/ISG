{
    'name': 'ISG Raporlama ve KPI Dashboard',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/ISG',
    'summary': 'TRIR, LWDR ve İSG performans göstergeleri raporlama modülü + QWeb PDF şablonları',
    'description': """
ISG Raporlama Modülü
=====================
- TRIR (Total Recordable Incident Rate) hesaplama
- LWDR (Lost Workday Rate) hesaplama
- Frequency Rate / Severity Rate
- İşyeri bazlı periyodik KPI snapshot
- Dashboard (grafik/pivot görünüm)
- QWeb PDF rapor şablonları (F5-002):
  * Risk Değerlendirmesi Raporu
  * Kaza/Ramak Kala Raporu
  * Denetim Raporu
  * Ekipman Periyodik Kontrol Raporu (EKİPNET)
  * İş Hijyeni Ölçüm Raporu
    """,
    'author': 'ISG Platform',
    'depends': [
        'isg_core',
        'isg_incident',
        'isg_audit',
        'isg_capa',
        'isg_risk',
        'isg_ppe',
        'isg_equipment',
        'isg_measurement_hygiene',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_reporting_views.xml',
        'views/isg_reporting_menus.xml',
        'reports/isg_risk_assessment_report.xml',
        'reports/isg_incident_report.xml',
        'reports/isg_audit_report.xml',
        'reports/isg_equipment_report.xml',
        'reports/isg_measurement_report.xml',
        'reports/isg_report_actions.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
