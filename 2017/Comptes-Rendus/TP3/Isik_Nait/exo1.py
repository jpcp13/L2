from math import *
from time import clock

def f(x):
	return exp(-x)
#EXO 1
x, dx = 0, 0.05


X, Y, Points = [], [], [] 

# initialisation de X, Y et Points
while x < 2.05:
    y = f(x)
    point = (x, y)  
    X.append(x) 
    Y.append(y) 
    Points.append(point) 
    x += dx
#affichage 

import matplotlib.pyplot as graphe 
graphe.plot(X, Y, 'r') #initialisation du graphe
graphe.grid('on') #grille
graphe.savefig('fig1.png')


