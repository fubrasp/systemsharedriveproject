#!/usr/bin/python
# coding=utf-8

#TO DO
# We have to :
# PURPOSES OF IMPROVEMENT
# LOOK IN THE CODE WHERE -PURPOSE- IS

## Main algorithm which manage users interactions and several processes ##

## Import/uses
from constants import *
from person import *


# Start with asking the number of processes
numberOfProcesses = int(input(processesQuestion))
print(processesSelection, numberOfProcesses, processWord)

# -PURPOSE- WE ALSO CAN IMPROVE THIS BY GIVING RANDOM NAME AND COLOR
# Put the list of users allowed on the server
for count in range(numberOfProcesses):
    currentInteratorString=str(count)
    user = Person("user"+str(currentInteratorString), "color"+str(currentInteratorString))
    listOfUsers.append(user)

print(listOfUsers)
