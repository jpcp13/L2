import matplotlib.pyplot as plt
from numpy import *
from math import *
from pylab import *

##exercice 3
def euler(f,u0,T,n):
	h=float (T)/n
	xx = np.zeros(n)
	uu = np.zeros((n, 2))
	ui=u0
	xi=0.0
	for i in range (0,n):
		xi = xi + h
		ui += h*f(xi,ui)
		xx[i]=xi
		uu[i,:]=ui
	return xx,uu
##exercice 5 c)

def euler2(F, U0, T, n):
	h = float(T)/n
	tt = np.zeros(n)
	UU = np.zeros((n, 2))
	ti = 0.0
	Ui = U0
	for i in range(n):
		ti = ti + h
		Ui += h*F(ti, Ui)

		print(Ui)
		tt[i] = ti
		UU[i, :] = Ui
	return tt, UU



