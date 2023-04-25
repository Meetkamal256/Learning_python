#!/usr/bin/python3
"""
a script 14-model_city.py that prints all City objects from the database hbtn_0e_14_usa
"""

from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

"""connect to mysql server"""
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
"""create a session"""
session = sessionmaker(bind=engine)
session = session()
query = session.query(City, State).join(State)
results = query.all()
for city, state in results:
    print('{}: ({}) {}'.format(state.name, city.id, city.name))
session.commit()
session.close()
