from math import *
from time import clock
import numpy as np
import matplotlib.pyplot as plt

def f(t , u):
    return -u

def F(t, U):
	w = 1.0
	u = U[0]
	v = U[1]
	Up = np.zeros(2)
	Up[0] = v
	Up[1] = -u*w**2
	return Up


def euler(f,u0,T,n):
	
	t0 = 0.0
	h = T/n
	tt = np.zeros(n+1)
	uu = np.zeros(n+1)
	uu[0] = u0
	tt[0] = t0

	for k in range(1,n+1):

		u1 = u0 + h*f(t0,u0)
		uu[k] = u1
		t1 = t0 + h
		tt[k] = t1
		u0 = u1
		t0 = t1

	return tt,uu

def euler2(F, U0, T, n):
	
	t0 = 0.0
	h = float(T)/n
	tt = np.zeros(n+1)
	UU = np.zeros((2, n+1))
	U1 = np.zeros(2)
	tt[0] = t0

	for i in range(n+1):
		U1 = U0 + h*F(t0, U0)
		t1 = t0 + h
		UU[:, i] = U1
		tt[i] = t1
		U0 = U1
		t0 = t1

	return tt, UU


