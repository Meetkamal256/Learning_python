#!/usr/bin/python3
"""
a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    # create an engine to connect to mysql server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a session
    session = sessionmaker(bind=engine)
    session = session()
    # creates a new query object that selects all records from the state table then adds a filter to the query that only selects records where the name column contains the letter a
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)
    # iterates over the result of the query and prints each record's id and name columns
    for state in states:
        print('{}:{}'.format(state.id, state.name))
        session.close()
