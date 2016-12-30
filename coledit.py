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
AUTHENTIFICATION_REUSSIE = verifierAuthentificationReussie(ARGUMENTS)
print("TEST AUTHENTIFICATION")
print(AUTHENTIFICATION_REUSSIE)

try:
    if AUTHENTIFICATION_REUSSIE and SERVEUR_EN_LIGNE:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("", 1111))
        followThread = RafraichirClientThread(s, ARGUMENTS[DOCUMENT])

        print("""
        1. Ecrire dedans
        2. Supprimer quelque chose dedans
        3. Quitter l'application
        """)

        REP = input("Que voulez-vous faire avec le fichier " + ARGUMENTS[DOCUMENT] + " ? ")

        if REP == "1":
            print("Vous voulez écrire dans " + ARGUMENTS[
                DOCUMENT] + "\n")  # Paramètres d'initialisation du client pour communiquer avec le serveur

            print("Vous allez travailler sur le document : " + ARGUMENTS[DOCUMENT])

            # On boucle tant que le client ne quitte pas il peut écrire :
            followThread.start()

            s.send(REP.encode())
            TEXTE_A_ENVOYER = INIT_STRING
            while TEXTE_A_ENVOYER not in CMD_QUITTER_EDITION:
                effacerConsole()  # À chaque ajout, on nettoie la console

                lireDansDoc(DOSSIER_FICHIERS_TXT + ARGUMENTS[DOCUMENT])  # On affiche le document

                print("[TAPEZ EXIT POUR QUITTER L'EDITION DU FICHIER " + ARGUMENTS[DOCUMENT] + "]")
                TEXTE_A_ENVOYER = input(">> ")
                s.send(TEXTE_A_ENVOYER.encode())

        elif REP == "2":
            print("Vous voulez supprimer du texte de " + ARGUMENTS[
                DOCUMENT] + "\n")  # Paramètres d'initialisation du client pour communiquer avec le serveur

            print("Vous allez travailler sur le document : " + ARGUMENTS[DOCUMENT])

            # On boucle tant que le client ne quitte pas il peut écrire :
            followThread.start()

            TEXTE_A_SUPPRIMER = INIT_STRING
            s.send(REP.encode())
            while TEXTE_A_SUPPRIMER != CMD_QUITTER_EDITION and TEXTE_A_SUPPRIMER != CMD_QUITTER_EDITION.upper():
                effacerConsole()  # À chaque ajout, on nettoie la console

                lireDansDoc(DOSSIER_FICHIERS_TXT + ARGUMENTS[DOCUMENT])  # On affiche le document

                print("[TAPEZ EXIT POUR QUITTER L'EDITION DU FICHIER " + ARGUMENTS[DOCUMENT] + "]")
                TEXTE_A_SUPPRIMER = input(">> ")
                s.send(TEXTE_A_SUPPRIMER.encode())

        elif REP == "3":
            print("Vous avez demandé à quitter l'application ! \n")
            sys.exit(0)

        elif REP != "":
            print("Choix invalide, essayez encore. \n")

    else:
        if SERVEUR_EN_LIGNE == False:
            print("Le serveur n'est pas en route, lancez-le afin d'y accéder")

        if AUTHENTIFICATION_REUSSIE == False:
            effacerConsole()
            print(
                "Authentification impossible, vérifiez vos identifiants s'il vous plaît : 1) nom d'utilisateur, 2) "
                "fichier souhaité")


except KeyboardInterrupt:
    print(ARGUMENTS[PSEUDO] + " " + MSG_CLIENT_HORS_LIGNE)
    followThread.stop()
    sys.exit(0)
