# -*- coding: utf-8 -*-
{
    'name': 'İSG DÖF/CAPA Yönetimi',
    'version': '18.0.1.0.0',
    'category': 'İSG',
    'summary': 'Düzeltici ve Önleyici Faaliyet Yönetimi',
    'author': 'İSG Platform',
    'depends': ['isg_core', 'isg_security', 'isg_hr', 'isg_document', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/isg_capa_data.xml',
        'views/isg_capa_views.xml',
        'views/isg_capa_action_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
