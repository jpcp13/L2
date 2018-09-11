#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#SELVARAJAH DINUSAN
#SABABADY KAMALA

message = raw_input("\nQuelle est le message?\n").decode("utf-8").lower()
cle = input("\nQuelle est la clé?\n")

# Dans la variable lettres, on met les 26 lettres de l'alphabet.
lettres = "abcdefghijklmnopqrstuvwxyz"
lettres = lettres.decode("utf-8")

# On créé une variable crypted qui va recevoir notre message crypté.
crypted = ""
 
# On lance une boucle pour aller chercher chaque caractère dans notre message.
for car in message:
	# On lance une condition.
	if car in lettres :
		# On va chercher l'index du caractère dans la variable "lettres" . En Python "a" dans "lettres" est le numéro 0,"b" est le numéro 1, "c" le numéro 2, etc.
		num = lettres.find(car)
		# On ajoute le chiffre de la clé au numéro du caractère que l'on est en train de traiter.
		# Cette somme correspond au numéro de la lettre qui doit remplacer ce caractère!
		num += cle
		# Si la somme est plus grande que la longueur de "lettres", ça ne marchera pas, parce ce nombre ne correspondra à aucun caractère dans "lettres"!
		# Donc, dans ce cas là, on soustrait le nombre de caractères dans "lettres" pour revenir au début de la liste, en cas de dépassement.
		if num >= len(lettres):
			num = num - len(lettres)
		# Et finalement, on ajoute le caractère qui sert de remplacement dans notre variable "crypted"
		crypted += lettres[num]
	# Si le caractère dans le message n'existe pas dans "lettres" (par exemple la ponctuation), on l'ajoute simplement dans "crypted".
	else:
		crypted += car

print "\n*** Voici le message crypté ***"
print crypted + "\n"
