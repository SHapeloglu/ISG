# -*- coding: utf-8 -*-
{
    'name': 'ISG Mevzuat — Yükümlülük Motoru (F4-001)',
    'version': '18.0.1.0.0',
    'category': 'ISG/Legislation',
    'author': 'ISG Platform',
    'license': 'LGPL-3',
    'depends': [
        'isg_core',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_legislation_views.xml',
        'views/isg_obligation_views.xml',
    ],
    'installable': True,
    'application': False,
}
