{
    'name': 'İSG Party',
    'version': '18.0.1.0.0',
    'summary': 'İSG Platformu — Kurumsal Roller (OSGB, Laboratuvar, Alt İşveren, Tedarikçi)',
    'author': 'İSG Platform',
    'category': 'Health & Safety',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'isg_core', 'isg_security'],
    'data': [
        'security/ir.model.access.csv',
        'data/isg_party_data.xml',
        'views/isg_partner_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
