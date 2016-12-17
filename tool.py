#!/usr/bin/python
# coding=utf-8

## Imports/uses
from constants import *


# Generic function in order to get args
def args(listOfArgs):
    parser = argparse.ArgumentParser()
    for current in listOfArgs:
        #each node of the list corresponds to an array of two values, the first for the option, the secund for the content of the option
        parser.add_argument(str(current[0]), str(current[1]), help=helpPError, type=str)

    args = parser.parse_args()

    if args.pseudo:
        dictArgs[str(pseudo)] = args.pseudo

    if args.document:
        dictArgs[str(document)] = args.document

    return dictArgs
