{
    'name': 'ISG - Mevzuat ve Yükümlülük Motoru',
    'version': '18.0.1.0.0',
    'category': 'ISG',
    'summary': 'Türkiye İSG mevzuatı, yükümlülük tanımı ve uygulanabilirlik kuralları',
    'author': 'ISG Development Team',
    'depends': ['base', 'isg_core', 'isg_document'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/isg_legislation_views.xml',
        'views/isg_obligation_views.xml',
        'data/isg_legislation_data.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
