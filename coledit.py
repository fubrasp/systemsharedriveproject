#!/usr/bin/python
# coding=utf-8

# ==> CODE DU CLIENT DE NOTRE APPLICATION

# --> IMPORTS
from tool import *
from coleditargs import *
import socket

# --> USAGE : coledit -p <pseudo> -d <document>
arguments = args(listArgs)

serverRunningresult = True  # checkServerIsRunning(str("Python servedit.py -d "+arguments[document]))
authentificationResult = True  # checkAuthenticate(arguments)

# print(testServerIsRunning)
# print(serverRunningresult)
# print(testAuthentificationIsWorking)
# print(authentificationResult)

if (authentificationResult and serverRunningresult):

    # Paramètres d'initialisation du client pour communiquer avec le serveur

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("", 1111))

    print("Vous allez travailler sur le document : " + arguments[document])

    # On boucle tant que le client ne quitte pas il peut écrire :

    textToSend = input(">> ")
    while textToSend not in LEFT_EDITOR:
        # À chaque ajout, on nettoie la console
        cleanConsole()

        # On affiche le document
        displayDoc(FILES_DIRECTORY + arguments[document])

        textToSend = input(">> ")
        s.send(textToSend.encode())


else:
    if (serverRunningresult == False):
        print("Le serveur n'est pas en route, lancez-le afin d'y accéder")

    if (authentificationResult == False):
        print(
            "Authentification impossible, vérifiez vos identifiants s'il vous plaît : 1) nom d'utilisateur, 2) fichier souhaité")
