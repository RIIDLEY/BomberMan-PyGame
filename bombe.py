import pygame
from constant import *
import random as rand
import time
import calendar
from playsound import playsound

class bombe:
    """class du bombe"""

    def __init__(self):
        """initialisation des variables de la class"""
        self.sprit = image_bombe
        self.id =  rand.randint(21,29)
        self.ligne = 0
        self.colonne = 0
        self.planted = False
        #print("Init bombe")

    def set_bombe(self, joueur, niveau):
        if (self.planted == False):
            niveau.structure[joueur.ligne][joueur.colonne] = self.id
            self.ligne = joueur.ligne
            self.colonne = joueur.colonne
            joueur.ligne = joueur.last_ligne
            joueur.colonne = joueur.last_colonne
            niveau.structure[joueur.ligne][joueur.colonne] = joueur.id
            niveau.updateLvl()
            self.planted = True

    def get_sprite(self):
        return self.sprit

    def get_planted(self):
        return self.planted
    
    def explose(self, niveau, event):
        if (self.planted == True):
            event.wait(1)
            #print("Explosion")
            #playsound('sounds\explosion.mp3')
            self.planted = False
            self.sprit = image_explosion
            niveau.updateLvl()
            event.wait(0.1)
            self.sprit = image_explosion2
            niveau.updateLvl()
            event.wait(0.1)
            self.sprit = image_explosion3
            niveau.updateLvl()
            event.wait(0.1)
            self.sprit = image_explosion_centre

            #Explosion haut sur joueur
            if (niveau.structure[self.ligne-1][self.colonne] > 10 and niveau.structure[self.ligne-1][self.colonne] < 20):
                niveau.arrayJoueur[niveau.structure[self.ligne-1][self.colonne]].mort()

            #Explosion bas sur joueur
            if (niveau.structure[self.ligne+1][self.colonne] > 10 and niveau.structure[self.ligne+1][self.colonne] < 20):
                niveau.arrayJoueur[niveau.structure[self.ligne+1][self.colonne]].mort()

            #Explosion gauche sur joueur
            if (niveau.structure[self.ligne][self.colonne-1] > 10 and niveau.structure[self.ligne][self.colonne-1] < 20):
                niveau.arrayJoueur[niveau.structure[self.ligne][self.colonne-1]].mort()

            #Explosion droite sur joueur
            if (niveau.structure[self.ligne][self.colonne+1] > 10 and niveau.structure[self.ligne][self.colonne+1] < 20):
                niveau.arrayJoueur[niveau.structure[self.ligne][self.colonne+1]].mort()

            #Explosion haut
            if (niveau.structure[self.ligne-1][self.colonne] != 1):
                niveau.structure[self.ligne-1][self.colonne] = 3

            #Explosion bas
            if (niveau.structure[self.ligne+1][self.colonne] != 1):
                niveau.structure[self.ligne+1][self.colonne] = 4

            #Explosion gauche
            if (niveau.structure[self.ligne][self.colonne-1] != 1):
                niveau.structure[self.ligne][self.colonne-1] = 5

            #Explosion droite
            if (niveau.structure[self.ligne][self.colonne+1] != 1):
                niveau.structure[self.ligne][self.colonne+1] = 6

            niveau.updateLvl()
            event.wait(0.2)

            niveau.structure[self.ligne][self.colonne] = 0

            #Explosion haut
            if (niveau.structure[self.ligne-1][self.colonne] != 1):
                niveau.structure[self.ligne-1][self.colonne] = 0

            #Explosion bas
            if (niveau.structure[self.ligne+1][self.colonne] != 1):
                niveau.structure[self.ligne+1][self.colonne] = 0

            #Explosion gauche
            if (niveau.structure[self.ligne][self.colonne-1] != 1):
                niveau.structure[self.ligne][self.colonne-1] = 0

            #Explosion droite
            if (niveau.structure[self.ligne][self.colonne+1] != 1):
                niveau.structure[self.ligne][self.colonne+1] = 0

            niveau.updateLvl()

            self.sprit = image_bombe
        else:
            print("Pas d'explosion")