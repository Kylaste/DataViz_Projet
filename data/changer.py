from pandas import DataFrame, read_csv
from datetime import datetime
import pandas as pd;
import csv;

        
# TGV: trajets par mois/par années
with open("regularite-mensuelle-tgv.csv", "r") as fichier:
    cr = csv.reader(fichier,delimiter=";");
    
    with open("trajets_tgv.csv", "w") as denFile:
        fileWriter = csv.writer(denFile, delimiter=",")
        fileWriter.writerow(
            ["source", "target", "weight", "annee", "mois", "commentaire"])
        compteur = 0
        moyenne = {}
        nbMois = {}
        for row in cr:
                if( compteur > 0):
                    datetime_object = datetime.strptime(row[0], '%Y-%m')
                    id = row[2]+"-"+row[3]+"-"+str(datetime_object.year)
                    
                    if(row[8] != ""):
                        if( id in moyenne):
                            moyenne[id] += float(row[8])
                            nbMois[id] += 1
                        else:
                            moyenne[id] = float(row[8])
                            nbMois[id] = 1
                    fileWriter.writerow([row[2], row[3], row[8], datetime_object.year, datetime_object.month, row[9]])
                compteur = compteur + 1
        for row in moyenne:
            
            info = row.split('-')
            moyenne[row] =round(float(moyenne[row])/nbMois[row], 2)
            fileWriter.writerow([info[0], info[1], moyenne[row], info[2], 0, ""])
            
# Intercité: index_villes
with open("regularite-mensuelle-intercites.csv", "r") as fichier:
    
    cr = csv.reader(fichier,delimiter=";");
    index_villes = []
    
    for row in cr:
        if( (row[3]!="Départ") & (row[4] != "Arrivée")):
            if( (row[3] in index_villes) is not True):
                index_villes.append(row[3])
            if( (row[4] in index_villes) is not True):
                index_villes.append(row[4])
            
        
    with open("index_intercites.csv", "w") as denFile:
        fileWriter = csv.writer(denFile, delimiter=",")
        fileWriter.writerow(
            ["id", "numericId"])
        compteur = 0
        for i in index_villes:
            fileWriter.writerow([i, compteur])
            compteur = compteur + 1

# Intercités: trajets
with open("regularite-mensuelle-intercites.csv", "r") as fichier:
    
    cr = csv.reader(fichier,delimiter=";");
        
    with open("trajets_intercites.csv", "w") as denFile:
        fileWriter = csv.writer(denFile, delimiter=",")
        fileWriter.writerow(
            ["source", "target", "weight"])
        compteur = 0
        for row in cr:
            if( compteur > 0):
                fileWriter.writerow([row[3], row[4], row[9]])
            compteur = compteur + 1
            


