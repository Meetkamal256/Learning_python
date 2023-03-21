import json


class Base:
    """define a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constuctor"""
        if id == None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        empty_list = []
        if list_objs == None:
            return "[]"
        else:
            for obj in list_objs:
                empty_list.append(obj.to_dictionary())

        json_string = cls.to_json_string(empty_list)
        with open(cls.__name__ + ".json", "w") as myFile:
            myFile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        # create an instance of an existing class
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
