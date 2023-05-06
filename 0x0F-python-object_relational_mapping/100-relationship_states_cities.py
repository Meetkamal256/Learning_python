#!/usr/bin/python3
"""
This script maps all City and State objects in the database
to each other.
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get all cities and states
    from the database. Map all cities to their respective states.
    """

    db_uri = "mysql+mysqldb://kamal:Kamal256$@localhost:3306/hbtn_0e_6_usa"
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    # get all cities and states from the database
    all_states = session.query(State).all()
    all_cities = session.query(City).all()

    # map all cities to their respective states
    for city in all_cities:
        for state in all_states:
            if city.state_id == state.id:
                state.cities.append(city)
                break

    session.commit()
    session.close()
