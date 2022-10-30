import pygame
from constant import *

class Niveau:
    """class de l'ffichage du terrain"""

    def __init__(self):
        """initialisation des variables de la class"""
        self.x = 20
        self.y = 20
        self.screen = pygame.display.set_mode((1280, 720))
        self.structure = grid
        print("Init Niveau")

    def generer(self):
        print("Genere Niveau")
        for y, line in enumerate(self.structure):
            for x, c in enumerate(line):
                if (c==0):#Sol
                    print("Sol")
                    self.screen.blit(image_sol, (x * 20, y * 20))
                if (c==1):#Murs
                    print("Murs")
                    self.screen.blit(image_brick, (x * 20, y * 20))
