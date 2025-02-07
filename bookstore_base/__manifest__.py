{
    'name': 'Bookstore Base',
    'version': '1.0',
    'summary': 'Módulo base para manejo de librería',
    'category': 'Ventas',
    'author': 'Edwin Fandiño',
    'depends': ['base'],
      'data': [
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/author_views.xml',
        'views/book_views.xml',
        'views/customer_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}