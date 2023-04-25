#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base

if __name__ == '__main__':
    # create an engine to connect to mysql server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a session
    session = sessionmaker(bind=engine)
    session = session()
    states = session.query(State).filter(State.name.contains('a'))
    # This code block checks if any states were returned by the query. If so, it loops over each state and deletes it from the database using the delete method of the Session object.
    if states is not None:
        for state in states:
            session.delete(state)
            session.commit()
            print("Deleted successfully")
            session.close()
