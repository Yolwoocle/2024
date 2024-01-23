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
    for i in range(nb_mouv):
        m = max(villes[(i + j) % nb_villes] for j in range(k))
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
