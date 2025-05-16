from time import perf_counter
from count import comptage
from cards import *
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
    nbSancRequis = 5
    combi_sanctu=[tuple(combinations(S,i)) for i in range(nbSancRequis,8)]
    permu_region=permutations(R,8)

    for re in permu_region:
        #s+=1
        #if perf_counter() - start >= 12.05: break

        couples_ordonnais = 0
        for i in range(1,8):
            if re[i]>re[i-1] : couples_ordonnais += 1

        if couples_ordonnais>=nbSancRequis:
            for san in combi_sanctu[couples_ordonnais-nbSancRequis]:
                #q+=1
                pts, ress = comptage(re,san)
                if pts > maximum[2]:
                    maximum = [re, san, pts, ress]
    #print(s,q)
    timeh = perf_counter()-start
    Ecriture("BigHistory.txt", (R,S), (maximum, timeh))
    return maximum, timeh
    
M,temps=RechercheGlouton('test.txt')

def AffichageReprCartes(M,temps):
    global T
    R = M[0]
    S = M[1]
    Pts = M[2]
    print('R : ')
    for r in R:
        print(T[r])

    print('S : ')
    for s in S:
        print(T[s])


AffichageReprCartes(M,temps)





