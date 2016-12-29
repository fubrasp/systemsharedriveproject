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

try:
        print("""
        1. Ecrire dedans
        2. Supprimer quelque chose dedans
        3. Quitter l'application
        """)

        REP = input("Que voulez-vous faire avec le fichier " + ARGUMENTS[DOCUMENT] + " ? ")

        if REP == "1":
            print("Vous voulez écrire dans " + ARGUMENTS[DOCUMENT] + "\n")

            if AUTHENTIFICATION_REUSSIE and SERVEUR_EN_LIGNE:
                # Paramètres d'initialisation du client pour communiquer avec le serveur

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(("", 1111))

                print("Vous allez travailler sur le document : " + ARGUMENTS[DOCUMENT])

                # On boucle tant que le client ne quitte pas il peut écrire :
                followThread = RafraichirClientThread(s, ARGUMENTS[DOCUMENT])
                followThread.start()

                s.send(REP.encode())
                TEXTE_A_ENVOYER = INIT_STRING
                while TEXTE_A_ENVOYER not in CMD_QUITTER_EDITION:
                    effacerConsole()  # À chaque ajout, on nettoie la console

                    lireDansDoc(DOSSIER_FICHIERS_TXT + ARGUMENTS[DOCUMENT])  # On affiche le document

                    print("Tapez exit pour quitter l'édition du fichier " + ARGUMENTS[DOCUMENT])
                    TEXTE_A_ENVOYER = input(">> ")
                    s.send(TEXTE_A_ENVOYER.encode())
            else:
                if SERVEUR_EN_LIGNE == False:
                    print("Le serveur n'est pas en route, lancez-le afin d'y accéder")

                if AUTHENTIFICATION_REUSSIE == False:
                    print(
                        "Authentification impossible, vérifiez vos identifiants s'il vous plaît : 1) nom d'utilisateur, 2) "
                        "fichier souhaité")

        elif REP == "2":
            print("Vous voulez supprimer du texte de " + ARGUMENTS[DOCUMENT] + "\n")

            if AUTHENTIFICATION_REUSSIE and SERVEUR_EN_LIGNE:
                # Paramètres d'initialisation du client pour communiquer avec le serveur

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(("", 1111))

                print("Vous allez travailler sur le document : " + ARGUMENTS[DOCUMENT])

                # On boucle tant que le client ne quitte pas il peut écrire :
                followThread = RafraichirClientThread(s, ARGUMENTS[DOCUMENT])
                followThread.start()

                TEXTE_A_SUPPRIMER = INIT_STRING
                s.send(REP.encode())
                while TEXTE_A_SUPPRIMER != CMD_QUITTER_EDITION and TEXTE_A_SUPPRIMER != CMD_QUITTER_EDITION.upper():
                    effacerConsole()  # À chaque ajout, on nettoie la console

                    lireDansDoc(DOSSIER_FICHIERS_TXT + ARGUMENTS[DOCUMENT])  # On affiche le document

                    print("Tapez exit pour quitter l'édition du fichier " + ARGUMENTS[DOCUMENT])
                    TEXTE_A_SUPPRIMER = input(">> ")
                    s.send(TEXTE_A_SUPPRIMER.encode())
            else:
                if SERVEUR_EN_LIGNE == False:
                    print("Le serveur n'est pas en route, lancez-le afin d'y accéder")

                if AUTHENTIFICATION_REUSSIE == False:
                    print(
                        "Authentification impossible, vérifiez vos identifiants s'il vous plaît : 1) nom d'utilisateur, 2) "
                        "fichier souhaité")

        elif REP == "3":
            print("Vous avez demandé à quitter l'application ! \n")
            sys.exit(0)

        elif REP != "":
            print("Choix invalide, essayez encore. \n")

except KeyboardInterrupt:
    print(ARGUMENTS[PSEUDO] + " " + MSG_CLIENT_HORS_LIGNE)
    followThread.stop()
    sys.exit(0)