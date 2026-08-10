{
    'name': 'İSG Alt İşveren Yönetimi',
    'version': '18.0.1.0.0',
    'category': 'İSG Platform',
    'summary': 'Alt işveren zinciri, belge matrisi, çalışan bildirimi',
    'author': 'ISG Platform',
    'depends': ['base', 'mail', 'isg_core', 'isg_security', 'isg_document', 'isg_party'],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_contractor_views.xml',
        'views/isg_contractor_document_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
