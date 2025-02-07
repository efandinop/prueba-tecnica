from odoo import api, SUPERUSER_ID

class BookRepository:
    @staticmethod
    def get_books_by_author(author_id):
        env = api.Environment(api.cr, SUPERUSER_ID, {})
        return env['bookstore.book'].search([('author_id', '=', author_id)])