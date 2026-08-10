{
    'name': 'İSG Location',
    'version': '18.0.1.0.0',
    'summary': 'İSG Platformu — Fiziksel Lokasyon Ağacı (Kampüs/Fabrika/Bina/Kat/Hat/Saha)',
    'author': 'İSG Platform',
    'category': 'Health & Safety',
    'license': 'LGPL-3',
    'depends': ['base', 'isg_core', 'isg_security'],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_site_ext_views.xml',
        'views/isg_assembly_point_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
