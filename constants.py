#!/usr/bin/python
# coding=utf-8

# ==> FICHIER REGROUPANT TOUTES LES CONSTANTES DE L'ENSEMBUE DU PROJET

# --> Arguments du programme
ARGS_LISTE = {}
PSEUDO = "pseudo"
DOCUMENT = "document"

# --> Questions/messages du programme
QUESTION_NB_UTILISATEURS = "À combien d'utilisateurs l'accès sera-t-il autorisé sur le document "
processesSelection = "Vous avez selectionné : "
processWord = "processus"

# --> Message d'identification de l'utilisateur
DESCRIPTION_PERSONNE = "La personne est "
LISTE_UTILISATEURS = []

# --> Messages relatifs à l'authentification
EST_AUTHENTIFIE = " est authentifié"
NEST_PAS_AUTHENTIFIE = "Erreur d'authentification"

# --> Messages émis par le serveur
MSG_SERVEUR_HORS_LIGNE = "Serveur hors-ligne."
MSG_CLIENT_HORS_LIGNE = "Client déconnecté."
MSG_SERVEUR_EN_ECOUTE = "En attente de connexions..."

# --> Chemins utilisés durant le projet
DOSSIER_FICHIERS_TXT = "files/"
DOSSIER_UTILISATEURS_FICHIERS_TXT = "files_users/"

# --> Messages de test
testServerIsRunning = "TEST => Le serveur fonctionne ! "
testAuthentificationIsWorking = "TEST => L'authentification fonctionne !"

# --> Commande pour voir si le serveur marche
CMD_VERIFIER_SERVEUR_EN_LIGNE = "ps ax | grep servedit.py | tail -1"

# --> Commande pour quitter l'édition d'un fichier
CMD_QUITTER_EDITION = "exit"

# --> Messages
DATA_SEND = "_DBS_"
SERVER_QUIT = "_SQ_"

# --> Messages erreur de lecture d'un fichier
MSG_ERREUR_LECTURE_FICHIER = "Erreur de lecture du fichier !"
MSG_ERREUR_ECRITURE_FICHIER = "Ecriture impossible dans le fichier !"
MSG_ERREUR_SUPPRESSION_FICHIER = "Suppression impossible dans le fichier !"

INIT_STRING = "Initialisation chaîne"