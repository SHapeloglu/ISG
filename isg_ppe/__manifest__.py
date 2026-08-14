# -*- coding: utf-8 -*-
{
    'name': 'İSG KKD Yönetimi',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/ISG',
    'summary': 'KKD envanter, zimmet kaydı, yenileme takibi ve isg_hr beden ölçüleri entegrasyonu',
    'author': 'ISG Platform',
    'depends': [
        'isg_core',
        'isg_security',
        'isg_hr',
        'isg_location',
        'isg_document',
    ],
    'data': [
        'security/isg_ppe_security.xml',
        'security/ir.model.access.csv',
        'data/isg_ppe_sequence.xml',
        'data/isg_ppe_type.xml',
        'views/isg_ppe_views.xml',
        'views/isg_ppe_menus.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
