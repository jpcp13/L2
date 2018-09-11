import numpy as np
from time import *
from methodes import *

#a

theta =np.linspace(0,2*np.pi,100)
x=np.cos(theta)
y=np.sin(theta)

import matplotlib.pyplot as plt 
plt.plot(x, y)
plt.grid()
plt.show()

#b

liste=[]
liste_2=[]
for i in range(10):
	liste.append(np.random.rand())
#print('notre premiere liste est{0}'.liste)

for i in range(10):
	liste_2.append(2*np.random.rand()-1)
print(liste_2)

n = 10
a = -0.5
b = 0.5

#c

n=1000
cmpt = 0

for i in range(n) :
	xpoint = 2*np.random.rand() - 1
	ypoint = 2*np.random.rand() - 1

	if (xpoint**2 + ypoint**2) < 1 :
		plt.scatter(xpoint, ypoint, color='yellow', marker='.')
		cmpt = cmpt + 1
	else :
		plt.scatter(xpoint, ypoint, color='black', marker='.')

plt.xlim(-1.25,1.25)
plt.ylim(-1.25,1.25)
plt.savefig('figure2.png')

#d
INT = 0
EXT = 0
k = clock()


Sapprox = (4.0*cmpt) / n
erreur = abs( Sapprox - np.pi )
temps = clock() - k


# le temps de calcul de l'integrale
T = []
G = []
Q = []
AUX = []
n=1000
aux = 10
while aux <= n:
	q, r, g = monte_carlo(aux)
	T.append(aux)
    	G.append(g)
    	Q.append(q)
	AUX.append(aux)
    	aux = aux*10

print('{0:10s}|{1:10s}|{2:10s}'.format('n','erreur','temps'))
print('--------------------------------')

for x in T:

    temps, S, erreur = monte_carlo(x)
    print('{0:10d}|{1:g}|{2:g}'.format(x, erreur, temps))



