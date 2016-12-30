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

    # Constructeur de Person
    def __init__(self, login, color):
        self.login = login
        self.color = color

    # Methode renvoyant les attributs d'une personne
    def __repr__(self):
        return str(self.login)+" "+str(self.color)
