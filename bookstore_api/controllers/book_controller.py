from odoo import http
from odoo.http import request, Response
import json
import jwt
import datetime

SECRET_KEY = 'supersecreto'

class BookstoreAPI(http.Controller):
    
    def generate_token(self, user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    def decode_token(self, token):
        try:
            return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    @http.route('/api/token', type='json', auth='public', methods=['POST'])
    def get_token(self, user_id):
        token = self.generate_token(user_id)
        return {'token': token}

    @http.route('/api/books', type='json', auth='public', methods=['GET'])
    def get_books(self, author_id=None, in_stock=None, token=None):
        decoded_token = self.decode_token(token)
        if not decoded_token:
            return Response(json.dumps({'error': 'Token inválido o expirado'}), status=401, content_type='application/json')
        
        domain = []
        if author_id:
            domain.append(('author_id', '=', int(author_id)))
        if in_stock:
            domain.append(('stock', '>', 0))
        
        books = request.env['bookstore.book'].search(domain)
        data = [{
            'id': book.id,
            'title': book.title,
            'author': book.author_id.name,
            'publication_year': book.publication_year,
            'price': book.price,
            'stock': book.stock
        } for book in books]
        
        return data

    @http.route('/api/books', type='json', auth='public', methods=['POST'])
    def purchase_book(self, book_id, quantity, token=None):
        decoded_token = self.decode_token(token)
        if not decoded_token:
            return Response(json.dumps({'error': 'Token inválido o expirado'}), status=401, content_type='application/json')
        
        book = request.env['bookstore.book'].browse(int(book_id))
        if book and book.stock >= int(quantity):
            book.stock -= int(quantity)
            return {'message': 'Compra realizada con éxito', 'remaining_stock': book.stock}
        else:
            return Response(json.dumps({'error': 'Stock insuficiente'}), status=400, content_type='application/json')