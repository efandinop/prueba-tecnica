from odoo.tests import common, tagged

@tagged('-at_install', 'post_install')
class TestBookstoreCRM(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.book_model = self.env['bookstore.book']
        self.sale_model = self.env['bookstore.sale']
        self.customer_model = self.env['bookstore.customer']

        # Crear autor
        self.author = self.env['bookstore.author'].create({'name': 'Gabriel García Márquez'})
        
        # Crear cliente
        self.customer = self.customer_model.create({'name': 'Juan Pérez'})
        
        # Crear libro
        self.book = self.book_model.create({
            'title': 'Cien Años de Soledad',
            'author_id': self.author.id,
            'publication_year': 2010,
            'price': 10000,
            'stock': 20
        })

    def test_discount_logic(self):
        """ Verifica que los descuentos se aplican correctamente """
        self.customer.write({'purchase_history': [self.book.id] * 11})  # Simular más de 10 compras
        sale = self.sale_model.create({
            'customer_id': self.customer.id,
            'book_id': self.book.id,
            'quantity': 1
        })
        self.assertEqual(sale.discount, 10, "El descuento para clientes frecuentes debería ser del 10%")
        
        # Simular libro con más de 5 años
        self.book.write({'publication_year': 2015})
        sale_january = self.sale_model.create({
            'customer_id': self.customer.id,
            'book_id': self.book.id,
            'quantity': 1
        })
        self.assertEqual(sale_january.discount, 10, "El descuento para clientes frecuentes debería seguir siendo 10%")

    def test_api_purchase(self):
        """ Prueba la API de compra de libros """
        response = self.env['ir.http'].sudo()._handle_with_cr(self.env.cr, {
            'type': 'json',
            'method': 'POST',
            'params': {'book_id': self.book.id, 'quantity': 1},
            'path': '/api/books'
        })
        
        self.assertIn('message', response, "La respuesta debe contener un mensaje de éxito")
        self.assertEqual(self.book.stock, 19, "El stock debe reducirse en 1 unidad")

    def test_sale_permissions(self):
        """ Verifica que un usuario vendedor solo vea sus ventas """
        sales_user_group = self.env.ref('bookstore.group_sales_user')
        test_user = self.env['res.users'].create({
            'name': 'Test Vendedor',
            'login': 'test_vendedor',
            'groups_id': [(6, 0, [sales_user_group.id])]
        })
        
        sale = self.sale_model.create({
            'customer_id': self.customer.id,
            'book_id': self.book.id,
            'quantity': 1,
            'create_uid': test_user.id
        })
        
        sales = self.sale_model.sudo(test_user).search([])
        self.assertEqual(len(sales), 1, "El vendedor solo debe ver su propia venta")
        self.assertEqual(sales[0].id, sale.id, "El vendedor solo debe acceder a su propia venta")