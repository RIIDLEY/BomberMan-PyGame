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

#1 = Mur
#0 = Sol
#2 = Mur destructible
#3 = explosion haut
#4 = explosion bas
#5 = explosion gauche
#6 = explosion droite
#8/9 = Safe zone
#>10 <20 = Joueur
#>20 <30 = Bombe
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

image_explosion = pygame.image.load("images/explosion/1.png")
image_explosion = pygame.transform.scale(image_explosion, (40, 40))

image_explosion2 = pygame.image.load("images/explosion/2.png")
image_explosion2 = pygame.transform.scale(image_explosion2, (40, 40))

image_explosion3 = pygame.image.load("images/explosion/3.png")
image_explosion3 = pygame.transform.scale(image_explosion3, (40, 40))

image_explosion_centre = pygame.image.load("images/explosion/tile082.png")
image_explosion_centre = pygame.transform.scale(image_explosion_centre, (40, 40))

image_explosion_haut = pygame.image.load("images/explosion/tile015.png")
image_explosion_haut = pygame.transform.scale(image_explosion_haut, (40, 40))

image_explosion_bas = pygame.image.load("images/explosion/tile047.png")
image_explosion_bas = pygame.transform.scale(image_explosion_bas, (40, 40))

image_explosion_gauche = pygame.image.load("images/explosion/tile080.png")
image_explosion_gauche = pygame.transform.scale(image_explosion_gauche, (40, 40))

image_explosion_droite = pygame.image.load("images/explosion/tile083.png")
image_explosion_droite = pygame.transform.scale(image_explosion_droite, (40, 40))
