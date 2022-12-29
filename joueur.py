from constant import *
import random as rand
from bombe import *

class joueur:
    """class du joueur"""

    def __init__(self, sprite, niveau):
        """initialisation des variables de la class"""
        self.id = rand.randint(11,19)
        while (self.id in niveau.arrayJoueur):
            self.id =  rand.randint(11,19)
        self.speed = 1
        self.ligne = 0
        self.colonne = 0
        self.position = [2, 0]
        self.last_ligne = 0
        self.last_colonne = 0
        self.vivant = True
        self.sprit = sprite
        self.bombe = bombe()
        #print("Init Joueur")

    def get_pos(self):
        return self.ligne, self.colonne

    def get_sprite(self):
        return self.sprit

    def get_bombe(self):
        return self.bombe

    def move_up(self, niveau):
        if (niveau.structure[self.ligne - 1][self.colonne] != 1 and niveau.structure[self.ligne - 1][self.colonne] != 2 and niveau.structure[self.ligne - 1][self.colonne] != 3 and niveau.structure[self.ligne - 1][self.colonne] < 10):
            niveau.structure[self.ligne][self.colonne] = 0
            self.last_colonne = self.colonne
            self.last_ligne = self.ligne
            self.ligne -= 1
            niveau.structure[self.ligne][self.colonne] = self.id
            self.position = [self.ligne, self.colonne]
            niveau.updateLvl()
            #print("Move up YES")

    def move_down(self, niveau):
        if (niveau.structure[self.ligne + 1][self.colonne] != 1 and niveau.structure[self.ligne + 1][self.colonne] != 2 and niveau.structure[self.ligne + 1][self.colonne] != 3 and niveau.structure[self.ligne + 1][self.colonne] < 10):
            niveau.structure[self.ligne][self.colonne] = 0
            self.last_colonne = self.colonne
            self.last_ligne = self.ligne
            self.ligne += 1
            niveau.structure[self.ligne][self.colonne] = self.id
            self.position = [self.ligne, self.colonne]
            niveau.updateLvl()
            #print("Move down YES")

    def move_left(self, niveau):
        if (niveau.structure[self.ligne][self.colonne - 1] != 1 and niveau.structure[self.ligne][self.colonne - 1] != 2 and niveau.structure[self.ligne][self.colonne - 1] != 3 and niveau.structure[self.ligne][self.colonne - 1] < 10):
            niveau.structure[self.ligne][self.colonne] = 0
            self.last_colonne = self.colonne
            self.last_ligne = self.ligne
            self.colonne -= 1
            niveau.structure[self.ligne][self.colonne] = self.id
            self.position = [self.ligne, self.colonne]
            niveau.updateLvl()
            #print("Move left YES")


    def move_right(self, niveau):
        if (niveau.structure[self.ligne][self.colonne + 1] != 1 and niveau.structure[self.ligne][self.colonne + 1] != 2 and niveau.structure[self.ligne][self.colonne + 1] != 3 and niveau.structure[self.ligne][self.colonne + 1] < 10):
            niveau.structure[self.ligne][self.colonne] = 0
            self.last_colonne = self.colonne
            self.last_ligne = self.ligne
            self.colonne += 1
            niveau.structure[self.ligne][self.colonne] = self.id
            self.position = [self.ligne, self.colonne]
            niveau.updateLvl()
            #print("Move right YES")

    def mort(self):
        self.vivant = False
