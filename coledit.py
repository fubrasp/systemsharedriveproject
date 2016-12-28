#!/usr/bin/python
# coding=utf-8

# ==> CODE DU CLIENT DE NOTRE APPLICATION

# --> IMPORTS
from tool import *
from coleditargs import *
import socket
import threading

# --> USAGE : coledit -p <pseudo> -d <document>
arguments = args(listArgs)

serverRunningresult = True  # checkServerIsRunning(str("Python servedit.py -d "+arguments[document]))
authentificationResult = True  # checkAuthenticate(arguments)

# print(testServerIsRunning)
# print(serverRunningresult)
# print(testAuthentificationIsWorking)
# print(authentificationResult)

# 1 thread s'éxécute en continue avec le client pour permettre de détecter tout changement (sans bloquer le programme) sur le document et effectuer ainsi le refresh sur la vue client
class ClientRefreshThread(threading.Thread):

    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock=sock
        print("=> Nouveau thread suiveur "+arguments[pseudo])

    def run(self):
        while True:
            receiveData=s.recv(9999999).decode()
            checkRefresh= receiveData in DATA_SEND
            #print("TEST REFRESH")
            #print(receiveData)
            #print(checkRefresh)
            if checkRefresh:
                refreshClient(arguments[document])
                #print("Tapez exit pour quitter l'édition du fichier " + arguments[document])
                #textToSend = input(">> ")
                #self.sock.send(textToSend.encode())
        print("MERDE")


if (authentificationResult and serverRunningresult):

    # Paramètres d'initialisation du client pour communiquer avec le serveur

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("", 1111))

    print("Vous allez travailler sur le document : " + arguments[document])


    followThread= ClientRefreshThread(s)
    followThread.start()

    # On boucle tant que le client ne quitte pas il peut écrire :
    textToSend = "init"
    while textToSend not in LEFT_EDITOR:
        refreshClient(arguments[document])
        print("Tapez exit pour quitter l'édition du fichier " + arguments[document])
        textToSend = input(">> ")
        s.send(textToSend.encode())

else:
    if (serverRunningresult == False):
        print("Le serveur n'est pas en route, lancez-le afin d'y accéder")

    if (authentificationResult == False):
        print(
            "Authentification impossible, vérifiez vos identifiants s'il vous plaît : 1) nom d'utilisateur, 2) fichier souhaité")

