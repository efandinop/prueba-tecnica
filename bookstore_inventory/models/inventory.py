from odoo import models, fields
from ..repositories.inventory_repository import InventoryRepository

class BookstoreInventory(models.Model):
    _name = 'bookstore.inventory'
    _description = 'Inventario de Libros'

    book_id = fields.Many2one('bookstore.book', string='Libro', required=True)
    quantity = fields.Integer(string='Cantidad en Inventario', required=True, default=0)

    @staticmethod
    def get_stock_by_book(book_id):
        return InventoryRepository.get_stock_by_book(book_id)