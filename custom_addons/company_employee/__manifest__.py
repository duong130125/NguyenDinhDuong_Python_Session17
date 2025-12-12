{
    'name': 'Company Employee Management',
    'version': '1.0',
    'summary': 'Manage company employees and their details',
    'author': 'Dương',
    'category': 'Human Resources',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
