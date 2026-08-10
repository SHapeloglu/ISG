# -*- coding: utf-8 -*-
{
    'name': 'İSG Ziyaretçi Yönetimi',
    'version': '18.0.1.0.0',
    'category': 'İSG',
    'summary': 'Ziyaretçi Kayıt, Giriş/Çıkış ve KKD Bildirimi',
    'author': 'İSG Platform',
    'depends': ['isg_core', 'isg_security', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/isg_visitor_data.xml',
        'views/isg_visitor_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
