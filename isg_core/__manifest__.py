{
    'name': 'İSG Core',
    'version': '18.0.1.0.0',
    'summary': 'İSG Platformu — Temel Mimari (Holding/Şirket/İşyeri/Site)',
    'description': """
        Odoo 18 İSG Platformunun temel modülü.
        Holding → Şirket → İSG İşyeri → Fiziksel Site hiyerarşisini tanımlar.
        Tüm diğer İSG modülleri bu modüle bağımlıdır.
    """,
    'author': 'İSG Platform',
    'category': 'Health & Safety',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_workplace_views.xml',
        'views/isg_site_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
