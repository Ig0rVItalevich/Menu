from abc import ABC, abstractmethod
from structs.submenu import SubMenuShow

from .models import Dish, Submenu
from .database import DB

class AbstractSubmenuRepository(ABC):
    @abstractmethod
    def get_submenus(self):
        pass

    @abstractmethod
    def get_submenu(self, submenu_id):
        pass

    @abstractmethod
    def create_submenu(self, submenu):
        pass

    @abstractmethod
    def update_submenu(self, submenu_id, submenu_update):
        pass

    @abstractmethod
    def delete_submenu(self, submenu_id):
        pass

class SubmenuRepository(AbstractSubmenuRepository):
    def __init__(self, db: DB):
        self.db = db

    def get_submenus(self) -> list[SubMenuShow]:
        submenus = []

        with self.db.session_scope() as s:
            for submenu in s.query(Submenu).all():
                dishes_count = s.query(Dish).filter(
                    Dish.submenu_id == submenu.id,
                ).count()

                submenus.append(
                    SubMenuShow(
                        id=str(submenu.id),
                        title=submenu.title,
                        description=submenu.description,
                        menu_id=submenu.menu_id,
                        dishes_count=dishes_count,
                    ),
                )

        return submenus

    def get_submenu(self, submenu_id: str) -> SubMenuShow:
        submenu_res = None

        with self.db.session_scope() as s:
            submenu = s.query(Submenu).filter(Submenu.id == submenu_id).first()
            if submenu is None:
                return None
            dishes_count = s.query(Dish).filter(
                Dish.submenu_id == submenu_id,
            ).count()

            submenu_res = SubMenuShow(
                id=str(submenu.id), title=submenu.title,
                description=submenu.description, menu_id=submenu.menu_id,
                dishes_count=dishes_count,
            )

        return submenu_res

    def create_submenu(self, submenu: Submenu) -> Submenu:
        with self.db.session_scope() as s:
            s.add(submenu)

        return submenu

    def update_submenu(self, submenu_id: str, submenu_update: Submenu) -> Submenu:
        with self.db.session_scope() as s:
            submenu = s.query(Submenu).filter(Submenu.id == submenu_id).first()
            if submenu is None:
                return None

            submenu.title = submenu_update.title
            submenu.description = submenu_update.description

        return submenu_update

    def delete_submenu(self, submenu_id: str) -> str:
        with self.db.session_scope() as s:
            submenu = s.query(Submenu).filter(Submenu.id == submenu_id).first()
            if submenu is None:
                return None

            s.delete(submenu)

        return submenu_id
