from math import*
import numpy as np

def f(x):
	return x/log(x)

def fermat(n):
	return 2**2**n +1

def is_prime(p):

	card_div_p = 0
	d = 2

	while d <= floor(sqrt(p)):

		if (p % d == 0):
			card_div_p += 1

		d += 1


	if card_div_p == 0:
		return True


	else:
		return False

def primes(n):

	P = [] 

	for i in range(2,n+1):

		if is_prime(i):
			P.append(i)
	return P

def comparer_pi_f(n):

	for i in range (2,n):

		P = primes(i)
		card = len(P)
		y = f(i)

		I.append(i)
		PI_N.append(card) 
		Y.append(y)

	return I ,PI_N ,Y


Q = []
Q = primes(200)

R = len(Q) 

#c.


titre = 'Liste des nombres premiers inferieurs a 1000'
n=1000
cmpt = 1
i = 0
P = []
P= primes(n)

with open('prime.txt','w') as fichier:
	fichier.write(titre +'\n\n')

	for i in P:
		fichier.write(str(i)+' ')
		if cmpt %10 == 0:
			fichier.write('\n')
		cmpt += 1		


#d.

n=10000
P = []
PI_N = []
I = []

for i in range (2,n):

	

	P = primes(i)
	card = len(P)

	I.append(i)
	PI_N.append(card) 


# image n/log(n)

Y = []
for i in I:

	y = f(i)
	Y.append(y)

#affichage 

import matplotlib.pyplot as graphe 
graphe.plot(I, PI_N, 'r') #initialisation du graphe
graphe.plot(I, Y, 'g')
graphe.grid('on') #grille
graphe.savefig('fig1.png')


#e.


titre = 'Tableau comparant pi(n) et n/log(n)'
entete = '{0:10s}|{1:15s}|{2:15s}'.format('n','pi(n)','n/log(n)')
tirets = '-'*42
n = 10**6
aux = 10

with open('tableau.txt','w') as fichier:
	fichier.write(titre +'\n\n')
	fichier.write(entete+'\n')
	fichier.write(tirets+'\n')
	while aux <= n:

		y = f(aux)
		P = primes(aux)
		card = len(P) 


		ligne = '{0:10d}|{1:15g}|{2:15g}'.format(aux, card, y)
		print(ligne)
		fichier.write(ligne+'\n')
		aux = aux*10
	fichier.write('\n')





