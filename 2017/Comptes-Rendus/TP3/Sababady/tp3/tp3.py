#SABABADY Kamala
#SELVARAJAH Dinusan

import math
import numpy as np

def f(t,u):
	return -u
def f1(t,u):
	return -u + t
def f2(t,u):
	return u**2
def f3(t,u):
	return u**2 - t

def f5(t,U):
	w = 1.0
	u = U[0]
	v = U[1]
	U_out = np.zeros(2) 
	U_out[0] = v
	U_out[1] = -w**2*u
	return U_out # U_out est un np.array de taille 2

def euler(f, U0, T, n):
	U = U0
	d = U0.shape[0]
	t = 0.0
	h = T/n
	tt = np.zeros(n)
	UU = np.zeros((d, n))
	for i in range(n):
		UU[:, i] = U
		tt[i] = t
		U = U + h*f(t, U)
		t += h

	return tt, UU

