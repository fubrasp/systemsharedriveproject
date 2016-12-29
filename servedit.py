#!/usr/bin/python
# coding=utf-8

# ==> CODE DU SERVEUR DE NOTRE APPLICATION

# --> IMPORT
from tool import *
from serveditargs import *
import socket
import threading

# --> USAGE : servedit -d <document>

# On vérifie les arguments
arguments = args(LISTE_ARGUMENTS)

# On créé le fichier en vérifiant qu'il n'existe pas
DOCUMENT_COURANT = creerFichier(arguments[DOCUMENT])

# Nombre d'utilisateurs
NB_UTILISATEURS = int(input(QUESTION_NB_UTILISATEURS + arguments[DOCUMENT] + " ? "))

# Création des utilisateurs suivant le nombre soumis + on associe 1 couleur / utilisateur
LISTE_UTILISATEURS = associerUtilisateursAUnFichier(arguments[DOCUMENT], NB_UTILISATEURS)

# Affichage des utilisateurs
print("Les utilisateurs qui auront accès à votre fichier sont les suivants : ")
print(LISTE_UTILISATEURS)

# Variable globale indiquant le nb de clients connectés au serveur
global NB_CLIENTS_CONNECTES
NB_CLIENTS_CONNECTES = 0

# 1 thread / client, ça permet de paralléliser les traitements entre les utilisateurs
class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("=> Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connexion de %s %s" % (self.ip, self.port,))

        BUFF_SIZE = 35
        TEXTE_ENTIER = ""

        while True:
            MESSAGE = self.clientsocket.recv(BUFF_SIZE)
            TEXTE_ENTIER += " " + MESSAGE.decode()
            print(MESSAGE.decode())
            ecrireDansDoc(DOSSIER_FICHIERS_TXT + arguments[DOCUMENT], " " + MESSAGE.decode())

            # Mettre fin à la saisie par le client
            if (sys.getsizeof(MESSAGE) < BUFF_SIZE) or (CMD_QUITTER_EDITION in MESSAGE.decode()):
                break

        # On décrémente quand le client quitte
        print(MSG_CLIENT_HORS_LIGNE)
        global NB_CLIENTS_CONNECTES
        NB_CLIENTS_CONNECTES -= 1
        print("Nombre de clients restants : " + str(NB_CLIENTS_CONNECTES))

# Paramètres pour lancer le serveur
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

# Code du serveur :
while True:
    tcpsock.listen(10)
    print(MSG_SERVEUR_EN_ECOUTE)
    (clientsocket, (ip, port)) = tcpsock.accept()

    # Nouveau client = nouveau thread
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()

    # Ajout du client à la variable globale
    NB_CLIENTS_CONNECTES += 1
    print("Nombre de clients restants : " + str(NB_CLIENTS_CONNECTES))
