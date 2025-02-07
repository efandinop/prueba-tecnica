{
    'name': 'Inventario de Librería',
    'version': '1.0',
    'summary': 'Gestión de stock y ventas de libros',
    'category': 'Ventas',
    'author': 'Edwin Fandiño',
    'depends': ['bookstore_base'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/inventory_views.xml',
        'views/sale_views.xml',
        'views/menu_views.xml',
        'views/audit_log_views.xml',

    ],
    'installable': True,
    'application': False,
}
