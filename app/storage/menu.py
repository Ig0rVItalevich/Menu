from .models import Menu, Submenu, Dish
from structs import menu as MN


class MenuRepository():
    def __init__(self, db):
        self.db = db

    def getMenus(self):
        menus = []

        with self.db.session_scope() as s:
            for menu in s.query(Menu).all():
                submenusCount = s.query(Submenu).filter(
                    Submenu.menu_id == menu.id).count()
                dishesCount = s.query(Menu, Submenu, Dish).filter(
                    (Menu.id == Submenu.menu_id) & (Submenu.id == Dish.submenu_id)).count()

                menus.append(MN.MenuShow(id=str(menu.id), title=menu.title, description=menu.description,
                                         submenus_count=submenusCount, dishes_count=dishesCount))

        return menus

    def getMenu(self, menuId):
        menuRes = None

        with self.db.session_scope() as s:
            menu = s.query(Menu).filter(Menu.id == menuId).first()
            if menu is None:
                return None
            
            submenusCount = s.query(Submenu).filter(
                Submenu.menu_id == menuId).count()
            dishesCount = s.query(Menu, Submenu, Dish).filter(
                (Menu.id == Submenu.menu_id) & (Submenu.id == Dish.submenu_id)).count()

            menuRes = MN.MenuShow(id=str(menu.id), title=menu.title, description=menu.description,
                                  submenus_count=submenusCount, dishes_count=dishesCount)

        return menuRes

    def createMenu(self, menu):
        with self.db.session_scope() as s:
            s.add(menu)

        return menu

    def updateMenu(self, menuId, menuUpdate):
        with self.db.session_scope() as s:
            menu = s.query(Menu).filter(Menu.id == menuId).first()
            if menu is None:
                return None
            
            menu.title = menuUpdate.title
            menu.description = menuUpdate.description

        return menuUpdate

    def deleteMenu(self, menuId):
        with self.db.session_scope() as s:
            menu = s.query(Menu).filter(Menu.id == menuId).first()
            if menu is None:
                return None
            
            s.delete(menu)
        return menuId
