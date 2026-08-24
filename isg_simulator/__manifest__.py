# -*- coding: utf-8 -*-
{
    'name': 'ISG - Müfettiş Simülasyonu',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/ISG',
    'summary': 'İşyeri profiline göre uygunluk değerlendirmesi ve tahmini ceza simülasyonu',
    'author': 'ISG Platform Contributors',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'isg_core',
        'isg_legislation',
        'isg_compliance',
        'isg_penalty',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_simulator_run_views.xml',
        'data/isg_simulator_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
