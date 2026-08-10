# -*- coding: utf-8 -*-
{
    'name': 'İSG Yazışma Takibi',
    'version': '18.0.1.0.0',
    'category': 'İSG',
    'summary': 'Gelen/Giden Resmi Yazışma ve Yasal Süre Takibi',
    'author': 'İSG Platform',
    'depends': ['isg_core', 'isg_security', 'isg_document', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/isg_correspondence_data.xml',
        'views/isg_correspondence_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
