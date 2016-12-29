#!/usr/bin/python
# coding=utf-8

# ==> IMPORTS
from constants import *

# CLASSE POUR DEFINIR UNE PERSONNE
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
