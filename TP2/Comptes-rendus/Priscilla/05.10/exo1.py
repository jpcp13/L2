#ENGUIX Precillia
#RAJA GANAPATHY Srinivas

#FONCTIONS
from math import sqrt
from math import pi
from time import clock

def f(x):
        return sqrt(1 - x**2)

#EXERCICE 1

#1B.

x, dx = -0.5, 0.1
X, Y, Points = [], [], []


while x < 0.5:
        y = f(x)
        point = (x, y)

        X.append(x) 
        Y.append(y) 
        Points.append(point) 
        x += dx
print('\n')

import matplotlib.pyplot as plt
plt.plot(X, Y, '*r')
plt.grid()
#plt.show()
#plt.savefig('fig2.png') 

#1C.

#a voir
