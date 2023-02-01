from abc import ABC, abstractmethod

from cache.cache import AbstractCache
from storage import models
from storage.repository import Repository
from structs.dish import DishCreate, DishCreated, DishShow


class AbstractDishService(ABC):
    @abstractmethod
    def get_dishes(self, submenu_id):
        pass

    @abstractmethod
    def get_dish(self, menu_id, submenu_id, dish_id):
        pass

    @abstractmethod
    def create_dish(self, dish, menu_id, submenu_id):
        pass

    @abstractmethod
    def update_dish(self, dish_update, menu_id, submenu_id, dish_id):
        pass

    @abstractmethod
    def delete_dish(self, menu_id, submenu_id, dish_id):
        pass


class DishService(AbstractDishService):
    def __init__(self, repos: Repository, cache: AbstractCache):
        self.repos = repos
        self.cache = cache

    def get_dishes(self, submenu_id: str) -> list[DishShow]:
        dishes = self.repos.get_dishes(submenu_id)

        for dish in dishes:
            cache_id = f'dish:{dish.id}'
            self.cache.set(
                cache_id, {
                    'id': dish.id,
                    'title': dish.title,
                    'description': dish.description,
                    'submenu_id': dish.submenu_id,
                    'price': dish.price,
                },
            )

        return dishes

    def get_dish(
        self, menu_id: str, submenu_id: str,
        dish_id: str,
    ) -> DishShow:
        cache_id = f'dish:{dish_id}'
        cache_value = self.cache.get(cache_id)
        if cache_value is not None:
            return cache_value

        bd_value = self.repos.get_dish(dish_id)
        if bd_value is None:
            return bd_value
        self.cache.set(
            cache_id, {
                'id': bd_value.id,
                'title': bd_value.title,
                'description': bd_value.description,
                'submenu_id': bd_value.submenu_id,
                'price': bd_value.price,
            },
        )

        return bd_value

    def create_dish(
        self, dish: DishCreate, menu_id: str,
        submenu_id: str,
    ) -> DishCreated:
        dish_model = models.Dish(
            title=dish.title,
            description=dish.description,
            price=dish.price,
            submenu_id=submenu_id,
        )
        dish_created = self.repos.create_dish(dish_model)

        return dish_created

    def update_dish(
        self, dish_update: DishCreate,
        menu_id: str, submenu_id: str, dish_id: str,
    ) -> DishCreated:
        dish_model = models.Dish(
            title=dish_update.title,
            description=dish_update.description,
            price=dish_update.price,
            submenu_id=dish_update.submenu_id,
        )
        updated_dish = self.repos.update_dish(dish_id, dish_model)

        self.cache.delete(f'dish:{dish_id}')

        return updated_dish

    def delete_dish(self, menu_id: str, submenu_id: str, dish_id: str):
        self.repos.delete_dish(dish_id)

        self.cache.delete(f'dish:{dish_id}')
        self.cache.delete(f'submenu:{submenu_id}')
        self.cache.delete(f'menu:{menu_id}')
