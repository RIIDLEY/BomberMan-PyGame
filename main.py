import threading
import pygame
import sys
import gc
from niveau import *
from joueur import *
from bombe import *
from ia import *
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
fenetre = pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    SCREEN.fill("black")
    niveau = Niveau()
    niveau.generer()
    if (niveau.init):
        print("Init OK")
        
        joueur1 = joueur(image_joueur1,niveau)
        niveau.add_joueur(joueur1)

        joueur2 = joueur(image_joueur2,niveau)
        niveau.add_joueur(joueur2)

        joueur3 = joueur(image_joueur3,niveau)
        niveau.add_joueur(joueur3)

        ia1 = ia(joueur3, niveau)

        niveau.printstructure()
        niveau.updateLvl()
        niveau.printstructure()

        if (ia1.joueur.vivant):
            event_ia1 = threading.Event()
            thread_ia1 = threading.Thread(
                target=ia1.dijkstra_move, args=(niveau, event_ia1))
            thread_ia1.start()

    while True and niveau.partie_end() == False:

        if (ia1.joueur.vivant and thread_ia1.is_alive() == False):
            event_ia1 = threading.Event()
            thread_ia1 = threading.Thread(
                target=ia1.dijkstra_move, args=(niveau, event_ia1))
            thread_ia1.start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                if event.key == pygame.K_j:
                    ia1.dijkstra_chemin(niveau)
                # Joueur 1
                if event.key == pygame.K_RIGHT and joueur1.vivant == True:
                    joueur1.move_right(niveau)
                if event.key == pygame.K_LEFT and joueur1.vivant == True:
                    joueur1.move_left(niveau)
                if event.key == pygame.K_UP and joueur1.vivant == True:
                    joueur1.move_up(niveau)
                if event.key == pygame.K_DOWN and joueur1.vivant == True:
                    joueur1.move_down(niveau)
                if event.key == pygame.K_SPACE and joueur1.vivant == True:
                    if (joueur1.bombe.get_planted() == False):
                        joueur1.get_bombe().set_bombe(joueur1, niveau)
                        event_joueur1 = threading.Event()
                        thread_joueur1 = threading.Thread(
                            target=joueur1.get_bombe().explose, args=(niveau, event_joueur1))
                        thread_joueur1.start()
                        # bombe1.explose(niveau)

                # Joueur 2
                if event.key == pygame.K_d and joueur2.vivant == True:
                    joueur2.move_right(niveau)
                if event.key == pygame.K_q and joueur2.vivant == True:
                    joueur2.move_left(niveau)
                if event.key == pygame.K_z and joueur2.vivant == True:
                    joueur2.move_up(niveau)
                if event.key == pygame.K_s and joueur2.vivant == True:
                    joueur2.move_down(niveau)
                if event.key == pygame.K_LSHIFT and joueur2.vivant == True:
                    if (joueur2.bombe.get_planted() == False):
                        joueur2.get_bombe().set_bombe(joueur2, niveau)
                        event_joueur2 = threading.Event()
                        thread_joueur2 = threading.Thread(
                            target=joueur2.get_bombe().explose, args=(niveau, event_joueur2))
                        thread_joueur2.start()

        pygame.display.update()
    
    if(thread_ia1.is_alive()):
        thread_ia1.join()
    gc.collect()
    game_over()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render(
            "LES OPTIONS", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="Menu", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250),
                             text_input="Jouer", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="Options", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 550),
                             text_input="Quitter", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def game_over():
    while True:
        GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("White")

        GAME_OVER_TEXT = get_font(45).render(
            "GAME OVER", True, "Black")
        GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(GAME_OVER_TEXT, GAME_OVER_RECT)

        GAME_OVER_BACK = Button(image=None, pos=(640, 460),
                                text_input="Menu", font=get_font(75), base_color="Black", hovering_color="Green")

        GAME_OVER_BACK.changeColor(GAME_OVER_MOUSE_POS)
        GAME_OVER_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME_OVER_BACK.checkForInput(GAME_OVER_MOUSE_POS):
                    main_menu()

        pygame.display.update()


main_menu()
