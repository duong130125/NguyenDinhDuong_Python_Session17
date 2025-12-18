{
    'name': 'IT support ticket',
    'version': '1.0',
    'category': 'Unknown',
    'summary': 'Ứng dụng quản lý sự cố IT',
    'depends': ['base'],
    'data': [
        'security/it_groups.xml',
        'security/ir.model.access.csv',
        'security/it_rules.xml',
        'views/it_ticket_views.xml',
    ],
    'installable': True,
    'application': True,
    'author': 'Dương',
    'license': 'LGPL-3'
}