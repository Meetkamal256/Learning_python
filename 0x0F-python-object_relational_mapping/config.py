from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

# create engine and session
engine = create_engine(
    "mysql+mysqldb://kamal:Kamal256$@localhost:3306/hbtn_0e_14_usa", echo=True
)
Session = sessionmaker(bind=engine)
session = Session()

# create all tables defined in models
Base.metadata.create_all(engine)

# close session
session.close()
