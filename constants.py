#!/usr/bin/python
# coding=utf-8

# ==> FICHIER REGROUPANT TOUTES LES CONSTANTES DE L'ENSEMBUE DU PROJET

# --> Arguments du programme
ARGS_LISTE = {}
PSEUDO = "pseudo"
DOCUMENT = "document"

# --> Questions/messages du programme
QUESTION_NB_UTILISATEURS = "À combien d'utilisateurs l'accès sera-t-il autorisé sur le document "

# --> Message d'identification de l'utilisateur
DESCRIPTION_PERSONNE = "La personne est "
LISTE_UTILISATEURS = []

# --> Message serveur hors ligne
MSG_UILISTEUR_SERVEUR_HORS_LIGNE="Le serveur n'est pas en route, lancez-le afin d'y accéder"

# --> Messages relatifs à l'authentification
NEST_PAS_AUTHENTIFIE = "Erreur d'authentification E/S"
AUTHENTIFICATION_IMPOSSIBLE="Authentification impossible, vérifiez vos identifiants s'il vous plaît : 1) nom d'utilisateur, 2) " "fichier souhaité"

# --> Texte du menu
MENU_CHOIX_INVALIDE="Choix invalide, essayez encore. \n"
MENU_QUITTER_APPLICATION="Vous avez demandé à quitter l'application ! \n"
MENU="""
        1. Ecrire dedans
        2. Supprimer quelque chose dedans
        3. Quitter l'application
        """

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