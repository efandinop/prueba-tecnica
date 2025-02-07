from odoo import models, fields, api

class BookstoreAuditLog(models.Model):
    _name = 'bookstore.audit.log'
    _description = 'Registro de Auditoría'
    _order = 'create_date desc'

    model_name = fields.Char(string='Modelo')
    record_id = fields.Integer(string='ID del Registro')
    user_id = fields.Many2one('res.users', string='Usuario')
    change_type = fields.Selection([
        ('create', 'Creación'),
        ('write', 'Modificación'),
        ('unlink', 'Eliminación')
    ], string='Tipo de Cambio')
    old_value = fields.Text(string='Valor Anterior')
    new_value = fields.Text(string='Nuevo Valor')
    change_date = fields.Datetime(string='Fecha de Cambio', default=fields.Datetime.now)

### bookstore_base/models/bookstore_book.py

from odoo import models, api
import json

class BookstoreBook(models.Model):
    _inherit = 'bookstore.book'

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            record._log_audit('create', old_value=None, new_value=json.dumps(record.read()[0]))
        return records

    def write(self, vals):
        for record in self:
            old_value = json.dumps(record.read()[0])
            res = super().write(vals)
            record._log_audit('write', old_value=old_value, new_value=json.dumps(record.read()[0]))
            return res

    def unlink(self):
        for record in self:
            record._log_audit('unlink', old_value=json.dumps(record.read()[0]), new_value=None)
        return super().unlink()

    def _log_audit(self, change_type, old_value, new_value):
        self.env['bookstore.audit.log'].create({
            'model_name': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'change_type': change_type,
            'old_value': old_value,
            'new_value': new_value,
        })
