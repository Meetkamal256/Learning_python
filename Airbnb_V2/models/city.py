#!/usr/bin/python3
"""creates a class called City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """City class to store city information"""
    __tablename__ = 'cities'

    name = Column(String(128),
                  nullable=False)
    state_id = Column(String(60),
                      ForeignKey('states.id'),
                      nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes our City instance"""
        super().__init__(*args, **kwargs)
