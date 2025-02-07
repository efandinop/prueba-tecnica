from odoo import api, SUPERUSER_ID

class CustomerRepository:
    @staticmethod
    def get_customer_by_email(email):
        env = api.Environment(api.cr, SUPERUSER_ID, {})
        return env['bookstore.customer'].search([('email', '=', email)])
