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

serverRunningresult=checkServerIsRunning(str("python servedit.py -d "+arguments[document]))
authentificationResult=checkAuthenticate(arguments)


print("TEST GOOD SERVER IS RUNNING")
print(serverRunningresult)

print("TEST RESULTAT DE L'AUTHENTIFICATION")
print(authentificationResult)

print("TEST EDITION FICHIER")
editFile(arguments[document])




