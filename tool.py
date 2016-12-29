#!/usr/bin/python
# coding=utf-8

# IMPORTS
import os, io, argparse, sys
from person import *

# Generic function in order to get args
def args(LISTE_ARGUMENTS):
    PARSEUR = argparse.ArgumentParser()

    for current in LISTE_ARGUMENTS: PARSEUR.add_argument(str(current[0]), str(current[1]), help="", type=str)

    ARGUMENTS = PARSEUR.parse_args()

    if hasattr(ARGUMENTS, 'pseudo'): ARGS_LISTE[str(PSEUDO)] = args.pseudo

    if hasattr(ARGUMENTS, 'document'): ARGS_LISTE[str(DOCUMENT)] = args.document

    return ARGS_LISTE


def verifierServeurEnLigne(CMD_SERVEUR):
    os.system(CMD_VERIFIER_SERVEUR_EN_LIGNE + " >tmp")
    RES = open('tmp', 'r').read()

    if CMD_SERVEUR in RES: return True
    else: return False

def verifierAuthentificationReussie(ARGUMENTS):
    TAB_USER_COURANT = []
    USER_TROUVE = False

    try:
        with io.open("users_" + ARGUMENTS[DOCUMENT], "r", encoding="utf-8") as DONNEES_UTILISATEURS:
            for LIGNE in DONNEES_UTILISATEURS:
                TAB_USER_COURANT = str(LIGNE[:-1]).split(':')
                if TAB_USER_COURANT[0] == ARGUMENTS[pseudo]:
                    USER_TROUVE = True
                    break
    except IOError:
        print(NEST_PAS_AUTHENTIFIE)

    if USER_TROUVE: return True
    else:
        return False
        sys.exit()

def associerUtilisateursAUnFichier(DOCUMENT, NB_UTILISATEURS):

    for count in range(NB_UTILISATEURS):
        COMPTEUR = str(count)
        UTILISATEUR = Person("Utilisateur n°" + str(COMPTEUR), "(Couleur " + str(COMPTEUR) + ")")
        LISTE_UTILISATEURS.append(UTILISATEUR)

    with open(DOSSIER_UTILISATEURS_FICHIERS_TXT + "users_" + DOCUMENT, "w") as DONNEES_UTILISATEURS:
        for UTILISATEUR in LISTE_UTILISATEURS:
            DONNEES_UTILISATEURS.write(UTILISATEUR.login + UTILISATEUR.color + "\n")

    return LISTE_UTILISATEURS


def creerFichier(NOM_FICHIER):
    if os.path.exists(DOSSIER_FICHIERS_TXT + NOM_FICHIER) == False :
        os.system("touch " + DOSSIER_FICHIERS_TXT + NOM_FICHIER)
    else :
        lireDansDoc(DOSSIER_FICHIERS_TXT + NOM_FICHIER)
        # print("Le fichier " + fileName + " existe déjà ! Choisissez un autre nom")
        sys.exit()

def modifierFichier(NOM_FICHIER):
    os.system("vim " + NOM_FICHIER)


def finirSession(NOM_FICHIER, MESSAGE):
    os.system("git add " + NOM_FICHIER)
    os.system("git commit -m " + MESSAGE + "")
    # os.system("git push")

def initialiserGitRepo(DOSSIER):
    os.system("git init " + DOSSIER)


def suivreGitRepo(DOSSIER):
    os.system("git log " + DOSSIER)

#fonctions sytemes usuelles
def effacerConsole():
    os.system("clear")

# on choisit une approche non systeme pour ne pas perdre en interactivite
def lireDansDoc(NOM_FICHIER):
    try:
        with io.open(NOM_FICHIER, "r", encoding="utf-8") as _file:
            for LIGNE in _file:
                print(LIGNE)
    except IOError:
        print(MSG_ERREUR_LECTURE_FICHIER)

def ecrireDansDoc(NOM_FICHIER, TEXTE):
    try:
        with io.open(NOM_FICHIER, "a", encoding="utf-8") as _file:
            _file.write(TEXTE)
            _file.close()
    except IOError:
        print(MSG_ERREUR_ECRITURE_FICHIER)

def supprimerDansDoc(NOM_FICHIER):
    try:
        with io.open(NOM_FICHIER, "a", encoding="utf-8") as _file:
            _file.write()
            _file.close()
    except IOError:
        print(MSG_ERREUR_SUPPRESSION_FICHIER)