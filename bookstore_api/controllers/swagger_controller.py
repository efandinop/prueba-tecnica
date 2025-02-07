from odoo import http
from odoo.http import request

class SwaggerController(http.Controller):
    @http.route('/api/docs', type='http', auth='public', methods=['GET'])
    def swagger_ui(self):
        swagger_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Documentación API</title>
            <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui-bundle.js"></script>
            <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui.css"/>
        </head>
        <body>
            <div id="swagger-ui"></div>
            <script>
                const ui = SwaggerUIBundle({
                    url: '/api/swagger.json',
                    dom_id: '#swagger-ui'
                });
            </script>
        </body>
        </html>
        """
        return request.make_response(swagger_html, [('Content-Type', 'text/html')])

    @http.route('/api/swagger.json', type='json', auth='public', methods=['GET'])
    def swagger_spec(self):
        return {
            "openapi": "3.0.0",
            "info": {
                "title": "Bookstore API",
                "version": "1.0"
            },
            "paths": {
                "/api/books": {
                    "get": {
                        "summary": "Obtener lista de libros",
                        "parameters": [
                            {"name": "author_id", "in": "query", "required": False, "schema": {"type": "integer"}},
                            {"name": "in_stock", "in": "query", "required": False, "schema": {"type": "boolean"}}
                        ],
                        "responses": {"200": {"description": "Lista de libros"}}
                    }
                }
            }
        }