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
    resultat : tuple avec list maximum (regions, sanctuaires, score) puis temps de calcul
    """
    with open(fichierEcriture, "w") as fichier:
        fichier.write("Instance : "+str(len(instance[0]))+"_"+str(len(instance[1]))+"\n"   )
        fichier.write("     Cartes : "+str(instance[0])+" "+str(instance[1])+"\n"   )
        #fichier.write("     Temps de resolution : "+str(resultat[1])+" secondes\n" )
        fichier.write("     Score :"+str(resultat[0][2])+"\n" )
        fichier.write("     Regions :"+str(resultat[0][0])+"\n" )
        fichier.write("     Sanctuaires :"+str(resultat[0][1])+"\n\n" )
