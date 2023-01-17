from pydantic import BaseModel

class SubMenuCreate(BaseModel):
    title: str
    description: str
    menu_id: int = 0
    
class SubMenuShow(BaseModel):
    id: str
    title: str
    description: str
    menu_id: int
    dishes_count: int
    
class SubMenuCreated(BaseModel):
    id: str
    title: str
    description: str