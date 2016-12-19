#!/usr/bin/python
# coding=utf-8

## Imports/uses
from tool import *
from serveditargs import *
from person import *
import time


# USAGE
#servedit -d <document>
arguments = args(listArgs)
print(arguments)

## Main algorithm which manage users interactions and several processes ##

# Start with asking the number of processes
numberOfProcesses = int(input(processesQuestion))
print(processesSelection, numberOfProcesses, processWord)

# WE ALSO CAN IMPROVE THIS BY GIVING RANDOM NAME AND COLOR
# Put the list of users allowed on the server
for count in range(numberOfProcesses):
    currentInteratorString=str(count)
    user = Person("user"+str(currentInteratorString), "color"+str(currentInteratorString))
    listOfUsers.append(user)

print(listOfUsers)

with open("users", "wb") as usersData:
    for user in listOfUsers:
        usersData.write(user.login+":"+user.color+"\n")

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print(leftServer)
        sys.exit()