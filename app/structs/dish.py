from typing import List

from pydantic import BaseModel


class DishCreate(BaseModel):
    title: str
    description: str
    price: float
    submenu_id: int = 0


class DishShow(BaseModel):
    id: str
    title: str
    description: str
    price: str
    submenu_id: int


class DishCreated(BaseModel):
    id: str
    title: str
    description: str
    price: str
