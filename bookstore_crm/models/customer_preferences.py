from odoo import models, fields
from ..repositories.customer_preferences_repository import CustomerPreferencesRepository

class BookstoreCustomerPreferences(models.Model):
    _name = 'bookstore.customer.preferences'
    _description = 'Preferencias del Cliente'

    customer_id = fields.Many2one('bookstore.customer', string='Cliente', required=True)
    preferred_genres = fields.Char(string='Géneros Preferidos')
    frequent_buyer = fields.Boolean(string='Cliente Frecuente')

    @staticmethod
    def get_preferences_by_customer(customer_id):
        return CustomerPreferencesRepository.get_preferences_by_customer(customer_id)