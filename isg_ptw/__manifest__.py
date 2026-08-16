# -*- coding: utf-8 -*-
{
    'name': 'ISG İş İzni ve LOTO Sistemi',
    'version': '18.0.1.0.0',
    'category': 'Health and Safety/ISG',
    'summary': 'Permit to Work (PTW), LOTO, ön koşul kontrol listeleri, çok aşamalı onay',
    'author': 'ISG Platform',
    'depends': [
        'isg_core',
        'isg_security',
        'isg_document',
        'isg_capa',
    ],
    'data': [
        'security/isg_ptw_security.xml',
        'security/ir.model.access.csv',
        'data/isg_ptw_sequence.xml',
        'data/isg_ptw_type_data.xml',
        'views/isg_ptw_views.xml',
        'views/isg_ptw_menus.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
