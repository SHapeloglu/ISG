{
    'name': 'İSG İnsan Kaynakları',
    'version': '18.0.1.0.0',
    'category': 'İSG Platform',
    'summary': 'Çalışan İSG profili: SEG, işyeri ataması, uzman/hekim süre bağlantısı',
    'author': 'ISG Platform',
    'depends': ['hr', 'isg_core', 'isg_security', 'isg_document'],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_hr_employee_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
