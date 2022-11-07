import pygame
from constant import *
from random import randrange


class Niveau:
    """class de l'ffichage du terrain"""

    def __init__(self):
        """initialisation des variables de la class"""
        self.x = 40
        self.y = 40
        self.screen = pygame.display.set_mode((1280, 720))
        self.structure = grid
        print("Init Niveau")

    def generer(self):
        print("Genere Niveau")
        for y, line in enumerate(self.structure):
            for x, c in enumerate(line):
                if (c==0):#Sol
                    print("Sol")
                    if(randrange(0, 100) < 70):
                        print("Box")
                        self.screen.blit(image_box, (x*self.x, y*self.y))
                    else:
                        print("Sol")
                        self.screen.blit(image_sol, (x * self.x, y * self.y))
                if(c==9 or c==8):#Mur
                    print("Sol")
                    self.screen.blit(image_sol, (x * self.x, y * self.y))
                if (c==1):#Murs
                    print("Murs")
                    self.screen.blit(image_brick, (x * self.x, y * self.y))
        print("Fin génération")