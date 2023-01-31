from dataclasses import dataclass

from .database import DB
from .dish import AbstractDishRepository, DishRepository
from .menu import AbstractMenuRepository, MenuRepository
from .submenu import AbstractSubmenuRepository, SubmenuRepository


@dataclass
class Repository():
    menu_repository: AbstractMenuRepository
    submenu_repository: AbstractSubmenuRepository
    dish_repository: AbstractDishRepository


def new_repository(db: DB) -> Repository:
    return Repository(
        menu_repository=MenuRepository(db),
        submenu_repository=SubmenuRepository(db),
        dish_repository=DishRepository(db),
    )
