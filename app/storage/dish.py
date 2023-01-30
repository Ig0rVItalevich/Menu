from structs import dish as DSH

from .models import Dish


class DishRepository():
    def __init__(self, db):
        self.db = db

    def getDishes(self, submenuId):
        dishes = []

        with self.db.session_scope() as s:
            for dish in s.query(Dish).filter(
                    Dish.submenu_id == submenuId,
            ).all():
                dishes.append(
                    DSH.DishShow(
                        id=str(dish.id),
                        title=dish.title,
                        description=dish.description,
                        price=f'{dish.price:.2f}',
                        submenu_id=dish.submenu_id,
                    ),
                )

        return dishes

    def getDish(self, dishId):
        dishRes = None

        with self.db.session_scope() as s:
            dish = s.query(Dish).filter(Dish.id == dishId).first()
            if dish is None:
                return None

            dishRes = DSH.DishShow(
                id=str(dish.id),
                title=dish.title,
                description=dish.description,
                price=f'{dish.price:.2f}',
                submenu_id=dish.submenu_id,
            )

        return dishRes

    def createDish(self, dish):
        with self.db.session_scope() as s:
            s.add(dish)

        return dish

    def updateDish(self, dishId, dishUpdate):
        with self.db.session_scope() as s:
            dish = s.query(Dish).filter(Dish.id == dishId).first()
            if dish is None:
                return None

            dish.title = dishUpdate.title
            dish.description = dishUpdate.description
            dish.price = dishUpdate.price

        return dishUpdate

    def deleteDish(self, dishId):
        with self.db.session_scope() as s:
            dish = s.query(Dish).filter(Dish.id == dishId).first()
            if dish is None:
                return None

            s.delete(dish)

        return dishId
