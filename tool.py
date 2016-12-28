#!/usr/bin/python
# coding=utf-8

# IMPORTS
import os, io, argparse, sys
from person import *

# Generic function in order to get args
def args(listOfArgs):
    parser = argparse.ArgumentParser()
    for current in listOfArgs:
        # each node of the list corresponds to an array of two values, the first for the option, the secund for the content of the option
        parser.add_argument(str(current[0]), str(current[1]), help="", type=str)

    args = parser.parse_args()

    if hasattr(args, 'pseudo'):
        dictArgs[str(pseudo)] = args.pseudo

    if hasattr(args, 'document'):
        dictArgs[str(document)] = args.document

    return dictArgs


def checkServerIsRunning(serverCommand):
    os.system(commandCheckServer + " >tmp")
    result = open('tmp', 'r').read()
#    print(str(serverCommand))
#    print(str(result))
    if (serverCommand in result):
        return True
    else:
        return False

def checkAuthenticate(arguments):
    currUserArr = []
    userListed = False

    try:
        with io.open("users_" + arguments[document], "r", encoding="utf-8") as usersData:
            for line in usersData:
                currUserArr = str(line[:-1]).split(':')
                if currUserArr[0] == arguments[pseudo]:
                    userListed = True
                    break
    except IOError:
        print("***FAIL***")

    if userListed:
        return True
    else:
        return False
        sys.exit()


def initializeServer(document, numberOfProcesses):
    # WE ALSO CAN IMPROVE THIS BY GIVING RANDOM NAME AND COLOR
    # Put the list of users allowed on the server
    for count in range(numberOfProcesses):
        currentInteratorString = str(count)
        user = Person("Utilisateur n°" + str(currentInteratorString), "(Couleur " + str(currentInteratorString) + ")")
        listOfUsers.append(user)

    with open(FILES_USERS_DIRECTORY + "users_" + document, "w") as usersData:
        for user in listOfUsers:
            usersData.write(user.login + user.color + "\n")

    return listOfUsers


def createDocument(fileName):
    if os.path.exists(FILES_DIRECTORY + fileName) == False :
        os.system("touch " + FILES_DIRECTORY + fileName)
    else :
        displayDoc(FILES_DIRECTORY + fileName)
        # print("Le fichier " + fileName + " existe déjà ! Choisissez un autre nom")
        sys.exit()

# def saveSessionFile(document):

def editFile(document):
    os.system("vim " + document)


def endSession(document, message):
    os.system("git add " + document)
    os.system("git commit -m " + message + "")
    # os.system("git push")


def initHistory(dossier):
    os.system('git init ' + dossier)


def followHistory(document):
    os.system("git log")

#fonctions sytemes usuelles
def cleanConsole():
    os.system('clear')

# on choisit une approche non systeme pour ne pas perdre en interactivite
def displayDoc(document):
    try:
        with io.open(document, "r", encoding="utf-8") as _file:
            for line in _file:
                print(line)
    except IOError:
        print("Erreur de lecture du fichier !")

def writeInDoc(document, text):
    try:
        with io.open(document, "a", encoding="utf-8") as _file:
            _file.write(text)
            _file.close()
    except IOError:
        print("Erreur lors de l'écriture dans le fichier !")

def deleteInDoc(document):
    try:
        with io.open(document, "a", encoding="utf-8") as _file:
            _file.write()
            _file.close()
    except IOError:
        print("Erreur lors d'une modification dans un fichier")

def refreshClient(args):
    # On nettoie la console
    cleanConsole()
    # On affiche le document
    displayDoc(FILES_DIRECTORY + args)