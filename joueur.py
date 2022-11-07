import pygame
from constant import *
from random import *
import time
import calendar

class joueur:
    """class du joueur"""

    def __init__(self):
        """initialisation des variables de la class"""
        self.id = randrange(10, 1000)
        self.speed = 1
        self.ligne = 0
        self.colonne = 0
        self.sprit = image_joueur
        print("Init Joueur")

    def get_pos(self):
        return self.ligne, self.colonne

    def get_sprite(self):
        return self.sprit
