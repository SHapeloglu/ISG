# -*- coding: utf-8 -*-
{
    'name': 'ISG Ekipman ve Periyodik Kontrol',
    'version': '18.0.1.0.0',
    'category': 'Health and Safety/ISG',
    'summary': 'EK-II ekipman kataloğu, periyodik kontrol, EKİPNET entegrasyonu',
    'author': 'ISG Platform',
    'depends': [
        'isg_core',
        'isg_security',
        'isg_document',
        'isg_party',
    ],
    'data': [
        'security/isg_equipment_security.xml',
        'security/ir.model.access.csv',
        'data/isg_equipment_sequence.xml',
        'data/isg_equipment_type_data.xml',
        'views/isg_equipment_views.xml',
        'views/isg_equipment_menus.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
