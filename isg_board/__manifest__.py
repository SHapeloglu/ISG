# -*- coding: utf-8 -*-
{
    'name': 'İSG Kurulu Yönetimi',
    'version': '18.0.1.0.0',
    'category': 'İSG',
    'summary': '6331 md.22 İSG Kurulu ve Toplantı Yönetimi',
    'author': 'İSG Platform',
    'depends': ['isg_core', 'isg_security', 'isg_hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/isg_board_data.xml',
        'views/isg_board_member_views.xml',
        'views/isg_board_meeting_views.xml',
        'views/isg_board_decision_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
