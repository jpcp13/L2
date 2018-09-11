#Chargement de la librairie pandas
import pandas as pd


# Creation d'un tableau dataFrame

#Donnees brutes

data = {"state": ["Ohio", "Ohio", "Ohio","Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9]}


# Conversion en DataFrame

frame=pd.DataFrame(data, columns=["year", "state","pop"], 
                   index=["one", "two", "three", "four", "five"])

#Affichage du tableau

print(frame)