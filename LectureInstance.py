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


def Ecriture(fichierEcriture: str, instance: tuple, resultat: tuple):
    """
    ficherEcriture : str, chemin du fichier
    instance : tuple de 2 list avec régions et sanctuaires
    resultat : tuple avec list maximum (regions, sanctuaires, score, ressourses) puis temps de calcul
    """
    fichier = open(fichierEcriture, "a")

    fichier.write("Instance : "+str(len(instance[0]))+"_"+str(len(instance[1]))+"\n"   )
    fichier.write("     Temps de resolution : "+str(resultat[1])+" secondes\n" )
    fichier.write("     Resultat :"+str(resultat[0])+"\n\n" )

    fichier.close()



#Ecriture("BigHistory.txt",    ([3,5,42],[101,105,112]),      ([(3,8,9), (108,111,112), 78, {'r' : 1, 'k' : 5}], 1.5))

#print(Lecture('15_9.txt'))




































