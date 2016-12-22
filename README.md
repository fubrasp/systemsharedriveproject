# systemsharedriveproject
project for Ms. Christine BOURJOT

UTILISER Python 3.6 et un système UNIX
###DEADLINE 03/01/2017 ###

#file meaning
coledit.py ==> connect an user to a shared document

servedit.py ==> manage acess issues on document

tool.py ==> some commons functions in order to use in all parts of the source code

person.py ==> symbolize a person (Class)

coleditargs.py ==> rules of the command line for coledit.py

serveditargs.py ==> rules of the command line for servedit.py



client.py ==> exemple d'internet

server.py ==> exemple d'internet

clientCB.py ==> exemple modifié

serveurCB.py ==> exemple modifié
#TO DO

Ce que je propose (Guillaume):
--> faire une architecture client serveur analogue à celle du cours ce qui est implémenté en partie dans client.py et server.py


EDITION DE FICHIER/GESTION DE CONFLITS --> Il faut en discuter:

si on suit ce qui me semble coller au mieux au sujet (priorité absolue):

là on sait envoyer et recevoir du texte (mais on doit):

--> envoyer aux serveur et tout broadcaster en terme de texte

--> faire ça en boucle

*Nom et couleur random dans une base de noms

*A FINIR/A TESTER utiliser git pour historiser en appelant quand l'user quitte (signal ctrl^c) par exemple ?

*bug message usage

#Légende du TO DO
*pas important

#Fonctionnalités dévellopées (commit cddc3774bd7ffd68b50d333997f5e54f5a15776b)
DANS SERVEDIT.PY ET COLEDIT.PY

*utilisation  des arguments en ligne de commande (bug sur l'indication du help) se base sur coleditargs.py et serveditargs.py 

*client qui peut se connecter en apparence, s'authentifier

*serveur qui initialise et créer les utilisateurs, gère la gestion des accès pour chaque document

tout ca en monothread

DANS SERVERCB.PY ET CLIENTCB.PY

serveur gérant plusieurs threads

*afficher le nombre de client (à chaque connexion/déconnexion sur la vue serveur)
