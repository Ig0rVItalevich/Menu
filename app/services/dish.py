from structs import dish as DSH
from storage import models


class DishService():
    def __init__(self, repos):
        self.repos = repos

    def getDishes(self, submenuId):
        return self.repos.getDishes(submenuId)

    def getDish(self, dishId):
        return self.repos.getDish(dishId)

    def createDish(self, dish):
        dishModel = models.Dish(
            title=dish.title, description=dish.description, price=dish.price, submenu_id=dish.submenu_id)
        dishCreated = self.repos.createDish(dishModel)

        return DSH.DishCreated(id=int(dishCreated.id), title=dishCreated.title,
                               description=dishCreated.description, price="{:.2f}".format(dishCreated.price))

    def updateDish(self, dishUpdate, dishId):
        dishModel = models.Dish(
            title=dishUpdate.title, description=dishUpdate.description, price=dishUpdate.price,
            submenu_id=dishUpdate.submenu_id)
        updatedDish = self.repos.updateDish(dishId, dishModel)
        
        return DSH.DishCreated(id=str(updatedDish.id), title=updatedDish.title,
                               description=updatedDish.description, price="{:.2f}".format(updatedDish.price))

    def deleteDish(self, dishId):
        self.repos.deleteDish(dishId)
