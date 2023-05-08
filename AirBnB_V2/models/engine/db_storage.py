#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """this class manages storage of hbnb models in a MYSQL database"""
    __engine = None
    __session = None
    
    def __init__(self):
        """instantiates a new DBStorage object"""
        db_user = getenv('HBNB_MYSQL_USER')
        db_pwd = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db_name = getenv('HBNB_MYSQL_DB', 'hbnb_dev_db')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            db_user, db_pwd, db_host, db_name), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
    
    def all(self, cls=None):
        """ queries all objects of a certain class or all objects if class is none"""
        new_dict = {}
        if cls is not None:
            objects = self.__session.query(cls).all()
            for obj in objects:  # loop thru each object retrieved from the database
                key = "{}.{}".format(obj.__class__.name__, obj.id)
                # add object to dictionary with generated key as the dictionary key
                new_dict[key] = obj
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for cls in classes:
                objects = self.__session.query(cls).all()
                for obj in objects:
                    key = key = "{}.{}".format(
                        obj.__class__.name__, obj.id)
                    new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        """adds new object to the current database session"""
        self.__session.add(obj)
    
    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """deletes the object from the current database"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """reloads objects from the database"""
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)