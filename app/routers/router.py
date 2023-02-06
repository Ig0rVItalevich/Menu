from fastapi import FastAPI

from .dish import dish_router
from .menu import menu_router
from .submenu import submenu_router
from .filling import filling_router
from .data import data_router


def init_router():
    router = FastAPI()

    prefix_menu = '/api/v1/menus'
    prefix_submenu = '/api/v1/menus/{menu_id}/submenus'
    prefix_dishes = '/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes'
    prefix_filling = '/api/v1/filling'
    prefix_data = '/api/v1/data'

    router.include_router(
        menu_router,
        prefix=prefix_menu,
        tags=['menu'],
    )
    router.include_router(
        submenu_router,
        prefix=prefix_submenu,
        tags=['submenu'],
    )
    router.include_router(
        dish_router,
        prefix=prefix_dishes,
        tags=['dish'],
    )
    router.include_router(
        filling_router,
        prefix=prefix_filling,
        tags=['filling'],
    )
    router.include_router(
        data_router,
        prefix=prefix_data,
        tags=['data'],
    )

    return router
