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

@pytest.fixture(autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

class TestUsers:
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

    @pytest.mark.asyncio
    async def test_get_user_not_found(self, async_client):
        response = await async_client.get("/users/999")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "User not found" in response.json()["detail"]

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
        