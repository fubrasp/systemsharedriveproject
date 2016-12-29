#!/usr/bin/python
# coding=utf-8

# ==> CODE DU CLIENT DE NOTRE APPLICATION

# --> IMPORTS
from tool import *
from coleditargs import *
import socket
from threadrafraichir import *
import signal
import sys

# --> USAGE : coledit -p <pseudo> -d <document>
ARGUMENTS = args(LISTE_ARGUMENTS)

SERVEUR_EN_LIGNE = True  # verifierServeurEnLigne(str("Python servedit.py -d "+arguments[document]))
AUTHENTIFICATION_REUSSIE = True  # checkAuthenticate(arguments)


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

if AUTHENTIFICATION_REUSSIE and SERVEUR_EN_LIGNE:

    # Paramètres d'initialisation du client pour communiquer avec le serveur

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("", 1111))

    print("Vous allez travailler sur le document : " + ARGUMENTS[DOCUMENT])

    # On boucle tant que le client ne quitte pas il peut écrire :

    TEXTE_A_ENVOYER = input(">> ")
    followThread = RafraichirClientThread(s, ARGUMENTS[DOCUMENT])
    followThread.start()

    #signal.signal(signal.SIGINT, signal_handler)
    #print('Press Ctrl+C')
    #signal.pause()
    #followThread.stop()

    while TEXTE_A_ENVOYER not in CMD_QUITTER_EDITION :

        effacerConsole() # À chaque ajout, on nettoie la console

        lireDansDoc(DOSSIER_FICHIERS_TXT + ARGUMENTS[DOCUMENT]) # On affiche le document

        print("Tapez exit pour quitter l'édition du fichier " + ARGUMENTS[DOCUMENT])
        TEXTE_A_ENVOYER = input(">> ")
        s.send(TEXTE_A_ENVOYER.encode())

else:
    if SERVEUR_EN_LIGNE == False:
        print("Le serveur n'est pas en route, lancez-le afin d'y accéder")

    if AUTHENTIFICATION_REUSSIE == False:
        print("Authentification impossible, vérifiez vos identifiants s'il vous plaît : 1) nom d'utilisateur, 2) fichier souhaité")
