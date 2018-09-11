from math import sqrt
import matplotlib.pyplot as plt 

def f(x):
	return sqrt(1-x**2)

x, dx = -0.5, 0.01
X, Y, Point = [], [], [] 

while x < 0.5:
   	y = f(x)
    	pt = (x, y) 
    	X.append(x) 
    	Y.append(y)
    	Point.append(pt) 
    	x += dx

plt.plot(X, Y, 'g')
plt.grid()
plt.savefig('Courbef.png')
