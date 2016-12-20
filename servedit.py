#!/usr/bin/python
# coding=utf-8

## Imports/uses
from tool import *
from serveditargs import *
import time


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



while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print(leftServer)
        sys.exit()