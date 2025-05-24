from count import comptage
from itertools import permutations,combinations # Merci à itertools de nous permettre d'éviter de programmer ces 
                                                # fonctions horribles

def RecherchePresqueGlouton(R, S):
    """
    Prend une instance et recherche de manière presque gloutonne la meilleure solution de 8 régions et 7 sactuaires 
    """
    maximum=[42,42,0]
    nbSancRequis = 5 # On oblige au moins 5 couples ordonnés vu qu'on a vu qu'en dessous c'était vraiment pas ouf
    combi_sanctu=[tuple(combinations(S,i)) for i in range(nbSancRequis,8)]
    permu_region=permutations(R,8)
    tour=1
    for re in permu_region:

        couples_ordonnais = 0
        for i in range(1,8):
            if re[i]>re[i-1] : couples_ordonnais += 1
        if couples_ordonnais>=nbSancRequis:
            for san in combi_sanctu[couples_ordonnais-nbSancRequis]:
                tour+=1
                if tour%2==0:
                    pts = comptage(re,san)
                    if pts > maximum[2]:
                        maximum = [re, san, pts]
    return maximum
