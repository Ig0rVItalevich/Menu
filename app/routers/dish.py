from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse
from typing import List

from init import service
from structs.dish import *

dishRouter = APIRouter()


@dishRouter.get(path="/",
                summary="Get dishes",
                description="Get all dishes",
                response_model=List[DishShow],
                status_code=status.HTTP_200_OK)
def getDishes(submenu_id: int = Path(...)):
    return service.dishService.getDishes(submenu_id)


@dishRouter.get(path="/{dish_id}",
                summary="Get dish",
                description="Get concrete dish",
                response_model=DishShow,
                status_code=status.HTTP_200_OK)
def getDish(menu_id: int = Path(..., gt=0), submenu_id: int = Path(..., gt=0), dish_id: int = Path(..., gt=0)):
    dishSelected = service.dishService.getDish(menu_id, submenu_id, dish_id)

    if dishSelected is None:
        return JSONResponse(content={"detail": "dish not found"}, status_code=status.HTTP_404_NOT_FOUND)
    else:
        return dishSelected


@dishRouter.post(path="/",
                 summary="Post dish",
                 description="Post one dish",
                 response_model=DishCreated,
                 status_code=status.HTTP_201_CREATED)
def createDish(dish: DishCreate, menu_id: int = Path(..., gt=0), submenu_id: int = Path(...)):
    dishCreated = service.dishService.createDish(dish, menu_id, submenu_id)

    return DishCreated(id=str(dishCreated.id), title=dishCreated.title,
                            description=dishCreated.description, price="{:.2f}".format(dishCreated.price))


@dishRouter.patch(path="/{dish_id}",
                  summary="Upgrade dish",
                  description="Upgrade one dish",
                  response_model=DishCreated,
                  status_code=status.HTTP_200_OK)
def updateDish(dish: DishCreate, menu_id: int = Path(..., gt=0), submenu_id: int = Path(..., gt=0), dish_id: int = Path(..., gt=0)):
    dishUpdated = service.dishService.updateDish(
        dish, menu_id, submenu_id, dish_id)

    if dishUpdated is None:
        return JSONResponse(content={"detail": "dish not found"}, status_code=status.HTTP_404_NOT_FOUND)
    else:
        return DishCreated(id=str(dishUpdated.id), title=dishUpdated.title,
                                description=dishUpdated.description, price="{:.2f}".format(dishUpdated.price))


@dishRouter.delete(path="/{dish_id}",
                   summary="Delete dish",
                   description="Delete one dish",
                   status_code=status.HTTP_200_OK)
def deleteDish(menu_id: int = Path(..., gt=0), submenu_id: int = Path(..., gt=0), dish_id: int = Path(..., gt=0)):
    service.dishService.deleteDish(menu_id, submenu_id, dish_id)
