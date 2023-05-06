#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    a class that defines attributes id,
    created_at, updated_at and methods
    """

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
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """
        returns a string representation of our object
        """
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()





      def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """

        # creates a new dictionary with a copy of the instance's __dict__ attribute. The __dict__ attribute contains all the instance's attributes and their values.
        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()})
        return my_dict
