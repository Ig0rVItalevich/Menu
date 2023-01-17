from structs import submenu as SM
from storage import models


class SubmenuService():
    def __init__(self, repos):
        self.repos = repos

    def getSubmenus(self):
        return self.repos.getSubmenus()

    def getSubmenu(self, submenuId):
        return self.repos.getSubmenu(submenuId)

    def createSubmenu(self, submenu):
        submenuModel = models.Submenu(
            title=submenu.title, description=submenu.description, menu_id=submenu.menu_id)
        submenuCreated = self.repos.createSubmenu(submenuModel)

        return SM.SubMenuCreated(id=submenuCreated.id, title=submenuCreated.title,
                                 description=submenuCreated.description)

    def updateSubmenu(self, submenuUpdate, submenuId):
        submenuModel = models.Submenu(
            title=submenuUpdate.title, description=submenuUpdate.description, menu_id=submenuUpdate.menu_id)
        return self.repos.updateSubmenu(submenuId, submenuModel)

    def deleteSubmenu(self, submenuId):
        self.repos.deleteSubmenu(submenuId)
