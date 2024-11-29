# CRUD Operations API Development

## Overview
This is a FastAPI-based CRUD (Create, Read, Update, Delete) application that handles **Users** and **Orders**, featuring full test coverage.

## Setup and Installation

### Prerequisites
To install the necessary dependencies, run the following command:

```bash
pip install fastapi uvicorn sqlalchemy asyncpg alembic pytest pytest-asyncio httpx email-validator python-multipart
```

### Database Setup
1. **Install PostgreSQL and pgAdmin**: Ensure you have PostgreSQL and pgAdmin installed on your machine.
2. **Create a Database**: Create a new database named `fastapi_db` in PostgreSQL.
3. **Update Database URL**: Modify the database URL in `database.py` with your PostgreSQL credentials.

### SSL Certificate Generation
Generate SSL certificates for HTTPS support by running:

```bash
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

### Application Structure
The application follows best practices for structure and design, including:
- **Separation of concerns**: Organized into models, schemas, and routers.
- **Async/await**: Async database operations for better performance.
- **Comprehensive error handling**: Proper handling of errors throughout the app.
- **Input validation**: Using Pydantic models to validate input data.
- **Type hints**: All functions and parameters are typed for clarity and better development experience.
- **Test coverage**: Includes test cases for all endpoints.

### Key Features
- **Full CRUD operations** for both Users and Orders.
- **Async database operations** for improved performance.
- **Foreign key relationships** between Users and Orders.
- **Input validation** using Pydantic.
- **Error handling** for user-friendly responses.
- **SSL support** for secure communication.
- **Multiple worker support** via `uvicorn`.
- **Database constraints** for data integrity.
- **Comprehensive testing** with `pytest` and `pytest-asyncio`.

### Prerequisites
- Python 3.8+
- PostgreSQL
- FastAPI
- SQLAlchemy
- SSL
- 

## Running the Application

To start the FastAPI application, run the following command:

```bash
python main.py
```

The API will be available at `https://localhost:8000`.

## Running Tests

To run the test cases for the application, use:

```bash
pytest tests/
```

This will execute all tests located in the `tests/` directory.

---

## API Documentation
![Screenshot (58)](https://github.com/user-attachments/assets/e7e8bf07-335c-4193-91cf-5e83fd3008ce)

### Users API

#### 1. Create User
- **Endpoint**: `POST /users/`
- **URL**: `https://localhost:8000/users/`
- **Request Body**:
```json
{
    "name": "sandesh bhujbal",
    "email": "sandeshbhujbal300@gmail.com"
}
```
- **Success Response** (201 Created):
```json
{
    "name": "sandesh bhujbal",
    "email": "sandeshbhujbal300@gmail.com",
    "id": 1,
    "created_at": "2024-11-28T09:43:00.712603Z"
}
```

#### 2. Get User
- **Endpoint**: `GET /users/{id}`
- **URL**: `https://localhost:8000/users/2`
- **Success Response** (200 OK):
```json
{
    "name": "sandesh bhujbal",
    "email": "sandeshbhujbal300@gmail.com",
    "id": 1,
    "created_at": "2024-11-28T09:43:00.712603Z"
}
```

#### 3. Get All Users
- **Endpoint**: `GET /users`
- **URL**: `https://localhost:8000/users/`
- **Success Response** (200 OK):
```json
[
    {
        "name": "sandesh bhujbal",
        "email": "sandeshbhujbal300@gmail.com",
        "id": 1,
        "created_at": "2024-11-28T09:43:00.712603Z"
    },
    {
        "name": "sanket tamhane",
        "email": "sankettamhane@gmail.com",
        "id": 2,
        "created_at": "2024-11-28T09:46:30.955441Z"
    }
]
```

#### 4. Update User
- **Endpoint**: `PUT /users/{id}`
- **URL**: `https://localhost:8000/users/1`
- **Request Body**:
```json
{
    "name": "Sandesh Prakash Bhujbal",
    "email": "sandeshbhujbal300@gmail.com"
}
```
- **Success Response** (200 OK):
```json
{
    "name": "Sandesh Prakash Bhujbal",
    "email": "sandeshbhujbal300@gmail.com",
    "id": 1,
    "created_at": "2024-11-28T09:43:00.712603Z"
}
```

#### 5. Delete User
- **Endpoint**: `DELETE /users/{id}`
- **URL**: `https://localhost:8000/users/6`
- **Success Response** (200 OK):
```json
{
    "message": "User deleted successfully with ID - 6"
}
```

### Orders API

#### 1. Create Order
- **Endpoint**: `POST /orders`
- **URL**: `https://localhost:8000/orders`
- **Request Body**:
```json
{
    "user_id": 1,
    "product_name": "Laptop",
    "quantity": 2
}
```
- **Success Response** (201 Created):
```json
{
    "product_name": "Laptop",
    "quantity": 2,
    "id": 1,
    "user_id": 1,
    "order_date": "2024-11-28T10:03:30.475560Z"
}
```

#### 2. Get Order
- **Endpoint**: `GET /orders/{id}`
- **URL**: `https://localhost:8000/orders/1`
- **Success Response** (200 OK):
```json
{
    "product_name": "Laptop",
    "quantity": 2,
    "id": 1,
    "user_id": 1,
    "order_date": "2024-11-28T10:03:30.475560Z"
}
```

#### 3. Get All Orders
- **Endpoint**: `GET /orders`
- **URL**: `https://localhost:8000/orders`
- **Success Response** (200 OK):
```json
[
    {
        "product_name": "Laptop",
        "quantity": 2,
        "id": 1,
        "user_id": 1,
        "order_date": "2024-11-28T10:03:30.475560Z"
    },
    {
        "product_name": "mobiles",
        "quantity": 5,
        "id": 2,
        "user_id": 1,
        "order_date": "2024-11-28T10:05:40.412382Z"
    }
]
```

#### 4. Update Order
- **Endpoint**: `PUT /orders/{id}`
- **URL**: `https://localhost:8000/orders/1`
- **Request Body**:
```json
{
    "user_id": 1,
    "product_name": "Gaming Laptop",
    "quantity": 3
}
```
- **Success Response** (200 OK):
```json
{
    "product_name": "Gaming Laptop",
    "quantity": 3,
    "id": 1,
    "user_id": 1,
    "order_date": "2024-11-28T10:03:30.475560Z"
}
```

#### 5. Delete Order
- **Endpoint**: `DELETE /orders/{id}`
- **URL**: `https://localhost:8000/orders/3`
- **Success Response** (200 OK):
```json
{
    "message": "Order deleted successfully with ID - 3"
}
```
---------------------------
# FastAPI CRUD Application Test Documentation

## Users API Tests

### 1. User Creation Tests

#### 1.1 Successful User Creation
**Description**: Verifies that a new user can be created successfully with valid data.

**Test Case**: `test_create_user_success`
```python
@pytest.mark.asyncio
async def test_create_user_success(self, async_client):
    response = await async_client.post(
        "/users/",
        json={"name": "Test User", "email": "test@example.com"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert "created_at" in data
```

**Test Result**: 
- **Status**: ✅ PASSED
- **Observations**: 
  - User creation successful
  - Returned status code 201
  - User data correctly saved and returned
  - ID and timestamp generated as expected

#### 1.2 Duplicate Email Prevention
**Description**: Verifies that the system prevents creation of users with duplicate emails.

**Test Case**: `test_create_user_duplicate_email`
```python
@pytest.mark.asyncio
async def test_create_user_duplicate_email(self, async_client):
    # Create first user
    await async_client.post(
        "/users/",
        json={"name": "Test User", "email": "test@example.com"}
    )
    
    # Try to create second user with same email
    response = await async_client.post(
        "/users/",
        json={"name": "Another User", "email": "test@example.com"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Email already registered" in response.json()["detail"]
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - Duplicate email creation blocked
  - Returned status code 400
  - Appropriate error message displayed
  - Database integrity maintained

### 2. User Retrieval Tests

#### 2.1 Successful User Retrieval
**Description**: Verifies that an existing user can be retrieved by ID.

**Test Case**: `test_get_user_success`
```python
@pytest.mark.asyncio
async def test_get_user_success(self, async_client):
    # Create user
    create_response = await async_client.post(
        "/users/",
        json={"name": "Test User", "email": "test@example.com"}
    )
    user_id = create_response.json()["id"]

    # Get user
    response = await async_client.get(f"/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - User successfully retrieved
  - Returned status code 200
  - User details match created user

#### 2.2 Non-existent User Retrieval
**Description**: Verifies proper handling of requests for non-existent users.

**Test Case**: `test_get_user_not_found`
```python
@pytest.mark.asyncio
async def test_get_user_not_found(self, async_client):
    response = await async_client.get("/users/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "User not found" in response.json()["detail"]
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - Non-existent user request handled correctly
  - Returned status code 404
  - Appropriate error message displayed

### 3. User Update Tests

#### 3.1 Successful User Update
**Description**: Verifies that an existing user's information can be updated.

**Test Case**: `test_update_user_success`
```python
@pytest.mark.asyncio
async def test_update_user_success(self, async_client):
    # Create user
    create_response = await async_client.post(
        "/users/",
        json={"name": "Test User", "email": "test@example.com"}
    )
    user_id = create_response.json()["id"]

    # Update user
    response = await async_client.put(
        f"/users/{user_id}",
        json={"name": "Updated Name", "email": "updated@example.com"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["name"] == "Updated Name"
    assert data["email"] == "updated@example.com"
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - User successfully updated
  - Returned status code 200
  - Name and email correctly modified

### 4. User Deletion Tests

#### 4.1 Successful User Deletion
**Description**: Verifies that a user can be deleted successfully.

**Test Case**: `test_delete_user_success`
```python
@pytest.mark.asyncio
async def test_delete_user_success(self, async_client):
    # Create user
    create_response = await async_client.post(
        "/users/",
        json={"name": "Test User", "email": "test@example.com"}
    )
    user_id = create_response.json()["id"]

    # Delete user
    response = await async_client.delete(f"/users/{user_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verify user is deleted
    get_response = await async_client.get(f"/users/{user_id}")
    assert get_response.status_code == status.HTTP_404_NOT_FOUND
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - User successfully deleted
  - Returned status code 204
  - Subsequent retrieval returns 404
  - User completely removed from system

## Orders API Tests

### 1. Order Creation Tests

#### 1.1 Successful Order Creation
**Description**: Verifies that a new order can be created successfully.

**Test Case**: `test_create_order_success`
```python
@pytest.mark.asyncio
async def test_create_order_success(self, async_client, test_user):
    response = await async_client.post(
        "/orders/",
        json={
            "user_id": test_user["id"],
            "product_name": "Test Product",
            "quantity": 1
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["product_name"] == "Test Product"
    assert data["quantity"] == 1
    assert data["user_id"] == test_user["id"]
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - Order created successfully
  - Returned status code 201
  - Order details correctly saved
  - User association maintained

#### 1.2 Invalid User Order Creation
**Description**: Verifies that orders cannot be created for non-existent users.

**Test Case**: `test_create_order_invalid_user`
```python
@pytest.mark.asyncio
async def test_create_order_invalid_user(self, async_client):
    response = await async_client.post(
        "/orders/",
        json={
            "user_id": 999,
            "product_name": "Test Product",
            "quantity": 1
        }
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "User not found" in response.json()["detail"]
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - Invalid user order creation blocked
  - Returned status code 404
  - Appropriate error message displayed

#### 1.3 Invalid Quantity Order Creation
**Description**: Verifies quantity validation for order creation.

**Test Case**: `test_create_order_invalid_quantity`
```python
@pytest.mark.asyncio
async def test_create_order_invalid_quantity(self, async_client, test_user):
    response = await async_client.post(
        "/orders/",
        json={
            "user_id": test_user["id"],
            "product_name": "Test Product",
            "quantity": 0  # Invalid quantity
        }
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - Invalid quantity order creation blocked
  - Returned status code 400
  - Quantity validation working correctly

### 2. Order Retrieval Tests

#### 2.1 Successful Order Retrieval
**Description**: Verifies that an existing order can be retrieved.

**Test Case**: `test_get_order_success`
```python
@pytest.mark.asyncio
async def test_get_order_success(self, async_client, test_user):
    # Create order
    create_response = await async_client.post(
        "/orders/",
        json={
            "user_id": test_user["id"],
            "product_name": "Test Product",
            "quantity": 1
        }
    )
    order_id = create_response.json()["id"]

    # Get order
    response = await async_client.get(f"/orders/{order_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["product_name"] == "Test Product"
    assert data["quantity"] == 1
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - Order retrieved successfully
  - Returned status code 200
  - Order details match created order

### 3. Order Update Tests

#### 3.1 Successful Order Update
**Description**: Verifies that an existing order can be updated.

**Test Case**: `test_update_order_success`
```python
@pytest.mark.asyncio
async def test_update_order_success(self, async_client, test_user):
    # Create order
    create_response = await async_client.post(
        "/orders/",
        json={
            "user_id": test_user["id"],
            "product_name": "Test Product",
            "quantity": 1
        }
    )
    order_id = create_response.json()["id"]

    # Update order
    response = await async_client.put(
        f"/orders/{order_id}",
        json={
            "product_name": "Updated Product",
            "quantity": 2
        }
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["product_name"] == "Updated Product"
    assert data["quantity"] == 2
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - Order updated successfully
  - Returned status code 200
  - Product name and quantity modified correctly

### 4. Order Deletion Tests

#### 4.1 Successful Order Deletion
**Description**: Verifies that an order can be deleted successfully.

**Test Case**: `test_delete_order_success`
```python
@pytest.mark.asyncio
async def test_delete_order_success(self, async_client, test_user):
    # Create order
    create_response = await async_client.post(
        "/orders/",
        json={
            "user_id": test_user["id"],
            "product_name": "Test Product",
            "quantity": 1
        }
    )
    order_id = create_response.json()["id"]

    # Delete order
    response = await async_client.delete(f"/orders/{order_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
```

**Test Result**:
- **Status**: ✅ PASSED
- **Observations**:
  - Order deleted successfully
  - Returned status code 204
  - Order removed from system




