#!/usr/bin/python
# coding=utf-8

## Imports/uses
from tool import *
from serveditargs import *
import time
import socket
import threading


# USAGE
#servedit -d <document>
arguments = args(listArgs)

## Main algorithm which manage users interactions and several processes ##

# Start with asking the number of processes
numberOfProcesses = int(input(processesQuestion))

listOfUsers=initializeServer(arguments[document], numberOfProcesses)
currentDocument=createDocument(arguments[document])

print("TEST LIST USERS")
print(listOfUsers)

#vient du code modifie de l'exemple
global numberOfClients
numberOfClients = 0


class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connection de %s %s" % (self.ip, self.port,))

        r = self.clientsocket.recv(2048)
        print("TRAITEMENT DEMANDE D'ACCES FICHIER")
        #os.system("")
        #echo $?

        print("Ouverture du fichier: ", r, "...")
        fp = open(r, 'rb')
        self.clientsocket.send(fp.read())
        print("Client déconnecté...")
        #global numberOfClients
        global numberOfClients
        numberOfClients -= 1
        print("NOMBRE DE CLIENTS RESTANTS: " + str(numberOfClients))


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
    #global numberOfClients
    numberOfClients += 1
    print("NOMBRE DE CLIENTS RESTANTS: "+str(numberOfClients))



#while True:
#    try:
#        time.sleep(1)
#    except KeyboardInterrupt:
#        print(leftServer)
#        sys.exit()