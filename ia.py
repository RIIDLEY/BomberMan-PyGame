import random as rand

class ia:

    def __init__(self, joueur):
        self.joueur = joueur
        self.possible = {"bas": False, "haut": False, "gauche": False, "droite": False}
        self.possible_bombe = False

    def scan_map(self, niveau):
        if niveau.structure[self.joueur.ligne + 1][self.joueur.colonne] == 0 or niveau.structure[self.joueur.ligne + 1][self.joueur.colonne] == 8 or niveau.structure[self.joueur.ligne + 1][self.joueur.colonne] == 9:
            self.possible["bas"] = True
        if niveau.structure[self.joueur.ligne - 1][self.joueur.colonne] == 0 or niveau.structure[self.joueur.ligne - 1][self.joueur.colonne] == 8 or niveau.structure[self.joueur.ligne - 1][self.joueur.colonne] == 9:
            self.possible["haut"] = True
        if niveau.structure[self.joueur.ligne][self.joueur.colonne + 1] == 0 or niveau.structure[self.joueur.ligne][self.joueur.colonne + 1] == 8 or niveau.structure[self.joueur.ligne][self.joueur.colonne + 1] == 9:
            self.possible["droite"] = True
        if niveau.structure[self.joueur.ligne][self.joueur.colonne - 1] == 0 or niveau.structure[self.joueur.ligne][self.joueur.colonne - 1] == 8 or niveau.structure[self.joueur.ligne][self.joueur.colonne - 1] == 9:
            self.possible["gauche"] = True

    def move(self, niveau, event):
        event.wait(5)
        self.scan_map(niveau)
        tmpKey, tmpVal = rand.choice(list(self.possible.items()))
        if tmpVal == True:
            if tmpKey == "bas":
                self.joueur.move_down(niveau)
            elif tmpKey == "haut":
                self.joueur.move_up(niveau)
            elif tmpKey == "droite":
                self.joueur.move_right(niveau)
            elif tmpKey == "gauche":
                self.joueur.move_left(niveau)