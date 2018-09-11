from math import sqrt
from math import pi
import numpy as np

I = sqrt(3.0)/4 + (pi/6)

def f(x):
        return sqrt(1 - x**2)

def point_milieu(f,a,b,n) : 
	h = ( b - a ) / n
	S = 0
	for i in range (n):
		c = a + (h/2) * (2*i + 1)
		s = h * f( c )
		S += s
	return S

def trapeze(f, a, b, n):
	h = (b - a) / n
	S = 0
	for i in range(n):
		s=( f( a + (i*h) - h ) + f( a + (i*h) ) ) * (h/2)
		S += s
	return S

def simpson(f, a, b, n):
	h = ( b - a ) / n
	S = 0
	for i in range (n):
		gauche =  a + i*h
		milieu =  a + i*h + h/2
		droite = a + i*h
		s = h * ( f(gauche) + 4 * f(milieu) + f(droite) )/6
		S += s
	return S

def monte_carlo(N):

	x = np.random.uniform(-1, 1, N)
	y = np.random.uniform(-1, 1, N)

	I = 0
	for i in range(N):
		if (x[i]**2 + y[i]**2) <= 1:
			I += 1
	m = ((I*4.0)/N)
	return m


def monte_carlo2(N):

	x = np.random.uniform(-1, 1, N)
	y = np.random.uniform(-1, 1, N)
	z = np.random.uniform(-1, 1, N)


	I = 0
	for i in range(N):
		if (x[i]**2 + y[i]**2 + z[i]**2) <= 1:
			I += 1
	m = ((I*6.0)/N)
	return m












