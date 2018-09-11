import numpy as np
from time import *
from math import *

I = np.pi/6 + np.sqrt(3)/4

def pm(f,a,b,n) :
	k  = clock()
	Sub = []
	M = []
	Haut = []
	h = (b-a)/n
	So=0.0

	# les subdivisions regulieres

	for i in range(n+1):

		sub= a + h*i
		Sub.append(sub)

	# les milieux

	for i in range(n):

		m = (Sub[i] + Sub[i+1])/2
		M.append(m)

	# les images des milieux

	for i in M:
		haut=f(i)
		Haut.append(haut)

	# l'integrale

	for i in Haut:
		somme = h*i
		So=So+somme

	e = abs(I-So) 
	temps = clock() - k
	return temps, So, e

def trapeze(f, a, b, n):
	k  = clock()
	h = (b-a)/n
	
	for i in range(n):
		xg = a + h*i
		xd = a + h
		s = h * (f(xg)+f(xd))/2
		
	e = abs(I-n)
	temps = clock() - k
	return e, temps

def simpson(f, a, b, n) :
	k = clock()
	h = (b-a)/n
	S = 0.0
	x1 = a
	x2 = a + h
	
	for i in range(n) :
		S += ((x2 - x1) / 6) * (f(x1) + 4 * f((x1 + x2) / 2) + f(x2))
		x1 += h
		x2 += h

	e = abs(I - S)
	t = clock() - k
	return S, e, t


def monte_carlo(n):

	t = clock()

	#x = np.cos(theta)
	#y = np.sin(theta)

	cmpt = 0

	for i in range(n) :
		xpoint = 2*np.random.rand() - 1
		ypoint = 2*np.random.rand() - 1

		if (xpoint**2 + ypoint**2) < 1 :
			 cmpt = cmpt + 1
	
	surface = (cmpt/float(n)*4)	
	temps = clock() - t
	erreur = abs( surface - np.pi )

	return temps, surface, erreur


def monte_carlo_2(N):
	X = np.random.uniform(-1,1,N)
	Y = np.random.uniform(-1,1,N)
	Z = np.random.uniform(-1,1,N)
	I = 0
	for i in range(N):
		if (X[i]**2+Y[i]**2+Z[i]**2)<=1:
			I+=1
	return m


