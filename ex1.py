from typing import List

def le_plus_grand_saut(n: int, differences: List[int]) -> None:
    """
    :param n: le nombre de branches de l'arbre moins 1
    :param differences: la liste des différences en hauteur des branches consécutives
    """
    # TODO Afficher le plus grand saut que devra effectuer Höder pour atteindre
    # la branche la plus haute de l'Yggdrasil.
    max_hauteur = differences[0]
    max_hauteur_idx = 0
    hauteur = 0
    for i in range(n):
        diff = differences[i]
        
        hauteur += diff
        if hauteur > max_hauteur:
            max_hauteur = hauteur
            max_hauteur_idx = i
    
    return max(differences[:max_hauteur_idx+1])
        

if __name__ == "__main__":
    n = int(input())
    differences = list(map(int, input().split()))
    print(le_plus_grand_saut(n, differences))
