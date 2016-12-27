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
#number of all client who are connected to the server
global numberOfClients
numberOfClients = 0

#Thread for each client
class ClientThread(threading.Thread):
    #construct the thread
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

#initialize socket
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

#when server is starting wait for ask (no limit of time)
while True:
    tcpsock.listen(10)
    print(IS_LISTENING)
    (clientsocket, (ip, port)) = tcpsock.accept()
    #new thread
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