from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


class DB():
    def __init__(self, config: dict, base):
        self.declarative_base = base
        self.engine = create_engine(URL(**config))
        self.session = sessionmaker(bind=self.engine, expire_on_commit=False)

    def create_tables(self):
        self.declarative_base.metadata.create_all(self.engine)

    def drop_tables(self):
        self.declarative_base.metadata.drop_all(self.engine)

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
