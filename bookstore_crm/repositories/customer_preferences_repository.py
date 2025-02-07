from odoo import api, SUPERUSER_ID

class CustomerPreferencesRepository:
    @staticmethod
    def get_preferences_by_customer(customer_id):
        env = api.Environment(api.cr, SUPERUSER_ID, {})
        return env['bookstore.customer.preferences'].search([('customer_id', '=', customer_id)])
