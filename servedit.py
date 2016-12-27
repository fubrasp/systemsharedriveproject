#!/usr/bin/python
# coding=utf-8

## Main algorithm which manage users interactions and several processes ##

## Imports/uses
from tool import *
from serveditargs import *
import time
import socket
import threading


# USAGE
#servedit -d <document>
#On verifie les arguments
arguments = args(listArgs)
#on creer le fichier - verif des cas d'erreurs
currentDocument = createDocument(arguments[document])

#demander le nombre d'utilisateurs
numberOfProcesses = int(input(processesQuestion + arguments[document] + " ?"))

#creer les utilisateurs suivant le nombre demande en leur associant une couleur
listOfUsers = initializeServer(arguments[document], numberOfProcesses)

#affiche les utilisateurs creer cf variable precedente
print("Les utilisateurs qui auront accès à votre fichier sont les suivants : ")
print(listOfUsers)

#vient du code modifie de l'exemple
#number of all client who are connected to the server
#variable globale nombre de personne sur le serveur (clients)
global numberOfClients
numberOfClients = 0

#Thread for each client
#un thread pour chaque client, ca permet de paralleliser les traitement et surtout d editer le document en meme temps
class ClientThread(threading.Thread):
    #construct the thread
    #constructeur du thread
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    #run method of the thread
    def run(self):
        print("Connection de %s %s" % (self.ip, self.port,))

        r = self.clientsocket.recv(2048)
        #print("Nous traitons la demande d'accès au fichier demandé...")
        print("Nous avons reçu le texte")
        print(str(r))

        #print("Ouverture du fichier : ", r, "...")
        #fp = open(r, 'rb')
        #self.clientsocket.send(fp.read())


        #on decremente quand l'user quitte
        print(leftClient)
        global numberOfClients
        numberOfClients -= 1
        print("Nombre de clients restants : " + str(numberOfClients))

#initialize socket
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

#when server is starting wait for ask (no limit of time)
while True:
    tcpsock.listen(10)
    print(IS_LISTENING)
    (clientsocket, (ip, port)) = tcpsock.accept()
    #nouveau client donc nouveau thread
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
    #ajout du client
    numberOfClients += 1
    print("Nombre de clients restants : "+str(numberOfClients))
