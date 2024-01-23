from typing import List
import itertools
    
class Graphe:
    def __init__(self, id, voisins_nom, voisins_prenom) -> None:
        self.id = id
        self.voisins_nom = voisins_nom
        self.voisins_prenom = voisins_prenom

def obtenir_chemin(n: int, dieux) -> None:
    """
    :param n: le nombre de dieux
    :param dieux: liste des prénoms et noms des dieux séparés par un espace
    """
    # TODO S'il n'existe aucun chemin qui permette de faire passer le message
    # par tous les dieux en respectant le protocole HTTP, afficher sur une
    # ligne le message `IMPOSSIBLE`. Sinon, afficher, sur une ligne par dieu et
    # dans l'ordre désiré, les noms complets des dieux par lesquels le message
    # doit passer. Si plusieurs solutions existent, afficher n'importe laquelle
    # d'entre elles.
    
    def profondeur(i: int, nom: bool = True):
        def aux(dieu: Graphe, i: int, chemin: List[int], nom: bool, parcourus: List[bool]):
            parcourus[i] = True
            chemin = chemin[:]
            parcourus = parcourus[:]
            
            chemin.append(i)
            a_parcourir = dieu.voisins_nom if nom else dieu.voisins_prenom
            for voisin in a_parcourir:
                if not parcourus[voisin.id]:
                    c = aux(voisin, voisin.id, chemin[:], not nom, parcourus[:])
                    if len(c) == n:
                        return c
            return chemin
        return aux(dieux[i], i, [], nom, [False for _ in range(n)])

    
    for i in range(n):
        c = profondeur(i, True)
        # print(f"prof({i}, True) = {c}")
        # print()
        if len(c) == n:
            return c
            
        c = profondeur(i, False)
        # print(f"prof({i}, False) = {c}")
        # print()
        if len(c) == n:
            return c
    
    # print("IMPOSSIBLE")
    return None

def afficher(li: List[str], dieux):
    for i in range(len(li)):
        print(" ".join(dieux[li[i]]))


def main():
    n = int(input())
    dieux = [input().split() for _ in range(n)]
    
    noeuds = [Graphe(i, [], []) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if dieux[i][0] == dieux[j][0]:
                    noeuds[i].voisins_prenom.append(noeuds[j])
                elif dieux[i][1] == dieux[j][1]:
                    noeuds[i].voisins_nom.append(noeuds[j])
    
    c = (obtenir_chemin(n, noeuds))
    if c == None:
        print("IMPOSSIBLE")
        return
    else:
        afficher(c, dieux)
        return

    
if __name__ == "__main__":
    main()

# b A
# c A
# c B
# d B
# d A
# a A