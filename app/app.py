import configparser

from storage import repository as repo
from storage import models
from services import service as srvc

config = configparser.ConfigParser()
config.read("config.ini")

CONFIG = {
    "drivername": config["DATABASE"]["drivername"],
    "host": config["DATABASE"]["host"],
    "port": config["DATABASE"]["port"],
    "username": config["DATABASE"]["username"],
    "password": config["DATABASE"]["password"],
    "database": config["DATABASE"]["database"]
}

db = repo.DB(CONFIG, models.DeclarativeBase)
db.recreate_tables()
repository = repo.Repository(db)
service = srvc.Service(repository)
