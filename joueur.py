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

    def move_up(self, niveau):
        if (niveau.structure[self.ligne - 1][self.colonne] != 1 and niveau.structure[self.ligne - 1][self.colonne] != 2):
            niveau.structure[self.ligne][self.colonne] = 0
            self.ligne -= 1
            niveau.structure[self.ligne][self.colonne] = self.id
            niveau.updateLvl()
            print("Move up YES")
        else:
            print("Move up NO")

    def move_down(self, niveau):
        if (niveau.structure[self.ligne + 1][self.colonne] != 1 and niveau.structure[self.ligne + 1][self.colonne] != 2):
            niveau.structure[self.ligne][self.colonne] = 0
            self.ligne += 1
            niveau.structure[self.ligne][self.colonne] = self.id
            niveau.updateLvl()
            print("Move down YES")
        else:
            print("Move down NO")

    def move_left(self, niveau):
        if (niveau.structure[self.ligne][self.colonne - 1] != 1 and niveau.structure[self.ligne][self.colonne - 1] != 2):
            niveau.structure[self.ligne][self.colonne] = 0
            self.colonne -= 1
            niveau.structure[self.ligne][self.colonne] = self.id
            niveau.updateLvl()
            print("Move left YES")
        else:
            print("Move left NO")

    def move_right(self, niveau):
        if (niveau.structure[self.ligne][self.colonne + 1] != 1 and niveau.structure[self.ligne][self.colonne + 1] != 2):
            niveau.structure[self.ligne][self.colonne] = 0
            self.colonne += 1
            niveau.structure[self.ligne][self.colonne] = self.id
            niveau.updateLvl()
            print("Move right YES")
        else:
            print("Move right NO")