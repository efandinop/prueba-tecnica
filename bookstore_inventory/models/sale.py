from odoo import models, fields
from ..repositories.sale_repository import SaleRepository

class BookstoreSale(models.Model):
    _name = 'bookstore.sale'
    _description = 'Venta de Libros'

    customer_id = fields.Many2one('bookstore.customer', string='Cliente', required=True)
    book_id = fields.Many2one('bookstore.book', string='Libro', required=True)
    quantity = fields.Integer(string='Cantidad', required=True, default=1)
    sale_date = fields.Date(string='Fecha de Venta', required=True)

    @staticmethod
    def get_sales_by_customer(customer_id):
        return SaleRepository.get_sales_by_customer(customer_id)