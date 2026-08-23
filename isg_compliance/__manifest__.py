{
    'name': 'ISG Uygunluk Değerlendirmesi',
    'version': '18.0.1.0.0',
    'category': 'ISG/Compliance',
    'summary': 'İşyeri uygunluk değerlendirmesi, yükümlülük takibi, kanıt kontrolü',
    'author': 'ISG Dev Team',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'isg_legislation',
        'isg_capa',
        'isg_document',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/isg_compliance_views.xml',
        'views/isg_compliance_evidence_views.xml',
        'data/isg_compliance_demo.xml',
    ],
    'external_dependencies': {
        'python': [],
    },
    'application': False,
    'installable': True,
    'auto_install': False,
}
