#!/bin/python3
"""
a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    state_name = argv[4]
    # create an engine to connect to mysql server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3], argv[4]), pool_pre_ping=True)
    # create session
    session = sessionmaker(bind=engine)
    session = session()
    query = session.query(State).filter_by(name=state_name).first()
    # print the result or "Not found"
    if query is None:
        print("Not found")
    else:
        print(query.id)
    # close session
    session.close()
