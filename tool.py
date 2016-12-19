#!/usr/bin/python
# coding=utf-8

## Imports/uses
from constants import *
import mmap
import os





# Generic function in order to get args
def args(listOfArgs):
    parser = argparse.ArgumentParser()
    for current in listOfArgs:
        #each node of the list corresponds to an array of two values, the first for the option, the secund for the content of the option
        parser.add_argument(str(current[0]), str(current[1]), help=helpPError, type=str)

    args = parser.parse_args()

    if hasattr(args, 'pseudo'):
        dictArgs[str(pseudo)] = args.pseudo

    if hasattr(args, 'document'):
        dictArgs[str(document)] = args.document

    return dictArgs

def checkServerIsRunning(serverCommand):
    os.system(commandCheckServer+ " >tmp")
    result=open('tmp', 'r').read()
    if (str(serverCommand) in str(result)):
        return True
    else:
        return False


def checkAuthenticate(arguments):
    currUserArr = []
    userListed = False

    try:
        with open("users_"+arguments[document], "r+b") as usersData:
            # memory-map the file, size 0 means whole file
            mm = mmap.mmap(usersData.fileno(), 0)
            # read content via standard file methods
            for line in mm:
                currUserArr = str(usersData.readline()[:-1]).split(':')
                # check if user has the rule for authenticate
                if currUserArr[0] == arguments[pseudo]:
                    userListed = True
                    break
            mm.close()
    except IOError:
        return False

    if userListed:
        print(arguments[pseudo] + isAuthenticated)
        return True
    else:
        print(failToAuthenticate)
        return False
        sys.exit()


