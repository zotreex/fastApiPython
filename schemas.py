from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: float
    description: str

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
