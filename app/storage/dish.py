from abc import ABC, abstractmethod
from structs.dish import DishShow

from .models import Dish
from .database import DB


class AbstractDishRepository(ABC):
    @abstractmethod
    def get_dishes(self, submenu_id):
        pass

    @abstractmethod
    def get_dish(self, dish_id):
        pass

    @abstractmethod
    def create_dish(self, dish):
        pass

    @abstractmethod
    def update_dish(self, dish_id, dish_update):
        pass

    @abstractmethod
    def delete_dish(self, dish_id):
        pass


class DishRepository(AbstractDishRepository):
    def __init__(self, db: DB):
        self.db = db

    def get_dishes(self, submenu_id: str) -> list[DishShow]:
        dishes = []

        with self.db.session_scope() as s:
            for dish in s.query(Dish).filter(
                    Dish.submenu_id == submenu_id,
            ).all():
                dishes.append(
                    DishShow(
                        id=str(dish.id),
                        title=dish.title,
                        description=dish.description,
                        price=f'{dish.price:.2f}',
                        submenu_id=dish.submenu_id,
                    ),
                )

        return dishes

    def get_dish(self, dish_id: str) -> DishShow:
        dish_res = None

        with self.db.session_scope() as s:
            dish = s.query(Dish).filter(Dish.id == dish_id).first()
            if dish is None:
                return None

            dish_res = DishShow(
                id=str(dish.id),
                title=dish.title,
                description=dish.description,
                price=f'{dish.price:.2f}',
                submenu_id=dish.submenu_id,
            )

        return dish_res

    def create_dish(self, dish: Dish) -> Dish:
        with self.db.session_scope() as s:
            s.add(dish)

        return dish

    def update_dish(self, dish_id: str, dish_update: Dish) -> Dish:
        with self.db.session_scope() as s:
            dish = s.query(Dish).filter(Dish.id == dish_id).first()
            if dish is None:
                return None

            dish.title = dish_update.title
            dish.description = dish_update.description
            dish.price = dish_update.price

        return dish_update

    def delete_dish(self, dish_id: str) -> str:
        with self.db.session_scope() as s:
            dish = s.query(Dish).filter(Dish.id == dish_id).first()
            if dish is None:
                return None

            s.delete(dish)

        return dish_id
