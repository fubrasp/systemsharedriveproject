#!/usr/bin/python
# coding=utf-8

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
    def toString(self):
        print(personDefineSentence, self.login, ":")
        print(self.color)