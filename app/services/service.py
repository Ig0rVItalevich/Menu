from dataclasses import dataclass

from cache.cache import AbstractCache
from storage.repository import Repository

from .dish import AbstractDishService, DishService
from .menu import AbstractMenuService, MenuService
from .submenu import AbstractSubmenuService, SubmenuService


@dataclass
class Service():
    menu_service: AbstractMenuService
    submenu_service: AbstractSubmenuService
    dish_service: AbstractDishService


def new_service(repos: Repository, cache: AbstractCache) -> Service:
    return Service(
        menu_service=MenuService(repos.menu_repository, cache),
        submenu_service=SubmenuService(repos.submenu_repository, cache),
        dish_service=DishService(repos.dish_repository, cache),
    )
