from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse

from init import service

data_router = APIRouter()


@data_router.post(
    path='/',
    summary='Generate excel file',
    description='Generate excel file',
    status_code=status.HTTP_202_ACCEPTED,
)
def generate_file():
    pass

@data_router.get(
    path='/{task_id}',
    summary='Get excel file',
    description='Get excel file',
    status_code=status.HTTP_200_OK,
)
def get_file():
    service.data_service.get_data()
