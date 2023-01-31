from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse
from init import service
from structs.menu import MenuCreate, MenuCreated, MenuShow

menu_router = APIRouter()


@menu_router.get(
    path='/',
    summary='Get menus',
    description='Get all menus',
    response_model=list[MenuShow],
    status_code=status.HTTP_200_OK,
)
def get_menus():
    return service.menu_service.get_menus()


@menu_router.get(
    path='/{menu_id}',
    summary='Get menu',
    description='Get concrete menu',
    response_model=MenuShow,
    status_code=status.HTTP_200_OK,
)
def get_menu(menu_id: int = Path(..., gt=0)):
    menu_selected = service.menu_service.get_menu(menu_id)

    if menu_selected is None:
        return JSONResponse(
            content={'detail': 'menu not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        return menu_selected


@menu_router.post(
    path='/',
    summary='Post menu',
    description='Post one menu',
    response_model=MenuCreated,
    status_code=status.HTTP_201_CREATED,
)
def create_menu(menu: MenuCreate):
    menu_created = service.menu_service.create_menu(menu)

    return MenuCreated(
        id=menu_created.id,
        title=menu_created.title,
        description=menu_created.description,
    )


@menu_router.patch(
    path='/{menu_id}',
    summary='Upgrade menu',
    description='Upgrade one menu',
    response_model=MenuCreate,
    status_code=status.HTTP_200_OK,
)
def update_menu(menu: MenuCreate, menu_id: int = Path(..., gt=0)):
    menu_updated = service.menu_service.update_menu(menu, menu_id)

    if menu_updated is None:
        return JSONResponse(
            content={'detail': 'menu not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        return MenuCreated(
            id=str(menu_updated.id),
            title=menu_updated.title,
            description=menu_updated.description,
        )


@menu_router.delete(
    path='/{menu_id}',
    summary='Delete menu',
    description='Delete one menu',
    status_code=status.HTTP_200_OK,
)
def delete_menu(menu_id: int = Path(..., gt=0)):
    service.menu_service.delete_menu(menu_id)
