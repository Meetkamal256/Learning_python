#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    try:
        # create an engine to connect to mysql server
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    except Exception as e:
        print("Error:{}".format(e))
        exit()

    # create a session
    session = sessionmaker(bind=engine)
    session = session()

    # query all state in database and also check if state exists
    state_exists = session.query(State).filter_by(name='Louisiana').first()
    if state_exists:
        print("state already exists")
    else:
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        print("State added to database")
