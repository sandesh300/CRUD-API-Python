from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

class UserInDB(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    product_name: str
    quantity: int

class OrderCreate(OrderBase):
    user_id: int

class OrderUpdate(OrderBase):
    product_name: Optional[str] = None
    quantity: Optional[int] = None

class OrderInDB(OrderBase):
    id: int
    user_id: int
    order_date: datetime

    class Config:
        from_attributes = True
        