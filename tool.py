#!/usr/bin/python
# coding=utf-8

## Imports/uses
from constants import *
import mmap
import os
import io
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
    if (str(serverCommand) in str(result)):
        return True
    else:
        return False


def checkAuthenticate(arguments):
    currUserArr = []
    userListed = False

    try:
        with io.open("users_" + arguments[document], "r", encoding="utf-8") as usersData:
            #print(usersData)
            # memory-map the file, size 0 means whole file
            #mm = mmap.mmap(usersData.fileno(), 0)
            # read content via standard file methods
            for line in usersData:
                currUserArr = str(usersData.readline()[:-1]).split(':')
                # check if user has the rule for authenticate
                #EN FUCKING PYTHON 3.5.2 il traite non pas comme une ligne mais comme chaque caractere!!!
                #print("LIGNE")
                #print(line)
                print(currUserArr)
                if currUserArr[0] == arguments[pseudo]:
                    #print("***OK***")
                    userListed = True
                    break
            #mm.close()
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
        user = Person("user" + str(currentInteratorString), "color" + str(currentInteratorString))
        listOfUsers.append(user)

    with open("users_" + document, "w") as usersData:
        for user in listOfUsers:
            usersData.write(user.login + ":" + user.color + "\n")

    return listOfUsers


def createDocument(document):
    # with open("users_" + document, "wb") as newDocument:
    #    newDocument.write("#shared document "+document)
    currentDocument = open(str(document), "wb")
    # return currentDocument


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
