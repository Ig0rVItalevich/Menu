import pytest

from storage import models
from main import app

from init import db, repository

from fastapi.testclient import TestClient

adding_menus = [
    {
        "title": "My menu 1",
        "description": "My menu description 1"
    },
    {
        "title": "My menu 2",
        "description": "My menu description 2"
    }]

adding_submenus = [
    {
        "title": "My submenu 1",
        "description": "My submenu description 1",
        "menu_id": 1
    },
    {
        "title": "My submenu 2",
        "description": "My submenu description 2",
        "menu_id": 1
    }]

adding_dishes = [
    {
        "title": "My dish 1",
        "description": "My dish description 1",
        "price": "12.50",
        "submenu_id": 1
    },
    {
        "title": "My dish 2",
        "description": "My dish description 2",
        "price": "15.75",
        "submenu_id": 1
    }]


@pytest.fixture()
def storage_menus():
    return adding_menus


@pytest.fixture()
def adding_menu():
    return {
        "id": "3",
        "title": "My menu 3",
        "description": "My menu description 3"
    }


@pytest.fixture()
def upgrade_adding_menu():
    return {
        "title": "My upgrade menu 3",
        "description": "My upgrade menu description 3"
    }


@pytest.fixture()
def storage_submenus():
    return adding_submenus


@pytest.fixture()
def adding_submenu():
    return {
        "id": "3",
        "title": "My submenu 3",
        "description": "My submenu description 3",
        "menu_id": 1
    }


@pytest.fixture()
def upgrade_adding_submenu():
    return {
        "title": "My upgrade submenu 3",
        "description": "My upgrade submenu description 3"
    }


@pytest.fixture()
def storage_dishes():
    return adding_dishes


@pytest.fixture()
def adding_dish():
    return {
        "id": "3",
        "title": "My dish 3",
        "description": "My dish description 3",
        "price": "1678.20",
        "submenu_id": 1
    }


@pytest.fixture()
def upgrade_adding_dish():
    return {
        "title": "My upgrade dish 3",
        "description": "My upgrade dish description 3",
        "price": "150.30"
    }


@pytest.fixture(scope="session")
def init_db():
    for menu in adding_menus:
        repository.menuRepository.createMenu(models.Menu(
            title=menu["title"], description=menu["description"]))
        
    for submenu in adding_submenus:
        repository.submenuRepository.createSubmenu(models.Submenu(
            title=submenu["title"], description=submenu["description"], menu_id=submenu["menu_id"]))
        
    for dish in adding_dishes:
        repository.dishRepository.createDish(models.Dish(
            title=dish["title"], description=dish["description"], price=dish["price"], submenu_id=dish["submenu_id"]))

    yield
    
    db.recreate_tables()


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as client:
        yield client
