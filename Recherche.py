from count import comptage
from time import perf_counter
from itertools import permutations,combinations

def RecherchePresqueGlouton(R, S):
    """
    Prend une instance et recherche de manière gloutonne la solution optimale pendant 1 min (?)
    """
    maximum=[42,42,0]
    nbSancRequis = 5
    start = perf_counter()
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
                if tour%2!=0:
                    pts = comptage(re,san)
                    if pts > maximum[2]:
                        maximum = [re, san, pts]
                """if perf_counter() - start >= 159.7:
                    timeh = perf_counter()-start
                    return maximum, timeh"""
    timeh = perf_counter()-start
    return maximum, timeh
