import numpy as np 
from math import *
import time 

#valeurs fixes
I = (pi/6) + sqrt(3)/4
#fin des valeurs fixes

#definition de la fonction f(x)
def f(x):
	return np.sqrt(1-x**2)

x, pas = -0.5, 0.02
X, Y, Points = [], [], []

# initialisation de X, Y et Points 


while x <= 0.5:
	y = f(x) 
	point = (x, y) 
	X.append(x) 
	Y.append(y) 
	Points.append(point) 
	x += pas 
"""
import matplotlib.pyplot as graphe  
graphe.plot(X, Y, '*y') #initialisation du graphe 
graphe.grid() #grille 
graphe.show() #afficher 
"""

#definition de la fonction point milieu
def pt_milieu(f,a,b,n) :
 h=(b-a)/float(n) #longueur de chaque rectangle
 z=0.0 #premier rectangle
 i=1
 while i <= n :		
	z=z+h*f(((a+i*h)+(a+(i-1)*h))/2)
	i+=1
 return z 


#premier test
"""
S = pt_milieu(f,-0.5,0.5,10000)

print S
"""

t=time.clock()
n=10
while n < 100000000 :

	S = abs(pt_milieu(f,-0.5,0.5,n)-I)
	
	
	n=n*10
o=time.clock() - t
