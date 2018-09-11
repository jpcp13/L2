
from tp2 import *
from math import pi  

#Exercice 1

#a)voir fichier tp2.py
#b)Representation graphique de f(x) sur l'intervalle

x, dx = -0.5, 0.01
X, Y, Points = [], [], [] 

while x < 0.5 :
    	y = f(x)
	point = (x, y) 
   
	X.append(x) #liste de reels
	Y.append(y) #liste de reels
	Points.append(point)#liste de couples reel
	x += dx
   
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(-0.5, 0.5, 0.01) # intervalle [-0.5;0.5]
plt.plot(X, Y,'r') 
plt.grid('on')
plt.axis('equal')
plt.savefig('graphF..png')

#c) voir fichier odt

