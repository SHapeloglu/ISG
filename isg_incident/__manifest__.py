{
    'name': 'İSG İş Kazası Yönetimi',
    'version': '18.0.1.0.0',
    'summary': 'İş kazası, ramak kala, meslek hastalığı kaydı, SGK bildirimi, dönüş eğitimi',
    'description': """
        İş Kazası Yönetim Modülü
        - İş kazası / ramak kala / meslek hastalığı kaydı (6331 s.K. md.14)
        - SGK 3 iş günü bildirimi uyarı sistemi
        - Yaralanma detayı (tür, beden bölümü, kayıp gün)
        - Koku analizi (CAPA) bağlantısı
        - Otomatik dönüş eğitimi tetikleyicisi
        - TRIR/LWDR hesabına entegrasyon
    """,
    'author': 'İSG Platform',
    'category': 'Health & Safety',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'isg_core', 'isg_capa', 'isg_training'],
    'data': [
        'security/ir.model.access.csv',
        'data/isg_incident_sequence.xml',
        'views/isg_incident_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
