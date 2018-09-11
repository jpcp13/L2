#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#SELVARAJAH DINUSAN
#SABABADY KAMALA

message = raw_input("\nQuelle est le message crypté ?\n").decode("utf-8").lower()
cle = input("\nQuelle est la clé?\n")

#Il faut les mêmes lettres de l'alphabet pour avoir notre message decrypté.
lettres = "abcdefghijklmnopqrstuvwxyz"
lettres = lettres.decode("utf-8")

# On créé une variable decrypted qui va recevoir notre message decrypté.
decrypted = ""
 

for car in message:
	if car in lettres:
		num = lettres.find(car)
		# La différence c'est que ici que on soustraie, au lieu d'additionner.
		# Donc on recule dans "lettres" désormais pour revenir à la lettre originale.
		num -= cle
 
# À l'inverse du prg précédent, si la soustraction est inférieure à zéro, on ne trouvera pas la lettre originale dans "lettres"! donc, si le cas se présente, on additionne le nombre de caractères au total dans lettres.
		if num < 0 :
			num = num + len(lettres)
 
		decrypted += lettres[num]
	else:
		decrypted += car
 

print "\n*** Voici le message décrypté ***"
print  decrypted + "\n"
