from pydantic import BaseModel


class MenuCreate(BaseModel):
    title: str
    description: str


class MenuShow(BaseModel):
    id: str
    title: str
    description: str
    submenus_count: int
    dishes_count: int


class MenuCreated(BaseModel):
    id: str
    title: str
    description: str
