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
        self.arrayBombes = {}
        self.screen = pygame.display.set_mode((520, 520))
        self.structure = grid
        #print("Init Niveau")

    def generer(self):
        #print("Genere Niveau")
        #random.seed(calendar.timegm(time.gmtime()))
        for y, line in enumerate(self.structure):
            for x, c in enumerate(line):
                if (c==0):#Sol
                    if(randrange(0, 100) < 60):
                        a=1
                        #print("box")
                        self.screen.blit(image_box, (x*self.x, y*self.y))
                        self.structure[y][x] = 2
                    else:
                        self.screen.blit(image_sol, (x * self.x, y * self.y))
                if(c==9 or c==8):#Mur
                    self.screen.blit(image_sol, (x * self.x, y * self.y))
                if (c==1):#Murs
                    self.screen.blit(image_brick, (x * self.x, y * self.y))
        self.init = True
        #print("Fin génération")

    def set_pos_joueur(self, ligne, colonne, joueur):
        self.structure[ligne][colonne] = joueur.id

    def add_bombe(self, bombe):
        self.arrayBombes[bombe.id] = bombe

    def add_joueur(self, joueur):
        self.arrayJoueur[joueur.id] = joueur
        self.add_bombe(joueur.bombe)
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
        #print("Update Niveau")
        for y, line in enumerate(self.structure):
            for x, c in enumerate(line):
                if (c > 10 and c < 20):#Joueur
                    self.screen.blit(self.arrayJoueur[c].get_sprite(), (x * self.x, y * self.y))
                if (c == 0):#sol
                    self.screen.blit(image_sol, (x * self.x, y * self.y))
                if (c > 20 and c < 30):#Bombe
                    self.screen.blit(image_sol, (x * self.x, y * self.y))
                    self.screen.blit(self.arrayBombes[c].get_sprite(), (x * self.x, y * self.y))
                if (c == 3):
                    self.screen.blit(image_sol, (x * self.x, y * self.y))
                    self.screen.blit(image_explosion_haut, (x * self.x, y * self.y))
                if (c == 4):
                    self.screen.blit(image_sol, (x * self.x, y * self.y))
                    self.screen.blit(image_explosion_bas, (x * self.x, y * self.y))
                if (c == 5):
                    self.screen.blit(image_sol, (x * self.x, y * self.y))
                    self.screen.blit(image_explosion_gauche, (x * self.x, y * self.y))
                if (c == 6):
                    self.screen.blit(image_sol, (x * self.x, y * self.y))
                    self.screen.blit(image_explosion_droite, (x * self.x, y * self.y))
    
    def partie_end(self):
        nb = 0
        for i in self.arrayJoueur:
            if(self.arrayJoueur[i].vivant):
                nb+=1
        if(nb<2):
            return True
        else:
            return False

    def get_case(self, ligne, colonne):
        return self.structure[ligne][colonne]

    def get_grille(self):
        return self.structure
    
    def get_taille(self):
        return 12