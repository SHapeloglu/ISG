# -*- coding: utf-8 -*-
{
    'name': 'ISG - Risk Değerlendirmesi',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/ISG',
    'summary': 'İşyeri risk değerlendirmesi, tehlike analizi ve kontrol önlemleri yönetimi (6331 md.10, Risk Değerlendirmesi Yönetmeliği)',
    'author': 'ISG Platform Contributors',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'isg_core',
        'isg_capa',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_risk_matrix_views.xml',
        'views/isg_risk_hazard_views.xml',
        'views/isg_risk_assessment_views.xml',
        'data/isg_risk_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
