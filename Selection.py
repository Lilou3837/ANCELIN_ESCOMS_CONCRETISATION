from cards import *
from LectureInstance import *

def Selection(chemin :str):
    """
    chemin : instance
    """
    global T
    R,S=Lecture(chemin)
    cartes = R+S
    scores=[ cartes, [0 for i in range(len(cartes))] ]
    print(scores)
    for i in range(len(cartes)) :
        carte_cond = T[scores[0][i]]
        if "a" not in carte_cond.score.keys():
            for c in carte_cond.score : 
                for j in range(len(cartes)) : 
                    carte_sc = T[scores[0][j]]
                    if c in ["r","j","b","v"]:
                        if carte_sc.couleur == c : 
                            scores[1][j] += 1
                    elif c=='n':
                        if carte_sc.nuit == 1 :
                            scores[1][j] +=1
                    elif c=='i':
                        if carte_sc.indice == 1 :
                            scores[1][j] +=1
                    elif c in ["p", "chi", "cha"] : 
                        for m in carte_sc.merveille:
                            if m==c : 
                                scores[1][j] +=1
    print(scores)

Selection("test.txt")