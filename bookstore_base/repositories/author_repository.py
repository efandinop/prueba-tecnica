from odoo import api, SUPERUSER_ID

class AuthorRepository:
    @staticmethod
    def get_author_by_name(name):
        env = api.Environment(api.cr, SUPERUSER_ID, {})
        return env['bookstore.author'].search([('name', '=', name)])
