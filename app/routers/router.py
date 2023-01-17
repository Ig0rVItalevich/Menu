from fastapi import FastAPI

from .menu import menuRouter
from .submenu import submenuRouter
from .dish import dishRouter

def init_router():
    router = FastAPI()

    router.include_router(menuRouter, prefix='/api/v1/menus', tags=['menu'])
    router.include_router(submenuRouter, prefix='/api/v1/menus/{menu_id}/submenus', tags=['submenu'])
    router.include_router(dishRouter, prefix='/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes', tags=['dish'])
    
    return router