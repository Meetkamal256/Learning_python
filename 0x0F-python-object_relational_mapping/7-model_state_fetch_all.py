#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
db_name = sys.argv[3]

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_user, mysql_password, db_name, pool_pre_ping=True))
   # engine = create_engine(
   #     'mysql+mysqldb://kamal:Kamal256$@localhost:3306/hbtn_0e_6_usa', pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()
    query = session.query(State).order_by(State.id)
    results = query.all()
    for State in results:
        print("{}: {}".format(State.id, State.name))
        session.close()
