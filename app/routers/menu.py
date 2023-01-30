from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse
from typing import List

from init import service
from structs.menu import *

menuRouter = APIRouter()


@menuRouter.get(path="/",
                summary="Get menus",
                description="Get all menus",
                response_model=List[MenuShow],
                status_code=status.HTTP_200_OK)
def getMenus():
    return service.menuService.getMenus()


@menuRouter.get(path="/{menu_id}",
                summary="Get menu",
                description="Get concrete menu",
                response_model=MenuShow,
                status_code=status.HTTP_200_OK)
def getMenu(menu_id: int = Path(..., gt=0)):
    menuSelected = service.menuService.getMenu(menu_id)

    if menuSelected is None:
        return JSONResponse(content={"detail": "menu not found"}, status_code=status.HTTP_404_NOT_FOUND)
    else:
        return menuSelected


@menuRouter.post(path="/",
                 summary="Post menu",
                 description="Post one menu",
                 response_model=MenuCreated,
                 status_code=status.HTTP_201_CREATED)
def createMenu(menu: MenuCreate):
    menuCreated = service.menuService.createMenu(menu)

    return MenuCreated(id=menuCreated.id, title=menuCreated.title, description=menuCreated.description)

@menuRouter.patch(path="/{menu_id}",
                  summary="Upgrade menu",
                  description="Upgrade one menu",
                  response_model=MenuCreate,
                  status_code=status.HTTP_200_OK)
def updateMenu(menu: MenuCreate, menu_id: int = Path(..., gt=0)):
    menuUpdated = service.menuService.updateMenu(menu, menu_id)

    if menuUpdated is None:
        return JSONResponse(content={"detail": "menu not found"}, status_code=status.HTTP_404_NOT_FOUND)
    else:
        return menuUpdated


@menuRouter.delete(path="/{menu_id}",
                   summary="Delete menu",
                   description="Delete one menu",
                   status_code=status.HTTP_200_OK)
def deleteMenu(menu_id: int = Path(..., gt=0)):
    service.menuService.deleteMenu(menu_id)
