#ENGUIX Precillia
#RAJA GANAPATHY Srinivas

#FONCTIONS

import numpy as np

def u(t) :
	return np.exp(-t)

def f(t, u) :
	return -u

def f1(t, u) :
	return -u + t

def f2(t,u) :
	return u**2

def f3(t,u) :
	return u**2 - t

def euler(f, u0, T, n) :
	h = T/n
	tt = np.zeros(n + 1)
	for k in range(n + 1) :
		tt[k] = k*h
	uu = np.zeros(n + 1)
	uu[0] = u0
	for k in range(1, n +1) :
		u1 = u0 + h * f(tt[k - 1], u0)
		uu[k] = u1
		u0 = u1
	return tt, uu

def euler_2(f, U0, T, n):
	U = U0
	d = U0.shape[0]
	t = 0.0
	h = T/n
	tt = np.zeros(n)
	UU = np.zeros((d,n))
	for i in range (n) :

		if (d == 1) :
			UU = U	
		else :
			UU[:, i] = U

		tt[i] = t
		U = U + h*f(t,U)
		t += h
	return tt, UU

def F(t, U) :
	w = 1.0
	u = U[0]
	v = U[1]
	U_out = np.zeros(2)
	U_out[0] = v
	U_out[1] = -w**2 * u

	return U_out
