{
    'name': 'İSG Temel Altyapı',
    'version': '18.0.1.0.0',
    'category': 'İSG Platform',
    'summary': 'UUID mixin, entegrasyon outbox, retry/hata günlüğü',
    'author': 'ISG Platform',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
