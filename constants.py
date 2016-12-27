#!/usr/bin/python
# coding=utf-8

# ==> FICHIER REGROUPANT TOUTES LES CONSTANTES DE L'ENSEMBUE DU PROJET

# --> Arguments du programme
dictArgs = {}
pseudo = "pseudo"
document = "document"

# --> Questions/messages du programme
processesQuestion = "À combien d'utilisateurs l'accès sera-t-il autorisé sur le document "
processesSelection = "Vous avez selectionné : "
processWord = "processus"

# --> Message d'identification de l'utilisateur
personDefineSentence = "La personne est "
listOfUsers=[]

# --> Messages relatifs à l'authentification
isAuthenticated = " est authentifié"
failToAuthenticate = "Erreur d'authentification"

# --> Messages émis par le serveur
leftServer = "Serveur hors-ligne."
leftClient = "Client déconnecté."
IS_LISTENING = "En attente de connexions..."

# --> Chemins utilisés durant le projet
FILES_DIRECTORY = "files/"
FILES_USERS_DIRECTORY = "files_users/"

# --> Messages de test
testServerIsRunning = "[TEST] : le serveur fonctionne ! "
testAuthentificationIsWorking = "[TEST] : l'authentification fonctionne !"

# --> Commande pour voir si le serveur marche
commandCheckServer = "ps ax | grep servedit.py | tail -1"

# --> Commande pour quitter l'édition d'un fichier
LEFT_EDITOR = "exit"

# --> Messages
DATA_SEND = "_DBS_"