#!/usr/bin/python3
""" class BaseModel base class attributes/methods for other classes"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Represent Base class """

    def __init__(self, *args, **kwargs):
        """ Initialize a base class
        Args:
        id (int): The identity of the new base
        created_at(datetime): created time
        updated_at(datetime): updated time
        """
        if not kwargs:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.__dict__["created_at"] = datetime.strptime(
                self.__dict__["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__["updated_at"] = datetime.strptime(
                self.__dict__["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            
            
                        
                        
                        
            

        

    def save(self):
        """Update the attribute updated_at with the current time """
        self.updated_at = datetime.now()

    def __str__(self):
        """ Return the print and str representation of Base model """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def to_dict(self):
        my_dict = {}
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
    
    
