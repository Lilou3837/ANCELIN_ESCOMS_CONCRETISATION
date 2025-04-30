from count import comptage, point, ressource
from cards import * 
from LectureInstance import *
from time import *


R,S=Lecture('test.txt')

#Score=comptage(R,S)

#print(Score)

from itertools import permutations, combinations

maximum = [42,42,0]
start = perf_counter()
"""
for re in permutations(R,8):
    if perf_counter() - start >= 59.75: break
    couples_ordonnais = 0
    for i in range(1,len(re)):
        if re[i]>re[i-1] : couples_ordonnais += 1

    for san in combinations(S,couples_ordonnais):
        pts = comptage(re,san)
        if pts > maximum[2]:
            maximum = [re, san, pts]
"""        

end = perf_counter()

print(maximum, end - start)


l=[1,2,3,4,5,6]
for e in permutations(l,3):
    print(e)























