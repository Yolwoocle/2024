from typing import List


def batiments(nb_villes: int, nb_mouv: int, k: int, villes: List[int]) -> None:
    """
    :param n: le nombre de villes
    :param r: le nombre de mouvements du serpent
    :param k: le nombre de villes impliquées dans chaque mouvement
    :param villes: le nombre de bâtiments cassés dans chaque ville
    """
    # TODO Afficher le nombre de bâtiments cassés à chaque ville après les $R$
    # mouvements sous la forme d'une suite d'entiers séparés par des espaces.
    
    max_queue = max(villes[j % nb_villes] for j in range(1, k))
    m = max(villes[0], max_queue)
    villes[0] = m
    
    for i in range(1, nb_mouv):
        m = max(max_queue)
        villes[i % nb_villes] = m

    for i in range(nb_villes):
        v = villes[i]
        print(v, end=(" " if i < nb_villes-1 else "\n"))


if __name__ == "__main__":
    n = int(input())
    r = int(input())
    k = int(input())
    villes = list(map(int, input().split()))
    batiments(n, r, k, villes)
