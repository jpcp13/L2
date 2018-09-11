#!/usr/bin/env python
# -*- coding: utf-8 -*-

#SELVARAJAH Dinusan 

#SABABADY Kamala



# On demande le message à décrypté et la clé.

message = raw_input("\nQuel est le message à décrypté?\n").decode("utf-8").upper()

key = raw_input("\nQuelle est la clé?\n").decode("utf-8").upper()
 
lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
keyIndex = 0
 
decrypted = ""
 
for car in message:
	
	num = lettres.find(car)
	
	if num != -1:

		# Au lieu d'additionner, on soustraie

		# le nombre qui correspond à la lettre

		# de la clé.

		num -= lettres.find(key[keyIndex])

		num %= len(lettres)

		decrypted += lettres[num]

		keyIndex += 1

		if keyIndex == len(key):

			keyIndex = 0
 
	else:

		decrypted += car
 
print "\n *** Voici le message décrypté ***"

print decrypted + "\n"
