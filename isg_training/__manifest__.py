{
    'name': 'İSG Eğitim Yönetimi',
    'version': '18.0.1.0.0',
    'category': 'İSG Platform',
    'summary': 'Eğitim planı, katılım kaydı, 2 Nisan 2026 yönetmelik uyumu',
    'author': 'ISG Platform',
    'depends': ['hr', 'isg_core', 'isg_security', 'isg_document', 'isg_hr', 'isg_base'],
    'data': [
        'security/ir.model.access.csv',
        'data/isg_training_type_data.xml',
        'views/isg_training_type_views.xml',
        'views/isg_training_plan_views.xml',
        'views/isg_training_record_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
