from abc import ABC, abstractmethod
from structs.menu import MenuShow

from .models import Dish, Menu, Submenu
from .database import DB


class AbstractMenuRepository(ABC):
    @abstractmethod
    def get_menus(self):
        pass

    @abstractmethod
    def get_menu(self, menu_id):
        pass

    @abstractmethod
    def create_menu(self, menu):
        pass

    @abstractmethod
    def update_menu(self, menu_id, menu_update):
        pass

    @abstractmethod
    def delete_menu(self, menu_id):
        pass


class MenuRepository(AbstractMenuRepository):
    def __init__(self, db: DB):
        self.db = db

    def get_menus(self) -> list[MenuShow]:
        menus = []

        with self.db.session_scope() as s:
            for menu in s.query(Menu).all():
                submenus_count = s.query(Submenu).filter(
                    Submenu.menu_id == menu.id,
                ).count()
                dishes_count = s.query(Menu, Submenu, Dish).filter(
                    (Menu.id == Submenu.menu_id) & (
                        Submenu.id == Dish.submenu_id
                    ),
                ).count()

                menus.append(
                    MenuShow(
                        id=str(menu.id),
                        title=menu.title,
                        description=menu.description,
                        submenus_count=submenus_count,
                        dishes_count=dishes_count,
                    ),
                )

        return menus

    def get_menu(self, menu_id: str) -> MenuShow:
        menu_res = None

        with self.db.session_scope() as s:
            menu = s.query(Menu).filter(Menu.id == menu_id).first()
            if menu is None:
                return None

            submenus_count = s.query(Submenu).filter(
                Submenu.menu_id == menu_id,
            ).count()
            dishes_count = s.query(Menu, Submenu, Dish).filter(
                (Menu.id == Submenu.menu_id) & (Submenu.id == Dish.submenu_id),
            ).count()

            menu_res = MenuShow(
                id=str(menu.id),
                title=menu.title,
                description=menu.description,
                submenus_count=submenus_count,
                dishes_count=dishes_count,
            )

        return menu_res

    def create_menu(self, menu: Menu) -> Menu:
        with self.db.session_scope() as s:
            s.add(menu)

        return menu

    def update_menu(self, menu_id: str, menu_update: Menu) -> Menu:
        with self.db.session_scope() as s:
            menu = s.query(Menu).filter(Menu.id == menu_id).first()
            if menu is None:
                return None

            menu.title = menu_update.title
            menu.description = menu_update.description

        return menu_update

    def delete_menu(self, menu_id: str) -> str:
        with self.db.session_scope() as s:
            menu = s.query(Menu).filter(Menu.id == menu_id).first()
            if menu is None:
                return None

            s.delete(menu)
        return menu_id
