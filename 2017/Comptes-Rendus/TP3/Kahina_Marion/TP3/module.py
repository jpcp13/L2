from math import *
import numpy as np
import matplotlib.pyplot as plt


def u(t):
    return np.exp(-t)


def f(t , u):
    return -u


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
	h = float(T)/n
	tt = np.zeros(n)
	UU = np.zeros((n, 2))
	ti = 0.0
	Ui = U0
	for i in range(n):
		ti = ti + h
		Ui += h*F(ti, Ui)
		#~ print(Ui)
		tt[i] = ti
		UU[i, :] = Ui
	return tt, UU


def F(t,U):
	w=1.0
	u=U[0]
	v=U[1]
	Up=np.zeros(2)
	Up[0]=v
	Up[1]=-u*w**2
	return Up
