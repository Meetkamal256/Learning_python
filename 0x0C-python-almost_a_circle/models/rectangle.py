try:
    from models.base import Base
except ModuleNotFoundError:
    Base = __import__('base').Base


class Rectangle(Base):
    """defines a new class rectangle that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height mube be >= 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @x.setter
    def y(self, value):
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle using # """
        for y in range(self.y):
            print("")
        for column in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for row in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - / {self.__width}/{self.__height}"

    def update(self, *args):
        """Assigns an argument to each attribute"""

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        # elif kwargs and len(kwargs) != 0:
        #     for k, v in kwargs.items():
        #         if k == "id":
        #             if v is None:
        #                 self.__init__(self.width, self.height, self.x, self.y)
        #             else:
        #                 self.id = v
        #         elif k == "width":
        #             self.width = v
        #         elif k == "height":
        #             self.height = v
        #         elif k == "x":
        #             self.x = v
        #         elif k == "y":
        #             self.y = v

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
# print("-----------")

# r1 = Rectangle(10, 2)
# print(r1.id)

# r2 = Rectangle(2, 10)
# print(r2.id)

# r3 = Rectangle(10, 2, 0, 0, 12)
# print(r3.id)
# print("-------------")

# try:
#     Rectangle(10, "2")
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r = Rectangle(10, 2)
#     r.width = -10
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r = Rectangle(10, 2)
#     r.x = {}
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     Rectangle(10, 2, 3, -1)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
# print("-----------------------------")

# r1 = Rectangle(3, 2)
# print(r1.area())

# r2 = Rectangle(2, 10)
# print(r2.area())

# r3 = Rectangle(8, 7, 0, 0, 12)
# print(r3.area())
# print("----------------")

# r1 = Rectangle(4, 6)
# r1.display()
# print("---")

# r1 = Rectangle(4, 6, 2, 1, 12)
# print(r1)

# r2 = Rectangle(5, 5, 1)
# print(r2)
# print("------------------")

# r1 = Rectangle(2, 3, 2, 2)
# r1.display()

# print("---")

# r2 = Rectangle(3, 2, 1, 0)
# r2.display()
# print("--------------------")


# r1 = Rectangle(10, 10, 10, 10)
# print(r1)

# r1.update(89)
# print(r1)

# r1.update(89, 2)
# print(r1)

# r1.update(89, 2, 3)
# print(r1)

# r1.update(89, 2, 3, 4)
# print(r1)

# r1.update(89, 2, 3, 4, 5)
# print(r1)