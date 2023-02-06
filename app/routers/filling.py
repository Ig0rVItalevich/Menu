from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse

from init import service, DATA_PATH


filling_router = APIRouter()


@filling_router.post(
    path='/',
    summary='Filling DB',
    description='Populates the database with test data',
    status_code=status.HTTP_201_CREATED,
)
def filling_db():
    service.filling_service.filling_db(path=DATA_PATH)
