from time import perf_counter
from count import comptage
from LectureInstance import *
from itertools import permutations,combinations

#à supp plus tard
start = perf_counter()

def RechercheGlouton(chemin: str):
    """
    Prend une instance et recherche de manière gloutonne la solution optimale pendant 1 min (?)
    """
    R,S=Lecture(chemin)

    maximum=[42,42,0]
    combi_sanctu=[combinations(S,i) for i in range(0,8)]
    permu_region=permutations(R,8)

    for re in permu_region:
        if perf_counter() - start >= 12.05: break
        couples_ordonnais = 0
        for i in range(1,8):
            if re[i]>re[i-1] : couples_ordonnais += 1
        if couples_ordonnais>4:
            for san in combi_sanctu[couples_ordonnais]:
                pts = comptage(re,san)
                if pts > maximum[2]:
                    maximum = [re, san, pts]
    return maximum, perf_counter()-start


print(RechercheGlouton('test.txt'))











