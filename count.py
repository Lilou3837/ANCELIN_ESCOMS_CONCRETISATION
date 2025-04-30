from cards import *

point=0
ressource ={'r' : 0,
            'b' : 0, 
            'v' : 0, 
            'j' : 0, 
            'n' : 0, 
            'i' : 0, 
            'p' : 0, 
            'chi' : 0, 
            'cha' : 0}


def sanctuaire_ressource(sanctuaire):
    """
    comptage des ressources des sanctuaires
    sanctuaire : list de int (valeur des cartes sanctuaires)
    """
    global T, ressource
    for i in range(len(sanctuaire)):
        carte = T[sanctuaire[i]]
        couleur = carte.couleur
        if couleur != "" :
            ressource[couleur] += 1
        ressource['n'] += carte.nuit
        ressource['i'] += carte.indice
        for m in carte.merveille:
            ressource[m] += carte.merveille[m]


def region(region):
    """
    comptage ressources et points des cartes regions
    region : list de int (valeur des cartes regions)
    """
    global T, ressource, point
    for i in range(len(region)-1,-1,-1):
        carte = T[region[i]]
        couleur = carte.couleur
        ressource[couleur] += 1
        ressource['n'] += carte.nuit
        ressource['i'] += carte.indice
        for m in carte.merveille:
            ressource[m] += carte.merveille[m]

        ens = min([ressource['r'], ressource['b'], ressource['j'], ressource['v']])
        condition = True
        for c in carte.condition:
            if ressource[c] < carte.condition[c] :
                condition = False
                break
        if condition : 
            for s in carte.score:
                if s == 'a' :
                    point += carte.score[s]
                elif s == 'e' :
                    point += carte.score[s] * ens
                else :
                    point += carte.score[s] * ressource[s]

def sanctuaire_point(sanctuaire):
    """
    comptage ressources et points des cartes sanctuaires
    region : list de int (valeur des cartes sanctuaires)
    """
    global T, ressource, point
    for i in range(len(sanctuaire)):
        carte = T[sanctuaire[i]]
        ens = min([ressource['r'], ressource['b'], ressource['j'], ressource['v']])
        for s in carte.score:
                if s == 'e' :
                    point += carte.score[s] * ens
                else :
                    point += carte.score[s] * ressource[s]


def comptage(region, sanctuaire):
    sanctuaire_ressource(sanctuaire)
    region(region)
    sanctuaire_point(sanctuaire)
    return ressource