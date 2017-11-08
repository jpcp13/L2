import numpy as np
import matplotlib.pyplot as plt
import time
import math
import numpy.random as rd
from integration import *
from pylab import *

#a

theta = np.linspace(0, 2*pi, 40)

x = cos(theta)
y = sin(theta)
plt.plot(x, y)
plt.axis("equal")
plt.xlim(-3,3)

plt.grid()
plt.show()

S = math.pi # car le rayon vaut 1.

#b

T1 = rd.uniform(0, 1, 7)
print ("valeur pour l'intervalle[0,1]",T1)

print("\n")

T2 = rd.uniform(-1, 1, 7)
print ("valeur pour l'intervalle[-1,1]",T2)

#c



R1, R2 =[],[] # liste des valeurs dans le cercle (rouge)
V1, V2 =[],[] # liste des valeurs hors du cercle (vert)

I = 0   # Nombre de points interieur
E = 0	# Nombre de points exterieur

for i in range (1000):
	x = rd.uniform(-1, 1)
	y = rd.uniform(-1, 1)

	if (x*x + y*y) <= 1:
		R1.append(x)
		R2.append(y)
		I += 1
	else:
		V1.append(x)
		V2.append(y)
		E += 1

theta = np.linspace(0, 2*pi, 40)
x = cos(theta)
y = sin(theta)
plt.plot(x, y)
plt.plot(R1, R2, 'ro')
plt.plot(V1, V2, 'go')
plt.axis("equal")
plt.xlim(-3,3)
plt.grid()
plt.show()

print("\n")

#d 

print("Points rouges", I)
print("Points verts", E) 

erreur_commise = abs((4*float(I)/1000)-math.pi)
print("L'erreur commise vaut", erreur_commise)

#e

def Monte_CarloD(N):
	R1, R2 =[],[] # liste des valeurs dans le cercle (rouge)
	V1, V2 =[],[] # liste des valeurs hors du cercle (vert)

	I = 0   # Nombre de points interieur
	E = 0	# Nombre de points exterieur

	for i in range (N):
		x = rd.uniform(-1, 1)
		y = rd.uniform(-1, 1)

		if (x*x + y*y) <= 1:
			R1.append(x)
			R2.append(y)
			I += 1
		else:
			V1.append(x)
			V2.append(y)
			E += 1
	return 4*float(I)/N

#f


print('      N     erreur       temps')
print('------------------------------')
for i in range (1,7):
	N = 10**i
	t1 = time.clock()
	M = Monte_CarloD(N)
	delta =time.clock() - t1
	erreur = abs(float(M)-math.pi)
	print('{0:>7d}  {1:>.3e}  {2:>.3e}'.format(N, erreur, delta))

with open('tabmc','w') as fichier:
	fichier.write('n\terreur\t\ttemps\t\n')
	fichier.write('-----------------------------------------------\n')
	for i in range (1,7):		
		N = 10**i
		t1 = time.clock()
		M = Monte_CarloD(N)
		delta =time.clock() - t1
		erreur = abs(float(M)-math.pi)
		ligne ='{0:>7d}  {1:>.3e}  {2:>.3e}'.format(N, erreur, delta)
		fichier.write(ligne + '\n')

