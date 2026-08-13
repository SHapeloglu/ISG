# -*- coding: utf-8 -*-
{
    'name': 'İSG Acil Durum Planı ve Tatbikat',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/ISG',
    'summary': 'Acil durum planı hazırlama, tatbikat planı ve kaydı, tahliye planı',
    'author': 'ISG Platform',
    'depends': [
        'isg_core',
        'isg_security',
        'isg_hr',
        'isg_location',
        'isg_document',
    ],
    'data': [
        'security/isg_emergency_security.xml',
        'security/ir.model.access.csv',
        'data/isg_emergency_sequence.xml',
        'views/isg_emergency_views.xml',
        'views/isg_emergency_menus.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
