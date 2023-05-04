#!/usr/bin/python3
"""creates a class called state """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """class State to store State information"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')

        @property
        def cities(self):
            """Return the list of City instances with
            state_id equals to the current State.id
            """
            cities_list = []
            for city in models.storage.all('City').values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
