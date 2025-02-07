from odoo.tests import common, tagged

@tagged('-at_install', 'post_install')
class TestBookstoreInventory(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.book_model = self.env['bookstore.book']
        self.book = self.book_model.create({
            'title': 'Ficciones',
            'author_id': self.env['bookstore.author'].create({'name': 'Jorge Luis Borges'}).id,
            'publication_year': 1944,
            'price': 12000,
            'stock': 25
        })

    def test_stock_update(self):
        """ Verifica que el stock se actualiza correctamente """
        self.book.write({'stock': 20})
        self.assertEqual(self.book.stock, 20, "El stock debería haberse actualizado a 20")
