from odoo import models, fields
from ..repositories.author_repository import AuthorRepository

class BookstoreAuthor(models.Model):
    _name = 'bookstore.author'
    _description = 'Autor'

    name = fields.Char(string='Nombre', required=True)
    biography = fields.Text(string='Biografía')

    @staticmethod
    def get_author_by_name(name):
        return AuthorRepository.get_author_by_name(name)
