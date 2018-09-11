#from fonctions import * 
#from pylab import * 
import numpy as np

def f(t, u):
	return -u
# a) 

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


u0 = 1.0
T = 2.0
n = 100
tt, uu = euler(f, u0, T, n) 


# b) 

