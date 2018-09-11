import time
from math import *
import numpy as np

def f(x):
	from math import sqrt
	return sqrt(1-x**2)

I = pi/6 + sqrt(3)/4

def point_milieu(f, a, b, n):
	s=0
	s4= 0.95
	temps = time.clock()
	for i in range(0,n):
		x1 = a + (b-a)*i/float(n)
		x2 = a + (b-a)*(i+1)/float(n)
		s+= f((x1+x2)/2.0)*(x2-x1)

	return s, time.clock()-temps


def trapezes(f, a, b, n) :
	t = time.clock()
    	h = abs(b - a)/n
    	s = 0
    	for i in range(n):
        	s = s + h * (f(a + i*h) + f( a + (i+1)*h))/2
    	return s, time.clock()-t


def simpson(f, a, b, n): 
    
    S = 0 
    for i in range(0, n): 
        x1 = a + (b - a) * i / float(n) 
        x2 = a + (b - a) * (i + 1) / float(n) 
        S += (f(x1) + 4 * f((x1 + x2) / 2.0) + f(x2)) * (x2 - x1) / 6.0 
    return S 

def montecarlo(N):
	t=time.clock()
	cmpt=0
	for i in range(N):
		xpoint = 2*np.random.rand()-1
		ypoint = 2*np.random.rand()-1
		if (xpoint**2+ypoint**2)<1:
			#~ plt.scatter(xpoint, ypoint, color='red', marker='.')
			cmpt = cmpt + 1
	S = (cmpt /float(N)*4)
	return S, time.clock()-t


