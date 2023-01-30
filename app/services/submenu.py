from storage import models


class SubmenuService():
    def __init__(self, repos, cache):
        self.repos = repos
        self.cache = cache

    def getSubmenus(self):
        return self.repos.getSubmenus()

    def getSubmenu(self, menuId, submenuId):
        cacheId = f'submenu:{submenuId}'
        cacheValue = self.cache.get(cacheId)
        if cacheValue is not None:
            return cacheValue

        bdValue = self.repos.getSubmenu(submenuId)
        if bdValue is None:
            return bdValue
        self.cache.set(
            cacheId, {
                'title': bdValue.title,
                'description': bdValue.description,
                'menu_id': bdValue.menu_id,
                'dishes_count': bdValue.dishes_count,
            },
        )

        return bdValue

    def createSubmenu(self, submenu, menuId):
        submenuModel = models.Submenu(
            title=submenu.title,
            description=submenu.description,
            menu_id=menuId,
        )
        submenuCreated = self.repos.createSubmenu(submenuModel)

        self.cache.delete(f'menu:{menuId}')

        return submenuCreated

    def updateSubmenu(self, submenuUpdate, menuId, submenuId):
        submenuModel = models.Submenu(
            title=submenuUpdate.title,
            description=submenuUpdate.description,
            menu_id=submenuUpdate.menu_id,
        )

        self.cache.delete(f'submenu:{submenuId}')

        return self.repos.updateSubmenu(submenuId, submenuModel)

    def deleteSubmenu(self, menuId, submenuId):
        self.repos.deleteSubmenu(submenuId)

        self.cache.delete(f'submenu:{submenuId}')
        self.cache.delete(f'menu:{menuId}')
