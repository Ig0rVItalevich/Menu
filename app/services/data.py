from abc import ABC, abstractmethod
import json

from services.menu import AbstractMenuService
from services.submenu import AbstractSubmenuService
from services.dish import AbstractDishService

from structs.menu import MenuCreate
from structs.submenu import SubMenuCreate
from structs.dish import DishCreate

from openpyxl import Workbook


class AbstractDataService(ABC):
    # @abstractmethod
    # def generate_file(self):
    #     pass

    abstractmethod
    def get_data(self):
        pass


class DataService(AbstractDataService):
    def __init__(self, menu_service: AbstractMenuService):
        self.menu_service = menu_service
    
    def get_data(self) -> None:
        data = self.menu_service.get_all_data()
        
        wb = Workbook()
        ws = wb.active
        
        column_dimensions = {"A": 5, "B": 10, "C": 20, "D": 30, "E": 50, "F": 10}
        for col, value in column_dimensions.items():
            ws.column_dimensions[col].width = value
        
        for menu_id, menu in data.items():
            ws.append([menu_id, menu["title"], menu["description"]])
            
            for submenu_id, submenu in menu["submenus"].items():
                ws.append(["", submenu_id, submenu["title"], submenu["description"]])
                for dish_id, dish in submenu["dishes"].items():
                    ws.append(["", "", dish_id, dish["title"], dish["description"], dish["price"]])
                    
        wb.save("test.xlsx")
        
        
