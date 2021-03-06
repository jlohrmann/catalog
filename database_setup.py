import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#class restaurant takes argument Base
#   creates table space for Restaurant
#       columns name, id
class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        # returns object data in easily serializable format
        return {
            'name': self.name,
            'id': self.id
        }

#class MenuItem takes argument Base
#   creates table space for MenuItem
#       columns name, id, course, description,price
#       foreign key restaurant_id identifies the restaurant the menu item belongs to
class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        # returns object data in easily serializable format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course
        }


#Creates database restaurantmenu.db
engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
