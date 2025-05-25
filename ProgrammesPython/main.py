from time import perf_counter
from lecture_ecriture_instance import *
from selection import Selection
from recherche import RecherchePresqueGlouton
from random import choice

def OnPrendLesBest(SR,SS):
    """ 
    Fonction qui garde seulement les régions et sanctuaires qui ont permit d'atteindre des
    scores au dessus de la moyenne de tous les scores
    """
    moyenneScores = sum(SR)/len(SR)
    NewR = []
    NewS = []
    for score in SR:
        if score > moyenneScores:
            for carteR in SR[score]:
                if carteR not in NewR : NewR.append(carteR)
            for carteS in SS[score]:
                if carteS not in NewS : NewS.append(carteS)
    
    return NewR,NewS

def FonctionMere(instance: str):
    """ 
    instance : Chaine de caractere du fichier instance qui doit être examiné.
    Résultat écrit dans le dossier Results.
    """
    start=perf_counter()
    R,S, nbCarte= Lecture(instance)
    RInit = [k for k in R]
    SInit = [k for k in S]

    EmplacementResult = f"../Results/{instance[13:-4]}_{nbCarte}_result.txt"
    m=[42,42,0]
    new=m
    nb_tours=0
    limit = 0

    STOCK_REGIONS={}
    STOCK_SANCTUAIRES={}

    for limit in [6,9,12]:
        R0 = [k for k in R]
        S0 = [k for k in S]

        print("Cartes disponibles :",R,S)
        
        while perf_counter()-start < limit : 
            I=[1,10]
            R1=[k for k in R0]
            S1=[k for k in S0]
            R,S = Selection(R1,S1,I)

            Max = RecherchePresqueGlouton(R,S) 

            if Max[2] not in STOCK_REGIONS:
                STOCK_REGIONS[Max[2]]={}
            if Max[2] not in STOCK_SANCTUAIRES:
                STOCK_SANCTUAIRES[Max[2]]={}
            for carte in Max[0]:
                STOCK_REGIONS[Max[2]][carte] = 1 
            for carte in Max[1]:
                STOCK_SANCTUAIRES[Max[2]][carte] = 1
            nb_tours += 1

            if m!=new :
                new=m
                print('new :',m)

            if Max[2]>m[2] : m=[k for k in Max]

        
        R,S=OnPrendLesBest(STOCK_REGIONS,STOCK_SANCTUAIRES)
        if len(S)<7 : 
            while len(S)<7 :
                element = choice(S0)
                if element not in S : S.append(element)

    Ecriture(EmplacementResult, (RInit, SInit),m)
    print(perf_counter()-start)
    print("Meilleur score trouvé :",m)
    

FonctionMere('../Instances/competition_01.txt')

"""
- 1) Enregistrer votre fichier instance dans le répertoire Instances
-- 2) Remplacer 'votre_fichier' par le nom du fichier texte de votre instance dans la ligne de commande au dessus.
--- 3) Faîtes attention à bien être placé dans le repertoire ProgrammesPython pour éxecuter main.py
---- 4) Votre fichier résultat sera écrit dans le répertoire Results
"""