{
    'name': 'ISG Çalışan Sağlık Modülü (KVKK Uyumlu)',
    'version': '18.0.1.0.0',
    'category': 'Occupational Health & Safety',
    'author': 'ISG Development Team',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'isg_base',
        'isg_hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/isg_health_security.xml',
        'views/isg_employee_health_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
