from odoo import api, SUPERUSER_ID

class SaleRepository:
    @staticmethod
    def get_sales_by_customer(customer_id):
        env = api.Environment(api.cr, SUPERUSER_ID, {})
        return env['bookstore.sale'].search([('customer_id', '=', customer_id)])