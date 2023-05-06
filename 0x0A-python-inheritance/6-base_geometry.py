class BaseGeometry:
    """this class represents a basegeometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area is not implemented")


bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
