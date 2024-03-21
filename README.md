<h1 align="center">
  <img
    width="400"
    alt="django"
    src="https://live.staticflickr.com/65535/53591772632_1f84a8da4d_z.jpg">
</h1>

---
<h3 align="center">
  <strong>
🗃 Django Pizza Delivery App 🗃

  </strong>
</h3>

---
<p align="center">
  <img 
    width="1000"
    alt="home"
    src="https://live.staticflickr.com/65535/53592971624_c585273a0c_b.jpg"/>
</p>

---
## Pizza Delivery App - Django REST API
### Description

This project is a complete backend solution for a pizza delivery service, built using Django REST Framework. It provides endpoints for user authentication, managing user profiles, creating, viewing, updating, and deleting pizza orders. The API is designed to be intuitive, secure, and easily extendable.

---

## Features
- **User Authentication(Dockerized):** Users can sign up, log in, and log out securely. Authentication is implemented using JSON Web Tokens (JWT) provided by Django Rest Framework. The authentication system is containerized within the Docker environment for easy deployment and management.
- **User Management(Dockerized):** Users can update their profiles, including details like first name, last name, username, email, phone number, date of birth, and delivery address. User management functionalities are containerized within Docker for seamless integration with the overall application environment.
- **Order Management(Dockerized):** Users can create new pizza orders, view details of their orders, update the status of their orders, and delete their orders. Additionally, administrators have the capability to update the status of any order. Order management functionalities are containerized within Docker for improved scalability and portability.
- **API Documentation(Dockerized):** The API is documented using Swagger UI and ReDoc, providing clear and interactive documentation for developers to explore the available endpoints. The API documentation system is containerized within Docker, ensuring consistency and easy access to documentation across different environments.

<p align="center">
  <img 
    width="600"
    alt="home"
    src="https://live.staticflickr.com/65535/53593108625_3169d784e3_b.jpg"/>
</p>
<p align="center">
  <img 
    width="600"
    alt="home"
    src="https://live.staticflickr.com/65535/53593108605_c15657a863_b.jpg"/>
         
</p>

---
## Technologies Used
- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework (DRF):** A powerful and flexible toolkit for building Web APIs in Django, providing serializers, views, authentication, and more.
- **Djoser:** A Django REST framework providing a set of prebuilt views and serializers for handling user authentication, registration, and account management.
- **Simple JWT:** A JSON Web Token authentication plugin for Django REST Framework, providing secure authentication via JWTs.
- **Swagger UI and ReDoc:** Tools for automatically generating interactive API documentation from OpenAPI specifications, making it easy to explore and understand the API endpoints.
- **MySQL:** A popular open-source relational database management system used for storing and managing data in the application.
- **Python Decouple:** A Python library for separating settings from code, allowing for easier management of environment variables.
- **Pathlib:** A module in Python's standard library providing classes representing filesystem paths, used for resolving file paths within the project.
- **Phonenumber Field:** A Django model and form field for normalizing and validating phone numbers, ensuring consistent formatting and data integrity.
- **Docker:** A platform for developing, shipping, and running applications in containers, providing a consistent environment across different systems.
- **Docker Compose:** A tool for defining and running multi-container Docker applications, simplifying the process of managing complex containerized environments.

  <p align="left">
  <img src="https://img.shields.io/badge/django-00008B?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/django rest framework-acace6?style=for-the-badge&logo=DRF&logoColor=white"/>
  <img src="https://img.shields.io/badge/djoser-800000?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
  <img src="https://img.shields.io/badge/swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white"/>
  <img src="https://img.shields.io/badge/simplejwt-ffa500?style=for-the-badge&logo=simplejwt&logoColor=white"/>
  <img src="https://img.shields.io/badge/mysql-FF0000?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/docker-0000FF?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

---
## API Endpoints
### Authentication

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* | ```/auth/jwt/create/``` | _Login user_|_All users_|
| *POST* | ```/auth/jwt/refresh/``` | _Refresh the access token_|_All users_|
| *POST* | ```/auth/jwt/verify/``` | _Verify the validity of a token_|_All users_|
| *GET*  | ```/auth/user/<int:user_id>/``` | Get a specific user profile |_All users_|
| *PUT*  | ```/auth/user/<int:user_id>/``` | Edit a specific user profile |_All users_|
| *DELETE* | ```/auth/user/<int:user_id>/``` | Delete a specific user profile |_All users_|
| *GET* | ```/auth/users/``` | Get all users | _Super user_ |

### Orders
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/orders/``` | _Place an order_|_All users_|
| *POST* | ```/orders/``` | _Get all orders_|_All users_|
| *GET* | ```/order/{order_id}/``` | _Retrieve an order_|_All users_|
| *PUT* | ```/orders/{order_id}/``` | _Update an order_|_All users_|
| *PUT* | ```/update-status/{order_id}/``` | _Update order status_|_Superuser_|
| *DELETE* | ```/delete/{order_id}/``` | _Delete/Remove an order_ |_All users_|

### User
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/user/{user_id}/orders/``` | _Get user's orders_|_Superuser_|
| *GET* | ```/user/{user_id}/order/{order_id}/``` | _Get user's specific order_|_Superuser_|

---
## Installation

1- **Clone the repository:**
```
git clone https://github.com/your_username/pizza-delivery.git
cd pizza-delivery

```
2- **Create your virtualenv and activate it:**
```
Pipenv or virtualenv
```
3- **Install dependencies:**
```
pip install -r requirements.txt
```
4- **Set up environment variables:**
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=mysql://username:password@localhost:3306/pizza-delivery
```
5- **Apply database migrations:**
```
python manage.py migrate
```
6- **Run the development server:**
```
python manage.py runserver

```
7- **Access the API at:**
```
http://localhost:8000/
```
---

## Example Requests

### User Signup
### Request
```
POST /auth/signup/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "email": "johndoe@example.com",
    "phone_number": "+1234567890",
    "password": "securepassword",
    "date_of_birth": "1990-01-01",
    "delivery_address": "123 Main St, Cityville"
}
```
### Response
```
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "email": "johndoe@example.com",
    "phone_number": "+1234567890",
    "date_of_birth": "1990-01-01",
    "delivery_address": "123 Main St, Cityville",
    "date_joined": "2024-03-17T12:00:00Z"
}

```

### Create a new pizza order
### Request
```
POST /orders/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
    "size": "LARGE",
    "order_status": "PENDING",
    "quantity": 2,
    "flavour": "Pepperoni"
}

```
### Response
```
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 1,
    "customer": 1,
    "size": "LARGE",
    "order_status": "PENDING",
    "quantity": 2,
    "flavour": "Pepperoni",
    "created_at": "2024-03-17T12:00:00Z",
    "updated_at": "2024-03-17T12:00:00Z"
}

```
### Update status
```
PUT /update-status/1/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
    "order_status": "DELIVERED"
}
```
---

## License
This project is licensed under the [MIT License](LICENSE).

---
### Built with ❤️ by Payam Anari

Thank you for exploring the Gym Fitness app! If you have any questions, feedback, or just want to say hi, feel free to [reach out](mailto:anari.p62@gmail.com). Happy fitness journey!

---
