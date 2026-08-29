# -*- coding: utf-8 -*-
{
    'name': 'İSG Çevre Yönetimi',
    'version': '18.0.1.0.0',
    'category': 'İSG',
    'summary': 'Atık Yönetimi, Depolama, Bertaraf',
    'author': 'ISG Team',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mail',
        'isg_core',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/isg_environment_security.xml',
        'views/isg_waste_code_views.xml',
        'views/isg_waste_storage_views.xml',
        'views/isg_waste_disposal_views.xml',
        'data/isg_waste_code_data.xml',
        'views/isg_environment_menus.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
