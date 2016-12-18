#!/usr/bin/python
# coding=utf-8

## Imports/uses
#we don t need to re import constants.py which is already import in tool.py
from tool import *
from coleditargs import *
# USAGE
#coledit -p <pseudo> -d <document>
#use the arguments define in coleditargs
arguments = args(listArgs)

authentificationResult=checkAuthenticate(arguments)

print("TEST RESULTAT DE L'AUTHENTIFICATION")
print(authentificationResult)



