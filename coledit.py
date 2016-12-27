#!/usr/bin/python
# coding=utf-8

## Imports/uses
# we don t need to re import constants.py which is already import in tool.py
from tool import *
from coleditargs import *
import socket

# USAGE
# coledit -p <pseudo> -d <document>
# use the arguments define in coleditargs
arguments = args(listArgs)

serverRunningresult = True  # checkServerIsRunning(str("Python servedit.py -d "+arguments[document]))
authentificationResult = True  # checkAuthenticate(arguments)

# print(testServerIsRunning)
# print(serverRunningresult)

# print(testAuthentificationIsWorking)
# print(authentificationResult)

if (authentificationResult and serverRunningresult):
    # vient du code modifie de l'exemple
    # initialize socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("", 1111))

    ##unuseful
    print("Vous allez travailler sur le document : " + arguments[document])
    # Just ask something to user and print nice ask line
    textToSend = input(">> ")
    while textToSend not in "exit":
        textToSend = input(">> ")
        s.send(textToSend.encode())


else:
    if (serverRunningresult == False):
        print("Le serveur n'est pas en route, lancez-le afin d'y accéder")

    if (authentificationResult == False):
        print(
            "Authentification impossible, vérifiez vos identifiants s'il vous plaît : 1) nom d'utilisateur, 2) fichier souhaité")
