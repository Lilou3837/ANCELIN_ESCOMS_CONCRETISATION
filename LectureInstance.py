def Lecture(chemin: str):
    """
    Lis une instance et renvoie les 2 tableaux de régions et de sanctuaires
    chemin : str, nom du fichier.txt
    """
    fichier = open(chemin, "r")
    chaine=fichier.read()
    TAB = chaine.split(' ')
    Region = []
    Sanctuaire = []
    for n in TAB:
        if int(n) < 90:
            Region.append(int(n))
        else:
            Sanctuaire.append(int(n))

    fichier.close()
    return Region, Sanctuaire


#print(Lecture('15_9.txt'))




































