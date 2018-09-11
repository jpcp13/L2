import matplotlib.pyplot as plt
#matplotlib.pyplot
import numpy as np
from math import *

def f(x):
	return np.sqrt(1-x**2)

#representation graphique sur [-0.5,0.5]
x = -0.5
dx = 0.1
X, Y, Points = [], [], []

while x < 0.5 :
	y = f(x)
	point =(x, y)
	X.append(x)
	Y.append(y)
	Points.append(point)
	x= x+dx
print(X)
print(Y)

plt.plot(X, Y, '*r')
plt.grid()
plt.show()

#calcul de l'integrale I=0.95


