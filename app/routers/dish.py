from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse

from init import service
from structs import dish

dishRouter = APIRouter()

@dishRouter.get("/")
def getDishes(submenu_id: int = Path(...)):
    return service.dishService.getDishes(submenu_id)

@dishRouter.get("/{dish_id}")
def getDish(dish_id: int = Path(..., gt=0)):
    dishSelected = service.dishService.getDish(dish_id)
    print(dishSelected)
    if dishSelected is None:
        return JSONResponse(content={"detail": "dish not found"}, status_code=404)
    else:
        return dishSelected

@dishRouter.post("/", status_code=201)
def createDish(dish: dish.DishCreate, submenu_id: int = Path(...)):
    dish.submenu_id = submenu_id
    return service.dishService.createDish(dish)    

@dishRouter.patch("/{dish_id}")
def updateDish(dish: dish.DishCreate, dish_id: int = Path(..., gt=0)):
    dishUpdated = service.dishService.updateDish(dish, dish_id)
    if dishUpdated is None:
        return JSONResponse(content={"detail": "dish not found"}, status_code=404)
    else:
        return dishUpdated

@dishRouter.delete("/{dish_id}")
def deleteDish(dish_id: int = Path(..., gt=0)):
    service.dishService.deleteDish(dish_id)

