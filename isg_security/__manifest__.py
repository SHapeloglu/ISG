{
    'name': 'İSG Security',
    'version': '18.0.1.0.0',
    'summary': 'İSG Platformu — Rol Matrisi ve Erişim Kontrolü',
    'author': 'İSG Platform',
    'category': 'Health & Safety',
    'license': 'LGPL-3',
    'depends': ['base', 'isg_core'],
    'data': [
        'security/isg_groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/res_users_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
