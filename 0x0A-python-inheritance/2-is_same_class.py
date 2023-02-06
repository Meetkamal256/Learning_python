#!/usr/bin/python3
"""it checks if an object is an instance of a class"""
def is_same_class(obj, a_class):
    """returns true if an object is an instance of a class, 
    otherwise false"""
    return type(obj) == a_class


a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

    