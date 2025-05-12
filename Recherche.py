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
    #S=[i for i in range(101, 146)]
    q=0
    s=0
    maximum=[42,42,0,42]
    combi_sanctu=[tuple(combinations(S,i)) for i in range(5,8)]
    permu_region=permutations(R,8)

    for re in permu_region:
        s+=1
        #if perf_counter() - start >= 12.05: break
        couples_ordonnais = 0
        for i in range(1,8):
            if re[i]>re[i-1] : couples_ordonnais += 1
        if couples_ordonnais>=5:
            for san in combi_sanctu[couples_ordonnais-5]:
                q+=1
                pts, ress = comptage(re,san)
                if pts > maximum[2]:
                    maximum = [re, san, pts, ress]
    return maximum, perf_counter()-start,s,q


print(RechercheGlouton('test.txt'))











