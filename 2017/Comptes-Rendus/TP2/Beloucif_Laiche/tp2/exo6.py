from math import *
from time import *
from string import *
from pylab import *
from random import *
from tp2 import *

S = montecarlo(10000)
print S

print('      n | erreur  | temps (sec) ')
print('---------------------------------')
for i in range(1,7):
	n = 10**i
	tps1 = clock()
	S = montecarlo(10000)
	tps2 = clock()
	tps3 = tps2 - tps1
	E = abs(S - I)
	print(' {0}  | {1}   | {2}  '.format(n,E,tps3))


entete = '      n | erreur  | temps (sec) '
pointilles = '---------------------------------'


with open ('tableau6', 'w') as fichier:
	fichier.write(entete + '\n')
	fichier.write(pointilles + '\n')
	for i in range(1,7):
		n = 10**i
		tps1 = clock()
		S = montecarlo(10000)
		tps2 = clock()
		tps3 = tps2 - tps1
		E = abs(S - I)
		fichier.write(' {0}  | {1}   | {2}  \n'.format(n,E,tps3))

X,Y = [],[]
V,W = [],[]
I = 0 # compteur pour les points rouges
E = 0 # compteur pour les points verts

for i in range(1000):
	x = uniform(-1,1) #'uniform' genere des valeurs au hasard
	y = uniform(-1,1)
	if x*x + y*y <= 1: #module d'un point (x,y)
		X.append(x)
		Y.append(y)
		I += 1
	else:
		V.append(x)
		W.append(y)
		E += 1 
print I 
print E

teta = np.linspace(0, 2*np.pi, 100)

x = np.cos(teta)
y = np.sin(teta)
plt.plot(x, y)
plot(X, Y, 'ro', linewidth = 2)
plot(V, W, 'go', linewidth = 1)
axis("equal")

plt.grid()
plt.savefig('cercleexo6.png')

