from odoo import models, fields
from ..repositories.customer_repository import CustomerRepository

class BookstoreCustomer(models.Model):
    _name = 'bookstore.customer'
    _description = 'Cliente'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico')
    purchase_history = fields.One2many('bookstore.book', 'author_id', string='Historial de Compras')

    @staticmethod
    def get_customer_by_email(email):
        return CustomerRepository.get_customer_by_email(email)