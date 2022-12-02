import random as rand

class ia:

    def __init__(self, joueur):
        self.joueur = joueur
        self.possible = {"bas": False, "haut": False, "gauche": False, "droite": False}
        self.chemin_movement = []
        self.cible = None
        self.last_move = ""
        self.possible_bombe = False

    def set_cible(self, cible):
        self.cible = cible

    def scan_map(self, niveau):
        if niveau.structure[self.joueur.ligne + 1][self.joueur.colonne] == 0 or niveau.structure[self.joueur.ligne + 1][self.joueur.colonne] == 8 or niveau.structure[self.joueur.ligne + 1][self.joueur.colonne] == 9:
            self.possible["bas"] = True
        if niveau.structure[self.joueur.ligne - 1][self.joueur.colonne] == 0 or niveau.structure[self.joueur.ligne - 1][self.joueur.colonne] == 8 or niveau.structure[self.joueur.ligne - 1][self.joueur.colonne] == 9:
            self.possible["haut"] = True
        if niveau.structure[self.joueur.ligne][self.joueur.colonne + 1] == 0 or niveau.structure[self.joueur.ligne][self.joueur.colonne + 1] == 8 or niveau.structure[self.joueur.ligne][self.joueur.colonne + 1] == 9:
            self.possible["droite"] = True
        if niveau.structure[self.joueur.ligne][self.joueur.colonne - 1] == 0 or niveau.structure[self.joueur.ligne][self.joueur.colonne - 1] == 8 or niveau.structure[self.joueur.ligne][self.joueur.colonne - 1] == 9:
            self.possible["gauche"] = True

    def scan_map_bombe(self, niveau):
        if niveau.structure[self.joueur.ligne + 1][self.joueur.colonne] == 2:
            self.possible_bombe = True
        if niveau.structure[self.joueur.ligne - 1][self.joueur.colonne] == 2:
            self.possible_bombe = True
        if niveau.structure[self.joueur.ligne][self.joueur.colonne + 1] == 2:
            self.possible_bombe = True
        if niveau.structure[self.joueur.ligne][self.joueur.colonne - 1] == 2:
            self.possible_bombe = True


    def move(self, niveau, event):
        event.wait(0.05)
        self.scan_map(niveau)
        tmpKey, tmpVal = rand.choice(list(self.possible.items()))

        while tmpVal == False and self.last_move != tmpKey:
            tmpKey, tmpVal = rand.choice(list(self.possible.items()))

        if tmpVal == True:
            if tmpKey == "bas":
                self.joueur.move_down(niveau)
                self.last_move = "bas"
            elif tmpKey == "haut":
                self.joueur.move_up(niveau)
                self.last_move = "haut"
            elif tmpKey == "droite":
                self.joueur.move_right(niveau)
                self.last_move = "droite"
            elif tmpKey == "gauche":
                self.joueur.move_left(niveau)
                self.last_move = "gauche"

        self.possible = {"bas": False, "haut": False, "gauche": False, "droite": False}

    def move_to_cible(self, niveau, event):
        event.wait(0.05)
        self.scan_map(niveau)
        if self.cible != None:
            if self.joueur.ligne < self.cible.ligne and  niveau.structure[self.joueur.ligne + 1][self.joueur.colonne] == 0 or niveau.structure[self.joueur.ligne + 1][self.joueur.colonne] == 8 or niveau.structure[self.joueur.ligne + 1][self.joueur.colonne] == 9:
                self.joueur.move_down(niveau)
                self.last_move = "bas"
            elif self.joueur.ligne > self.cible.ligne and niveau.structure[self.joueur.ligne - 1][self.joueur.colonne] == 0 or niveau.structure[self.joueur.ligne - 1][self.joueur.colonne] == 8 or niveau.structure[self.joueur.ligne - 1][self.joueur.colonne] == 9:
                self.joueur.move_up(niveau)
                self.last_move = "haut"
            elif self.joueur.colonne < self.cible.colonne and niveau.structure[self.joueur.ligne][self.joueur.colonne + 1] == 0 or niveau.structure[self.joueur.ligne][self.joueur.colonne + 1] == 8 or niveau.structure[self.joueur.ligne][self.joueur.colonne + 1] == 9:
                self.joueur.move_right(niveau)
                self.last_move = "droite"
            elif self.joueur.colonne > self.cible.colonne and niveau.structure[self.joueur.ligne][self.joueur.colonne - 1] == 0 or niveau.structure[self.joueur.ligne][self.joueur.colonne - 1] == 8 or niveau.structure[self.joueur.ligne][self.joueur.colonne - 1] == 9:
                self.joueur.move_left(niveau)
                self.last_move = "gauche"
            self.place_bombe(niveau)
        self.possible = {"bas": False, "haut": False, "gauche": False, "droite": False}

    def place_bombe(self, niveau):
        self.scan_map_bombe(niveau)
        if self.possible_bombe == True:
            self.joueur.get_bombe().set_bombe(self.joueur, niveau)
            self.possible_bombe = False
    
    
    # def path_cible(self, niveau, cible, event):
    #     event.wait(0.05)
    #     self.scan_map(niveau)
    #     if self.joueur.ligne < cible.ligne:
    #         if self.possible["bas"] == True:
    #             self.joueur.move_down(niveau)
    #             self.last_move = "bas"
    #         else:
    #             self.move(niveau, event)
    #     elif self.joueur.ligne > cible.ligne:
    #         if self.possible["haut"] == True:
    #             self.joueur.move_up(niveau)
    #             self.last_move = "haut"
    #         else:
    #             self.move(niveau, event)
    #     elif self.joueur.colonne < cible.colonne:
    #         if self.possible["droite"] == True:
    #             self.joueur.move_right(niveau)
    #             self.last_move = "droite"
    #         else:
    #             self.move(niveau, event)
    #     elif self.joueur.colonne > cible.colonne:
    #         if self.possible["gauche"] == True:
    #             self.joueur.move_left(niveau)
    #             self.last_move = "gauche"
    #         else:
    #             self.move(niveau, event)

    #     self.possible = {"bas": False, "haut": False, "gauche": False, "droite": False}