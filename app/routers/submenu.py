from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse
from init import service
from structs.submenu import SubMenuCreate, SubMenuCreated, SubMenuShow

submenu_router = APIRouter()


@submenu_router.get(
    path='/',
    summary='Get submenus',
    description='Get all submenus',
    response_model=list[SubMenuShow],
    status_code=status.HTTP_200_OK,
)
def get_submenus():
    return service.submenu_service.get_submenus()


@submenu_router.get(
    path='/{submenu_id}',
    summary='Get submenu',
    description='Get concrete submenus',
    response_model=SubMenuShow,
    status_code=status.HTTP_200_OK,
)
def get_submenu(
    menu_id: int = Path(..., gt=0),
    submenu_id: int = Path(..., gt=0),
):
    submenu_selected = service.submenu_service.get_submenu(menu_id, submenu_id)

    if submenu_selected is None:
        return JSONResponse(
            content={'detail': 'submenu not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        return submenu_selected


@submenu_router.post(
    path='/',
    summary='Post submenu',
    description='Post one submenu',
    response_model=SubMenuCreated,
    status_code=status.HTTP_201_CREATED,
)
def create_submenu(submenu: SubMenuCreate, menu_id: int = Path(..., gt=0)):
    submenu_created = service.submenu_service.create_submenu(submenu, menu_id)

    return SubMenuCreated(
        id=submenu_created.id, title=submenu_created.title,
        description=submenu_created.description,
    )


@submenu_router.patch(
    path='/{submenu_id}',
    summary='Upgrade submenu',
    description='Upgrade one submenu',
    response_model=SubMenuCreated,
    status_code=status.HTTP_200_OK,
)
def update_submenu(
    submenu: SubMenuCreate, menu_id: int = Path(..., gt=0),
    submenu_id: int = Path(..., gt=0),
):
    submenu_updated = service.submenu_service.update_submenu(
        submenu, menu_id, submenu_id,
    )

    if submenu_updated is None:
        return JSONResponse(
            content={'detail': 'submenu not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        return SubMenuCreated(
            id=str(submenu_updated.id),
            title=submenu_updated.title,
            description=submenu_updated.description,
        )


@submenu_router.delete(
    path='/{submenu_id}',
    summary='Delete submenu',
    description='Delete one submenu',
    status_code=status.HTTP_200_OK,
)
def delete_submenu(
    menu_id: int = Path(..., gt=0),
    submenu_id: int = Path(..., gt=0),
):
    service.submenu_service.delete_submenu(menu_id, submenu_id)
