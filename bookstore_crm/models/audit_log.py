from odoo import models, api
import json

class BookstoreSale(models.Model):
    _inherit = 'bookstore.sale'

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
