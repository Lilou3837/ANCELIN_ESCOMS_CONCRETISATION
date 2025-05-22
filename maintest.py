from time import perf_counter
start=perf_counter()
from LectureInstance import *
from SelectionTest import Selection
from Recherche import RecherchePresqueGlouton
from random import uniform



def FonctionMere(instance: str):
    R,S = Lecture(instance)

    R0 = [k for k in R]
    S0 = [k for k in S]
    NomFichier = f"{instance[13:-4]}_result.txt"
    m=[42,42,0]
    new=m
    b=uniform(6,10)
    print(b)
    while perf_counter()-start <59 : 
        #nb = uniform(0,10)
        I=[1,10]
        R1=[k for k in R0]#deepcopy(R0)
        S1=[k for k in S0]
        R,S = Selection(R1,S1,I)
        
        Max, temps = RecherchePresqueGlouton(R,S)
        if m!=new :
            new=m
            print('new :',m[2])
        if Max[2]>m[2] : m=[k for k in Max]
    
    Ecriture(f'Competitions_Results/{NomFichier}', (R0, S0), (m, temps))
    print( perf_counter()-start)


FonctionMere('Competitions/competition_15.txt')