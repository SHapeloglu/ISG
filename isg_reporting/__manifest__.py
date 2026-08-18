{
    'name': 'ISG Raporlama ve KPI Dashboard',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/ISG',
    'summary': 'TRIR, LWDR ve İSG performans göstergeleri raporlama modülü',
    'description': """
ISG Raporlama Modülü
=====================
- TRIR (Total Recordable Incident Rate) hesaplama
- LWDR (Lost Workday Rate) hesaplama
- Frequency Rate / Severity Rate
- İşyeri bazlı periyodik KPI snapshot
- Dashboard (grafik/pivot görünüm)
- QWeb PDF rapor şablonları (F5-002'de eklenecek)
    """,
    'author': 'ISG Platform',
    'depends': [
        'isg_core',
        'isg_incident',
        'isg_audit',
        'isg_capa',
        'isg_risk',
        'isg_ppe',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_reporting_views.xml',
        'views/isg_reporting_menus.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
