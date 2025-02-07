from odoo import models, fields
from ..repositories.book_repository import BookRepository

class BookstoreBook(models.Model):
    _name = 'bookstore.book'
    _description = 'Libro'

    title = fields.Char(string='Título', required=True)
    author_id = fields.Many2one('bookstore.author', string='Autor', required=True)
    publication_year = fields.Integer(string='Año de Publicación')
    price = fields.Float(string='Precio')
    stock = fields.Integer(string='Inventario', default=0)

    @staticmethod
    def get_books_by_author(author_id):
        return BookRepository.get_books_by_author(author_id)