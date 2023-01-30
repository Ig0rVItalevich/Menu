from fastapi import status


def test_get_menus(client, storage_menus):
    response = client.get('/api/v1/menus')

    assert response.status_code == status.HTTP_200_OK

    response = response.json()
    for i in range(len(response)):
        assert response[i]['title'] == storage_menus[i]['title'] and \
            response[i]['description'] == storage_menus[i]['description']


def test_post_menu(client, adding_menu):
    response = client.post('/api/v1/menus', json=adding_menu)

    assert response.status_code == status.HTTP_201_CREATED

    response = response.json()
    assert response['id'] is not None
    assert response['title'] == adding_menu['title'] and response['description'] == adding_menu['description']


def test_get_menu_positive(client, adding_menu):
    response = client.get(f"/api/v1/menus/{adding_menu['id']}")

    assert response.status_code == status.HTTP_200_OK

    response = response.json()
    assert response['id'] == adding_menu['id'] and response['title'] == adding_menu['title'] and \
        response['description'] == adding_menu['description']


def test_get_menu_negative(client):
    response = client.get('/api/v1/menus/100')

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_patch_menu(client, adding_menu, upgrade_adding_menu):
    response = client.patch(
        f"/api/v1/menus/{adding_menu['id']}", json=upgrade_adding_menu,
    )

    assert response.status_code == status.HTTP_200_OK

    response = response.json()
    assert response['title'] == upgrade_adding_menu['title'] and \
        response['description'] == upgrade_adding_menu['description']


def test_delete_menu(client, adding_menu):
    response = client.delete(f"/api/v1/menus/{adding_menu['id']}")

    assert response.status_code == status.HTTP_200_OK
