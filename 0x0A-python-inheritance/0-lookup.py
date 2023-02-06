#!/usr/bin/python3
"""
    This module returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """This functions looks out for all attributes and methods of an object"""
    return dir(obj)


class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))