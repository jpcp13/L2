from math import *

def f(x) :
	return sqrt(1-x**2)

x = -0.5
X, Y, Points = [], [], [] 

while x <= 0.5:
	print(x)
	y = f(x)
	point = (x, y)
	X.append(x)
	Y.append(y)
	Points.append(point) 
	x += 0.01

#print(X)
#print(Y)
#print(Points)

import matplotlib.pyplot as plt
plt.plot(X, Y, '*r')
plt.grid()
plt.show()


