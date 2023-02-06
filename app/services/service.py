from dataclasses import dataclass

from cache.cache import AbstractCache
from storage.repository import Repository

from .dish import AbstractDishService, DishService
from .menu import AbstractMenuService, MenuService
from .submenu import AbstractSubmenuService, SubmenuService
from .filling import AbstractFillingService, FilingService


@dataclass
class Service():
    menu_service: AbstractMenuService
    submenu_service: AbstractSubmenuService
    dish_service: AbstractDishService
    filling_service: AbstractFillingService


def new_service(repos: Repository, cache: AbstractCache) -> Service:
    service = Service(
        menu_service=MenuService(repos.menu_repository, cache),
        submenu_service=SubmenuService(repos.submenu_repository, cache),
        dish_service=DishService(repos.dish_repository, cache),
        filling_service=None,
    )

    service.filling_service = FilingService(
        service.menu_service,
        service.submenu_service,
        service.dish_service)
    
    return service
