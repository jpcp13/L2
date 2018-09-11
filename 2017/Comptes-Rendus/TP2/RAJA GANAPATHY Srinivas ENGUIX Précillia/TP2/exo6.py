from math import sqrt
import math
from time import clock
from module import *
import numpy as np
import matplotlib.pyplot as plt



#6A.
theta = np.linspace(0, 2*np.pi, 40)

x = np.cos(theta)
y = np.sin(theta)
plt.clf()
plt.plot(x, y)
plt.axis("equal")
plt.grid()
plt.savefig('fig1.png')

#B

T1 = np.random.uniform(-1, 1, 10)
print("la valeur pour l'intervalle [0,1]", T1)

T2 = np.random.uniform(-1, 1, 10)
print("la valeur pour l'intervalle[-1,1]", T2)

#C
N=1000
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)

SS, VV, DD,TT = [], [], [], []

I = 0
E = 0

for i in range (N):

		if (x[i]**2 + y[i]**2) < 1:
			S = x[i]
			SS.append(S)
			V = y[i]
			VV.append(V)
			I += 1

		else:
			D = x[i]
			DD.append(D)
			T = y[i]
			TT.append(T)
			E += 1


plt.plot(SS, VV, '.r', DD, TT, '.g')
plt.axis("equal")
plt.grid()
#plt.show()
plt.savefig('fig4.png')

s = math.pi
t0 = clock()
m = ((I*4.0)/N)
k = abs(m-s)
t1 = clock()
t2 = t1 - t0

print('nombre de point a l interieur du cercle')
print 'I =', I
print('nombre de point a l exterieur du cercle')
print 'E =' , E
print('la surface :')
print(s)
print('approximation de la surface :')
print(m)
print('erreur commise')
print(k)
print('temps de calcul :')
print(t2)
print('\n')


#D
titre = 'METHODE DE MONTE CARLO'
entete = '{0:15s}|{1:15s}|{2:15s}'.format('n','erreur','temps')
tirets = '-'*50

with open ("montecarlo.txt", 'w') as fichier:
	fichier.write(titre + '\n')
	fichier.write('\n')
	fichier.write(entete + '\n')
	fichier.write(tirets + '\n')
	for i in range (1,7):
		t5 = clock()
		p = monte_carlo(10**(i))
		t6 = clock()
		k = math.pi
		S = abs(p-k)
		y = t6 - t5
		ligne = '{0:15d}|{1:15g}|{2:15g}'.format(10**(i), S, y)
		fichier.write(ligne+'\n')
		fichier.write('\n')


print('test de monte carlo 2 ')
print('\n')
print('{0:10}|{1:17}|{2:10}'.format('n','erreur','temps'))

for i in range(1,7):
	t5 = clock()
	p = monte_carlo2(10**(i))
	t6 = clock()
	k = (4/3)*math.pi
	S = abs(p-k)
	y = t6 - t5
	print('{0:10}|{1:13}|{2:10}'.format(10**(i), S, y))


titre = 'METHODE DE MONTE CARLO 2'
entete = '{0:15s}|{1:15s}|{2:15s}'.format('n','erreur','temps')
tirets = '-'*50

with open ("montecarlo2.txt", 'w') as fichier:
	fichier.write(titre + '\n')
	fichier.write('\n')
	fichier.write(entete+'\n')
	fichier.write(tirets+'\n')
	for i in range (1, 7):
		t5 = clock()
		p = monte_carlo2(10**(i))
		t6 = clock()
		k = (4/3)*math.pi
		S = abs(p-k)
		y = t6 - t5
		ligne = '{0:15d}|{1:15g}|{2:15g}'.format(10**(i), S, y)
		fichier.write(ligne+'\n')
		fichier.write('\n')


