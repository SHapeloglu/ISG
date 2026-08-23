# -*- coding: utf-8 -*-
{
    'name': 'ISG - İdari Para Cezaları',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/ISG',
    'summary': 'Türkiye İSG idari para cezası tarifesi ve hesaplama motoru (ÇSGB 2026)',
    'description': """
İSG İdari Para Cezaları
========================
6331 sayılı İSG Kanunu md.26 kapsamında idari para cezası tarifesi.
isg_compliance modülündeki uygunsuzluklara bağlı olası ceza hesaplaması.

* isg.penalty.tariff — Ceza tarife kataloğu (madde, tutar, çarpan)
* isg.penalty — Fiili/olası ceza kaydı (compliance kaydına bağlı)
    """,
    'author': 'ISG Platform',
    'depends': ['base', 'isg_core', 'isg_compliance'],
    'data': [
        'security/ir.model.access.csv',
        'data/isg_penalty_sequence.xml',
        'data/isg_penalty_tariff_data.xml',
        'views/isg_penalty_tariff_views.xml',
        'views/isg_penalty_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
