#!/usr/bin/python3

""" sql alchemy """
from sqlalchemy import Sequence, Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy import create_engine
import MySQLdb
import sys


class City(Base):
    """ State object """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


engine = create_engine(
    'mysql+mysqlconnector://kamal:Kamal256$@localhost/hbtn_0e_14_usa')
Base.metadata.create_all(engine)
