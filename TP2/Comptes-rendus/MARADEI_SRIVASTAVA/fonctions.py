from math import *
from time import *
from string import *
from pylab import *
from random import *

def f(x):
	return sqrt(1-(x**2))

def aire(n):
	aire = 0.0
	a = -0.5
	b = 0.0
	for i in range(n):
		b = a+0.25 
		aire += 0.25*(f((a+b)/2))
		a += 0.25
	return aire	
	
def point_milieu(f, a, b, n):
	I = (b-a)/n #I devient l'intervalle
	aire = 0.0
	x1 = a # Creation de deux variables necessaires au calcul de la hauteur de chaque rectangle
	x2 = 0.0 # x2 s'exprime en fonction de x1
	for i in range(n):
		x2 = a+I
		aire += I*(f((x1+x2)/2))
		x1 += I
	return aire 

def erreur(x):
	return abs(x-(pi/6 + sqrt(3)/4))
	
def p(x, n): # definition d'une fonction puissance afin de faciliter la comprehension du code a la lecture
	if n>0:
		return x*p(x,n-1)
	else:
		return 1
	
def trapeze(f, a, b , n):
	I = (b-a)/float(n)
	aire = 0.0
	x1 = a 
	x2 = 0.0 
	for i in range(n):
		x2 = a+I
		aire += float(((f(x1)+f(x2))*I)/2
		x1 += I
	return aire 

def simpson(f, a, b, n):
	I = (b-a)/n
	aire = 0.0
	x1 = a
	x2 = a+I
	for i in range(n):
		aire += ((x2-x1)/6)*(f(x1)+4*f((x1+x2)/2)+f(x2))
		x1 += I
		x2 += I
	return aire 

def Monte_carlo(N):
	I = 0
	for i in range (N):
		x = uniform(-1,1)
		y = uniform(-1,1)
		if x*x + y*y <= 1:
			I += 1
	Suruthy = float(I)/N
	return Suruthy

	
