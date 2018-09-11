from math import *

import numpy as np
import matplotlib.pyplot as plt


def u(x):
	return np.exp(-x)

def f(t, u):
	return -u

def u2(x):
	return 2*np.exp(-x)+x-1

def f2(t, u):
	return -u+t


def u3(x):
	return -1 / (x-1)

def f3(t, u):
	return u**2




def euler(f, u, T, n):
	h = (float(T)/n)
	suite = []
	for i in range(0, n):
		suite.append(u)
		u = u + h*f(h*i, u)
	uu=np.asarray(suite)
	tt = np.linspace(0, T, n)
	return uu, tt

def F(t, U):
	omega = 1.0
	u = U[0]
	v = U[1]
	return np.array([v, u*omega**2])

