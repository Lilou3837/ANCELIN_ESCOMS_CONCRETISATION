from time import perf_counter
start = perf_counter()
from count import comptage
from LectureInstance import *



R,S=Lecture('test.txt')

#Score=comptage(R,S)
#print(Score)

from itertools import permutations, combinations

"""def permutliste(seq):
#Retourne la liste de toutes les permutations de la liste seq (non récursif).
    p = [seq]
    n = len(seq)
    for k in range(n-1):
        for i in range(len(p)):
            z = list(p[i])[:]
            for c in range(n-k-1):
                z.append(z.pop(k))
                p.append(z[:])
    return p"""


maximum = [42,42,0]
combi_sanctu=[combinations(S,i) for i in range(0,8)]

permu_region=permutations(R,8)


s=0
for re in permu_region:
    s+=1
    if perf_counter() - start >= 125.05: break

    couples_ordonnais = 0
    for i in range(1,8):
        if re[i]>re[i-1] : couples_ordonnais += 1
    #if couples_ordonnais>4:
    for san in combi_sanctu[couples_ordonnais]:
        
        pts = comptage(re,san)
        if pts > maximum[2]:
            maximum = [re, san, pts]

end = perf_counter()
print(maximum, end - start,s)



