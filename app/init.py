import configparser
import os

from cache.cache import Cache
from services.service import Service
from storage import models
from storage.repository import DB, Repository

config = configparser.ConfigParser()
config.read('config.ini')

CONFIG_DB = {
    'drivername': config['DATABASE']['drivername'],
    'host': config['DATABASE']['host'],
    'port': config['DATABASE']['port'],
    'username': config['DATABASE']['username'],
    # "password": os.environ.get('DB_PASSWORD'),
    'password': config['DATABASE']['password'],
    'database': config['DATABASE']['database'],
}

CONFIG_CACHE = {
    'host': config['CACHE']['host'],
    'port': config['CACHE']['port'],
    'db': config['CACHE']['db'],
}

db = DB(CONFIG_DB, models.DeclarativeBase)
db.recreate_tables()

repository = Repository(db)
cache = Cache(CONFIG_CACHE)
service = Service(repository, cache)
