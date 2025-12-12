{
    'name': 'Library Book',
    'version': '1.0',
    'summary': 'Manage library books',
    'author': 'Dương',
    'category': 'Library',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',   # action nằm ở đây → phải load trước
        'views/library_menu.xml',         # menu load sau
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
