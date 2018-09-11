import numpy as np
import matplotlib.pyplot as  plt
from scipy.integrate import odeint

#Fonction vu avant le TP
def euleur(F,t_0,t_max,y_0,h):
	nb_points = int((t_max-t_0)/h)
	T = np.zéros(nb_points)
	Y = np.zéros(nb_points)
	Y[0]= y_0
	T[0]= t_0
	y = y_0
	t = t_0
	for k in range(1,nb_points):
		y = y + h*F(y,t)
		Y[k] = y
		t = t + h
		T[k] = t 
	return T,Y


#Fonction répondant à la question
def euler(f, u0, T, n):
	h = T/n
	tt = np.zeros(n+1)
	for k in range(n+1) :
		tt[k] = k*h
	uu = np.zeros(n+1)
	uu[0] = u0
	for k in range(1, n+1) :
		u1 = u0 + h * f(tt[k-1], u0)
		uu[k] = u1
		u0 = u1
	return tt, uu
