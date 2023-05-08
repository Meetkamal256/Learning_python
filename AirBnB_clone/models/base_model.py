#!/usr/bin/python3
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)


    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            lst = list(kwargs)
            if 'updated_at' in lst:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            if 'created_at' in lst:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in lst:
                del kwargs['__class__']
            if "id" not in lst:
                self.id = str(uuid.uuid4())

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
        my_dict.update({
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()})
        return my_dict
