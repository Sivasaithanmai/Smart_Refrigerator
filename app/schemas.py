from pydantic import BaseModel
from datetime import date
from typing import Optional

class ItemBase(BaseModel):
    name: str
    quantity: Optional[float] = 1
    category: Optional[str] = "general"
    expiry_date: Optional[date] = None

class ItemCreate(ItemBase):
    pass

class ItemRead(ItemBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
