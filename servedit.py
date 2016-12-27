#!/usr/bin/python
# coding=utf-8

# ==> CODE DU SERVEUR DE NOTRE APPLICATION

# --> IMPORT
from tool import *
from serveditargs import *
import socket
import threading

# --> USAGE : servedit -d <document>

# On vérifie les arguments
arguments = args(listArgs)

# On créé le fichier en vérifiant qu'il n'existe pas
currentDocument = createDocument(arguments[document])

# Nombre d'utilisateurs
numberOfProcesses = int(input(processesQuestion + arguments[document] + " ? "))

# Création des utilisateurs suivant le nombre soumis + on associe 1 couleur / utilisateur
listOfUsers = initializeServer(arguments[document], numberOfProcesses)

# Affichage des utilisateurs
print("Les utilisateurs qui auront accès à votre fichier sont les suivants : ")
print(listOfUsers)

# Variable globale indiquant le nb de clients connectés au serveur
global numberOfClients
numberOfClients = 0

# 1 thread / client, ça permet de paralléliser les traitements entre les utilisateurs
class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("=> Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connexion de %s %s" % (self.ip, self.port,))

        BUFF_SIZE = 35
        data = ""

        while True:
            part = self.clientsocket.recv(BUFF_SIZE)
            data += " " + part.decode()
            print(part.decode())

            writeInDoc(FILES_DIRECTORY + arguments[document], " " + part.decode())

            # Mettre fin à la saisie par le client
            if ((sys.getsizeof(part) < BUFF_SIZE) or (LEFT_EDITOR in part.decode())):
                break

        # On décrémente quand le client quitte
        print(leftClient)
        global numberOfClients
        numberOfClients -= 1
        print("Nombre de clients restants : " + str(numberOfClients))

# Paramètres pour lancer le serveur
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

# Code du serveur :
while True:
    tcpsock.listen(10)
    print(IS_LISTENING)
    (clientsocket, (ip, port)) = tcpsock.accept()

    # Nouveau client = nouveau thread
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()

    # Ajout du client à la variable globale
    numberOfClients += 1
    print("Nombre de clients restants : " + str(numberOfClients))
