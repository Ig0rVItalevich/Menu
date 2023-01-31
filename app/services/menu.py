from abc import ABC, abstractmethod

from cache.cache import AbstractCache
from storage import models
from storage.repository import Repository
from structs.menu import MenuCreate, MenuCreated, MenuShow


class AbstractMenuService(ABC):
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
    def update_menu(self, menu_update, menu_id):
        pass

    @abstractmethod
    def delete_menu(self, menu_id):
        pass


class MenuService(AbstractMenuService):
    def __init__(self, repos: Repository, cache: AbstractCache):
        self.repos = repos
        self.cache = cache

    def get_menus(self) -> list[MenuShow]:
        return self.repos.get_menus()

    def get_menu(self, menu_id: str) -> MenuShow:
        cache_id = f'menu:{menu_id}'
        cache_value = self.cache.get(cache_id)
        if cache_value is not None:
            return cache_value

        bd_value = self.repos.get_menu(menu_id)
        if bd_value is None:
            return bd_value
        self.cache.set(
            cache_id, {
                'id': bd_value.id,
                'title': bd_value.title,
                'description': bd_value.description,
                'submenus_count': bd_value.submenus_count,
                'dishes_count': bd_value.dishes_count,
            },
        )

        return bd_value

    def create_menu(self, menu: MenuCreate) -> MenuCreated:
        menu_model = models.Menu(
            title=menu.title,
            description=menu.description,
        )
        menu_created = self.repos.create_menu(menu_model)

        return menu_created

    def update_menu(
        self, menu_update: MenuCreate,
        menu_id: str,
    ) -> MenuCreated:
        menu_model = models.Menu(
            title=menu_update.title,
            description=menu_update.description,
        )

        self.cache.delete(f'menu:{menu_id}')

        return self.repos.update_menu(menu_id, menu_model)

    def delete_menu(self, menu_id: str):
        self.repos.delete_menu(menu_id)

        self.cache.delete(f'menu:{menu_id}')
