from odoo.tests import common, tagged

@tagged('-at_install', 'post_install')
class TestBookstoreBase(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.author_model = self.env['bookstore.author']
        self.book_model = self.env['bookstore.book']

        self.author = self.author_model.create({'name': 'Julio Cortázar'})
        self.book = self.book_model.create({
            'title': 'Rayuela',
            'author_id': self.author.id,
            'publication_year': 1963,
            'price': 15000,
            'stock': 30
        })

    def test_book_creation(self):
        """ Verifica que los libros se crean correctamente """
        self.assertEqual(self.book.title, 'Rayuela', "El título del libro debería ser 'Rayuela'")
        self.assertEqual(self.book.stock, 30, "El stock inicial debería ser 30")
