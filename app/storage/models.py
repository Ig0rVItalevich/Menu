from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey

DeclarativeBase = declarative_base()

class Menu(DeclarativeBase):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(255), nullable=False)
    description = Column('description', Text, nullable=False)

    def __repr__(self):
        return f"id: {self.id}, title: {self.title}, description: {self.description}"
    
class Submenu(DeclarativeBase):
    __tablename__ = 'submenus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(255), nullable=False)
    description = Column('description', Text, nullable=False)
    menu_id = Column(Integer, ForeignKey('menus.id', ondelete='CASCADE'))
    
    menu = relationship(Menu, innerjoin = True)

    def __repr__(self):
        return f"id: {self.id}, title: {self.title}, description: {self.description}"

class Dish(DeclarativeBase):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(255), nullable=False)
    description = Column('description', Text, nullable=False)
    price = Column('price', DECIMAL, nullable=False)
    submenu_id = Column(Integer, ForeignKey('submenus.id', ondelete='CASCADE'))
    
    submenu = relationship(Submenu, innerjoin=True)

    def __repr__(self):
        return f"id: {self.id}, title: {self.title}, description: {self.description}, price: {self.price}"