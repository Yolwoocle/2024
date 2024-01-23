from typing import List


def somme_compatible(v: int, n: int, villes: List[List[str]], r: int, requetes: List[List[str]]):
    """
    :param v: le nombre de villes
    :param n: le nombre de dieux
    :param villes: pour chaque dieu, une chaîne de caractère binaire. Si le dieu veut le contrôle de la ville $i$, un `1` est présent dans la chaîne de caractère à la position $i$, un `0` sinon
    :param r: le nombre de requêtes
    :param requetes: pour chaque requête, une chaîne de caractère binaire représentant un sous-ensemble de villes. Si la ville $i$ est présente dans le sous-ensemble, alors un `1` est présent dans la chaîne de caractère à la position $i$, un `0` sinon
    """
    # TODO Initialisez `X`, `Y` et `Z` à 0. Pour chaque requête $S$ : appelez
    # la fonction `Hashe` avec toutes les valeurs de $R(S, \Delta)$, pour
    # toutes les valeurs de $\Delta$ entre $1$ et $N - 1$, puis affichez, sur
    # une ligne et séparés par un espace, les nouvelles valeurs de `X`, `Y` et
    # `Z`.
    x = 0
    y = 0
    z = 0
    def hashe(valeur):
        nonlocal x, y, z
        x = (x*valeur + z + 37) % 1000_000_007
        y = (x*13 + 36*y + 257) % 1000_000_009
        z = (y*valeur + 4*valeur + x*x + 7) % 998_244_353
    
    desirs = dict()
    for dieu in range(n):
        desir = villes[dieu]
        desirs[dieu] = set(i_ville for i_ville in range(v) if desir[i_ville] == "1")
    
    def est_compatible(requete, dieu1, dieu2):
        conflits = 0
        for ville in requete:
            if (ville in desirs[dieu1]) and (ville in desirs[dieu2]):
                conflits += 1
        return conflits % 2 == 0
    
    # # Étant donné un sous-ensemble S de villes dites abandonnées, et un entier
    # Δ, on appelle alors R(S, Δ) le nombre de X tels que les dieux X et X ⊕ Δ 
    # sont compatibles, où ⊕ représente l'opération "ou exclusif" au niveau du bit.
    def R(s, delta):
        # nb de dieux x, tq x et x ⊕ delta sont compatibles
        # compatible si le nombre de villes contestées par les deux dieux dans ce sous-ensemble est pair.
        nb = 0
        for dieu in range(n):
            xor = dieu ^ delta
            if est_compatible(s, dieu, xor):
                nb += 1
        return nb 

    for i in range(r):
        req = requetes[i]
        ens_req = set(i_ville for i_ville in range(v) if req[i_ville] == "1")
        for delta in range(1, n):
            r = R(ens_req, delta)
            hashe(r)
        print(x, y, z)

if __name__ == "__main__":
    v = int(input())
    n = int(input())
    villes = [list(input()) for _ in range(n)]
    r = int(input())
    requetes = [list(input()) for _ in range(r)]
    somme_compatible(v, n, villes, r, requetes)
