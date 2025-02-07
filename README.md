# 📚 Odoo Bookstore Module

Este es un módulo de Odoo 16 para la gestión de una librería. Incluye funcionalidades para administrar libros, autores, categorías y ventas dentro del sistema Odoo.

## 🏗️ Estructura del Módulo

El sistema está dividido en **tres módulos independientes**, siguiendo las mejores prácticas de modularidad en Odoo:

### **1️⃣ bookstore_base**
📌 **Funcionalidad:**  
Este es el **módulo principal** que define las entidades básicas de la librería. Se encarga de manejar la información relacionada con los libros y sus características.

🔹 **Modelos incluidos:**
- **`bookstore.book`** → Gestiona la información de los libros (título, autor, año de publicación, precio).
- **`bookstore.author`** → Almacena datos de los autores.
- **`bookstore.customer`** → Representa a los clientes de la librería.
- **`bookstore.category`** → Permite clasificar los libros en distintas categorías.

🔹 **Reglas de negocio:**
- Se validan los datos al registrar libros y autores.
- Se estructuran relaciones entre libros, autores y categorías.

---

### **2️⃣ bookstore_inventory**
📌 **Funcionalidad:**  
Este módulo se encarga del **manejo del inventario y las ventas** dentro de la librería.

🔹 **Modelos incluidos:**
- **`bookstore.stock`** → Controla la cantidad de libros disponibles en inventario.
- **`bookstore.sale`** → Registra las ventas de libros y sus detalles.
- **`bookstore.return`** → Administra las devoluciones de libros.

🔹 **Reglas de negocio:**
- Se reduce el stock al realizar una venta.
- Se permite la devolución de libros dentro de los primeros **7 días**.
- Los libros devueltos en mal estado **no se reintegran al inventario**.
- Aplicación automática de descuentos:
  - **Clientes frecuentes (+10 libros/año)** → **10% de descuento**.
  - **Libros con más de 5 años** → **20% de descuento en enero**.

---

### **3️⃣ bookstore_crm**
📌 **Funcionalidad:**  
Este módulo se encarga de la **gestión de clientes y sus preferencias**.

🔹 **Modelos incluidos:**
- **`bookstore.customer_preferences`** → Almacena géneros favoritos y hábitos de compra de los clientes.
- **`bookstore.notifications`** → Sistema de notificaciones para alertar sobre nuevas promociones o devoluciones aceptadas.

🔹 **Reglas de negocio:**
- Se personalizan recomendaciones de libros según el historial de compras.
- Se envían **notificaciones automáticas** cuando una devolución es aceptada o rechazada.

---

## 🔐 Seguridad y Permisos

El sistema implementa controles de acceso para diferentes roles en la librería:

| **Rol**              | **Permisos** |
|----------------------|-------------|
| `bookstore_manager`  | Acceso total a todo el sistema |
| `sales_user`        | Puede realizar ventas pero no modificar precios |
| `inventory_user`    | Maneja el stock sin acceso a ventas |

Además, se han implementado reglas de acceso (`ir.rule`):
- **Los vendedores solo pueden ver sus propias ventas.**
- **Solo los gerentes pueden modificar los precios de los libros.**

---

## ⚡ API REST

Se ha implementado una API REST en el módulo `bookstore_api`, que expone los siguientes endpoints:

- **`GET /api/books`** → Obtiene la lista de libros disponibles en la librería.
- **`GET /api/books?author=<nombre>`** → Filtra libros por autor.
- **`GET /api/books?stock_min=<cantidad>`** → Filtra libros según disponibilidad en stock.
- **`POST /api/books/sale`** → Realiza una compra y reduce el stock disponible.

Esta API permite integrar el sistema de librería con aplicaciones externas.

---

📌 **Este conjunto de módulos permite gestionar eficientemente una librería dentro de Odoo, aplicando lógica de negocio específica, asegurando integridad de datos y ofreciendo integración con sistemas externos a través de una API REST.**

## ⚙️ Requisitos Previos

Antes de instalar el módulo, asegúrate de tener lo siguiente:

- **Odoo 16** instalado en tu servidor.
- **Python 3 y pip** para manejar las dependencias.
- **Dependencias necesarias** (se instalarán automáticamente desde `requirements.txt`).
- **Azure DevOps** configurado con un agente self-hosted.

## 🚀 Instalación y Configuración

Seguir estos pasos para instalar el módulo:

1. **Clonar el repositorio** en la carpeta de módulos de Odoo:

   cd /opt/odoo/addons
   git clone https://github.com/tuusuario/odoo_bookstore.git
Instalar las dependencias del módulo:

cd /opt/odoo/addons/odoo_bookstore
pip install -r requirements.txt
Reiniciar el servicio de Odoo:
sudo systemctl restart odoo

Activar el modo desarrollador en Odoo y ve a Aplicaciones.

Instalar el módulo "Bookstore" desde la interfaz de Odoo.

▶️ Ejecución del Módulo
Para ejecutar pruebas unitarias del módulo:

cd /opt/odoo/odoo-server
source odoo-venv/bin/activate
./odoo-bin --addons-path=addons --test-enable --log-level=test --db-filter=^testdb$ --stop-after-init
Para iniciar Odoo manualmente:

./odoo-bin --addons-path=addons -c /etc/odoo/odoo.conf
_____________________________________________________________________________________________________


🛠 Pipeline de Azure DevOps
Este repositorio está configurado con Azure DevOps Pipelines para:

Instalar dependencias.
Ejecutar pruebas unitarias en Odoo.
Empaquetar el módulo.
Publicar los artefactos generados.
Desplegar el módulo en un servidor de staging.
El pipeline se define en el archivo azure-pipelines.yml y usa un agente auto-hospedado.

📄 Ejecución del Pipeline
El pipeline se activa con cada push a la rama main. También puedes ejecutarlo manualmente desde Azure DevOps > Pipelines.

🔗 Referencias y Enlaces Útiles
Documentación oficial de Odoo 16: https://www.odoo.com/documentation/16.0/
Portal de Azure DevOps Pipelines: https://learn.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops
Guía de gestión de módulos en Odoo: https://www.odoo.com/documentation/16.0/developer/howtos/backend.html
📌 Autor: Edwin Fandiño
📅 Fecha de última actualización: 2025-02-07
