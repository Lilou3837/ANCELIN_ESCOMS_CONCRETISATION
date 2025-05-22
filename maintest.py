from time import perf_counter
start=perf_counter()
from LectureInstance import *
from SelectionCoef import Selection
from Recherche import RecherchePresqueGlouton
from copy import deepcopy



def FonctionMere(instance: str):
    R,S = Lecture(instance)

    R0 = deepcopy(R)
    S0 = deepcopy(S)
    NomFichier = f"{instance[13:-4]}_result.txt"
    m=[42,42,0]
    R,S = Selection(R,S)
    Max, temps = RecherchePresqueGlouton(R,S)
    Ecriture(f'Competitions_Results/{NomFichier}', (R0, S0), (Max, temps))


FonctionMere('Competitions/competition_15.txt')