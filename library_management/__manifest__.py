{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Module for managing library books and issues',
    'author': 'KM',
    'depends': ['base', 'mail'],
    'data': [
        'views/knyga_views.xml',
        'views/zanras_views.xml',
        'views/knygos_isdavimas_views.xml',
        'data/knygos_isdavimas_cron.xml',
        'report/knygos_isdavimas_report.xml',
    ],
    'installable': True,
    'application': True,
}