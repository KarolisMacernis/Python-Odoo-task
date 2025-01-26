{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Module for managing library books and issues',
    'author': 'KM',
    'category': 'Library',
    'description': """
        This module helps in managing library books and their issuance.
        Features include:
        - Registering books with title, description, number of pages, and genres.
        - Issuing books to contacts with start and end dates, and status tracking.
        - Automated reminders for overdue books.
        - Reporting on book issuance history.
    """,
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