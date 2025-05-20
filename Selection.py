from cards import *

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


def ReductionSanctu(R, S, ns, ress):

    if len(S) == ns: # Arrêt
        return R,S
    else:
        # Les régions bougent pas
        SCORES=[0 for i in range(len(S))]

        for r in R:
            reg = T[r]         # Régions qui donnent des "conditions" que les sanctuaires doivent vérifier
            if ("a" or "e") not in reg.score:
                for parqqch in reg.score :   ### SCORE par qqch - max 2 éléments
                    for i in range(len(S)) : # Les sanctuaires
                        sanc = T[S[i]]
                        if sanc.couleur == parqqch : 
                            SCORES[i] += reg.score[parqqch]
                        elif parqqch=='n' and sanc.nuit == 1:
                            SCORES[i] += reg.score[parqqch]
                        elif parqqch=='i' and sanc.indice == 1:
                            SCORES[i] += reg.score[parqqch]
                        elif parqqch in ["p", "chi", "cha"] : 
                            for m in sanc.merveille:
                                if m==parqqch : 
                                    SCORES[i] += reg.score[parqqch]
                for cond in reg.condition: ### CONDITION POUR SCORE  - max 3 éléments
                    for i in range(len(S)) : # Les sanctuaires
                        sanc = T[S[i]]
                        mervSanctu = sanc.merveille
                        if cond in mervSanctu:
                            if ress[cond]*10/len(R) + mervSanctu[cond] >= reg.condition[cond]:
                                SCORES[i] += 1 # C'est pi sur 2 ;)
        for i in range(len(S)):
            sanc = T[S[i]]
            for parqqch in sanc.score :
                if parqqch != "a" and parqqch != "e":
                    if ress[parqqch] >= sanc.score[parqqch]:
                        SCORES[i] += sanc.score[parqqch]
                elif parqqch == 'a': # Merci la 121
                    SCORES[i] += sanc.score[parqqch]
                else: # parqqch == 'e'
                    ens = min([ress['r'], ress['b'], ress['j'], ress['v']])
                    SCORES[i] += sanc.score[parqqch] * ens
        
        S.pop(SCORES.index(min(SCORES)))
        SCORES.pop(SCORES.index(min(SCORES)))

        return ReductionSanctu(R, S, ns, ress)


def ReductionRegion(R, S, nr, ressS):

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
                            SCORES[i] += sanc.score[parqqch]
                        elif parqqch=='n' and reg.nuit == 1:
                            SCORES[i] += sanc.score[parqqch]
                        elif parqqch=='i' and reg.indice == 1:
                            SCORES[i] += sanc.score[parqqch]
                        elif parqqch in ["p", "chi", "cha"] : 
                            for m in reg.merveille:
                                if m==parqqch : 
                                    SCORES[i] += sanc.score[parqqch]
        for i in range(len(R)):
            reg = T[R[i]]         # Régions qui donnent des "conditions" que les autres doivent vérifier
            for parqqch in reg.score :
                nb_cond=0
                for c in reg.condition:
                    nb_cond += reg.condition[c] 
                if parqqch != "a" and parqqch != "e":
                    if ressS[parqqch] + ressR[parqqch] >= reg.score[parqqch]:
                        SCORES[i] += reg.score[parqqch]
                elif parqqch == 'a':
                    SCORES[i] += reg.score[parqqch]
                else: # parqqch == 'e'
                    ens = min([ressS['r']+ressR['r'], 
                                ressS['b']+ressR['b'], 
                                ressS['j']+ressR['j'], 
                                ressS['v']+ressR['v']])
                    SCORES[i] += reg.score[parqqch] * ens

            if reg.condition != {}:
                for cond in reg.condition: ### CONDITION POUR SCORE DES REGIONS  - max 3 éléments
                    for j in range(len(R)) : # Les régions
                        reg2 = T[R[j]]
                        mervRegion = reg2.merveille
                        if cond in mervRegion:
                            if ressR[cond] + ressS[cond] + mervRegion[cond] >= reg.condition[cond]:
                                SCORES[j] += 1  # Coucou c'est moi e
            else:
                SCORES[i] += 1
        
        R.pop(SCORES.index(min(SCORES)))
        SCORES.pop(SCORES.index(min(SCORES)))

        return ReductionRegion(R, S, nr, ressS)

def ReductionTotale(R, S, nr, ns):
    if len(R)==nr and len(S)==ns:
        return R,S 
    elif len(R)==nr:
        RESS=CollecteRess(R)
        return ReductionSanctu(R,S,ns,RESS)
    elif len(S)==ns:
        RESS=CollecteRess(S)
        return ReductionRegion(R,S,nr,RESS)
    else:
        RESS=CollecteRess(S)
        R,S = ReductionRegion(R,S,len(R)-1,RESS)
        RESS=CollecteRess(R)
        R,S = ReductionSanctu(R,S,len(S)-1,RESS)
        return ReductionTotale(R,S,nr,ns) 



def Selection(R, S):
    """
    R : Régions, S : Sanctuaires
    """

    # Conditions pour savoir vers quoi on va

    if len(R) == 8 and len(S) >= 14:
        RESS=CollecteRess(R)
        return ReductionSanctu(R,S,13,RESS)
    elif len(R) == 9 and len(S) >= 10:
        RESS=CollecteRess(R)
        return ReductionSanctu(R,S,9,RESS)
    elif len(R) == 10 and len(S) >= 8:
        RESS=CollecteRess(R)
        return ReductionSanctu(R,S,7,RESS)

    elif len(R) >= 11 and len(S) == 7:
        RESS=CollecteRess(S)
        return ReductionRegion(R,S,10,RESS)

    elif len(R) >= 11 and len(S) >= 8:
        return ReductionTotale(R,S,10,7)
    else: 
        return R,S # Part dans RechercheGlouton