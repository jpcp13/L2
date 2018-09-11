from math import sqrt
from cmath import exp
from cmath import polar
import numpy as np

Pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

def f2(a,b,c,X):
	return a*X**2 + b*X + c

def eq2(a,b,c):
	D = b**2 - 4*a*c
	if type(D) == complex :
		s1 = sqrtcmpx2(D)[0]
		return [(-b - s1)/(2*a),(-b + s1)/(2*a)]
	if type(D) == float :
		if (D > 0) :
			return [(-b - sqrt(D))/(2*a),(-b + sqrt(D))/(2*a)]
		elif (D == 0) :
			return [(-b)/(2*a),(-b)/(2*a)]
		else :
			return [(-b - 1j*sqrt(abs(D)))/(2*a),(-b + 1j*sqrt(abs(D)))/(2*a)]

def sqrtreel3(x):
	if x < 0 :
		y = abs(x)
		return -y**(1.0/3.0)	
	if x >= 0:
		return x**(1.0/3.0)

def sqrtcmpx2(x):
	if type(x) == float :
		x = x + 0j
	Pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
	mx = sqrt(abs(x))
	K =[]
	for k in range (0, 2):
		teta = (polar(x)[1] - 2.0*k*Pi)/2.0
		l = mx*exp(1j*teta)
		K.append(l)		
	return K

def sqrtcmpx3(x):
	if type(x) == float :
		x = x + 0j
	Pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
	mx = sqrtreel3(abs(x))
	K =[]
	for k in range (0, 3):
		teta = (polar(x)[1] - 2.0*k*Pi)/3.0
		l = mx*exp(1j*teta)
		K.append(l)		
	return K


def difference(A,B):
	C = []
	c =  np.shape(A)[0]
	for i in range(0, c):
		a = A[i]
		if a not in B:
			C.append(a)
	return C
