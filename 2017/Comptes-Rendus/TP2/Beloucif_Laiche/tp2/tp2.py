import numpy as np 
from math import *
from time import *
from random import *

#valeurs fixes
I = (pi/6) + sqrt(3)/4
#fin des valeurs fixes

#definition de la fonction f(x)
def f(x):
	return np.sqrt(1-x**2)

#definition de la fonction point milieu
def pt_milieu(f,a,b,n) :
	h=(b-a)/float(n) #longueur de chaque rectangle
	z=0.0 #premier rectangle
	i=1
	while i <= n :		
		z=z+h*f(((a+i*h)+(a+(i-1)*h))/2)
		i+=1
	return z 


#definition de la fonction trapeze
def t(f,a,b,n) :
	k=(b-a)/float(n) #longueur de chaque base de trapeze
	y=0.0 #premier trapeze
	i=1
	while i <= n :	
		x0 = a+(i-1)*k
		x1 = x0 + k
		m = (x0 + x1)/2
		
		y = y + k*( f(x0) + f(x1) )/2 
		i+=1
	return y

#defintion de la fonction simpson
def simpson(f,a,b,n) :
	h=(b-a)/float(n) #longueur de chaque base de trapeze
	z=0.0 #premier trapeze
	i=1
	while i <= n :
		x0 = a+(i-1)*h
		x1 = x0 + h
		m = (x0 + x1)/2
		
		z = z + h*( f(x0) + 4*f(m) + f(x1) )/6
		i+=1
	return z

#definition de la fonction monte carlo
def montecarlo(N) :
	I = 0
	for i in range (N):
		a = uniform(-1,1)
		b = uniform(-1,1)
		if a*a + b*b <= 1:
			I += 1
	M = float(I)/N
	return M

#definition de la fonction monte carlo pour la boule
def montecarlo2(N) :
	I = 0
	for i in range (N):
		a = uniform(-1,1)
		b = uniform(-1,1)
		c = uniform(-1,1)
		if a*a + b*b + c*c <= 1:
			I += 1
	M2 = float(I)/N
	return M2

	




