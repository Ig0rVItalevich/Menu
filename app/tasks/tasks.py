from openpyxl import Workbook

from celery.result import AsyncResult
from .celery import app


@app.task
def generate_data(data) -> AsyncResult:
    task_id = app.current_task.request.id

    wb = Workbook()
    ws = wb.active
    ws.title = "Меню"

    column_dimensions = {"A": 5, "B": 10, "C": 20, "D": 30, "E": 50, "F": 10}
    for column, value in column_dimensions.items():
        ws.column_dimensions[column].width = value

    for menu_id, menu in data.items():
        ws.append([menu_id,
                   menu["title"],
                   menu["description"]])

        for submenu_id, submenu in menu["submenus"].items():
            ws.append(["",
                       submenu_id,
                       submenu["title"],
                       submenu["description"]])

            for dish_id, dish in submenu["dishes"].items():
                ws.append(["",
                           "",
                           dish_id,
                           dish["title"],
                           dish["description"],
                           dish["price"]])

    wb.save(f"{task_id}.xlsx")

    return task_id


def get_info(task_id):
    result = AsyncResult(task_id)

    return {
        "id": result.id.__str__(),
        "status": result.status,
        "result": result.result,
    }
