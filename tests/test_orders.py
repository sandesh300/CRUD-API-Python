import pytest
from httpx import AsyncClient
from fastapi import status
from main import app
from database import engine, Base
import models

@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture
async def test_user(async_client):
    response = await async_client.post(
        "/users/",
        json={"name": "Test User", "email": "test@example.com"}
    )
    return response.json()

class TestOrders:
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

        # Verify order is deleted
        get_response = await async_client.get(f"/orders/{order_id}")
        assert get_response.status_code == status.HTTP_404_NOT_FOUND