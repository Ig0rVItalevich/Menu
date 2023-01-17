from structs import menu as MN
from storage import models


class MenuService():
    def __init__(self, repos):
        self.repos = repos

    def getMenus(self):
        return self.repos.getMenus()

    def getMenu(self, menuId):
        return self.repos.getMenu(menuId)

    def createMenu(self, menu):
        menuModel = models.Menu(title=menu.title, description=menu.description)
        menuCreated = self.repos.createMenu(menuModel)

        return MN.MenuCreated(id=menuCreated.id, title=menuCreated.title, description=menuCreated.description)

    def updateMenu(self, menuUpdate, menuId):
        menuModel = models.Menu(title=menuUpdate.title,
                                description=menuUpdate.description)
        return self.repos.updateMenu(menuId, menuModel)

    def deleteMenu(self, menuId):
        self.repos.deleteMenu(menuId)
