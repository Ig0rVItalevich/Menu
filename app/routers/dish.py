from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse
from init import service
from structs.dish import DishCreate, DishCreated, DishShow

dish_router = APIRouter()


@dish_router.get(
    path='/',
    summary='Get dishes',
    description='Get all dishes',
    response_model=list[DishShow],
    status_code=status.HTTP_200_OK,
)
def get_dishes(submenu_id: int = Path(...)):
    return service.dish_service.get_dishes(submenu_id)


@dish_router.get(
    path='/{dish_id}',
    summary='Get dish',
    description='Get concrete dish',
    response_model=DishShow,
    status_code=status.HTTP_200_OK,
)
def get_dish(
    menu_id: int = Path(..., gt=0), submenu_id: int = Path(..., gt=0),
    dish_id: int = Path(..., gt=0),
):
    dish_selected = service.dish_service.get_dish(menu_id, submenu_id, dish_id)

    if dish_selected is None:
        return JSONResponse(
            content={'detail': 'dish not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        return dish_selected


@dish_router.post(
    path='/',
    summary='Post dish',
    description='Post one dish',
    response_model=DishCreated,
    status_code=status.HTTP_201_CREATED,
)
def create_dish(
    dish: DishCreate, menu_id: int = Path(..., gt=0),
    submenu_id: int = Path(...),
):
    dish_created = service.dish_service.create_dish(dish, menu_id, submenu_id)

    return DishCreated(
        id=str(dish_created.id),
        title=dish_created.title,
        description=dish_created.description,
        price=f'{dish_created.price:.2f}',
    )


@dish_router.patch(
    path='/{dish_id}',
    summary='Upgrade dish',
    description='Upgrade one dish',
    response_model=DishCreated,
    status_code=status.HTTP_200_OK,
)
def update_dish(
    dish: DishCreate, menu_id: int = Path(..., gt=0),
    submenu_id: int = Path(..., gt=0),
    dish_id: int = Path(..., gt=0),
):
    dish_updated = service.dish_service.update_dish(
        dish, menu_id, submenu_id, dish_id,
    )

    if dish_updated is None:
        return JSONResponse(
            content={'detail': 'dish not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        return DishCreated(
            id=str(dish_updated.id),
            title=dish_updated.title,
            description=dish_updated.description,
            price=f'{dish_updated.price:.2f}',
        )


@dish_router.delete(
    path='/{dish_id}',
    summary='Delete dish',
    description='Delete one dish',
    status_code=status.HTTP_200_OK,
)
def delete_dish(
    menu_id: int = Path(..., gt=0),
    submenu_id: int = Path(..., gt=0),
    dish_id: int = Path(..., gt=0),
):
    service.dish_service.delete_dish(menu_id, submenu_id, dish_id)
