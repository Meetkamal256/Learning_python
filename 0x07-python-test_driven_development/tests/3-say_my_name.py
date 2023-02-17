#!/usr/bin/python3
"""This module contains a function
that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


# say_my_name("Bob", "stark")
# say_my_name("Tom", "cruise")
# say_my_name("")
# try:
#     say_my_name(11, "Maryam")
# except Exception as a:
#     print(a)
# try:
#     say_my_name("Mubarak", 12)
# except Exception as a:
#     print(a)
# try:
#     say_my_name()
# except Exception as a:
#     print(a)
# try:
#     say_my_name(None)
# except Exception as a:
#     print(a)
# try:
#     say_my_name("Abida")
# except Exception as a:
#     print(a)
