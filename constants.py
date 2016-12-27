#!/usr/bin/python
# coding=utf-8

## Imports/uses
from multiprocessing import Process, Manager
import sys, getopt, argparse


#memoryManager = Manager()

## Define some constants ##

#Program arguments
dictArgs = {}
pseudo="pseudo"
document="document"

#Questions
processesQuestion="À combien d'utilisateurs l'accès sera-t-il autorisé sur ce document ?"
processesSelection="Vous avez selectionné :"
processWord="processus"

#Users
personDefineSentence="La personne est "
#users_var
listOfUsers=[]

#help argv statement
#coledit
helpPError="indicate we use a pseudo/login"
helpPseudoError="pseudo with you sign in"
helpDError="indicate we want access to a document"
helpFileAccessError="file you want access"

#authenticate process
isAuthenticated=" is authenticated"
failToAuthenticate="FAIL TO AUTHENTICATE"

#Server mananging
leftServer="Serveur hors-ligne."
leftClient="Client déconnecté."
IS_LISTENING="En attente de connexions..."

##FILES DIRECTORY
FILES_DIRECTORY="data"

##TESTING
testServerIsRunning="TEST GOOD SERVER IS RUNNING"
testAuthentificationIsWorking="TEST RESULTAT DE L'AUTHENTIFICATION"

##COMMANDS
#command for check server is running
#commandCheckServer="ps ax | grep servedit.py | head -1"
commandCheckServer="ps ax | grep servedit.py | tail -1"