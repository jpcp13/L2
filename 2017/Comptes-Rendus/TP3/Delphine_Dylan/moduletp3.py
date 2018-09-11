import numpy as np
import matplotlib.pyplot as plt
from math import *


def u(t):
	return np.exp(-t)

def euler(f, u0, T, n):
	h = T/n
	tt = np.zeros(n+1)
	for k in range(n+1):
		tt[k] = k*h
	uu = np.zeros(n+1)
	uu[0] = u0
	for k in range(1, n+1):
		u1 = u0 + h*u0
		uu[k] = u1
		u0 = u1
	return tt, uu

def F(t, U):
	w = 1.0
	u = U[0]
	v = U[1]
	U_out = np.zeros(2)
	U_out[0] = v
	U_out[1] = -w**2*u

	return U_out

def euler2(F, U0, T, n):
	U = U0
	d = U0.shape[0]
	t = 0.0
	h = T/n
	tt = np.zeros(n)
	UU = np.zeros((d, n))
	for i in range(n):
		if(d==1):
			UU = U	
		else :
			UU [:, i] = U
		tt[i] = t
		U = U + h*F(t,U)
		t+= h
	return tt, UU
