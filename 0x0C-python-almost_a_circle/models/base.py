class Base:
    """define a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constuctor"""
        if id == None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id


# b1 = Base()
# print(b1.id)

# b2 = Base()
# print(b2.id)

# b3 = Base()
# print(b3.id)

# b4 = Base(12)
# print(b4.id)

# b5 = Base()
# print(b5.id)
    