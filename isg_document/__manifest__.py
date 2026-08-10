{
    'name': 'İSG Belge ve Kanıt Yönetimi',
    'version': '18.0.1.0.0',
    'category': 'İSG Platform',
    'summary': 'Belge/kanıt altyapısı: hash, sürüm, kilit, e-imza',
    'description': """
İSG Belge ve Kanıt Yönetimi
============================
- ir.attachment üzerine SHA-256 hash hesaplama
- isg.document: sürüm numarası, geçerlilik tarihi
- Kilit mekanizması (onaylanan belge değiştirilemez)
- e-imza alanları (5070 s.K. uyumlu)
    """,
    'author': 'ISG Platform',
    'depends': ['base', 'mail', 'isg_core', 'isg_security'],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_document_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
