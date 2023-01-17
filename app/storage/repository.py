from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from contextlib import contextmanager

from .menu import MenuRepository
from .submenu import SubmenuRepository
from .dish import DishRepository

class DB:
    def __init__(self, config, base):
        self.declarativeBase = base
        self.engine = create_engine(URL(**config))
        self.session = sessionmaker(bind=self.engine, expire_on_commit=False)
    
    def create_tables(self):
        self.declarativeBase.metadata.create_all(self.engine)
        
    def drop_tables(self):
        self.declarativeBase.metadata.drop_all(self.engine)
        
    def recreate_tables(self):
        self.drop_tables()
        self.create_tables()
        
    @contextmanager
    def session_scope(self):
        session = self.session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            
class Repository():
    def __init__(self, db):
        self.menuRepository = MenuRepository(db)
        self.submenuRepository = SubmenuRepository(db)
        self.dishRepository = DishRepository(db)