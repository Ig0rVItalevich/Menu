import pytest
from fastapi import status


def test_get_dishes(init_db, client, storage_dishes):
    response = client.get("/api/v1/menus/1/submenus/1/dishes")

    assert response.status_code == status.HTTP_200_OK

    response = response.json()
    for i in range(len(response)):
        assert response[i]["title"] == storage_dishes[i]["title"] and \
            response[i]["description"] == storage_dishes[i]["description"] and \
            response[i]["price"] == storage_dishes[i]["price"]


def test_post_dish(init_db, client, adding_dish):
    response = client.post("/api/v1/menus/1/submenus/1/dishes", json=adding_dish)

    assert response.status_code == status.HTTP_201_CREATED

    response = response.json()
    assert response["id"] is not None
    assert response["title"] == adding_dish["title"] and response["description"] == adding_dish["description"] and \
        response["price"] == adding_dish["price"]


def test_get_dish_positive(init_db, client, adding_dish):
    response = client.get(f"/api/v1/menus/1/submenus/1/dishes/{adding_dish['id']}")

    assert response.status_code == status.HTTP_200_OK

    response = response.json()
    assert response["id"] == adding_dish["id"] and response["title"] == adding_dish["title"] and \
        response["description"] == adding_dish["description"] and response["price"] == adding_dish["price"]


def test_get_dish_negative(init_db, client):
    response = client.get("/api/v1/menus/1/submenus/1/dishes/100")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_patch_dish(init_db, client, adding_dish, upgrade_adding_dish):
    response = client.patch(f"/api/v1/menus/1/submenus/1/dishes/{adding_dish['id']}", json=upgrade_adding_dish)

    assert response.status_code == status.HTTP_200_OK

    response = response.json()
    assert response["title"] == upgrade_adding_dish["title"] and \
        response["description"] == upgrade_adding_dish["description"] and response["price"] == upgrade_adding_dish["price"]


def test_delete_dish(init_db, client, adding_dish):
    response = client.delete(f"/api/v1/menus/1/submenus/1/dishes/{adding_dish['id']}")

    assert response.status_code == status.HTTP_200_OK  
