class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height: ")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter a number")

    @property
    def width(self):
        print("Retrieving the width: ")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter a number")

    def getArea(self):
        return int(self.__width) * int(self.__height)


def main():
    a_square = Square()
    height = input("Enter height of Square: ")
    width = input("Enter width of square: ")

    a_square.height = height
    a_square.height = width

    print("the height is:", a_square.height)
    print("the width is:", a_square.width)

    print("The area of square is:", a_square.getArea())


main()
