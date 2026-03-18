# -*- coding: utf-8 -*-
{
    'name': 'Portfolio Web',
    'version': '19.0.1.0.0',
    'summary': 'Portafolio web profesional para desarrolladores Odoo',
    'description': """
        Módulo para gestionar y publicar un portafolio profesional de desarrollador Odoo.
        Incluye:
        - Vista backend tipo "ficha de desarrollador" con ribbon de disponibilidad
        - Página web pública accesible en /portafolio
        - Toggle dark/light mode con persistencia en localStorage
    """,
    'author': 'Jordan Andres Pincay Vinces',
    'website': '',
    'category': 'Website',
    'depends': ['website', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/portfolio_developer_views.xml',
        'views/portfolio_website_templates.xml',
        'views/portfolio_backend_template.xml',
        'views/portfolio_quiz_views.xml',
        'views/portfolio_quiz_template.xml',
        'data/portfolio_demo_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'portafolio_web/static/src/css/portfolio_website.css',
            'portafolio_web/static/src/js/portfolio_website.js',
            'portafolio_web/static/src/css/portfolio_backend.css',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
