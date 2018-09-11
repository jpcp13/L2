#!/usr/bin/env python
# -*- coding: utf-8 -*-

#SABABADY Kamala
#SELVARAJAH Dinusan

# Ici, on demande à l'utilisateur le message à crypté et la clé.
# on décode, et on met tout en majuscule.
message = raw_input("\nQuel est le message à crypté?\n").decode("utf-8").upper()

key = raw_input("\nQuelle est la clé?\n").decode("utf-8").upper()

# On retrouve notre alphabet dans "lettres"
lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# On créé une variable qui va nous permettre de passer au 
# travers de chaque caractère de la clé pour crypter notre message.
keyIndex = 0

# Le message crypté va se retrouver dans "crypted"
crypted = ""

# On lance une boucle qui passe au travers de chaque caractère du message
for car in message:

 # On va chercher le numéro associé au caractère dans notre liste de lettres.
 # A est en position 0, B en 1, C en 2, etc.
 	num = lettres.find(car)

 	#Si "num" est différent de - 1, ça veut dire qu'il est dans la liste de lettres.
 	if num != -1:

 		# On ajoute à num le nombre associé
 		# à la lettre correspondante dans notre clé.
 		num += lettres.find(key[keyIndex])
 		# On fait le modulo de lettres sur "num",
 		# au cas où num serait égal ou supérieur à 26.
 		num %= len(lettres)
 		# On peut maintenant utiliser "num"
 		# pour aller chercher une nouvelle lettre
 		# dans "lettres". C'est la lettre cryptée!
 		# On l'ajoute à crypted.
 		crypted += lettres[num]
 		# On ajoute +1 à KeyIndex pour passer
 		# à la lettre suivante dans notre clé.
 		keyIndex += 1
 		# Mais il ne faut pas que notre KeyIndex
 		# dépassse le nombre de caractère de notre clé,
 		# sinon on va travailler dans le vide.
 		# Alors on le remet à zéro quand il est
 		# égal au nombre de caractère total de la clé.
 		if keyIndex == len(key):
 			keyIndex = 0
 			# Si num == -1, ça veut dire que le caractère
 			# dans le message n'est pas dans notre liste.
 			# Dans ce cas, on ajoute directement le caractère
 			# sans le crypter. (Ce sera généralement de la ponctuation.)
	else:
 			crypted += car

print "\n *** Voici le message crypté ***"
print crypted + '\n'
