from storage import models


class MenuService():
    def __init__(self, repos, cache):
        self.repos = repos
        self.cache = cache

    def getMenus(self):
        return self.repos.getMenus()

    def getMenu(self, menuId):
        cacheId = f'menu:{menuId}'
        cacheValue = self.cache.get(cacheId)
        if cacheValue is not None:
            return cacheValue

        bdValue = self.repos.getMenu(menuId)
        if bdValue is None:
            return bdValue
        self.cache.set(
            cacheId, {
                'id': bdValue.id,
                'title': bdValue.title,
                'description': bdValue.description,
                'submenus_count': bdValue.submenus_count,
                'dishes_count': bdValue.dishes_count,
            },
        )

        return bdValue

    def createMenu(self, menu):
        menuModel = models.Menu(
            title=menu.title,
            description=menu.description,
        )
        menuCreated = self.repos.createMenu(menuModel)

        return menuCreated

    def updateMenu(self, menuUpdate, menuId):
        menuModel = models.Menu(
            title=menuUpdate.title,
            description=menuUpdate.description,
        )

        self.cache.delete(f'menu:{menuId}')

        return self.repos.updateMenu(menuId, menuModel)

    def deleteMenu(self, menuId):
        self.repos.deleteMenu(menuId)

        self.cache.delete(f'menu:{menuId}')
