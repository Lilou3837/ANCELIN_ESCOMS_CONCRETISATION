from time import perf_counter
start=perf_counter()
from LectureInstance import *
from SelectionTest import Selection
from Recherche import RecherchePresqueGlouton
from random import uniform
from count import comptage

def OnPrendLesBest(SR,SS):
    moyenneScores = sum(SR)/len(SR)
    meilleurScore = max(SR)
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
    R,S = Lecture(instance)

    NomFichier = f"{instance[13:-4]}_result.txt"
    m=[42,42,0]
    new=m
    nb_tours=0
    limit = 0

    STOCK_REGIONS={}
    STOCK_SANCTUAIRES={}

    for _ in range(4):
        limit += 60/4
        R0 = [k for k in R]
        S0 = [k for k in S]

        print(R,S)
        
        while perf_counter()-start < limit : 
            I=[1,10]
            R1=[k for k in R0]
            S1=[k for k in S0]
            R,S = Selection(R1,S1,I)

            Max, temps = RecherchePresqueGlouton(R,S) 

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
        
        print('et c\'est reparti')

    #Ecriture(f'Competitions_Results/{NomFichier}', (R0, S0), (m, temps))
    print(perf_counter()-start)
    print(nb_tours)
    print(m)
    

FonctionMere('Competitions/competition_10.txt')



