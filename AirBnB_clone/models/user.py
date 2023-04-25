#!/usr/bin/python3
"""this module create a class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
