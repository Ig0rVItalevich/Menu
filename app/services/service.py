from .menu import MenuService
from .submenu import SubmenuService
from .dish import DishService


class Service():
    def __init__(self, repos, cache):
        self.menuService = MenuService(repos.menuRepository, cache)
        self.submenuService = SubmenuService(repos.submenuRepository, cache)
        self.dishService = DishService(repos.dishRepository, cache)
