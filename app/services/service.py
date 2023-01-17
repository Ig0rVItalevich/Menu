from .menu import MenuService
from .submenu import SubmenuService
from .dish import DishService

class Service():
    def __init__(self, repos):
        self.menuService = MenuService(repos.menuRepository)
        self.submenuService = SubmenuService(repos.submenuRepository)
        self.dishService = DishService(repos.dishRepository)