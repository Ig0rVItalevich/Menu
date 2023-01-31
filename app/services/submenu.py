from abc import ABC, abstractmethod

from cache.cache import AbstractCache
from storage import models
from storage.repository import Repository
from structs.submenu import SubMenuCreate, SubMenuCreated, SubMenuShow


class AbstractSubmenuService(ABC):
    @abstractmethod
    def get_submenus(self):
        pass

    @abstractmethod
    def get_submenu(self, menu_id, submenu_id):
        pass

    @abstractmethod
    def create_submenu(self, submenu, menu_id):
        pass

    @abstractmethod
    def update_submenu(self, submenu_update, menu_id, submenu_id):
        pass

    @abstractmethod
    def delete_submenu(self, menu_id, submenu_id):
        pass


class SubmenuService(AbstractSubmenuService):
    def __init__(self, repos: Repository, cache: AbstractCache):
        self.repos = repos
        self.cache = cache

    def get_submenus(self) -> list[SubMenuShow]:
        return self.repos.get_submenus()

    def get_submenu(self, menu_id: str, submenu_id: str) -> SubMenuShow:
        cache_id = f'submenu:{submenu_id}'
        cache_value = self.cache.get(cache_id)
        if cache_value is not None:
            return cache_value

        bd_value = self.repos.get_submenu(submenu_id)
        if bd_value is None:
            return bd_value
        self.cache.set(
            cache_id, {
                'title': bd_value.title,
                'description': bd_value.description,
                'menu_id': bd_value.menu_id,
                'dishes_count': bd_value.dishes_count,
            },
        )

        return bd_value

    def create_submenu(
        self, submenu: SubMenuCreate,
        menu_id: str,
    ) -> SubMenuCreated:
        submenu_model = models.Submenu(
            title=submenu.title,
            description=submenu.description,
            menu_id=menu_id,
        )
        submenu_created = self.repos.create_submenu(submenu_model)

        self.cache.delete(f'menu:{menu_id}')

        return submenu_created

    def update_submenu(
        self, submenu_update: SubMenuCreate,
        menu_id: str, submenu_id: str,
    ) -> SubMenuCreated:
        submenu_model = models.Submenu(
            title=submenu_update.title,
            description=submenu_update.description,
            menu_id=submenu_update.menu_id,
        )

        self.cache.delete(f'submenu:{submenu_id}')

        return self.repos.update_submenu(submenu_id, submenu_model)

    def delete_submenu(self, menu_id: str, submenu_id: str):
        self.repos.delete_submenu(submenu_id)

        self.cache.delete(f'submenu:{submenu_id}')
        self.cache.delete(f'menu:{menu_id}')
