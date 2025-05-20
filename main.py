from LectureInstance import *
from Selection import Selection
from Recherche import RecherchePresqueGlouton
from copy import deepcopy



def FonctionMere(instance: str):
    R,S = Lecture(instance)

    R0 = deepcopy(R)
    S0 = deepcopy(S)
    NomFichier = f"Competitions_Results/{instance[:-4]}_result.txt"

    R,S = Selection(R,S)
    Max, temps = RecherchePresqueGlouton(R,S)
    Ecriture('Competitions_Results/competition_02_result.txt', (R0, S0), (Max, temps))

FonctionMere('Competitions/competition_02.txt')