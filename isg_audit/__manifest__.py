# -*- coding: utf-8 -*-

{
    'name': 'İSG Denetim ve Kontrol Listeleri',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/ISG',
    'summary': 'Denetim planı, kontrol listesi şablonları, bulgu kaydı ve DÖF bağlantısı',
    'author': 'ISG Platform',
    'depends': [
        'isg_core',
        'isg_security',
        'isg_hr',
        'isg_location',
        'isg_document',
        'isg_capa',
    ],
    'data': [
        'security/isg_audit_security.xml',
        'security/ir.model.access.csv',
        'data/isg_audit_sequence.xml',
        'views/isg_audit_template_views.xml',
        'views/isg_audit_views.xml',
        'views/isg_audit_finding_views.xml',
        'views/isg_audit_menus.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
