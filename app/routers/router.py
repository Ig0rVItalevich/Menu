from fastapi import FastAPI

from .dish import dish_router
from .menu import menu_router
from .submenu import submenu_router


def init_router():
    router = FastAPI()

    prefix_menu = '/api/v1/menus'
    prefix_submenu = '/api/v1/menus/{menu_id}/submenus'
    prefix_dishes = '/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes'

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

    return router
