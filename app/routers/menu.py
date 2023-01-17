from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse

from init import service
from structs import menu

menuRouter = APIRouter()
    
@menuRouter.get("/")
def getMenus():
    return service.menuService.getMenus()

@menuRouter.get("/{menu_id}")
def getMenu(menu_id: int = Path(..., gt=0)):
    menuSelected = service.menuService.getMenu(menu_id)
    if menuSelected is None:
        return JSONResponse(content={"detail": "menu not found"}, status_code=404)
    else:
        return menuSelected

@menuRouter.post("/", status_code=201)
def createMenu(menu: menu.MenuCreate):
    return service.menuService.createMenu(menu)

@menuRouter.patch("/{menu_id}")
def updateMenu(menu: menu.MenuCreate, menu_id: int = Path(..., gt=0)):
    menuUpdated = service.menuService.updateMenu(menu, menu_id)
    if menuUpdated is None:
        return JSONResponse(content={"detail": "menu not found"}, status_code=404)
    else:
        return menuUpdated

@menuRouter.delete("/{menu_id}")
def deleteMenu(menu_id: int = Path(..., gt=0)):
    service.menuService.deleteMenu(menu_id)
