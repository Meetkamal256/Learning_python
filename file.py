#!/usr/bin/python3
"""
FileStorage module
"""
from json import dump, load
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class FileStorage:
    """
    the storage class to store an instance of any model
    """

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """
        Return all the objects saved in the file
        :return: dict
        """
        return self.__objects

    def new(self, obj):
        """
        adding new instances of a model class to the storage. It does so by adding the object to the __objects dictionary, with the key as the name of the class concatenated with the id of the object.
        This way, the object can later be retrieved using the all method and can also be saved to the JSON file using the save method.
        """
        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """
        The method opens the file located at __file_path in write mode.
        then uses the dump function from the json module to write the to_dict representation of each object in the __objects dictionary to the file.After all the objects have been written to the file, the method simply returns, and the file is closed.
        """
        with open(self.__file_path, mode="w", encoding="utf-8") as f_write:
            # opens file in a specified path in write mode
            serialized_objects = {}
            for key, value in self.__objects.items():
                # Convert each object to a dictionary using its to_dict method,
                # for each key-value pair, it converts the value object to a
                # dictionary using the to_dict() method, and stores it as a
                # value in the serialized_objects dictionary, using the key as its key.
                serialized_objects[key] = value.to_dict()
                # Write the serialized objects to the file in JSON format
            dump(serialized_objects, f_write)

        """
            The key-value pairs in the dictionary represent the objects stored in the FileStorage's __objects attribute. The keys are a concatenation of the object's class name and its id, which is used to uniquely identify the object. The values are the objects themselves, but transformed into a dictionary using the to_dict() method defined in the BaseModel class.
            In the save method, this dictionary is passed to the dump method from the json module, which serializes the dictionary to a JSON formatted string. This string is then written to the file specified by the __file_path attribute using a context manager.
        """

    def reload(self):
        """
        retrieves data from a file self.__file_path
        """
        if path.exists(self.__file_path):
            # This line checks if the file exists in the specified file path. If it does, then the method reads the data from the file. If it doesn't exist, the method returns without doing anything.
            with open(self.__file_path, mode="r", encoding="utf-8") as f_read:
                # This line opens the file specified in self.__file_path in read-only mode, with UTF-8 encoding, and assigns the file object to the variable f_read. The with statement ensures that the file is automatically closed when the block is exited.
                data_read = load(f_read)
                # This line loads the data from the file object f_read, which is assumed to contain a JSON string, and returns a dictionary. The load() function is from the json module in Python, and it deserializes a JSON string into a Python object.
                for _, value in data_read.items():
                    # This line iterates over the dictionary data_read, which contains key-value pairs representing each object that was saved to the file. Since we only care about the values, we use an underscore (_) to indicate that we are ignoring the keys
                    class_name = value.pop("__class__", None)
                    if class_name:
                        obj = eval(class_name)(**value)
                        self.new(obj)
