import numpy as np
import matplotlib.pyplot as plt

def is_prim(n):
	
	for i in range(2,n-1):
		if(n % i == 0):
			return False
		 
	return True

#Liste nombres premiers inferieur a 1000
def primes(n):
	X = []
	
	for i in range(2,n):
		if  (is_prim(i) == True):
			X.append(i)
	return X

X = primes(1000)



# Enregistrer liste dans un fichier txt

cpt = 0
with open("primes.txt", "w") as fichier:
	for p in X:
		cpt+=1
		if cpt%10 !=0:
			fichier.write("{0:4}". format(p))
		else:
			fichier.write("{0:4}\n". format(p))

#Nombre d'entiers premiers inferieur a n


def pi(n):
	X = primes(n)
	return len(X)


import math
def g(n):
	m = math.log(n)
	return n/m


N = 100

nn = range(2, N)
pi_n = [pi(n) for n in nn]
g_n  = [g(n) for n in nn]
plt.plot(nn, pi_n, 'r-',nn , g_n,'b')
plt.grid('on')
plt.axis('equal')
plt.show()

#Table
def save(string,n):
	with open ('tableau_{:s}.txt'.format(string),'w') as fichier :
		print('{O:6}|{1:7}|{2:10}'.format('   n  ',' pi(n) ',' n*log(n) '))
		fichier.write('{O:6}|{1:7}|{2:10}'.format('   n  ',' pi(n) ',' n*log(n) '))
		for j in range(1, n+1):
			pi_n = pi(n)
			g_n = g(n)
			print('{O:6}|{1:7}|{2:10}'.format(10**j, pi_n, g_n))
			fichier.write('{0:9e} | {1:e} | {2:d}\n'. format(10**j, pi_n, g_n))
	print('') 
save('thpremier',6)
"""
with open ('tableau_thpremier.txt','w') as fichier :
	print('{0:10}|{0:10}|{0:10}'.format('    n     ','   pi(n)  ',' n*log(n) '))
	fichier.write('{0:10}|{0:10}|{0:10}'.format('    n     ','   pi(n)  ',' n*log(n) '))
"""

