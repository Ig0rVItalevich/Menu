import configparser
import os

from cache.cache import new_cache
from services.service import new_service
from storage.database import DB
from storage.models import DeclarativeBase
from storage.repository import new_repository

config = configparser.ConfigParser()
config.read('config.ini')

CONFIG_DB = {
    'drivername': config['DATABASE']['drivername'],
    'host': config['DATABASE']['host'],
    'port': config['DATABASE']['port'],
    'username': config['DATABASE']['username'],
    'password': os.environ.get('DB_PASSWORD'),
    'database': config['DATABASE']['database'],
}

CONFIG_CACHE = {
    'host': config['CACHE']['host'],
    'port': config['CACHE']['port'],
    'db': config['CACHE']['db'],
}

db = DB(CONFIG_DB, DeclarativeBase)
db.recreate_tables()

repository = new_repository(db)
cache = new_cache(CONFIG_CACHE)
service = new_service(repository, cache)
