from cards import *
from LectureInstance import *

def Selection(chemin :str):
    """
    chemin : instance
    """
    global T

    R,S=Lecture(chemin)
    cartes = R+S
    scores=[0 for i in range(len(cartes))]

    ressources ={'r' : 0,
            'b' : 0, 
            'v' : 0, 
            'j' : 0, 
            'n' : 0, 
            'i' : 0, 
            'p' : 0, 
            'chi' : 0, 
            'cha' : 0}

    for i in range(len(cartes)):                ### COLLECTE RESSOURSES
        carte = T[cartes[i]]
        couleur = carte.couleur
        if couleur != "" :
            ressources[couleur] += 1
        ressources['n'] += carte.nuit
        ressources['i'] += carte.indice
        for m in carte.merveille:
            ressources[m] += carte.merveille[m]
    print(ressources)


    ### verif des conditions et mise à 0 ou à 1 du "score"


    for i in range(len(cartes)) :
        carte_cond = T[cartes[i]] # Cartes qui donne des "conditions" que les autres doivent vérifier
        if ("a" or "e") not in carte_cond.score:
            for c in carte_cond.score :                         ### CONTION SUR SCORE - max 2 éléments
                for j in range(len(cartes)) : # Les autres
                    carte_candidate = T[cartes[j]]
                    if carte_candidate.couleur == c : 
                        scores[j] += 1
                        scores[i] += 1
                    elif c=='n' and carte_candidate.nuit == 1:
                        scores[j] +=1
                        scores[i] += 1
                    elif c=='i' and carte_candidate.indice == 1:
                        scores[j] +=1
                        scores[i] += 1
                    elif c in ["p", "chi", "cha"] : 
                        for m in carte_candidate.merveille:
                            if m==c : 
                                scores[j] +=1
                                scores[i] += 1
                
    print(scores)

Selection("test.txt")