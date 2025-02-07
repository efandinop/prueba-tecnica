from odoo import models, fields, api
from datetime import date, timedelta

class BookstoreReturn(models.Model):
    _name = 'bookstore.return'
    _description = 'Devolución de Libros'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sale_id = fields.Many2one('bookstore.sale', string='Venta Original', required=True)
    return_date = fields.Date(string='Fecha de Devolución', default=fields.Date.today)
    damaged = fields.Boolean(string='Libro Dañado')
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('accepted', 'Aceptada'),
        ('rejected', 'Rechazada')
    ], string='Estado', default='pending', tracking=True)

    def process_return(self):
        for record in self:
            if record.damaged:
                record.state = 'rejected'
                record.notify_customer('rechazada')
                return
            if (date.today() - record.sale_id.sale_date) <= timedelta(days=7):
                record.sale_id.book_id.stock += record.sale_id.quantity
                record.state = 'accepted'
                record.notify_customer('aceptada')
            else:
                record.state = 'rejected'
                record.notify_customer('rechazada')

    def notify_customer(self, status):
        message = f"Su solicitud de devolución ha sido {status}."
        self.sale_id.customer_id.message_post(body=message, subject="Estado de Devolución")