#!/usr/bin/python
# coding=utf-8

## Imports/uses
from constants import *


## Class which define a person
"""
- login/pseudo
- color
"""
class Person():

    # Construct a Person
    def __init__(self, login, color):
        self.login = login
        self.color = color

    # Print his attributes
    def __repr__(self):
        return str(self.login)+" "+str(self.color)
