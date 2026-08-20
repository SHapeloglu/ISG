# -*- coding: utf-8 -*-
{
    'name': 'ISG Ölçüm Yönetimi — Çekirdek',
    'version': '18.0.1.0.0',
    'category': 'Health and Safety/ISG',
    'summary': 'Ölçüm kampanyası, cihaz kalibrasyon, numune ve sonuç kaydı — OEL/STEL uygunluk',
    'author': 'ISG Platform',
    'depends': [
        'isg_core',
        'isg_security',
        'isg_document',
        'isg_chemical',
        'isg_capa',
    ],
    'data': [
        'security/isg_measurement_security.xml',
        'security/ir.model.access.csv',
        'data/isg_measurement_sequence.xml',
        'views/isg_measurement_campaign_views.xml',
        'views/isg_measurement_device_views.xml',
        'views/isg_measurement_sample_views.xml',
        'views/isg_measurement_result_views.xml',
        'views/isg_measurement_limit_views.xml',
        'views/isg_measurement_menus.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
