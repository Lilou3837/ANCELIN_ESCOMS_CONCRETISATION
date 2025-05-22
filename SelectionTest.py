from cards import *
from random import random

def CollecteRess(TAB):
    ressources ={'r' : 0,
            'b' : 0, 
            'v' : 0, 
            'j' : 0, 
            'n' : 0, 
            'i' : 0, 
            'p' : 0, 
            'chi' : 0, 
            'cha' : 0}

    for t in TAB: ### COLLECTE RESSOURSES
            carte = T[t]
            couleur = carte.couleur
            if couleur != "":
                ressources[couleur] += 1
            ressources['n'] += carte.nuit
            ressources['i'] += carte.indice
            for m in carte.merveille:
                ressources[m] += carte.merveille[m]
    return ressources


def ReductionSanctu(R, S, ns, ress, nb):

    if len(S) == ns: # Arrêt
        return R,S
    else:
        # Les régions bougent pas
        SCORES=[0 for i in range(len(S))]

        for r in R:
            reg = T[r]         # Régions qui donnent des "conditions" que les sanctuaires doivent vérifier
            if ("a" or "e") not in reg.score:
                for parqqch in reg.score :   ### SCORE par qqch - max 2 éléments
                    nb_cond=0
                    for c in reg.condition:
                        nb_cond += 1 #reg.condition[c]
                    for i in range(len(S)) : # Les sanctuaires
                        sanc = T[S[i]]
                        if sanc.couleur == parqqch : 
                            if nb_cond!=0 : SCORES[i] += reg.score[parqqch]*2.7*nb/nb_cond
                            else : SCORES[i] += reg.score[parqqch]+1.5*nb
                        elif parqqch=='n' and sanc.nuit == 1:
                            if nb_cond!=0 : SCORES[i] += reg.score[parqqch]*2.7*nb/nb_cond
                            else : SCORES[i] += reg.score[parqqch]+1.5*nb
                        elif parqqch=='i' and sanc.indice == 1:
                            if nb_cond!=0 : SCORES[i] += reg.score[parqqch]*2.7*nb/nb_cond
                            else : SCORES[i] += reg.score[parqqch]+1.5*nb
                        elif parqqch in ["p", "chi", "cha"] : 
                            for m in sanc.merveille:
                                if m==parqqch : 
                                    if nb_cond!=0 : SCORES[i] += reg.score[parqqch]*2.7*nb/nb_cond
                                    else : SCORES[i] += reg.score[parqqch] +1.5*nb
                for cond in reg.condition: ### CONDITION POUR SCORE  - max 3 éléments
                    for i in range(len(S)) : # Les sanctuaires
                        sanc = T[S[i]]
                        mervSanctu = sanc.merveille
                        if cond in mervSanctu:
                            if ress[cond]*10/len(R) + mervSanctu[cond] >= reg.condition[cond]:
                                SCORES[i]+=1*nb

        for i in range(len(S)):
            sanc = T[S[i]]
            for parqqch in sanc.score :
                if parqqch != "a" and parqqch != "e":
                    if ress[parqqch]*10/len(R) >= sanc.score[parqqch]:
                        SCORES[i] += sanc.score[parqqch]*nb
                elif parqqch == 'a': # Merci la 121
                    SCORES[i] += sanc.score[parqqch]*nb
                else: # parqqch == 'e'
                    ens = min([ress['r']*10/len(R), ress['b']*10/len(R), ress['j']*10/len(R), ress['v']*10/len(R)])
                    SCORES[i] += sanc.score[parqqch] * ens*nb
        
        S.pop(SCORES.index(min(SCORES)))
        SCORES.pop(SCORES.index(min(SCORES)))

        return ReductionSanctu(R, S, ns, ress,nb)


def ReductionRegion(R, S, nr, ressS,nb):

    if len(R) == nr: # Arrêt
        return R,S
    else:
        # Les sanctuaires bougent pas
        SCORES=[0 for i in range(len(R))]
        ressR = CollecteRess(R)

        for s in S:
            sanc = T[s]         # Sanctuaires qui donnent des 'conditions' que les régions doivent vérifier
            if ("a" or "e") not in sanc.score:
                for parqqch in sanc.score :   ### SCORE par qqch - max 2 éléments
                    for i in range(len(R)) : # Les régions qui satisferont peut etre ce que demandent les sanctuaires pour leur score
                        reg = T[R[i]]
                        if reg.couleur == parqqch : 
                            SCORES[i] += sanc.score[parqqch]+1.5*nb
                        elif parqqch=='n' and reg.nuit == 1:
                            SCORES[i] += sanc.score[parqqch] +1.5*nb
                        elif parqqch=='i' and reg.indice == 1:
                            SCORES[i] += sanc.score[parqqch] + 1.5*nb
                        elif parqqch in ["p", "chi", "cha"] : 
                            for m in reg.merveille:
                                if m==parqqch : 
                                    SCORES[i] += sanc.score[parqqch] *nb
        for i in range(len(R)):
            reg = T[R[i]]         # Régions qui donnent des "conditions" que les autres doivent vérifier
            for parqqch in reg.score :
                nb_cond=0
                for c in reg.condition:
                    nb_cond += 1 #reg.condition[c] 
                if parqqch != "a" and parqqch != "e":
                    if ressS[parqqch]*7/len(S) + ressR[parqqch]*10/len(R) >= reg.score[parqqch]:
                        SCORES[i] += reg.score[parqqch]*nb
                elif parqqch == 'a':
                    if nb_cond!=0: SCORES[i] += reg.score[parqqch]*2.7*nb/nb_cond
                    else: SCORES[i] += reg.score[parqqch]+1.5*nb
                else: # parqqch == 'e'
                    ens = min([ressS['r']*7/len(S)+ressR['r']*10/len(R), 
                                ressS['b']*7/len(S)+ressR['b']*10/len(R), 
                                ressS['j']*7/len(S)+ressR['j']*10/len(R), 
                                ressS['v']*7/len(S)+ressR['v']*10/len(R)])
                    SCORES[i] += reg.score[parqqch] * ens*nb

            if reg.condition != {}:
                for cond in reg.condition: ### CONDITION POUR SCORE DES REGIONS  - max 3 éléments
                    for j in range(len(R)) : # Les régions
                        reg2 = T[R[j]]
                        mervRegion = reg2.merveille
                        if cond in mervRegion:
                            if ressR[cond]*10/len(R) + ressS[cond]*7/len(S) + mervRegion[cond] >= reg.condition[cond]:
                                SCORES[j]+=1*nb
            else:
                SCORES[i] += 1
        
        R.pop(SCORES.index(min(SCORES)))
        SCORES.pop(SCORES.index(min(SCORES)))

        return ReductionRegion(R, S, nr, ressS,nb)

def ReductionTotale(R, S, nr, ns,nb):
    if len(R)==nr and len(S)==ns:
        return R,S 
    elif len(R)==nr:
        RESS=CollecteRess(R)
        return ReductionSanctu(R,S,ns,RESS,nb)
    elif len(S)==ns:
        RESS=CollecteRess(S)
        return ReductionRegion(R,S,nr,RESS,nb)
    else:
        RESS=CollecteRess(S)
        R,S = ReductionRegion(R,S,len(R)-1,RESS,nb)
        RESS=CollecteRess(R)
        R,S = ReductionSanctu(R,S,len(S)-1,RESS,nb)
        return ReductionTotale(R,S,nr,ns,nb) 



def Selection(R, S):
    """
    R : Régions, S : Sanctuaires
    """

    # Conditions pour savoir vers quoi on va
    nb = random.random()
    if len(R) == 8 and len(S) >= 11:
        RESS=CollecteRess(R)
        return ReductionSanctu(R,S,10,RESS,nb)
    elif len(R) == 9 and len(S) >= 8:
        RESS=CollecteRess(R)
        return ReductionSanctu(R,S,7,RESS,nb)
    elif len(R) >=10 and len(S) ==7:
        RESS=CollecteRess(S)
        return ReductionRegion(R,S,9,RESS,nb)
    elif len(R) >= 9 and len(S) >= 8:
        return ReductionTotale(R,S,9,7)
    else: 
        return R,S # Part dans RechercheGlouton