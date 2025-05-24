def Lecture(chemin: str):
    """
    Lis une instance et renvoie les 2 tableaux de régions et de sanctuaires
    chemin : str, ../Instances/nom du fichier.txt
    """
    fichier = open(chemin, "r")
    chaine=fichier.read()
    TAB = chaine.split(' ')
    Region = []
    Sanctuaire = []
    for n in TAB:
        try : 
            if int(n) < 90:
                Region.append(int(n))
            else:
                Sanctuaire.append(int(n))
        except : pass

    fichier.close()
    return Region, Sanctuaire, f"{len(Region)}_{len(Sanctuaire)}"


def Ecriture(fichierEcriture: str, instance: tuple, resultat: list):
    """
    ficherEcriture : str, ../Results/nomfichier.txt
    instance : tuple de 2 list avec régions et sanctuaires
    resultat : list maximum (regions, sanctuaires, score)
    """
    with open(fichierEcriture, "w") as fichier:
        fichier.write("Instance : "+str(len(instance[0]))+"_"+str(len(instance[1]))+"\n"   )
        fichier.write("     Cartes : "+str(instance[0])+" "+str(instance[1])+"\n"   )
        fichier.write("     Score :"+str(resultat[2])+"\n" )
        fichier.write("     Regions :"+str(resultat[0])+"\n" )
        fichier.write("     Sanctuaires :"+str(resultat[1])+"\n\n" )