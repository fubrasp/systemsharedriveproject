#!/usr/bin/python
# coding=utf-8

## Imports/uses
#we don t need to re import constants.py which is already import in tool.py
from tool import *
from coleditargs import *
import socket

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

#vient du code modifie de l'exemple
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 1111))

print("Le nom du fichier surlequel voulez travailler:")
file_name = input(">> ")
s.send(file_name.encode())
file_name = 'data/%s' % (file_name,)
r = s.recv(9999999)
with open(file_name,'wb') as _file:
    _file.write(r)
print("Le fichier a été correctement créer ou ouvert dans : %s." % file_name)

#print("TEST EDITION FICHIER")
#editFile(arguments[document])




