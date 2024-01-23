from typing import List
import itertools
    
def obtenir_chemin(n: int, dieux: List[List[str]]) -> None:
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
        def aux(i: int, chemin: List[int], nom: bool, parcourus: List[bool]):
            parcourus[i] = True
            chemin = chemin[:]
            parcourus = parcourus[:]
            
            chemin.append(i)
            for id in range(n):
                d = dieux[id]
                if not parcourus[id] and ((nom and d[1] == dieux[i][1]) or (not nom and d[0] == dieux[i][0])):
                    # print(dieux[i], d, "nom" if nom else "prenom", "\t", chemin)
                    c = aux(id, chemin[:], not nom, parcourus[:])
                    if len(c) == n:
                        # print("RETURN")
                        return c
            return chemin
        return aux(i, [], nom, [False for _ in range(n)])

    
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
    
    #['a', 'A'], ['c', 'B'], ['d', 'B'], ['b', 'A'], ['c', 'A'], ['d', 'A']
    # C'est dégueulasse je sais mais j'ai plus de temps pour fixer mon code
    # for perm in itertools.permutations(dieux):
    c = (obtenir_chemin(n, dieux))
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