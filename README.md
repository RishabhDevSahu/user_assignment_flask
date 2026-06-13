# User Management API

This is a simple Flask REST API for managing users. It supports creating users, listing users with pagination/search, and getting a user by id.

## Setup Instructions

### 1. Clone or open the project

Open the project folder:

```bash
cd user_assignment
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
```

For Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add MySQL details:

```env
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_NAME=users
```

### 5. Create database and tables

```bash
python init_db.py
```

### 6. Run the application

```bash
python app.py
```

By default, the API will run on:

```text
http://127.0.0.1:5000
```

## API Endpoints

### 1. Create User

**Endpoint**

```http
POST /users
```

**Request Body**

```json
{
  "name": "Rishabh",
  "email": "rishabh@example.com",
  "role": "Full Stack Developer"
}
```

**Success Response**

```json
{
  "success": true,
  "message": "User created successfully",
  "data": {
    "id": 1,
    "name": "Rishabh",
    "email": "rishabh@example.com",
    "role": "Full Stack Developer"
  }
}
```

**Error Response**

```json
{
  "success": false,
  "error": "Email already exists"
}
```

Other validation errors can be:

```text
Invalid request data
Name is required
Email is required
Role is required
Invalid email format
```

### 2. Get All Users

**Endpoint**

```http
GET /users
```

**Query Parameters**

```text
search: optional, searches by name or email
page: optional, default is 1
limit: optional, default is 10
```

**Example**

```http
GET /users?page=1&limit=10
```

**Search Example**

```http
GET /users?search=rishabh&page=1&limit=10
```

**Success Response**

```json
{
  "success": true,
  "message": "Users retrieved successfully",
  "data": {
    "users": [
      {
        "id": 1,
        "name": "Rishabh",
        "email": "rishabh@example.com",
        "role": "Full Stack Developer"
      }
    ],
    "total": 1,
    "page": 1,
    "limit": 10,
    "pages": 1
  }
}
```

### 3. Get User By ID

**Endpoint**

```http
GET /users/{id}
```

**Example**

```http
GET /users/1
```

**Success Response**

```json
{
  "success": true,
  "message": "User retrieved successfully",
  "data": {
    "id": 1,
    "name": "Rishabh",
    "email": "rishabh@example.com",
    "role": "Full Stack Developer"
  }
}
```

**Error Response**

```json
{
  "success": false,
  "error": "User not found"
}
```

## Database Schema

Database name:

```text
users
```

Table name:

```text
users
```

| Column | Type | Constraints |
| --- | --- | --- |
| id | Integer | Primary Key |
| name | String(100) | Not Null |
| email | String(150) | Unique, Not Null |
| role | String(100) | Not Null |

## Assumptions Made

- Email should be unique for every user.
- Name, email, and role are required fields.
- Search is applied on name and email only.
- Pagination is used in the users list API.
- MySQL is used as the database.

## AI Usage Declaration

I used ChatGPT as an AI assistance tool while working on this project.

ChatGPT was used for guidance on Flask project structure, API implementation, validation logic, error handling, MySQL integration, and README documentation.

The project setup, folder and file creation, MySQL database creation, database configuration, API testing in Postman, Git commits, GitHub push, and Pull Request creation were done manually by me. I reviewed the suggested code, made changes where required, and tested the application to ensure the required APIs work correctly.

I understand the implementation and can explain the project structure, API flow, validation logic, database operations, error handling, and Git workflow used in this assignment.

## Short Answers

### 1. Why did you choose Flask?

I chose Flask because this project needed a simple REST API. Flask is easy to set up and good for small API-based projects. It also allows me to keep the code clean by using separate files for routes, models, services, and validation.

### 2. How would you scale this system?

To scale this system, I would first add proper indexes on fields like email and name because they are used for search and duplicate checks. I would also keep pagination for large data. For more users, I would run the app using Gunicorn and Nginx with multiple workers. I would also use caching where needed and use a managed MySQL database for better performance and reliability.

### 3. What changes would you make for production?

For production, I would turn off debug mode and keep sensitive values like database password in environment variables. I would add authentication, authorization, logging, rate limiting, and better error handling. I would also add database migrations, write basic tests, and run the app using a production server instead of the Flask development server.
