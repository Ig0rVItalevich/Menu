from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse
from init import service
from structs.submenu import SubMenuCreate, SubMenuCreated, SubMenuShow

submenuRouter = APIRouter()


@submenuRouter.get(
    path='/',
    summary='Get submenus',
    description='Get all submenus',
    response_model=list[SubMenuShow],
    status_code=status.HTTP_200_OK,
)
def getSubmenus():
    return service.submenuService.getSubmenus()


@submenuRouter.get(
    path='/{submenu_id}',
    summary='Get submenu',
    description='Get concrete submenus',
    response_model=SubMenuShow,
    status_code=status.HTTP_200_OK,
)
def getSubmenu(
    menu_id: int = Path(..., gt=0),
    submenu_id: int = Path(..., gt=0),
):
    submenuSelected = service.submenuService.getSubmenu(menu_id, submenu_id)

    if submenuSelected is None:
        return JSONResponse(
            content={'detail': 'submenu not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        return submenuSelected


@submenuRouter.post(
    path='/',
    summary='Post submenu',
    description='Post one submenu',
    response_model=SubMenuCreated,
    status_code=status.HTTP_201_CREATED,
)
def createSubmenu(submenu: SubMenuCreate, menu_id: int = Path(..., gt=0)):
    submenuCreated = service.submenuService.createSubmenu(submenu, menu_id)

    return SubMenuCreated(
        id=submenuCreated.id, title=submenuCreated.title,
        description=submenuCreated.description,
    )


@submenuRouter.patch(
    path='/{submenu_id}',
    summary='Upgrade submenu',
    description='Upgrade one submenu',
    response_model=SubMenuCreated,
    status_code=status.HTTP_200_OK,
)
def updateSubmenu(
    submenu: SubMenuCreate, menu_id: int = Path(..., gt=0),
    submenu_id: int = Path(..., gt=0),
):
    submenuUpdated = service.submenuService.updateSubmenu(
        submenu, menu_id, submenu_id,
    )

    if submenuUpdated is None:
        return JSONResponse(
            content={'detail': 'submenu not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        return SubMenuCreated(
            id=str(submenuUpdated.id),
            title=submenuUpdated.title,
            description=submenuUpdated.description,
        )


@submenuRouter.delete(
    path='/{submenu_id}',
    summary='Delete submenu',
    description='Delete one submenu',
    status_code=status.HTTP_200_OK,
)
def deleteSubmenu(
    menu_id: int = Path(..., gt=0),
    submenu_id: int = Path(..., gt=0),
):
    service.submenuService.deleteSubmenu(menu_id, submenu_id)
