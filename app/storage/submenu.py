from .models import Submenu, Dish
from structs import submenu as SB

class SubmenuRepository():
    def __init__(self, db):
        self.db = db
        
    def getSubmenus(self):
        submenus = []
        
        with self.db.session_scope() as s:
            for submenu in s.query(Submenu).all():
                dishesCount = s.query(Dish).filter(Dish.submenu_id == submenu.id).count()
            
                submenus.append(SB.SubMenuShow(id=str(submenu.id), title=submenu.title,
                                               description=submenu.description, menu_id=submenu.menu_id,
                                               dishes_count=dishesCount))
            
        return submenus
    
    def getSubmenu(self, submenuId):
        submenuRes = None
        
        with self.db.session_scope() as s:
            submenu = s.query(Submenu).filter(Submenu.id == submenuId).first()
            if submenu is None:
                return None
            dishesCount = s.query(Dish).filter(Dish.submenu_id == submenuId).count()
            
            submenuRes = SB.SubMenuShow(id=str(submenu.id), title=submenu.title,
                                               description=submenu.description, menu_id=submenu.menu_id,
                                               dishes_count=dishesCount)
            
        return submenuRes
    
    def createSubmenu(self, submenu):
        with self.db.session_scope() as s:
            s.add(submenu)
        
        return submenu
    
    def updateSubmenu(self, submenuId, submenuUpdate):
        with self.db.session_scope() as s:
            submenu = s.query(Submenu).filter(Submenu.id == submenuId).first()
            if submenu is None:
                return None
            
            submenu.title = submenuUpdate.title
            submenu.description = submenuUpdate.description
        
        return submenuUpdate
    
    def deleteSubmenu(self, submenuId):
        with self.db.session_scope() as s:
            submenu = s.query(Submenu).filter(Submenu.id == submenuId).first()
            if submenu is None:
                return None
            
            s.delete(submenu) 
        
        return submenuId