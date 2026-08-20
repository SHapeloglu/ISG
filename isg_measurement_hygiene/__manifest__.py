# -*- coding: utf-8 -*-
{
    'name': 'ISG Ölçüm — Hijyen Parametreleri (F3-002)',
    'version': '18.0.1.0.0',
    'category': 'ISG/Measurement',
    'author': 'ISG Platform',
    'license': 'LGPL-3',
    'depends': [
        'isg_measurement_core',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/isg_measurement_result_views.xml',
    ],
    'installable': True,
    'application': False,
}
