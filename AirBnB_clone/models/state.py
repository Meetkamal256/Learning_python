#!/usr/bin/python3
"""creates a class called state """
from models.base_model import BaseModel


class State(BaseModel):
    def __init__(self, name=""):
        self.name = name
