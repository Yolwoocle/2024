from typing import List

### LISTE CIRCULAIRE

class Noeud:
    def __init__(self, val):
        self.val = val
        self.prec = None
        self.suiv = None

def vers_liste_circulaire(list: List):
    racine = Noeud(list[0])
    noeud_act = racine
    for i in range(1, len(list)):
        suiv = Noeud(list[i])
        noeud_act.suiv = suiv
        suiv.prec = noeud_act
        
        noeud_act = suiv
    noeud_act.suiv = racine
    racine.prec = noeud_act
    return racine

def afficher_liste_circulaire(racine: Noeud):
    noeud_act = racine
    i = 0
    while i == 0 or noeud_act != racine:
        print(f"<{noeud_act.prec.val if noeud_act.prec != None else 'None'} {noeud_act.val} {noeud_act.suiv.val if noeud_act.suiv != None else 'None'}>")
        noeud_act = noeud_act.suiv
        i += 1

def enlever(noeud):
    # [prec] [noeud] [suiv]
    suiv = noeud.suiv
    noeud.prec.suiv = noeud.suiv
    noeud.suiv.prec = noeud.prec
    
    noeud.suiv = None
    noeud.prec = None
    return noeud

def inserer_suiv(noeud, nouveau):
    # [noeud] [nouveau] [suiv]
    suiv = noeud.suiv
    noeud.suiv = nouveau
    nouveau.prec = noeud
    nouveau.suiv = suiv
    suiv.prec = nouveau

def inserer_prec(noeud, nouveau):
    # [prec] [nouveau] [noeud]
    prec = noeud.prec
    noeud.prec = nouveau
    nouveau.suiv = noeud
    nouveau.prec = prec
    prec.suiv = nouveau


######################################################

def afficher_midgard_debug(villes: List[str], serp_pos: int, serp_sens: int, ):
    v = villes[:]
    v = v[:serp_pos] + [">" if serp_sens == 1 else "<"] + v[serp_pos:]
    print(" ".join(v))

def afficher_midgard(racine: Noeud, sens: int):
    noeud_act = racine
    i = 0
    while i == 0 or noeud_act != racine:
        print(noeud_act.val)
        if sens == 1:
            noeud_act = noeud_act.suiv
        else:
            noeud_act = noeud_act.prec
        i += 1

def situation_finale(n_villes: int, n_annees: int, villes: Noeud, actions: List[str]) -> None:
    """
    :param n: le nombre de villes autour de Midgard
    :param m: le nombre d'années avant le Ragnarök
    :param villes: le nom des villes autour de Midgard, en partant de la queue de Jörmungandr

    :param actions: la liste des actions prochaines de Jörmungandr
    
    Afficher, sur une ligne par ville, la liste des villes qui seront
    rencontrées lors du Ragnarök, dans l'ordre, en partant de la queue de
    Jörmungandr jusqu'à sa tête.
    """
    serp_pos = villes # [serp_pos.prec] [serpent est ici] [serp_pos]
    serp_sens = 1 # 1 ou -1
    serp_estomac = []
    for a in actions:
        if a == "A":
            if serp_sens == 1:
                serp_pos = serp_pos.suiv
            else:
                serp_pos = serp_pos.prec
            
        elif a == "M":
            ville_visee  = serp_pos      if (serp_sens == 1) else serp_pos.prec
            serp_pos = serp_pos.suiv if (serp_sens == 1) else serp_pos
            
            ville_suppr = enlever(ville_visee)
            serp_estomac.append(ville_suppr)
        
        elif a == "R":
            serp_sens *= -1
        
        elif a == "C":
            ville = serp_estomac.pop()
            inserer_prec(serp_pos, ville)
            if serp_sens == 1:
                serp_pos = ville
                
    afficher_midgard(serp_pos if serp_sens == 1 else serp_pos.prec, serp_sens)

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    villes = [input() for _ in range(n)]
    actions = list(input())
    
    villes_circ = vers_liste_circulaire(villes)
    situation_finale(n, m, villes_circ, actions)
