#!/usr/bin/python3
"""
a script that changes the name of a State object from the database
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base

if __name__ == "__main__":
    # create an engine to connect to mysql server
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    # create a session
    session = sessionmaker(bind=engine)
    session = session()
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
        print("Row updated successfully")
    else:
        print("Row not found")

    # close the connection
    session.close()
