{
    'name': 'Gestión de Clientes Librería',
    'version': '1.0',
    'summary': 'Manejo de clientes y sus preferencias',
    'category': 'Ventas',
    'author': 'Edwin Fandiño',
    'depends': ['bookstore_base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/customer_preferences_views.xml',
        'views/menu_views.xml',
        'views/audit_log_views.xml',
    ],
    'installable': True,
    'application': False,
}
