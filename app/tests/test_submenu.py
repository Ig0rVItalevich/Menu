import pytest

from fastapi import status

def test_get_submenus(client, storage_submenus):
    response = client.get("/api/v1/menus/1/submenus")

    assert response.status_code == status.HTTP_200_OK

    response = response.json()
    for i in range(len(response)):
        assert response[i]["title"] == storage_submenus[i]["title"] and \
            response[i]["description"] == storage_submenus[i]["description"]

def test_post_submenu(client, adding_submenu):
    response = client.post("/api/v1/menus/1/submenus", json=adding_submenu)

    assert response.status_code == status.HTTP_201_CREATED

    response = response.json()
    assert response["id"] is not None
    assert response["title"] == adding_submenu["title"] and response["description"] == adding_submenu["description"]

def test_get_submenu_positive(client, adding_submenu):
    response = client.get(f"/api/v1/menus/1/submenus/{adding_submenu['id']}")

    assert response.status_code == status.HTTP_200_OK

    response = response.json()
    assert response["id"] == adding_submenu["id"] and response["title"] == adding_submenu["title"] and \
        response["description"] == adding_submenu["description"]

def test_get_submenu_negative(client):
    response = client.get("/api/v1/menus/1/submenus/100")

    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_patch_submenu(client, adding_submenu, upgrade_adding_submenu):
    response = client.patch(f"/api/v1/menus/1/submenus/{adding_submenu['id']}", json=upgrade_adding_submenu)

    assert response.status_code == status.HTTP_200_OK

    response = response.json()
    assert response["title"] == upgrade_adding_submenu["title"] and \
        response["description"] == upgrade_adding_submenu["description"]

def test_delete_submenu(client, adding_submenu):
    response = client.delete(f"/api/v1/menus/1/submenus/{adding_submenu['id']}")

    assert response.status_code == status.HTTP_200_OK   