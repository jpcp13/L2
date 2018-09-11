from math import * 
from pylab import *
from numpy import * 

def u(t):
	return np.exp(-t)

def f0(t,u):
	return -u

def f1(t, u):
	return -u + t 

def f2(t, u):
	return u*u

def f3(t,u):
	return u*u - t

def euler (f, u0, T, n):
	h = float(T)/n
	print(h)
	tt = np.zeros(n+1)
	uu = np.zeros(n+1)
	tk = 0.0
	uk = u0
	tt[0] = tk
	uu[0] = uk
	for k in range (1, n+1):
		tk = tk + h 
		uk = uk + h*f(tk, uk) 
		tt[k] = tk	
		uu[k] = uk 
	return tt, uu 





