from typing import List

def afficher_midgard_debug(villes: List[str], serp_pos: int, serp_sens: int, ):
    v = villes[:]
    v = v[:serp_pos] + [">" if serp_sens == 1 else "<"] + v[serp_pos:]
    print(" ".join(v))
    
def afficher_midgard(villes: List[str], serp_pos: int, serp_sens: int):
    ville_queue = serp_pos if serp_sens == 1 else (serp_pos - 1) % len(villes)
    for i in range(len(villes)):
        print(villes[(ville_queue + serp_sens*i) % len(villes)])

def situation_finale(n_villes: int, n_annees: int, villes: List[str], actions: List[str]) -> None:
    """
    :param n: le nombre de villes autour de Midgard
    :param m: le nombre d'années avant le Ragnarök
    :param villes: le nom des villes autour de Midgard, en partant de la queue de Jörmungandr

    :param actions: la liste des actions prochaines de Jörmungandr
    
    Afficher, sur une ligne par ville, la liste des villes qui seront
    rencontrées lors du Ragnarök, dans l'ordre, en partant de la queue de
    Jörmungandr jusqu'à sa tête.
    """
    serp_pos = 0 # Entre la ville 0 et -1
    serp_sens = 1 # 1 ou -1
    serp_estomac = []
    # print("*", end=" ")
    # afficher_midgard_debug(villes, serp_pos, serp_sens)
    for a in actions:
        if a == "A":
            serp_pos = (serp_pos + serp_sens) % len(villes)
        elif a == "M":
            ville_visee = serp_pos if (serp_sens == 1) else (serp_pos-1) % len(villes)
            ville = villes.pop(ville_visee)
            serp_estomac.append(ville)
            if serp_sens == -1 and ville_visee < serp_pos:
                serp_pos = (serp_pos - 1) % len(villes)
        elif a == "R":
            serp_sens *= -1
        elif a == "C":
            ville = serp_estomac.pop()
            villes.insert(serp_pos, ville)
            if serp_sens == -1:
                serp_pos = (serp_pos + 1) % len(villes)
        # print(a, end=" ")
        # afficher_midgard_debug(villes, serp_pos, serp_sens)
    afficher_midgard(villes, serp_pos, serp_sens)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    villes = [input() for _ in range(n)]
    actions = list(input())
    situation_finale(n, m, villes, actions)
