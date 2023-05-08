#!/usr/bin/python3
"""
database engine
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """database ongine"""

    __engine = None
    __session = None

    def __init__(self):
        """init"""

        url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            "localhost",
            getenv("HBNB_MYSQL_DB"),
        )
        self.__engine = create_engine(url, pool_pre_ping=True, echo=False)

    def all(self, cls=None):
        """querry on database session all obj depending on class name"""

        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        new = []  # list of lists of obj |OR| list of obj
        obj = {}  # dict of obj
        if cls is None:
            lst = [State, City, User, Place, Review, Amenity]

            for i in lst:
                new.append(self.__session.query(i).all())
            for i in new:
                for j in i:
                    key = "{}.{}".format(j.__class__.__name__, j.id)
                    obj[key] = j
            return obj
        else:
            new = self.__session.query(cls).all()

            for j in new:
                key = "{}.{}".format(j.__class__.__name__, j.id)
                obj[key] = j
            return obj

    def new(self, obj):
        """UPDATE!!!"""
        self.__session.add(obj)

    def save(self):
        """UPDATE!!!"""
        self.__session.commit()

    def delete(self, obj=None):
        """UPDATE!!!"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """UPDATE!!!"""
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        self.__session = scoped_session(session)()

    def close(self):
        """method on the private session attribute"""
        self.__session.close()
