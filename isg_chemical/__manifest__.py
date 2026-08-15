# -*- coding: utf-8 -*-
{
    'name': 'ISG Kimyasal Yönetimi',
    'version': '18.0.1.0.0',
    'category': 'Health and Safety/ISG',
    'summary': 'Kimyasal envanter, GBF/SDS yönetimi ve tehlike sınıflandırması',
    'author': 'ISG Platform',
    'depends': [
        'isg_core',
        'isg_security',
        'isg_document',
    ],
    'data': [
        'security/isg_chemical_security.xml',
        'security/ir.model.access.csv',
        'data/isg_chemical_sequence.xml',
        'views/isg_chemical_views.xml',
        'views/isg_chemical_menus.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
