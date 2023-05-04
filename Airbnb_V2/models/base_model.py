#!/usr/bin/python3
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import os

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """
    a base class for all hbnb models
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    
    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
    
    def __str__(self):
        """
        returns a string representation of our object
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
    
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()  # creates a new dictionary with a copy of the instance's __dict__ attribute. The __dict__ attribute contains all the instance's attributes and their values.
        if '_sa_instance_state' in my_dict:
            del my_dict['_sa_instance_state']
        my_dict.update({
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()})
        return my_dict
    
    def delete(self):
        models.storage.delete(self)
