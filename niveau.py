import pygame
from constant import *
from random import *
from joueur import *
import time
import calendar


class Niveau:
    """class de l'ffichage du terrain"""

    def __init__(self):
        """initialisation des variables de la class"""
        self.x = 40
        self.y = 40
        self.init = False
        self.arrayJoueur = {}
        self.screen = pygame.display.set_mode((1280, 720))
        self.structure = grid
        print("Init Niveau")

    def generer(self):
        print("Genere Niveau")
        #random.seed(calendar.timegm(time.gmtime()))
        for y, line in enumerate(self.structure):
            for x, c in enumerate(line):
                if (c==0):#Sol
                    print("Sol")
                    if(randrange(0, 100) < 70):
                        print("Box")
                        self.screen.blit(image_box, (x*self.x, y*self.y))
                        self.structure[y][x] = 2
                    else:
                        print("Sol")
                        self.screen.blit(image_sol, (x * self.x, y * self.y))
                if(c==9 or c==8):#Mur
                    print("Sol")
                    self.screen.blit(image_sol, (x * self.x, y * self.y))
                if (c==1):#Murs
                    print("Murs")
                    self.screen.blit(image_brick, (x * self.x, y * self.y))
        self.init = True
        print("Fin génération")

    def set_pos_joueur(self, ligne, colonne, joueur):
        self.structure[ligne][colonne] = joueur.id

    def add_joueur(self, joueur):
        self.arrayJoueur[joueur.id] = joueur
        for y, line in enumerate(self.structure):
            for x, c in enumerate(line):
                if (c == 9):
                    self.structure[y][x] = joueur.id
                    joueur.ligne = y
                    joueur.colonne = x
                    return
    
    def printstructure(self):
        for i in self.structure:
            for j in i:
                print(j, end="|")
            print("\r")

    def updateLvl(self):
        print("Update Niveau")
        for y, line in enumerate(self.structure):
            for x, c in enumerate(line):
                if (c >= 10):
                    self.screen.blit(self.arrayJoueur[c].get_sprite(), (x * self.x, y * self.y))
                if (c == 0):
                    self.screen.blit(image_sol, (x * self.x, y * self.y))
