{
    'name': 'İSG Risk Değerlendirmesi',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/ISG',
    'summary': 'Risk Değerlendirmesi Yönetmeliği kapsamında tehlike tanımlama, risk puanlama (L Matrisi / Fine-Kinney) ve kontrol önlemleri yönetimi',
    'description': """
İSG Risk Değerlendirmesi
=========================
- Risk ekibi tanımı (6331 md.10 kapsamı)
- Tehlike tanımlama ve risk puanlama (L Matrisi ve Fine-Kinney)
- Kontrol önlemleri hiyerarşisi (Ortadan Kaldırma -> KKD)
- Kalıntı risk hesaplama
- Yenileme koşulları (kaza, taşınma, yeni ekipman, periyodik)
- Yüksek risk için otomatik DÖF (isg_capa) bağlantısı
    """,
    'author': 'ISG Platform',
    'depends': [
        'isg_core',
        'isg_security',
        'isg_hr',
        'isg_location',
        'isg_document',
        'isg_capa',
    ],
    'data': [
        'security/isg_risk_security.xml',
        'security/ir.model.access.csv',
        'data/isg_risk_sequence.xml',
        'views/isg_risk_assessment_views.xml',
        'views/isg_risk_line_views.xml',
        'views/isg_risk_menus.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
