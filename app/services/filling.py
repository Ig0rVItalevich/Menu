from abc import ABC, abstractmethod
import json

from services.menu import AbstractMenuService
from services.submenu import AbstractSubmenuService
from services.dish import AbstractDishService

from structs.menu import MenuCreate
from structs.submenu import SubMenuCreate
from structs.dish import DishCreate


class AbstractFillingService(ABC):
    @abstractmethod
    def filling_db(self, path):
        pass


class FilingService(AbstractFillingService):
    def __init__(self,
                 menu_service: AbstractMenuService,
                 submenU_service: AbstractSubmenuService,
                 dish_service: AbstractDishService):
        self.menu_service = menu_service
        self.submenu_service = submenU_service
        self.dish_service = dish_service

    def filling_db(self, path: str) -> None:
        with open(path, "r") as file:
            data = json.loads(file.read())

            for menu in data:
                menu_created = self.menu_service.create_menu(MenuCreate(title=menu["title"],
                                                                        description=menu["description"]))

                for submenu in menu["submenus"]:
                    submenu_created = self.submenu_service.create_submenu(SubMenuCreate(title=submenu["title"],
                                                                                        description=submenu["description"]),
                                                                          menu_created.id)

                    for dish in submenu["dishes"]:
                        self.dish_service.create_dish(DishCreate(title=dish["title"],
                                                                 description=dish["description"],
                                                                 price=float(dish["price"])),
                                                      menu_created.id,
                                                      submenu_created.id)
