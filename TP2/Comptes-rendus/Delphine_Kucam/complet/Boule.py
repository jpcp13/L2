import numpy as np
import matplotlib.pyplot as plt
import time
import math
import numpy.random as rd
from integration import *
from pylab import *

V = (4/3)*math.pi


R1, R2, R3 =[],[],[] # liste des valeurs dans la boule (rouge)	
V1, V2, V3 =[],[],[] # liste des valeurs hors de la boule (vert)

I = 0   # Nombre de points interieur
E = 0	# Nombre de points exterieur

for i in range (1000):
	x = rd.uniform(-1, 1)
	y = rd.uniform(-1, 1)
	z = rd.uniform(-1, 1)

	if (x*x + y*y + z*z) <= 1:
		R1.append(x)
		R2.append(y)
		R3.append(z)
		I += 1
	else:
		V1.append(x)
		V2.append(y)
		V3.append(z)
		E += 1

print("Points rouges", I)
print("Points verts", E)

def Monte_CarloB(N):
	
	R1, R2, R3 =[],[],[] # liste des valeurs dans la boule (rouge)	
	V1, V2, V3 =[],[],[] # liste des valeurs hors de la boule (vert)

	I = 0   # Nombre de points interieur
	E = 0	# Nombre de points exterieur
	
	for i in range (N):
		x = rd.uniform(-1, 1)
		y = rd.uniform(-1, 1)
		z = rd.uniform(-1, 1)

		if (x*x + y*y + z*z) <= 1:
			R1.append(x)
			R2.append(y)
			R3.append(z)
			I += 1
		else:
			V1.append(x)
			V2.append(y)
			V3.append(z)
			E += 1
	
	return 8*float(I)/N

print('      N     erreur       temps')
print('------------------------------')
for i in range (1,8):
	N = 10**i
	t1 = time.clock()
	M = Monte_CarloB(N)
	delta = abs(t1 - time.clock())
	erreur = abs(float(M)-V)
	ligne = "{0:>7d}  {1:>.3e}  {2:>.3e}".format(N, erreur, delta)
	print(ligne)

with open('TaBoulet','w') as fichier:
	fichier.write('n\terreur\t\ttemps\t\n')
	fichier.write('-----------------------------------------------\n')
	for i in range (1,7):		
		N = 10**i
		t1 = time.clock()
		M = Monte_CarloB(N)
		delta =time.clock() - t1
		erreur = abs(float(M)-math.pi)
		ligne ='{0:>7d}  {1:>.3e}  {2:>.3e}'.format(N, erreur, delta)
		fichier.write(ligne + '\n')
