from Partie_1 import *

#Commande pour importer le fichier tableau.txt (de type dataFrame)

df = pd.read_table("tableau.txt",sep = '\t',header = 0)


#Commande pour acceder a une colonne(variable) du tableau

print(frame.state)

#ou (autre syntaxe)

#print(frame['state'])


#Commande pour acceder a un ensemble de colonnes

print(frame[['year','state']])


print(frame['pop'].describe())
