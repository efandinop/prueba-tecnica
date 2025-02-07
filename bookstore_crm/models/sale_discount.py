from odoo import models, fields, api
from datetime import date, timedelta

class BookstoreSale(models.Model):
    _inherit = 'bookstore.sale'

    discount = fields.Float(string='Descuento', compute='_compute_discount', store=True)

    @api.depends('customer_id', 'book_id')
    def _compute_discount(self):
        for sale in self:
            discount = 0
            if sale.customer_id.purchase_history and len(sale.customer_id.purchase_history) > 10:
                discount += 10
            if sale.book_id.publication_year and sale.book_id.publication_year < (date.today().year - 5) and date.today().month == 1:
                discount += 20
            sale.discount = discount