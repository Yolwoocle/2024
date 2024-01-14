import debug_2
from typing import List

"""
Cette famille est composée de N personnes.

Le but est de ranger chaque personne en fonction de sa taille. Le premier sur la photo doit être 
le plus petit et le dernier doit être le plus grand. Pour ordonner tout ce monde, nous pouvons faire 
cette opération autant de fois que voulu :
- Choisir i.
- Inverser la iè et la (i+K)è personne.
K est le nombre magique, il vous est donné.

Afficher s'il est possible d'ordonner les personnes de la famille.

* Entrée
L'entrée contiendra :
- Sur la première ligne, un entier : K, le nombre magique.
- Sur la ligne suivante, un entier : N, le nombre de personnes.
- Sur la ligne suivante, une liste de N entiers séparés par des espaces : tailles, la liste des tailles de chaque personne.

* Sortie
Afficher OUI s'il est possible de trier les personnes par taille ou NON si ce n'est pas possible.
"""

def echange(li, i, j):
    li[i], li[j] = li[j], li[i]

def ordre(k: int, n: int, tailles: List[int]) -> None:
    """
    :param k: le nombre magique
    :param n: le nombre de personnes
    :param tailles: la liste des tailles de chaque personne
    """
    # Tri par sélection 
    for i in range(n):
        # On trouve le minimum
        j_min = i
        for j in range(i, n):
            if tailles[j] < tailles[j_min]:
                j_min = j
                
        # On vérifie si on peut l'amener à l'indice i
        if (j_min - i) % k != 0:
            return False
        
        # On effectue l'échange
        for j in range(j_min, i, -k):
            echange(tailles, j, j-k)
    return True

if __name__ == "__main__":
    k = int(input())
    n = int(input())
    tailles = list(map(int, input().split()))
    succes = ordre(k, n, tailles)
    print("OUI" if succes else "NON")