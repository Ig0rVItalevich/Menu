from fastapi import FastAPI

from .dish import dishRouter
from .menu import menuRouter
from .submenu import submenuRouter


def init_router():
    router = FastAPI()

    prefix_menu = '/api/v1/menus'
    prefix_submenu = '/api/v1/menus/{menu_id}/submenus'
    prefix_dishes = '/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes'

    router.include_router(
        menuRouter,
        prefix=prefix_menu,
        tags=['menu'],
    )
    router.include_router(
        submenuRouter,
        prefix=prefix_submenu,
        tags=['submenu'],
    )
    router.include_router(
        dishRouter,
        prefix=prefix_dishes,
        tags=['dish'],
    )

    return router
