import pygame
from constant import *
from random import *
import time
import calendar

class bombe:
    """class du bombe"""

    def __init__(self):
        """initialisation des variables de la class"""
        self.sprit = image_bombe
        self.ligne = 0
        self.colonne = 0
        print("Init bombe")

    def set_bombe(self, joueur):
        self.colonne = joueur.colonne
        self.ligne = joueur.ligne
    
    def get_sprite(self):
        return self.sprit
    
    def explose(self, niveau):
        if (niveau.structure[self.ligne][self.colonne] == 3):
            niveau.structure[self.ligne][self.colonne] = 0
            niveau.updateLvl()
            print("Explose")
        else:
            print("Pas d'explosion")