#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    # create_engine('mysql+mysqldb://username: password@localhost:port/database_name' pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()
    query = session.query(State).order_by(State.id)
    results = query.all()
    for State in results:
        print(f"{State.id}: {State.name}")
        session.close()
