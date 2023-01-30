from cache.cache import Cache
from storage import models


class DishService():
    def __init__(self, repos, cache: Cache):
        self.repos = repos
        self.cache = cache

    def getDishes(self, submenuId):
        return self.repos.getDishes(submenuId)

    def getDish(self, menuId, submenuId, dishId):
        cacheId = f'dish:{dishId}'
        cacheValue = self.cache.get(cacheId)
        if cacheValue is not None:
            return cacheValue

        bdValue = self.repos.getDish(dishId)
        if bdValue is None:
            return bdValue
        self.cache.set(
            cacheId, {
                'id': bdValue.id,
                'title': bdValue.title,
                'description': bdValue.description,
                'submenu_id': bdValue.submenu_id,
                'price': bdValue.price,
            },
        )

        return bdValue

    def createDish(self, dish, menuId, submenuId):
        dishModel = models.Dish(
            title=dish.title,
            description=dish.description,
            price=dish.price,
            submenu_id=submenuId,
        )
        dishCreated = self.repos.createDish(dishModel)

        return dishCreated

    def updateDish(self, dishUpdate, menuId, submenuId, dishId):
        dishModel = models.Dish(
            title=dishUpdate.title,
            description=dishUpdate.description,
            price=dishUpdate.price,
            submenu_id=dishUpdate.submenu_id,
        )
        updatedDish = self.repos.updateDish(dishId, dishModel)

        self.cache.delete(f'dish:{dishId}')

        return updatedDish

    def deleteDish(self, menuId, submenuId, dishId):
        self.repos.deleteDish(dishId)

        self.cache.delete(f'dish:{dishId}')
        self.cache.delete(f'submenu:{submenuId}')
        self.cache.delete(f'menu:{menuId}')
