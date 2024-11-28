from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from typing import List
from database import get_db
import models, schemas

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=schemas.OrderInDB, status_code=status.HTTP_201_CREATED)
async def create_order(order: schemas.OrderCreate, db: AsyncSession = Depends(get_db)):
    # Verify user exists
    user_result = await db.execute(select(models.User).filter(models.User.id == order.user_id))
    user = user_result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        db_order = models.Order(**order.dict())
        db.add(db_order)
        await db.commit()
        await db.refresh(db_order)
        return db_order
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Invalid order data"
        )

@router.get("/", response_model=List[schemas.OrderInDB])
async def get_all_orders(db: AsyncSession = Depends(get_db)):
    """Retrieve all orders"""
    result = await db.execute(select(models.Order))
    orders = result.scalars().all()
    return orders

@router.get("/{order_id}", response_model=schemas.OrderInDB)
async def read_order(order_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Order).filter(models.Order.id == order_id))
    order = result.scalar_one_or_none()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=schemas.OrderInDB)
async def update_order(
    order_id: int,
    order_update: schemas.OrderUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(models.Order).filter(models.Order.id == order_id))
    db_order = result.scalar_one_or_none()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    update_data = order_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_order, field, value)

    try:
        await db.commit()
        await db.refresh(db_order)
        return db_order
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Invalid order data"
        )

@router.delete("/{order_id}", status_code=status.HTTP_200_OK)
async def delete_order(order_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Order).filter(models.Order.id == order_id))
    order = result.scalar_one_or_none()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    await db.delete(order)
    await db.commit()
    return {"message": f"Order deleted successfully with ID - {order_id}"}