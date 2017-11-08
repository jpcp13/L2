
import numpy as np
import matplotlib.pyplot as plt
import time
import math


def f(x):
	return np.sqrt(1-x**2) # remplacé math. par np.

def point_milieu(f, a, b, n):
	I=(math.pi/6)+(math.sqrt(3)/4)
	S=0
	x1=a
	d=(b-a)/n
	x2=a+d

	for i in range(n):
		c=(x1+x2)/2
		s=d*f(c)
		S=S+s
		x1=x1+d
		x2=x2+d
	
	return S

def trapeze(f, a, b ,n):
    h = (b-a)/n
    print(h)
    S = 0.0
    for i in range (n):
        x1 = a + h*i
        x2 = x1 + h
        s = (f(x1) + f(x2))/2*h
        S += s
    return S

def simpson(f, a, b, n):
	h = (b-a)/n
	aire = 0.0
	x1 = a
	x2 = a+h
	for i in range(n):
		aire += ((x2-x1)/6)*(f(x1)+4*f((x1+x2)/2)+f(x2))
		x1 += h
		x2 += h
	return aire



def Monte_Carlo(N):
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
	return I/N
