#!/usr/bin/python3
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Sequence, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""create a new base class"""
Base = declarative_base()


class State(Base):
    """State object"""

    __tablename__ = "states"
    id = Column(Integer, Sequence("my_sequence"), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
