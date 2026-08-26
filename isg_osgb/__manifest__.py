{
    'name': 'İSG OSGB Planlama ve Görevlendirme',
    'version': '18.0.1.0.0',
    'summary': 'OSGB İşyeri Uzman/Hekim Atama, Süre Kontrolü, Kapasite Planlama',
    'description': """
        Ortak Sağlık ve Güvenlik Birliği (OSGB) yönetim modülü.
        - OSGB profili ve kadrosu (uzman/hekim)
        - İşyeri-uzman atama ve aylık ziyaret takibi
        - 6331 s.K. md.6 gereken/fiili süre uygunluk kontrolü
        - Kapasite planlama ve İSG-KATİP hazırlığı
    """,
    'author': 'İSG Platform',
    'category': 'Health & Safety',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'isg_core', 'isg_hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_osgb_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
