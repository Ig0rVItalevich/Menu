from fastapi import FastAPI

from .dish import dishRouter
from .menu import menuRouter
from .submenu import submenuRouter


def init_router():
    router = FastAPI()

    router.include_router(menuRouter, prefix='/api/v1/menus', tags=['menu'])
    router.include_router(
        submenuRouter, prefix='/api/v1/menus/{menu_id}/submenus',
        tags=['submenu'],
    )
    router.include_router(
        dishRouter, prefix='/api/v1/menus/{menu_id}/submenus/\
            {submenu_id}/dishes', tags=['dish'],
    )

    return router
