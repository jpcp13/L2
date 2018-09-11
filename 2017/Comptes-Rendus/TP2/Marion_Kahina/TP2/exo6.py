from math import *
from time import *
import numpy as np
import matplotlib.pyplot as plt

I = pi/6 + sqrt(3)/4

def f(x) :
	return sqrt(1-x**2)

n = 100
a = -0.5
b = 0.5
cmpt = 0

#petit a)

teta = np.linspace(0, 2*np.pi, 100)


x = np.cos(teta)
y = np.sin(teta)

plt.plot(x, y)
plt.grid()
plt.savefig('CercleExo6(0).png')

#petit b) sur [0;1]

for i in range(n) :
	xpoint = 2*np.random.rand()
	ypoint = 2*np.random.rand()

	if (xpoint**2 + ypoint**2) < 1 :
		plt.scatter(xpoint, ypoint, color='blue', marker='.')
		cmpt = cmpt + 1
	else :
		plt.scatter(xpoint, ypoint, color='yellow', marker='.')

plt.xlim(-0.25,1.25)
plt.ylim(-0.25,1.25)
plt.savefig('CercleExo6(1).png')

#petit b) sur [-1;1]
cmpt = 0

for i in range(n) :
	xpoint = 2*np.random.rand() - 1
	ypoint = 2*np.random.rand() - 1

	if (xpoint**2 + ypoint**2) < 1 :
		plt.scatter(xpoint, ypoint, color='blue', marker='.')
		cmpt = cmpt + 1
	else :
		plt.scatter(xpoint, ypoint, color='yellow', marker='.')

plt.xlim(-1.25,1.25)
plt.ylim(-1.25,1.25)
plt.savefig('CercleExo6(2).png')

#petit c)
n=1000
cmpt = 0

for i in range(n) :
	xpoint = 2*np.random.rand() - 1
	ypoint = 2*np.random.rand() - 1

	if (xpoint**2 + ypoint**2) < 1 :
		plt.scatter(xpoint, ypoint, color='red', marker='.')
		cmpt = cmpt + 1
	else :
		plt.scatter(xpoint, ypoint, color='green', marker='.')

plt.xlim(-1.25,1.25)
plt.ylim(-1.25,1.25)
plt.savefig('CercleExo6(3).png')


#petit d)
INT = 0
EXT = 0
k = clock()


Sapprox = (4.0*cmpt) / n
erreur = abs( Sapprox - pi )
temps = clock() - k

def Monte_Carlo(n):

	t = clock()

	x = np.cos(teta)
	y = np.sin(teta)

	cmpt = 0

	for i in range(n) :
		xpoint = 2*np.random.rand() - 1
		ypoint = 2*np.random.rand() - 1

		if (xpoint**2 + ypoint**2) < 1 :
			 cmpt = cmpt + 1
	
	surface = (cmpt/float(n)*4)	
	temps = clock() - t
	erreur = abs( Sapprox - pi )

	return temps, surface, erreur


# le temps de calcul de l'integrale
T = []
G = []
Q = []
AUX = []
n=1000000
aux = 10
while aux <= n:
	q, r, g = Monte_Carlo(aux)
	T.append(aux)
    	G.append(g)
    	Q.append(q)
	AUX.append(aux)
    	aux = aux*10

print('{0:10s}|{1:10s}|{2:10s}'.format('n','erreur','temps'))
print('--------------------------------')

for x in T:

    temps, S, erreur = Monte_Carlo(x)
    print('{0:10d}|{1:g}|{2:g}'.format(x, erreur, temps))

#petit g)

def monte_carlo_2(N):
	X = np.random.uniform(-1,1,N)
	Y = np.random.uniform(-1,1,N)
	Z = np.random.uniform(-1,1,N)
	I = 0
	for i in range(N):
		if (X[i]**2+Y[i]**2+Z[i]**2)<=1:
			I+=1
	return m
