DjangoProject-ShopAPI
DjangoProject-ShopAPI is a RESTful API built using Django and Django REST Framework (DRF). This project is designed to manage an e-commerce-like platform, including functionalities for categories, products, and shopping carts. It also integrates user authentication using JSON Web Tokens (JWT) to ensure secure access to the API.

Features
Product Management: Create, retrieve, update, and delete products.
Category Management: Organize products into categories for easier navigation.
Shopping Cart: Manage items in the shopping cart for users.
Authentication and Authorization:
User login and JWT-based authentication.
Token refresh functionality to maintain secure access.
Secure API Endpoints: Ensure only authenticated users can access protected resources.
Database: Uses SQLite for lightweight and easy local development.

Project Structure
The project is divided into multiple apps to separate concerns:
API: Handles general API logic and authentication endpoints.
Catalog: Manages the products and categories.
DjangoProject: The main configuration for the project.

Technology Stack
Framework: Django 5.1.4
REST API: Django REST Framework (DRF)
Authentication: Simple JWT for secure user token management
Database: SQLite (default setup, can be replaced with other databases)
Language: Python 3.12
Testing and Development: Postman is used for API testing.

API Endpoints
Authentication
POST /api/token/: Obtain a pair of access and refresh tokens.
POST /api/token/refresh/: Refresh the access token.
Products and Categories
GET /categories/: List all categories.
GET /products/: List all products.
GET /cart/: Get the current user's shopping cart.

How to Run the Project

Clone the repository:
git clone https://github.com/your-username/DjangoProject-ShopAPI.git
cd DjangoProject-ShopAPI

Create a virtual environment and install dependencies:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

Set up environment variables in a .env file:
SECRET_KEY=your-secret-key

Apply database migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Notes
Default SECRET_KEY is stored in .env for security reasons.
Make sure to use proper environment variables in production and replace the SQLite database with a production-ready solution.

Contributions
Feel free to fork this repository, open issues, and submit pull requests. Contributions are welcome!
