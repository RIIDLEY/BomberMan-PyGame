import pygame
"""Constantes du jeu"""


grid_1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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

grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 1],
        [1, 8, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 8, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 8, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 8, 1],
        [1, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# 1 = Mur
# 0 = Sol
# 2 = Mur destructible
# 3 = explosion haut
# 4 = explosion bas
# 5 = explosion gauche
# 6 = explosion droite
# 8/9 = Safe zone
# >10 <20 = Joueur
# >20 <30 = Bombe
# chemin des sprites et des textures du jeu

image_brick = pygame.image.load("images/terrain/block.png")
image_brick = pygame.transform.scale(image_brick, (60, 60))

image_sol = pygame.image.load("images/terrain/grass.png")
image_sol = pygame.transform.scale(image_sol, (60, 60))

image_box = pygame.image.load("images/terrain/box.png")
image_box = pygame.transform.scale(image_box, (60, 60))

image_joueur1 = pygame.image.load("images/hero/pf1.png")
image_joueur1 = pygame.transform.scale(image_joueur1, (60, 60))

image_joueur2 = pygame.image.load("images/enemy/e1f0.png")
image_joueur2 = pygame.transform.scale(image_joueur2, (60, 60))

image_joueur3 = pygame.image.load("images/enemy/e3f0.png")
image_joueur3 = pygame.transform.scale(image_joueur3, (60, 60))

image_joueur4 = pygame.image.load("images/enemy/e2f0.png")
image_joueur4 = pygame.transform.scale(image_joueur4, (60, 60))

image_bombe = pygame.image.load("images/bomb/1.png")
image_bombe = pygame.transform.scale(image_bombe, (60, 60))

image_explosion = pygame.image.load("images/explosion/1.png")
image_explosion = pygame.transform.scale(image_explosion, (60, 60))

image_explosion2 = pygame.image.load("images/explosion/2.png")
image_explosion2 = pygame.transform.scale(image_explosion2, (60, 60))

image_explosion3 = pygame.image.load("images/explosion/3.png")
image_explosion3 = pygame.transform.scale(image_explosion3, (60, 60))

image_explosion_centre = pygame.image.load("images/explosion/tile082.png")
image_explosion_centre = pygame.transform.scale(
    image_explosion_centre, (60, 60))

image_explosion_haut = pygame.image.load("images/explosion/tile015.png")
image_explosion_haut = pygame.transform.scale(image_explosion_haut, (60, 60))

image_explosion_bas = pygame.image.load("images/explosion/tile047.png")
image_explosion_bas = pygame.transform.scale(image_explosion_bas, (60, 60))

image_explosion_gauche = pygame.image.load("images/explosion/tile080.png")
image_explosion_gauche = pygame.transform.scale(
    image_explosion_gauche, (60, 60))

image_explosion_droite = pygame.image.load("images/explosion/tile083.png")
image_explosion_droite = pygame.transform.scale(
    image_explosion_droite, (60, 60))
