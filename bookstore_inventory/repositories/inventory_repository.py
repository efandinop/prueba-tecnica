from odoo import api, SUPERUSER_ID

class InventoryRepository:
    @staticmethod
    def get_stock_by_book(book_id):
        env = api.Environment(api.cr, SUPERUSER_ID, {})
        return env['bookstore.inventory'].search([('book_id', '=', book_id)])