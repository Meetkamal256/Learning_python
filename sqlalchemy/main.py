#!/usr/bin/python3
from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
db_name = sys.argv[3]

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    ssn = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    gender = Column(CHAR)
    age = Column(Integer)

    def __init__(self, ssn, first_name, last_name, gender, age):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return "({}) {} {} ({}) {}".format(
            self.ssn, self.first_name, self.last_name, self.gender, self.age
        )


engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ),
    echo=True,
)
# engine = create_engine(
#     "mysql+mysqlconnector://kamal:Kamal256$@localhost/hbtn_0e_4_usa",
#     echo=True
# )
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(12345, "Jamilah", "Muhammad", "m", 23)
session.add(person)
session.commit()

p1 = Person(45345, "Jamilah", "yuguda", "f", 29)
p2 = Person(52745, "Hafiz", "shuaib", "m", 33)
p3 = Person(92145, "Ummi", "Umar", "f", 31)

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()

p4 = Person(93245, "Mubarak", "Muhammad", "f", 28)
session.add(p4)
session.commit()

results = session.query(Person).filter(Person.first_name.in_(["Hafiz", "Mubarak"]))
for r in results:
    print(r)
