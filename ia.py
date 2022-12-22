import random as rand
from collections import deque, defaultdict
import math 

class ia:

    def __init__(self, joueur):
        self.joueur = joueur
        self.chemin_movement = []
        self.cible = None

    def set_cible(self, cible):
        self.cible = cible

    def dijkstra_chemin(self,niveau):
        # On récupère les coordonnées de la cible
        cible_pos = self.cible.get_pos()
        # On récupère les coordonnées du joueur
        joueurIA_pos = self.joueur.get_pos()

        # On récupère le niveau
        grille = niveau.get_grille()
        # On récupère la taille du niveau
        taille = niveau.get_taille()

        # On initialise le dictionnaire des chemins
        chemins = defaultdict(list)
        # On initialise la file des noeuds à visiter
        queue = deque([joueurIA_pos])        # On initialise la liste des noeuds visités
        visited = []

        path = []

        # On initialise le noeud temporaire pour stocker le meilleur noeud pour atteindre le joueur
        node_tmp = None

        # On ajoute le noeud de départ dans la liste des chemins
        chemins[cible_pos] = [cible_pos]

        # Tant que la file n'est pas vide
        while queue:
            # On récupère le noeud en tête de file
            noeud = queue.popleft()

            # Si le noeud n'a pas déjà été visité
            if noeud not in visited:
                # On récupère les voisins du noeud
                voisins = self.get_voisins(noeud, taille, niveau)
                node_tmp = voisins[0]
                # Pour chaque voisin
                for voisin in voisins:
                    # Si le voisin n'est pas un mur et que le voisin est plus proche du joueur que le noeud temporaire
                    if grille[voisin[0]][voisin[1]] != 1 and (self.manhattan(voisin, cible_pos, niveau) <= self.manhattan(node_tmp, cible_pos, niveau)):
                        # On met à jour le noeud temporaire
                        node_tmp = voisin
                        # Si le voisin est le joueur
                        if voisin == cible_pos:
                            # On sort de la boucle
                            break
                # On ajoute le noeud à la liste des noeuds visités
                queue.append(node_tmp)
                path.append(node_tmp)
                node_tmp = None

                visited.append(noeud)

        print("Chemin")
        path.pop(len(path)-1)
        path.pop(len(path)-1)
        print(path)
        return path
        

    def dijkstra_move(self,niveau):
        # On récupère les coordonnées de la cible
        cible_pos = self.cible.get_pos()
        # On récupère les coordonnées du joueur
        joueurIA_pos = self.joueur.get_pos()

        # On récupère le niveau
        grille = niveau.get_grille()
        # On récupère la taille du niveau
        taille = niveau.get_taille()

        # On initialise le dictionnaire des chemins
        chemins = defaultdict(list)
        # On initialise la file des noeuds à visiter
        # On initialise la liste des noeuds visités

        # On initialise le noeud temporaire pour stocker le meilleur noeud pour atteindre le joueur
        node_tmp = None

        # On ajoute le noeud de départ dans la liste des chemins
        chemins[cible_pos] = [cible_pos]

        # Tant que la file n'est pas vide

        voisins = self.get_voisins(joueurIA_pos, taille, niveau)
        node_tmp = voisins[0]
        for voisin in voisins:
            if grille[voisin[0]][voisin[1]] != 1 and (self.manhattan(voisin, cible_pos, niveau) <= self.manhattan(node_tmp, cible_pos, niveau)):
                node_tmp = voisin
        print(node_tmp)
        print(joueurIA_pos)
        #se deplace vers le noeud le plus proche de la cible
        if node_tmp[1] > joueurIA_pos[1] and node_tmp[0] == joueurIA_pos[0]:
            print('droite')
            self.joueur.move_right(niveau)
        elif node_tmp[1] < joueurIA_pos[1] and node_tmp[0] == joueurIA_pos[0]:
            print('gauche')
            self.joueur.move_left(niveau)
        elif node_tmp[1] == joueurIA_pos[1] and node_tmp[0] > joueurIA_pos[0]:
            print('bas')
            self.joueur.move_down(niveau)
        elif node_tmp[1] == joueurIA_pos[1] and node_tmp[0] < joueurIA_pos[0]:
            print('haut')
            self.joueur.move_up(niveau)
        
        return node_tmp



    def get_voisins(self, noeud, taille, niveau):
        # On initialise la liste des voisins
        voisins = []
        # On récupère les coordonnées du noeud
        x, y = noeud

        # On ajoute les voisins du haut
        if y > 0 and niveau.get_grille()[x][y-1] != 1:
            voisins.append((x, y - 1))
        # On ajoute les voisins du bas
        if y < taille - 1 and niveau.get_grille()[x][y+1] != 1:
            voisins.append((x, y + 1))
        # On ajoute les voisins de gauche
        if x > 0 and niveau.get_grille()[x-1][y] != 1:
            voisins.append((x - 1, y))
        # On ajoute les voisins de droite
        if x < taille - 1 and niveau.get_grille()[x+1][y] != 1:
            voisins.append((x + 1, y))

        # On retourne la liste des voisins
        return voisins

    def manhattan(self, nodeCourant, positionBot , niveau):
        if(niveau.get_grille()[nodeCourant[0]][nodeCourant[1]] == 2):
            return math.sqrt((nodeCourant[0] - positionBot[0])**2 + (nodeCourant[1] - positionBot[1])**2) + 1
        else:
            return math.sqrt((nodeCourant[0] - positionBot[0])**2 + (nodeCourant[1] - positionBot[1])**2)
