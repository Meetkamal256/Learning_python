#!/usr/bin/python3
"""a function that returns True if the object is an instance of, 
or if the object is an instance of a class that inherited from, 
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class
    or a class that the class in question inherits from
    """
    return isinstance(obj, a_class)


a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
