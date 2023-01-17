from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse

from init import service
from structs import submenu

submenuRouter = APIRouter()

    
@submenuRouter.get("/")
def getSubmenus():
    return service.submenuService.getSubmenus()

@submenuRouter.get("/{submenu_id}")
def getSubmenu(submenu_id: int = Path(..., gt=0)):
    submenuSelected =  service.submenuService.getSubmenu(submenu_id)
    if submenuSelected is None:
        return JSONResponse(content={"detail": "submenu not found"}, status_code=404)
    else:
        return submenuSelected

@submenuRouter.post("/", status_code=201)
def createSubmenu(submenu: submenu.SubMenuCreate, menu_id: int = Path(..., gt=0)):
    submenu.menu_id = menu_id
    return service.submenuService.createSubmenu(submenu)

@submenuRouter.patch("/{submenu_id}")
def updateSubmenu(submenu: submenu.SubMenuCreate, submenu_id: int = Path(..., gt=0)):
    submenuUpdated = service.submenuService.updateSubmenu(submenu, submenu_id)
    if submenuUpdated is None:
        return JSONResponse(content={"detail": "submenu not found"}, status_code=404)
    else:
        return submenuUpdated

@submenuRouter.delete("/{submenu_id}")
def deleteSubmenu(submenu_id: int = Path(..., gt=0)):
    service.submenuService.deleteSubmenu(submenu_id)
