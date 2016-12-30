# systemsharedriveproject
project for system course

UTILISER Python 3.5.2 et un système UNIX
###DEADLINE 03/01/2017 ###

#contenu des fichiers
coledit.py ==> connecte un utilisateur a un document

servedit.py ==> gère les accès sur un document (écritures/suppressions)

tool.py ==> fonctions utilitaires au projet

person.py ==> reoprésente une person (Class)

coleditargs.py ==> contraintes pour la ligne de commande utilisé par coledit.py

serveditargs.py ==> contraintes pour la ligne de commande utilisé par servedit.py

threadrafraichir.py ==> thread permettant de rafraichir un client

constants.py ==> toutes les constantes nécéssaires au fonctionnement de l'application

##TO DO

*Nom et couleur random dans une base de noms

*A FINIR/A TESTER utiliser git pour historiser en appelant quand l'user quitte (signal ctrl^c) par exemple ?

#Fonctionnalités dévellopées
DANS SERVEDIT.PY ET COLEDIT.PY

*utilisation  des arguments en ligne de commande se base sur coleditargs.py et serveditargs.py 

*client qui peut se connecter, s'authentifier

*serveur qui initialise et créer les utilisateurs, gère la gestion des accès pour chaque document (ajout ou suppression)

*serveur gérant plusieurs threads

*afficher le nombre de client (à chaque connexion/déconnexion sur la vue serveur)

*système temps réel

#INSTALLER L'ENVIRONNEMENT NECESSAIRE AU PROJET
Dans l'idéal pour travailler efficacement:
INSTALLER:

Mac:

Python:
https://www.python.org/ftp/python/3.6.0/python-3.6.0-macosx10.6.pkg

Prérequis à l'IDE (JAVA SE SDK) si pas installé:
http://download.oracle.com/otn-pub/java/jdk/8u112-b16/jdk-8u112-macosx-x64.dmg

IDE:
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac

