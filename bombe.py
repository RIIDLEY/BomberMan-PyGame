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
        print("Init bombe")

    def set_bombe(self, joueur, niveau):
        if (self.planted == False):
            niveau.structure[joueur.ligne][joueur.colonne] = self.id
            self.ligne = joueur.ligne
            self.colonne = joueur.colonne
            joueur.ligne = joueur.last_ligne
            joueur.colonne = joueur.last_colonne
            niveau.structure[joueur.ligne][joueur.colonne] = joueur.id
            niveau.printstructure()
            niveau.updateLvl()
            self.planted = True

    def get_sprite(self):
        return self.sprit

    def get_planted(self):
        return self.planted
    
    def explose(self, niveau, event):
        if (self.planted == True):
            event.wait(5)
            print("Explosion")
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
            niveau.structure[self.ligne][self.colonne] = 0
            niveau.updateLvl()
        else:
            print("Pas d'explosion")