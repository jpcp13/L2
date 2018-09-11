import matplotlib.pyplot as plt
from numpy import *
from math import *
from pylab import *

def f(t,u):
	return -u

def u(x):
	return exp(-x)

X,Y,Points = [],[],[]
x = 0
dx = 0.25
while x <= 2.5 :
	y = u(x)
	point = (x,y)
	X.append(x)
	Y.append(y)
	Points.append(point)
	x += dx


T = 2.0
n=10
h = float (T)/n
X,U = [],[]
u0=1
x0=0

ui=u0
xi=x0

X.append(x0)
U.append(u0)

for i in range (0,n):
	xi = xi + h
	ui = ui + h*f(xi,ui)
	X.append(xi)
	U.append(ui)
print(X)
print(U)
print(Y)

plt.clf()
plt.plot(X, Y, 'r', X, U, 'b')

plt.grid()
plt.show()
