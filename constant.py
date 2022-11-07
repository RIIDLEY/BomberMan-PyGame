import pygame
"""Constantes du jeu"""


grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 9, 8, 0, 0, 0, 0, 0, 0, 0, 8, 9, 1],
        [1, 8, 1, 0, 1, 0, 1, 0, 1, 0, 1, 8, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 8, 1, 0, 1, 0, 1, 0, 1, 0, 1, 8, 1],
        [1, 9, 8, 0, 0, 0, 0, 0, 0, 0, 8, 9, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# chemin des sprites et des textures du jeu

image_brick = pygame.image.load("images/terrain/block.png")
image_brick = pygame.transform.scale(image_brick, (40, 40)) 

image_sol = pygame.image.load("images/terrain/grass.png")
image_sol = pygame.transform.scale(image_sol, (40, 40)) 

image_box = pygame.image.load("images/terrain/box.png")
image_box = pygame.transform.scale(image_box, (40, 40)) 

image_joueur = pygame.image.load("images/hero/pf1.png")
image_joueur = pygame.transform.scale(image_joueur, (40, 40)) 

image_bombe = pygame.image.load("images/bomb/1.png")
image_bombe = pygame.transform.scale(image_bombe, (40, 40))